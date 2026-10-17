# AGENTS.md

This file is the entry point for any AI agent working on Folkhero.

## Mission

Folkhero is a systems-driven Belarusian folklore hack-and-slash / roguelike. The project is being built by a very small human team with AI agents. The goal is not to maximize generated output. The goal is to build a maintainable game and a reusable content-production system.

## Source of truth

Read these before making non-trivial changes:

1. Docs/Vision/Game_Vision.md
2. Docs/GameDesign/Game_Bible.md
3. Docs/GameDesign/System_Bible.md
4. Docs/Technical/Technical_Bible.md
5. Docs/Art/Art_Bible.md
6. Docs/Production/Production_Roadmap.md
7. Docs/Production/PP-01_Production_Foundation.md
8. Docs/Production/AI_Production_System.md

When documents disagree, stop making broad assumptions. Prefer the more specific document, record the conflict, and request a human decision if it affects product direction.

## Current phase

Pre-production, milestone PP-01: Production Foundation.

Do not scale content aggressively yet. Priorities are:
- prove game feel;
- define reusable gameplay grammar;
- establish Unity authoring architecture;
- establish AI workflows;
- create test playgrounds;
- benchmark end-to-end content production.

## Rules for agents

### 1. Reuse before invention

Before adding a new gameplay class, system or bespoke pipeline, check whether the request can be expressed with existing primitives, modifiers, data or composition.

A successful content task should make the next similar task cheaper.

### 2. Separate content from mechanics

Prefer data-driven definitions for:
- abilities;
- enemies;
- status effects;
- modifiers;
- encounters;
- loot;
- feedback profiles.

Avoid one script per weapon/enemy unless there is a genuinely new mechanic.

### 3. Human approval gates

Human approval is required before:
- changing game pillars;
- changing the core loop;
- introducing a new major dependency;
- committing to multiplayer architecture;
- replacing the rendering pipeline;
- changing save compatibility strategy;
- changing monetization or live-service assumptions;
- mass-generating production assets.

Agents may prototype alternatives without approval if they are isolated and reversible.

### 4. Concept before expensive production

For non-trivial visual or gameplay content:
brief -> cheap concept/reference -> human selection -> production implementation -> test -> review.

Do not spend large amounts of compute/API credits implementing an unapproved direction.

### 5. Test what you change

Every implementation task should define how it will be checked.

When Unity automation is available, prefer a closed loop:
change -> compile -> tests -> Play Mode -> inspect logs/screenshots -> fix -> report.

### 6. Do not hide failures

Record:
- failed approaches;
- rework;
- API cost if material;
- human intervention;
- new technical debt.

Failure information should improve future skills.

### 7. Promote successful workflows into skills

If a repeatable method succeeds, update AI/Skills with:
- prerequisites;
- steps;
- expected outputs;
- review checkpoints;
- common failure modes.

## Engineering principles

- Unity 6 + URP is the current engine direction.
- PC is the lead Early Access platform.
- Controller/mobile constraints should be considered architecturally but must not block early validation.
- Odin Inspector & Serializer should support data-driven authoring where useful.
- GeNa Pro is intended to support biome/world production, not replace level design.
- Feel / MMFeedbacks should be used as reusable feedback primitives rather than rebuilding hitstop, camera shake and flashes repeatedly.
- Prefer composition over inheritance for gameplay content.
- Avoid large global managers when a smaller domain service or data-driven system is enough.
- Keep prototypes isolated when their architecture is intentionally disposable.

## Definition of done for content

A content item is not done merely because it appears in the game.

Done means:
- behavior works;
- feedback is readable;
- it is testable in a playground;
- errors do not pollute the console;
- configuration is understandable;
- relevant documentation is updated;
- production time/lessons are recorded when it is a benchmark item.

## Git workflow

Until the workflow is revised:
- small documentation fixes may go directly to main;
- implementation work should normally use a focused branch and PR;
- do not mix unrelated refactors with a feature task;
- PR descriptions should explain intent, tests and known limitations.

## First implementation targets

The expected sequence is:

1. initialize Unity project;
2. integrate chosen tooling;
3. create CombatLab;
4. create first ability primitives;
5. create first enemy primitives;
6. create ContentLab;
7. complete one enemy end-to-end;
8. complete a second and third related enemy to measure production acceleration;
9. decide whether PP-01 exit criteria are met.
