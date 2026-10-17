# Technical Bible

Status: v0.2 architectural direction.

## Engine

Unity 6 + URP.

URP is preferred because the project values:
- broad performance scalability;
- PC-first development with later mobile targets;
- restrained rendering complexity;
- reusable stylized materials/VFX.

## Platform strategy

### Lead platform
PC for development and Early Access.

### Mobile
iOS/Android are later targets, but mobile constraints must influence architecture from the start:
- draw calls;
- shader complexity;
- memory;
- enemy counts;
- VFX budgets;
- UI scaling;
- input abstraction;
- thermal/performance targets.

Do not require simultaneous mobile polish for the Vertical Slice.

## Camera

3D top-down/isometric.

Baseline:
- fixed or very limited rotation;
- controlled zoom range;
- camera designed for combat readability and predictable environment production.

Free 360-degree rotation is not a baseline requirement.

## Input architecture

The input layer must support:
- keyboard/mouse;
- controller;
- later touch controls.

Current mobile-style prototype direction:
- movement stick;
- basic attack action;
- up to four skill actions;
- tap -> smart target/cast;
- hold/drag/release -> manual aim where relevant.

Exact target scoring and UI implementation are a prototype task.

Do not hardwire gameplay logic to one input device.

## Multiplayer commitment

Co-op is a committed core feature, not an optional late wrapper.

Long-term target:
- 1–4 players.

Pre-production and Vertical Slice target:
- solo;
- 2-player co-op.

Networking must be validated early.

### Authority goals

The exact networking technology is not yet selected.

Architecture must support authority strong enough for:
- combat state;
- enemy state;
- persistent loot;
- character progression;
- host campaign/world state;
- reconnect/failure handling.

### Campaign ownership

Each player owns persistent character progression:
- level;
- equipment;
- ornaments;
- resources;
- XP/loot.

The host owns:
- quests;
- narrative decisions;
- world-state consequences.

Guests do not automatically advance their personal campaign state.

## Required NetworkLab

NetworkLab is mandatory during pre-production.

Validate at minimum:
- 2-player host/join;
- player movement;
- basic attacks;
- skill/status synchronization;
- enemy authority/synchronization;
- weather/surface state where relevant;
- loot ownership;
- Downed/revive;
- guest progression persistence;
- host world-state ownership;
- disconnect/reconnect behavior;
- latency behavior.

If the core 2-player loop is not technically viable, stop and resolve it before scaling content.

## Architecture principles

### Data-driven content

Use serialized data definitions for:
- abilities;
- skill modifiers;
- status effects;
- reactions;
- surfaces;
- weather rules;
- enemy configurations;
- elite modifiers;
- encounters;
- ornaments;
- items;
- quest objective primitives;
- world-state reactions;
- feedback profiles.

Odin Inspector & Serializer may support practical authoring and validation.

### Composition over inheritance

Prefer small reusable behaviors/capabilities composed into entities.

Avoid deep inheritance such as:
Enemy -> MeleeEnemy -> PoisonMeleeEnemy -> ElitePoisonMeleeEnemy.

### Runtime/presentation separation

Core combat state must not depend on a particular VFX, animation or sound implementation.

Presentation reacts to gameplay events.

### Explicit state

Important gameplay state must be inspectable, serializable and testable.

Especially:
- statuses;
- surfaces;
- affinity totals;
- quest state;
- world state;
- co-op ownership;
- weather state.

### Determinism where useful

Full lockstep determinism is not currently required.

Use repeatable seeds/configurations where they improve:
- procedural-generation tests;
- encounter tests;
- regression reproduction;
- multiplayer diagnostics.

## Gameplay-system priorities

Early runtime foundations should support:
- Physical damage;
- Wet;
- Fire/Burning;
- Cold/Frozen;
- Shock/Lightning;
- Poison;
- Curse;
- reactions;
- surface state;
- weather modifiers;
- boss-safe reaction mappings.

Do not build every future status before these are proven.

## Player combat scope

Initial classes:
- Warrior;
- Vedun.

Initial resource model:
- basic attack;
- cooldown skills;
- no mana/stamina/rage.

Do not implement a universal dodge/roll merely because it is common in action games.

Movement/defense mechanics should be validated against the actual class kits.

## Planned playground scenes

### CombatLab
For:
- movement;
- camera;
- basic attacks;
- skill aiming;
- cooldowns;
- damage;
- healing;
- death;
- Downed/revive;
- feedback.

### SystemLab / ContentLab
For:
- applying any core status;
- forcing reactions;
- spawning surfaces;
- changing weather;
- changing ornament affinity totals;
- spawning any enemy configuration;
- applying elite modifiers.

### AnimationVFXLab
For:
- animation clips;
- VFX;
- MMFeedback profiles;
- status/reaction presentation.

### EncounterLab
For:
- role mixes;
- spawn patterns;
- environmental states;
- weather;
- encounter difficulty;
- co-op scaling experiments.

### ProceduralRegionLab
For:
- authored module connectivity;
- seeds;
- mandatory anchors;
- route generation;
- seasonal/weather overlays;
- encounter placement.

### PerformanceLab
For:
- enemy counts;
- particles;
- AI;
- navigation;
- procedural dressing;
- quality presets;
- representative PC/mobile budgets.

### NetworkLab
Required; see Multiplayer Commitment.

## Testing strategy

Initial layers:
- Edit Mode tests for pure systems and data validation;
- Play Mode tests for gameplay integration;
- deterministic reaction-matrix tests;
- procedural-generation seed tests;
- network smoke tests;
- scene-load tests;
- automated validation for missing references/config errors;
- screenshot/log review through Unity automation where available.

A PR cannot rely only on "the agent says it works."

## Save system

Persistent progression is fundamental.

Before public Early Access:
- version saves;
- support migrations;
- keep content IDs stable;
- persist character level/equipment/ornaments/resources;
- persist host campaign/world state;
- avoid serializing raw scene object assumptions.

Save architecture must account for co-op ownership rules from the start.

## Procedural generation

Target philosophy:
- authored modules;
- rule-based assembly;
- deterministic seeds where practical;
- required authored anchors;
- variable routes/encounters/events/weather.

Do not rely on unconstrained noise generation for gameplay spaces.

GeNa Pro may support dressing/biome rules after gameplay geometry and generation rules are defined.

## Telemetry

Telemetry should answer design questions, not merely collect events.

Candidate events:
- quest/expedition start/end;
- death source;
- Downed/revive;
- class;
- weapon;
- skill loadout;
- ornament affinity composition;
- reaction frequency;
- weather/season state;
- boss result;
- encounter duration;
- damage/status contribution;
- abandon point;
- repeat-farm activity.

Collect only what is necessary and compatible with privacy requirements.

## CI

Target:
- project validation/compile;
- Edit Mode tests;
- Play Mode smoke tests;
- network smoke tests when viable;
- build verification;
- clear logs/artifacts;
- data/schema validation.

Exact CI configuration follows Unity initialization.

## AI integration

Preferred control model:
agent -> explicit Unity tools/MCP -> Unity.

Avoid generic GUI automation when a structured API/tool exists.

Closed loop:
1. edit;
2. compile;
3. run tests;
4. enter Play Mode;
5. capture logs/screenshots;
6. inspect;
7. fix;
8. report.

## Technical decisions still open

Prototype/research rather than speculate:
- networking stack;
- exact touch/targeting implementation;
- exact procedural-generation implementation;
- save transport/backend needs, if any;
- mobile performance budgets;
- server/host model beyond the committed host-owned campaign semantics.
