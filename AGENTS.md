# AGENTS.md

This file is the entry point for any AI agent working on Folkhero.

## Mission

Folkhero is a story-driven cooperative systemic action RPG / hack-and-slash rooted in Belarusian and wider Slavic folklore.

The project is built by a very small human team with AI agents.

The goal is not to maximize generated output. The goal is to build:
1. a maintainable game;
2. a reusable content-production system.

The game uses persistent character progression. Do not assume roguelite run resets unless a future source-of-truth decision explicitly changes this.

## Source of truth

Read these before non-trivial changes:

1. Docs/Vision/Game_Vision.md
2. Docs/Vision/World_and_Narrative.md
3. Docs/GameDesign/Game_Bible.md
4. Docs/GameDesign/System_Bible.md
5. Docs/GameDesign/Progression_and_Itemization.md
6. Docs/GameDesign/Vertical_Slice_Spec.md
7. Docs/Technical/Technical_Bible.md
8. Docs/Art/Art_Bible.md
9. Docs/Production/Production_Roadmap.md
10. Docs/Production/PP-01_Production_Foundation.md
11. Docs/Production/Decision_Log.md
12. Docs/LiveOps/Early_Access_and_Live_Service.md
13. Docs/Production/AI_Production_System.md

When documents disagree:
- prefer the newer, more specific decision;
- check the Decision Log;
- record the conflict;
- request human direction if it changes product scope.

## Current phase

Pre-production, milestone **PP-01: Production Foundation**.

Do not scale content aggressively yet.

Priorities:
- prove Warrior + Vedun game feel;
- prove reusable combat/status grammar;
- prove ornament affinity buildcraft;
- prove meaningful weather/surface interaction;
- prove 2-player co-op early;
- prove procedural region assembly;
- establish Unity/AI closed-loop workflows;
- benchmark production acceleration.

## Locked product constraints

Agents must not casually change these:

- persistent progression, not roguelite run reset;
- initial classes are Warrior + Vedun only;
- co-op is a core Early Access feature;
- PC-first, mobile-aware architecture;
- fixed/limited-rotation top-down/isometric camera with zoom;
- basic attack + cooldown skills; no mana/stamina/rage initially;
- no universal dodge requirement;
- Physical is one damage type;
- core systemic set: Wet, Fire, Cold, Lightning, Poison, Curse;
- ornaments are learned recipes and build-wide affinity contributors;
- one primary ornament per item at baseline;
- weather materially changes gameplay;
- first region is Upper-Berezina-like forest/marsh;
- premium buy-to-play; no sale of power/progression.

See Decision Log for detail.

## Rules for agents

### 1. Reuse before invention

Before adding a gameplay class, system or bespoke pipeline, check whether the request can be expressed with:
- existing primitives;
- modifiers;
- tags;
- data;
- composition.

A successful content task should make the next similar task cheaper.

### 2. Separate content from mechanics

Prefer data-driven definitions for:
- abilities;
- skill modifiers;
- enemies;
- status effects;
- reactions;
- weather rules;
- surfaces;
- ornaments;
- encounters;
- quest primitives;
- loot;
- feedback profiles.

Avoid one script per weapon/enemy unless there is a genuinely new reusable mechanic.

### 3. Respect scope

Do not pre-build future complexity merely because it may be useful someday.

Examples currently deferred:
- more playable classes;
- mana/stamina/rage;
- universal dodge;
- complex crafting;
- many rarity tiers;
- 4-player production networking;
- permanent companion party;
- giant city simulation;
- broad procedural quest authoring for main story.

### 4. Human approval gates

Human approval is required before:
- changing game pillars;
- changing the core loop;
- introducing a major dependency;
- selecting/committing a networking architecture;
- replacing the rendering pipeline;
- changing save ownership/compatibility;
- changing monetization;
- mass-generating production assets;
- expanding class/region scope.

Agents may prototype isolated/reversible alternatives.

### 5. Concept before expensive production

For non-trivial visual or gameplay content:

brief
-> cheap concept/reference
-> human selection
-> production implementation
-> test
-> review.

Do not spend large compute/API budgets on an unapproved direction.

### 6. Test what you change

Every implementation task must define validation.

Preferred Unity loop:
change -> compile -> tests -> Play Mode -> inspect logs/screenshots -> fix -> report.

For systemic changes, test interactions, not only isolated functions.

Examples:
- Wet + Cold;
- Wet + Lightning;
- weather + surface state;
- host/guest persistence;
- boss-safe control mapping.

### 7. Co-op is not a late wrapper

Gameplay architecture must remain compatible with committed co-op.

When adding persistent systems, explicitly consider:
- authority;
- ownership;
- replication;
- save behavior;
- host vs guest state.

### 8. Do not hide failures

Record:
- failed approaches;
- rework;
- API cost if material;
- human intervention;
- new technical debt;
- networking/performance limitations.

Failure information should improve future skills.

### 9. Promote successful workflows into skills

If a repeatable method succeeds, update AI/Skills with:
- prerequisites;
- steps;
- expected outputs;
- review checkpoints;
- common failure modes.

## Engineering principles

- Unity 6 + URP.
- PC is lead Early Access platform.
- Mobile constraints matter architecturally from the start.
- Odin supports data-driven authoring/validation.
- GeNa Pro supports authored biome/dressing rules, not replacement of gameplay level design.
- Feel/MMFeedbacks provides reusable feedback primitives.
- Prefer composition over inheritance.
- Keep gameplay state explicit and testable.
- Avoid large global managers when smaller domain services are enough.
- Keep intentionally disposable prototypes isolated.
- NetworkLab is required during pre-production.

## Definition of done for content

A content item is not done because it appears in the game.

Done means:
- behavior works;
- feedback is readable;
- status/weather/network implications are considered;
- it is testable in a playground;
- errors do not pollute the console;
- configuration is understandable;
- relevant docs are updated;
- benchmark production time/lessons are recorded when appropriate.

## Git workflow

Until revised:
- tiny documentation fixes may go directly to main;
- broad documentation/design changes should use a focused branch/PR;
- implementation work should normally use a focused branch/PR;
- do not mix unrelated refactors with feature work;
- PR descriptions should explain intent, tests and known limitations.

## First implementation targets

Expected sequence:

1. initialize Unity project;
2. integrate baseline tooling;
3. select/prove Unity agent loop;
4. build CombatLab;
5. build NetworkLab;
6. prove Warrior + Vedun primitive attacks;
7. implement status/reaction foundation;
8. implement ornament affinity prototype;
9. build Content/SystemLab;
10. prove procedural first-region assembly;
11. benchmark one folklore enemy end-to-end;
12. benchmark second/third related enemies;
13. evaluate PP-01 exit criteria;
14. build the committed Vertical Slice.
