#!/usr/bin/env python3
"""Translate canonical Markdown documentation into a generated Russian mirror."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from openai import OpenAI


ROOT = Path(__file__).resolve().parents[2]
TARGET_ROOT = ROOT / "ru"
DOCS_ROOT = ROOT / "Docs"
README = ROOT / "README.md"
FENCE = chr(96) * 3

MARKER_RE = re.compile(
    r"<!-- AUTO-TRANSLATED: source=(?P<source>\S+) "
    r"sha256=(?P<sha>[0-9a-f]{64}) model=(?P<model>\S+) target=ru -->"
)

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
]


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


def strip_accidental_outer_fence(text: str) -> str:
    value = text.strip()
    if not value.startswith(FENCE):
        return value

    lines = value.splitlines()
    if len(lines) >= 3 and lines[-1].strip() == FENCE:
        return "\n".join(lines[1:-1]).strip()

    return value


def translation_prompt(source_path: Path, markdown: str) -> str:
    canonical_terms = ", ".join(CANONICAL_GAMEPLAY_TERMS)
    relative_source = source_path.relative_to(ROOT).as_posix()

    return f"""Translate the following Folkhero project documentation from English into natural Russian.

This is a faithful documentation translation, not a rewrite or summary.

Rules:
1. Return ONLY the translated Markdown document. Do not add commentary or wrap it in an outer code fence.
2. Preserve Markdown structure, heading levels, lists, tables, blockquotes, admonitions and spacing where practical.
3. Do NOT translate fenced code blocks, inline code, CLI commands, JSON/YAML/code identifiers, file paths, URLs, relative link destinations, GitHub issue/PR references, commit SHAs or version numbers.
4. Translate human-readable link text, but preserve every link destination exactly.
5. Preserve product/library names such as Folkhero, Unity, URP, Odin Inspector & Serializer, GeNa Pro, Feel/MMFeedbacks, GitHub, ComfyUI and OpenAI.
6. Treat these gameplay/system tokens as canonical identifiers and keep them exactly in English when they refer to game mechanics: {canonical_terms}.
7. Preserve deliberate project milestone names such as Vertical Slice and Early Access when they are used as named production stages; surrounding prose should be natural Russian.
8. Do not omit, merge, invent or soften requirements, numbers, acceptance criteria or decisions.
9. If the source already contains Russian text, keep it natural rather than translating it back to English.
10. Keep terminology consistent throughout the document.

Source file: {relative_source}

<markdown>
{markdown}
</markdown>
"""


def postprocess_translation(source: Path, translated: str) -> str:
    # README is mirrored one directory deeper, so its language-switch link
    # cannot preserve the canonical relative destination unchanged.
    if source == README:
        lines = translated.splitlines()
        for index, line in enumerate(lines):
            if "./ru/README.md" in line:
                lines[index] = "**Языки:** [English (canonical)](../README.md) · Русский"
                break
        translated = "\n".join(lines)

    return translated


def translate_markdown(client: OpenAI, model: str, source: Path, markdown: str) -> str:
    prompt = translation_prompt(source, markdown)

    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            response = client.responses.create(
                model=model,
                input=prompt,
                store=False,
                max_output_tokens=65536,
            )
            translated = strip_accidental_outer_fence(response.output_text)
            if not translated.strip():
                raise RuntimeError("Model returned an empty translation.")
            translated = postprocess_translation(source, translated)
            return translated.rstrip() + "\n"
        except Exception as exc:
            last_error = exc
            if attempt == 3:
                break
            wait = 2 ** attempt
            print(f"Translation attempt {attempt} failed for {source}: {exc}", file=sys.stderr)
            print(f"Retrying in {wait}s...", file=sys.stderr)
            time.sleep(wait)

    raise RuntimeError(f"Translation failed for {source}: {last_error}")


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
        default=os.environ.get("OPENAI_MODEL") or "gpt-6-luna",
    )
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is required.", file=sys.stderr)
        return 2

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

    if not translate_sources:
        print("No canonical Markdown files require translation.")
        return 0

    client = OpenAI()
    translated_count = 0
    skipped_count = 0

    for source in translate_sources:
        markdown = source.read_text(encoding="utf-8")
        source_hash = sha256_text(markdown)
        target = source_to_target(source)

        if not args.force and existing_source_hash(target) == source_hash:
            print(f"Up to date: {target.relative_to(ROOT)}")
            skipped_count += 1
            continue

        print(f"Translating {source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        translated = translate_markdown(client, args.model, source, markdown)

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            generated_header(source, source_hash, args.model, target) + translated,
            encoding="utf-8",
            newline="\n",
        )
        translated_count += 1

    print(
        f"Translation complete: {translated_count} translated, "
        f"{skipped_count} already up to date."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
