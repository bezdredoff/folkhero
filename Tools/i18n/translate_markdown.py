#!/usr/bin/env python3
"""Translate canonical Markdown documentation into a generated Russian mirror.

The translator runs a local open-source MarianMT model on the GitHub Actions
runner. No paid translation API or API key is required.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
from pathlib import Path

import torch
from transformers import MarianMTModel, MarianTokenizer


ROOT = Path(__file__).resolve().parents[2]
TARGET_ROOT = ROOT / "ru"
DOCS_ROOT = ROOT / "Docs"
README = ROOT / "README.md"

DEFAULT_MODEL = "Helsinki-NLP/opus-mt-en-ru"

MARKER_RE = re.compile(
    r"<!-- AUTO-TRANSLATED: source=(?P<source>\S+) "
    r"sha256=(?P<sha>[0-9a-f]{64}) model=(?P<model>\S+) target=ru -->"
)

FENCE_RE = re.compile(r"^\s*((?:\x60){3}|~~~)")
HEADING_RE = re.compile(r"^(\s{0,3}#{1,6}\s+)(.*)$")
LIST_RE = re.compile(r"^(\s*(?:(?:[-+*])|(?:\d+[.)]))\s+)(.*)$")
QUOTE_RE = re.compile(r"^(\s*>\s?)(.*)$")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*:?-{3,}:?\s*\|?\s*$")

LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)]*)\)")
INLINE_CODE_RE = re.compile(r"\x60[^\x60\n]+\x60")
RAW_URL_RE = re.compile(r"https?://[^\s>)\]]+")
HTML_RE = re.compile(r"<[^>\n]+>")
ISSUE_REF_RE = re.compile(r"(?<!\w)#\d+\b")
FILE_RE = re.compile(r"\b(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+\.(?:md|yml|yaml|json|cs|py|sh|ps1)\b")
EMPHASIS_RE = re.compile(r"(\*\*|__|~~|\*|_)")

CANONICAL_GAMEPLAY_TERMS = [
    "Physical",
    "Wet",
    "Burning",
    "Fire",
    "Cold",
    "Frozen",
    "Shock",
    "Lightning",
    "Poison",
    "Curse",
    "Armor",
    "Downed",
    "Shatter",
    "PP-01",
    "Vertical Slice",
    "Early Access",
]

PROTECTED_RE = re.compile(
    "|".join(
        [
            INLINE_CODE_RE.pattern,
            RAW_URL_RE.pattern,
            HTML_RE.pattern,
            ISSUE_REF_RE.pattern,
            FILE_RE.pattern,
            r"\b(?:" + "|".join(re.escape(term) for term in CANONICAL_GAMEPLAY_TERMS) + r")\b",
            EMPHASIS_RE.pattern,
        ]
    )
)


def run_git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stderr=subprocess.STDOUT,
    )


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def source_to_target(source: Path) -> Path:
    return TARGET_ROOT / source.relative_to(ROOT)


def all_source_files() -> list[Path]:
    files: list[Path] = []
    if README.exists():
        files.append(README)
    if DOCS_ROOT.exists():
        files.extend(sorted(p for p in DOCS_ROOT.rglob("*.md") if p.is_file()))
    return files


def normalize_repo_path(value: str) -> Path:
    return (ROOT / value).resolve()


def is_translatable_repo_path(value: str) -> bool:
    path = Path(value)
    if path == Path("README.md"):
        return True
    return len(path.parts) >= 2 and path.parts[0] == "Docs" and path.suffix.lower() == ".md"


def changed_operations(base: str, head: str) -> tuple[list[Path], list[Path]]:
    if not base or set(base) == {"0"}:
        return all_source_files(), []

    output = run_git(
        "diff",
        "--name-status",
        "--find-renames",
        base,
        head,
        "--",
        "README.md",
        "Docs",
    )

    translate: set[Path] = set()
    remove_targets: set[Path] = set()

    for raw_line in output.splitlines():
        if not raw_line.strip():
            continue

        parts = raw_line.split("\t")
        status = parts[0]

        if status.startswith("R") and len(parts) >= 3:
            old_name, new_name = parts[1], parts[2]
            if is_translatable_repo_path(old_name):
                remove_targets.add(source_to_target(normalize_repo_path(old_name)))
            if is_translatable_repo_path(new_name):
                source = normalize_repo_path(new_name)
                if source.exists():
                    translate.add(source)
            continue

        if len(parts) < 2:
            continue

        name = parts[1]
        if not is_translatable_repo_path(name):
            continue

        source = normalize_repo_path(name)
        if status.startswith("D"):
            remove_targets.add(source_to_target(source))
        elif source.exists():
            translate.add(source)

    return sorted(translate), sorted(remove_targets)


def existing_source_hash(target: Path) -> str | None:
    if not target.exists():
        return None

    try:
        first_lines = "\n".join(target.read_text(encoding="utf-8").splitlines()[:5])
    except UnicodeDecodeError:
        return None

    match = MARKER_RE.search(first_lines)
    return match.group("sha") if match else None


class LocalTranslator:
    def __init__(self, model_name: str, batch_size: int = 16) -> None:
        self.model_name = model_name
        self.batch_size = batch_size
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)
        self.model.eval()
        torch.set_num_threads(max(1, min(4, os.cpu_count() or 1)))

    @torch.inference_mode()
    def translate_many(self, texts: list[str]) -> list[str]:
        if not texts:
            return []

        output: list[str] = []

        for start in range(0, len(texts), self.batch_size):
            batch = texts[start : start + self.batch_size]
            encoded = self.tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=480,
            )
            generated = self.model.generate(
                **encoded,
                max_new_tokens=512,
                num_beams=4,
                early_stopping=True,
            )
            output.extend(
                self.tokenizer.batch_decode(generated, skip_special_tokens=True)
            )

        return output


def split_long_text(text: str, max_chars: int = 700) -> list[str]:
    if len(text) <= max_chars:
        return [text]

    parts = re.split(r"(?<=[.!?;:])(\s+)", text)
    chunks: list[str] = []
    current = ""

    for part in parts:
        if len(current) + len(part) <= max_chars:
            current += part
            continue

        if current:
            chunks.append(current)
            current = ""

        if len(part) <= max_chars:
            current = part
            continue

        for start in range(0, len(part), max_chars):
            piece = part[start : start + max_chars]
            if len(piece) == max_chars:
                chunks.append(piece)
            else:
                current = piece

    if current:
        chunks.append(current)

    return chunks


def add_translatable_segment(text: str, segments: list[str], markers: list[str]) -> str:
    if not text or not re.search(r"[A-Za-z]", text):
        return text

    pieces = split_long_text(text)
    rendered: list[str] = []

    for piece in pieces:
        if not re.search(r"[A-Za-z]", piece):
            rendered.append(piece)
            continue

        marker = f"@@TR{len(segments):06d}@@"
        segments.append(piece)
        markers.append(marker)
        rendered.append(marker)

    return "".join(rendered)


def mark_plain_inline(text: str, segments: list[str], markers: list[str]) -> str:
    output: list[str] = []
    cursor = 0

    for match in PROTECTED_RE.finditer(text):
        before = text[cursor : match.start()]
        output.append(add_translatable_segment(before, segments, markers))
        output.append(match.group(0))
        cursor = match.end()

    output.append(add_translatable_segment(text[cursor:], segments, markers))
    return "".join(output)


def mark_inline(text: str, segments: list[str], markers: list[str]) -> str:
    output: list[str] = []
    cursor = 0

    for match in LINK_RE.finditer(text):
        output.append(mark_plain_inline(text[cursor : match.start()], segments, markers))

        full = match.group(0)
        label = match.group(1)
        destination = match.group(2)
        prefix = "!" if full.startswith("!") else ""

        translated_label = mark_plain_inline(label, segments, markers)
        output.append(f"{prefix}[{translated_label}]({destination})")
        cursor = match.end()

    output.append(mark_plain_inline(text[cursor:], segments, markers))
    return "".join(output)


def mark_table_line(line: str, segments: list[str], markers: list[str]) -> str:
    if TABLE_SEPARATOR_RE.match(line):
        return line

    cells = line.split("|")
    translated: list[str] = []

    for cell in cells:
        leading = cell[: len(cell) - len(cell.lstrip())]
        trailing = cell[len(cell.rstrip()) :]
        core = cell.strip()
        if core:
            core = mark_inline(core, segments, markers)
        translated.append(leading + core + trailing)

    return "|".join(translated)


def build_template(markdown: str) -> tuple[str, list[str], list[str]]:
    segments: list[str] = []
    markers: list[str] = []
    output: list[str] = []
    in_fence = False
    fence_token = ""

    for line in markdown.splitlines(keepends=True):
        newline = "\n" if line.endswith("\n") else ""
        body = line[:-1] if newline else line

        fence = FENCE_RE.match(body)
        if fence:
            token = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_token = token
            elif token == fence_token:
                in_fence = False
                fence_token = ""
            output.append(body + newline)
            continue

        if in_fence or body.startswith("    "):
            output.append(body + newline)
            continue

        if "|" in body and not body.lstrip().startswith(">"):
            output.append(mark_table_line(body, segments, markers) + newline)
            continue

        prefix = ""
        content = body

        for regex in (HEADING_RE, LIST_RE, QUOTE_RE):
            match = regex.match(content)
            if match:
                prefix += match.group(1)
                content = match.group(2)
                break

        output.append(prefix + mark_inline(content, segments, markers) + newline)

    return "".join(output), segments, markers


def render_translation(translator: LocalTranslator, markdown: str) -> str:
    template, segments, markers = build_template(markdown)
    translated_segments = translator.translate_many(segments)

    if len(translated_segments) != len(markers):
        raise RuntimeError("Translation segment count mismatch.")

    result = template
    for marker, translated in zip(markers, translated_segments):
        result = result.replace(marker, translated, 1)

    return result


def fix_mirrored_links(source: Path, translated: str) -> str:
    if source == README:
        lines = translated.splitlines()
        for index, line in enumerate(lines):
            if "./ru/README.md" in line:
                lines[index] = "**Языки:** [English (canonical)](../README.md) · Русский"
                break
        translated = "\n".join(lines) + ("\n" if translated.endswith("\n") else "")

    return translated


def generated_header(source: Path, source_hash: str, model: str, target: Path) -> str:
    source_rel = source.relative_to(ROOT).as_posix()
    canonical_link = os.path.relpath(source, start=target.parent).replace(os.sep, "/")
    return (
        f"<!-- AUTO-TRANSLATED: source={source_rel} sha256={source_hash} "
        f"model={model} target=ru -->\n\n"
        "> [!NOTE]\n"
        f"> Это автоматически сгенерированный перевод. Каноническая версия: "
        f"[{source_rel}]({canonical_link}). Не редактируйте этот файл вручную — "
        "изменения будут перезаписаны автоматизацией.\n\n"
    )


def remove_empty_parents(path: Path) -> None:
    current = path.parent
    while current != TARGET_ROOT and current.exists():
        try:
            current.rmdir()
        except OSError:
            break
        current = current.parent


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--base", default="")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--model",
        default=os.environ.get("DOCS_TRANSLATION_MODEL") or DEFAULT_MODEL,
    )
    args = parser.parse_args()

    if args.all:
        translate_sources = all_source_files()
        remove_targets: list[Path] = []
    else:
        if not args.base:
            parser.error("--base is required unless --all is used")
        translate_sources, remove_targets = changed_operations(args.base, args.head)

    for target in remove_targets:
        if target.exists():
            print(f"Removing stale translation: {target.relative_to(ROOT)}")
            target.unlink()
            remove_empty_parents(target)

    pending: list[tuple[Path, Path, str, str]] = []

    for source in translate_sources:
        markdown = source.read_text(encoding="utf-8")
        source_hash = sha256_text(markdown)
        target = source_to_target(source)

        if not args.force and existing_source_hash(target) == source_hash:
            print(f"Up to date: {target.relative_to(ROOT)}")
            continue

        pending.append((source, target, source_hash, markdown))

    if not pending:
        print("No documentation requires translation.")
        return 0

    print(f"Loading local translation model: {args.model}")
    translator = LocalTranslator(args.model)

    for source, target, source_hash, markdown in pending:
        print(f"Translating {source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        translated = render_translation(translator, markdown)
        translated = fix_mirrored_links(source, translated)

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            generated_header(source, source_hash, args.model, target)
            + translated.rstrip()
            + "\n",
            encoding="utf-8",
            newline="\n",
        )

    print(f"Translation complete: {len(pending)} file(s) updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
