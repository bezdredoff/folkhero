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

## Workflow

GitHub Actions workflow:

.github/workflows/translate-docs-ru.yml

Translator:

Tools/i18n/translate_markdown.py

The workflow runs when canonical Markdown changes on main.

It can also be run manually with workflow_dispatch.

### On a normal push to main

Only changed canonical Markdown files are translated.

Deleted and renamed source files remove stale generated translations.

### On manual dispatch

All canonical documentation is considered.

Existing translations are skipped when their embedded source SHA-256 hash is current.

Use the force input to regenerate all translations.

## OpenAI API

The translator uses the OpenAI Responses API through the official Python SDK.

Required repository secret:

OPENAI_API_KEY

Add it in:

**Settings -> Secrets and variables -> Actions -> New repository secret**

The ChatGPT subscription and OpenAI API billing are separate. The secret must be an API key with access to the selected model.

## Model

Default:

gpt-6-luna

This is intentionally a low-cost, high-volume text model suitable for documentation translation.

Optional repository variable:

DOCS_TRANSLATION_MODEL

If this variable is empty, the translator falls back to gpt-6-luna.

## Translation PR

Generated changes are pushed to a persistent branch:

automation/docs-ru

The workflow opens or updates a pull request into main.

This keeps generated language changes reviewable and avoids direct writes to the protected/default branch.

If GitHub blocks Actions from creating pull requests, enable the repository option under:

**Settings -> Actions -> General -> Workflow permissions**

The translation branch is still pushed even if PR creation is blocked, so a PR can be opened manually.

## Translation guarantees

The prompt requires the model to preserve:

- Markdown structure;
- fenced code;
- inline code;
- URLs;
- relative link destinations;
- file paths;
- commands;
- issue/PR references;
- version numbers;
- canonical game-system identifiers.

Important gameplay tags such as Wet, Frozen, Curse, Shatter and Physical stay as canonical identifiers when used mechanically.

## Generated-file marker

Every generated file begins with metadata containing:

- canonical source path;
- source SHA-256 hash;
- model ID;
- target language.

The hash prevents unnecessary API calls when the canonical source has not changed.

## Local use

From the repository root:

    python -m pip install openai
    export OPENAI_API_KEY="..."
    python Tools/i18n/translate_markdown.py --all

To force regeneration:

    python Tools/i18n/translate_markdown.py --all --force

On Windows PowerShell:

    python -m pip install openai
    $env:OPENAI_API_KEY = "..."
    python Tools/i18n/translate_markdown.py --all

## Scope

The first version intentionally translates only project documentation.

It does not translate:

- source code;
- Unity assets;
- AI role/skill files outside Docs;
- issues;
- pull requests;
- game localization content.

Those can use separate pipelines later if needed.
