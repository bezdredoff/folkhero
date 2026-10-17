# Documentation Translation

Status: active automation design.

## Goal

Keep one canonical documentation tree while providing a readable Russian mirror for the project owner and Russian-speaking collaborators.

## Source of truth

Canonical documentation remains in English:

- README.md
- Docs/**/*.md

Generated Russian translations live under:

- ru/README.md
- ru/Docs/**/*.md

Do not edit generated files manually. The translation workflow overwrites them.

This one-way model avoids bidirectional synchronization conflicts and keeps AI agents, issue references and production terminology anchored to a single source of truth.

## Cost model

The translation pipeline is designed to run with **no paid translation API**.

It uses:

- a standard GitHub-hosted Ubuntu runner;
- the open-source Helsinki-NLP/opus-mt-en-ru MarianMT model;
- local CPU inference on the Actions runner;
- Hugging Face model caching between runs.

The Folkhero repository is public, so standard GitHub-hosted runners are suitable for this workflow without requiring an external translation service.

No OpenAI, DeepL, Google or other translation API key is required.

## Model

Default model:

Helsinki-NLP/opus-mt-en-ru

The model is an English -> Russian machine-translation model released under the Apache-2.0 license.

Optional repository variable:

DOCS_TRANSLATION_MODEL

If the variable is empty, the translator uses the default model.

Changing the model should be reviewed because different Hugging Face models may have different licenses, memory requirements and output quality.

## Workflow

GitHub Actions workflow:

.github/workflows/translate-docs-ru.yml

Translator:

Tools/i18n/translate_markdown.py

The workflow runs when canonical Markdown changes on main.

It can also be run manually with workflow_dispatch.

### Initial run

If ru/Docs does not exist yet, the workflow automatically translates the complete current documentation set.

### Normal push to main

After initialization, only changed canonical Markdown files are considered.

Deleted and renamed source files remove stale generated translations.

### Manual dispatch

All canonical documentation is considered.

Existing translations are skipped when their embedded source SHA-256 hash is current.

Use the force input to regenerate all translations.

## Translation branch and PR

Generated changes are pushed to:

automation/docs-ru

The workflow opens or updates a pull request into main.

This keeps generated translations reviewable instead of writing machine-generated language directly into the default branch.

If GitHub blocks Actions from creating pull requests, enable the relevant setting under:

**Settings -> Actions -> General -> Workflow permissions**

The translation branch is still pushed even if automatic PR creation is blocked.

## Markdown handling

The translator intentionally translates prose segments rather than sending raw Markdown syntax through the model.

It preserves:

- fenced and indented code;
- inline code;
- URLs;
- relative link destinations;
- file paths;
- issue references;
- Markdown structure;
- canonical gameplay/system identifiers.

Important gameplay tags such as Wet, Frozen, Curse, Shatter and Physical remain in English when used as mechanical identifiers.

Human-readable link labels can be translated while destinations stay unchanged.

## Generated-file marker

Every generated file begins with metadata containing:

- canonical source path;
- source SHA-256 hash;
- model ID;
- target language.

The source hash avoids unnecessary retranslation when a file has not changed.

## Performance

The first run is the slowest because it must:

1. install the Python ML dependencies;
2. download the translation model;
3. translate the whole documentation tree.

Later runs are cheaper in time because:

- the model download is cached by GitHub Actions;
- only changed/outdated files are translated.

The workflow is intentionally optimized for cost rather than maximum translation quality.

## Quality expectations

Helsinki-NLP/opus-mt-en-ru is a dedicated translation model, not a large reasoning model.

Expected strengths:
- ordinary technical prose;
- predictable terminology;
- zero API cost;
- deterministic, automatable output.

Expected weaknesses:
- less natural phrasing than a strong general-purpose LLM;
- weaker understanding of project-specific context;
- occasional awkward translations around heavily formatted Markdown.

For this reason the Russian tree is explicitly a generated mirror and the English tree remains canonical.

If higher translation quality becomes necessary later, the same pipeline can be switched to another local model or an API-backed provider.

## Local use

From the repository root:

    python -m pip install "transformers<5" sentencepiece torch
    python Tools/i18n/translate_markdown.py --all

To force regeneration:

    python Tools/i18n/translate_markdown.py --all --force

The first local run downloads the configured Hugging Face model.

## Scope

The first version intentionally translates only project documentation.

It does not translate:

- source code;
- Unity assets;
- AI role/skill files outside Docs;
- issues;
- pull requests;
- game localization content.

Those can use separate pipelines later.
