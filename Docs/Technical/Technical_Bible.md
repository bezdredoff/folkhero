# Technical Bible

Status: v0.1 architectural direction.

## Engine

Unity 6, URP.

URP is preferred because the project values broad performance scalability over high-end rendering complexity.

## Lead platform

PC for Early Access.

Controller support should be established early.

Mobile constraints may influence:
- draw calls;
- shader complexity;
- memory;
- enemy counts;
- UI scaling;
- input abstraction.

Mobile shipping is not required to validate the vertical slice.

## Architecture principles

### Data-driven content

Use serialized data definitions for:
- abilities;
- enemy configurations;
- status effects;
- elite modifiers;
- encounters;
- loot/upgrades;
- feedback profiles.

Odin Inspector & Serializer may be used to make these definitions practical to author and inspect.

### Composition over inheritance

Prefer small reusable behaviors/capabilities composed into entities.

Avoid deep inheritance trees such as Enemy -> MeleeEnemy -> PoisonMeleeEnemy -> ElitePoisonMeleeEnemy.

### Separate runtime logic and presentation

Core combat state should not depend on a specific VFX or animation implementation.

Presentation should react to gameplay events.

### Explicit state

Avoid hidden behavior that makes automated testing or save migration difficult.

### Determinism where valuable

Full deterministic simulation is not currently a requirement.

However, systems should support repeatable test setups with fixed seeds/configurations where practical.

## Planned playground scenes

### CombatLab

For:
- movement;
- attacks;
- dodge;
- damage;
- hit reactions;
- game feel.

### ContentLab

For:
- spawning any enemy;
- applying any modifier;
- equipping any weapon;
- testing statuses;
- testing upgrades.

### AnimationVFXLab

For:
- animation clips;
- VFX;
- MMFeedback profiles;
- timing review.

### EncounterLab

For:
- role mixes;
- spawn patterns;
- encounter difficulty;
- hazards.

### PerformanceLab

For stress testing:
- enemy counts;
- particles;
- AI;
- navigation;
- quality presets.

### NetworkLab

Only if multiplayer becomes a core commitment.

## Testing strategy

Initial layers:
- Edit Mode unit tests for pure systems/data validation;
- Play Mode tests for gameplay integration;
- smoke tests for scene loading and core loops;
- automated validation for missing references/config errors;
- screenshot/log review through Unity automation where available.

A future PR should not rely only on "agent says it works".

## AI integration

Preferred control model:
agent -> explicit Unity tools/MCP -> Unity.

Avoid GUI computer-use automation when a structured tool/API exists.

Closed-loop target:
1. edit;
2. compile;
3. run tests;
4. enter Play Mode;
5. capture logs/screenshots;
6. inspect;
7. fix;
8. report.

## Save system

A production save format is required by MVP.

Before Early Access:
- version saves;
- support migrations;
- keep content IDs stable;
- avoid serializing raw scene object assumptions.

## Telemetry

Telemetry should be designed before MVP so design questions can be answered.

Candidate events:
- run start/end;
- death source;
- weapon/ability choice;
- upgrade choice;
- boss result;
- encounter duration;
- damage contribution;
- build composition;
- abandon point.

Collect only what is necessary and compatible with privacy requirements.

## CI

Target CI capabilities:
- project validation;
- automated tests;
- build verification;
- artifact generation where practical.

Exact CI design will be added after Unity project initialization.

## Multiplayer decision

If co-op becomes a pillar, architecture cannot treat networking as a late wrapper.

NetworkLab should validate:
- 2-player join;
- player abilities;
- enemy authority/sync;
- rewards;
- disconnect/reconnect;
- save behavior;
- latency.

If this cannot be proven by MVP, multiplayer should not be promised for Early Access launch.
