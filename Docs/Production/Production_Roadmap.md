# Production Roadmap

Status: v0.1.

## Development principle

Each phase removes a different risk.

The sequence is:

Vision Lock
-> AI Production Foundation
-> Gameplay Risk Prototypes
-> System Grammar
-> Content Production Pipeline
-> Production Playgrounds
-> Vertical Slice
-> MVP / Alpha
-> Early Access
-> Live Service.

## Phase 0 — Vision Lock

Prove:
- we can explain the game;
- core pillars are coherent;
- run structure is understood;
- platform and multiplayer assumptions are explicit.

Deliverables:
- Game Vision;
- Game Bible;
- initial System Bible;
- open-decision list.

Exit:
two independent agents reading the repository should describe approximately the same product.

## Phase 1 — AI Production Foundation

Prove:
- agents have a reliable source of truth;
- work can be specialized;
- successful workflows can be captured;
- implementation can be tested.

Deliverables:
- AGENTS.md;
- AI/Roles;
- AI/Skills;
- Unity MCP/tool setup;
- Git workflow;
- production metrics;
- PP-01 backlog.

## Phase 2 — Gameplay Risk Prototypes

Create CombatLab with primitive art.

Validate:
- movement;
- camera;
- basic attack;
- ranged attack;
- AoE;
- dodge/dash;
- damage;
- death;
- hit feedback.

Exit:
combat feels promising without production art.

## Phase 3 — System Grammar

Implement initial reusable primitives.

Ability grammar:
delivery + effects + modifiers + feedback.

Enemy grammar:
chassis + movement + role + attack + defense + status + modifier.

Interaction grammar:
small set of status/environment systems that interact.

Exit:
multiple abilities/enemies can be authored mainly from existing primitives.

## Phase 4 — Content Production Pipeline

Benchmark one real folklore enemy end-to-end:
research -> gameplay role -> concept -> approval -> model -> cleanup -> rig -> animations -> Unity -> behavior -> VFX/SFX -> test -> documentation.

Then produce related enemy #2 and #3.

Exit:
production time should fall significantly rather than remain flat.

## Phase 5 — Production Playgrounds

Create:
- CombatLab;
- ContentLab;
- AnimationVFXLab;
- EncounterLab;
- PerformanceLab;
- optionally NetworkLab.

Exit:
common content can be inspected without playing a whole run.

# Gate A — Ready for Vertical Slice

Required:
- enjoyable primitive combat;
- proven system interactions;
- content production acceleration;
- risky technology tested;
- no core feature depends on a one-off hack.

# Vertical Slice

Target:
- 1 playable hero;
- 1 biome family;
- 3 sub-zones/states;
- 3 weapon families;
- about 6 base enemy roles;
- 5–8 elite modifiers;
- 1 miniboss;
- 1 boss;
- about 20 upgrades;
- 3–4 systemic interactions;
- 20–30 minute run.

Success:
- players want another run;
- another build feels different;
- additional content has predictable cost;
- architecture survives content growth.

# Gate B — Ready for MVP

Required:
- repeat-play intent;
- meaningful build variety;
- content uses factories/frameworks;
- smoke/regression tests;
- reproducible builds;
- agents can complete bounded production tasks and validate them.

# MVP / Alpha

Target:
- 2 characters/archetypes;
- 2 biomes;
- 4–5 weapon families;
- 12–15 enemy archetypes/variants;
- 3–4 bosses/minibosses;
- 40–60 meaningful upgrades;
- 40–60 minute full run;
- meta progression;
- production save system;
- telemetry;
- controller support.

If multiplayer is a core promise, 2-player full-run co-op must work here.

# Gate C — Ready for Early Access production

Required content factories:
- Ability Factory;
- Enemy Factory;
- Encounter Factory;
- Biome Factory;
- Loot Factory;
- VFX library;
- animation library;
- AI skills library;
- automated QA;
- telemetry;
- save migration;
- release pipeline.

# Early Access

Approximate launch target:
- 3 playable characters;
- 3–4 biome families;
- around 6 weapon families;
- 18–24 base enemy types;
- many effective variants through modifiers;
- 5–6 bosses;
- 80–100+ meaningful upgrades;
- complete meta progression;
- proven co-op only if stable.

The product should be sold on replayability, not linear campaign hours.

# Live Service

Cadence hypothesis:
- smaller balance/content patches;
- approximately 3 major folklore chapters per year.

Each major chapter should add a systemic variable, not only assets.

Example structure:
- biome/theme;
- new gameplay system;
- enemy family;
- boss;
- weapon/ability family;
- modifiers;
- encounters.

New systems should modify old content where possible.

# Year 2

Potential expansion areas:
- new character archetypes;
- deeper system interactions;
- world modifiers;
- boss mutations;
- endgame;
- new co-op interactions;
- remixed old biomes.

The live-service plan must remain sustainable for a very small team.
