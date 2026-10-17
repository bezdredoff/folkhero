# PP-01 — Production Foundation

This is the current project milestone.

## Purpose

Build the minimum production system required to begin the committed Vertical Slice responsibly.

PP-01 is complete when the team can create, test and review core solo/co-op gameplay content through a repeatable pipeline.

## Documentation

- [x] repository README
- [x] AGENTS.md
- [x] Game Vision v0.2
- [x] Game Bible v0.2
- [x] System Bible v0.2
- [x] Technical Bible v0.2
- [x] Art Bible framework/direction
- [x] Production Roadmap v0.2
- [x] AI Production System
- [x] first-region direction: Upper Berezina forest-marsh
- [x] first-player direction: Warrior + Vedun
- [x] committed co-op direction
- [x] persistent progression direction
- [ ] approved visual reference set
- [ ] detailed first enemy-family brief
- [ ] detailed Act I quest brief

## Repository / tooling

- [ ] initialize Unity 6 URP project
- [x] add appropriate Unity .gitignore
- [ ] define Unity folder conventions
- [ ] integrate Odin Inspector & Serializer
- [ ] integrate Feel/MMFeedbacks
- [ ] integrate GeNa Pro when region work begins
- [ ] select/connect Unity MCP/tooling
- [ ] validate agent compile/run/test loop
- [ ] establish CI smoke validation

## Gameplay foundation

### Player/camera
- [ ] movement prototype
- [ ] fixed/limited-rotation top-down camera
- [ ] controlled zoom
- [ ] health/damage/death
- [ ] limited healing charges
- [ ] Downed/revive

### Warrior
- [ ] Physical basic melee attack
- [ ] axe/spear prototype decision or minimal representative weapon
- [ ] 2 prototype skills

### Vedun
- [ ] ranged basic attack
- [ ] projectile skill
- [ ] persistent area/ritual skill

### Controls
- [ ] keyboard/mouse abstraction
- [ ] controller abstraction
- [ ] prototype touch-style smart targeting
- [ ] tap smart-cast
- [ ] hold/drag/release manual aim where relevant

Do **not** add a universal dodge/roll unless prototype evidence justifies it.

## Core systemic foundation

- [ ] Physical damage
- [ ] Wet
- [ ] Fire/Burning
- [ ] Cold/Frozen
- [ ] Shock/Lightning
- [ ] Poison
- [ ] Curse
- [ ] Wet + Cold reaction
- [ ] Wet + Lightning reaction
- [ ] Wet + Fire reaction
- [ ] Wet + Poison reaction
- [ ] Frozen + heavy impact -> Shatter
- [ ] Curse overlay behavior
- [ ] boss-safe control/reaction mappings

## Surface/weather foundation

- [ ] Water/Wet surface
- [ ] Snow/Ice surface
- [ ] Fire surface
- [ ] Poisoned Water
- [ ] rain rules
- [ ] cold/winter rules
- [ ] at least one visibly different seasonal/weather state

## Progression/item foundation

- [ ] persistent character level skeleton
- [ ] basic equipment data
- [ ] one ornament per item
- [ ] learned ornament recipe/library
- [ ] build-wide affinity totals
- [ ] affinity threshold changes a skill
- [ ] one-primary/one-secondary build experiment
- [ ] Armor + elemental/curse resistance data
- [ ] simple currency/material data

Defer:
- broad item upgrading;
- special item modification;
- large rarity ladder;
- complex crafting.

## Enemy/system foundation

- [ ] enemy configuration v0
- [ ] enemy capability composition v0
- [ ] human enemy example
- [ ] folklore/spirit enemy example
- [ ] elite modifier v0
- [ ] boss reaction profile v0
- [ ] encounter configuration v0

## Multiplayer foundation

Co-op is committed and cannot be postponed.

- [ ] NetworkLab
- [ ] 2-player host/join
- [ ] movement sync
- [ ] attack/skill sync
- [ ] enemy authority/sync
- [ ] status/reaction sync
- [ ] Downed/revive sync
- [ ] loot ownership
- [ ] guest character progression persistence
- [ ] host quest/world-state ownership
- [ ] disconnect/reconnect experiment

Exact networking technology remains a spike decision.

## Procedural-region foundation

Target: first Upper Berezina forest-marsh region.

- [ ] define authored module grammar
- [ ] define connectivity rules
- [ ] support required authored quest anchor
- [ ] generate variable route/layout
- [ ] place encounters/events by rules
- [ ] support weather/season state
- [ ] define GeNa dressing role
- [ ] deterministic/reproducible seeds where practical

## Playgrounds

- [ ] CombatLab
- [ ] Content/SystemLab
- [ ] AnimationVFXLab
- [ ] EncounterLab
- [ ] ProceduralRegionLab
- [ ] PerformanceLab
- [ ] NetworkLab

## Content pipeline benchmark

Produce Enemy #1 end-to-end.

Record:
- human time;
- agent runtime;
- API/cloud cost;
- iterations;
- rework;
- amount of new code;
- reused primitives;
- failures/lessons.

Then produce Enemy #2 and Enemy #3 from the same/related family.

Success:
later enemies require materially less human effort and bespoke code.

## Ability pipeline benchmark

Produce several abilities across both classes using the same underlying grammar.

Success:
later abilities are primarily data/composition rather than parallel bespoke architectures.

## PP-01 exit criteria

### Gameplay
Primitive Warrior + Vedun combat feels promising.

### Systems
Core statuses/reactions and ornament thresholds create meaningfully different decisions.

### Multiplayer
The 2-player core loop is technically credible.

### World
A small rule-generated forest/swamp space can host an authored anchor and at least two systemic weather/state variations.

### Production
Repeated content shows measurable acceleration.

### Technical
Unity, tests, networking spike and agent tooling are stable enough for continuous work.

### Knowledge
Important successful workflows are recorded as reusable skills.

## Not required for PP-01

Do not expand scope to:
- multiple finished regions;
- full five-act story implementation;
- more playable classes;
- complex crafting;
- final rarity names;
- 4-player production networking;
- final mobile build;
- final UI;
- 10–12 production bosses;
- marketing polish.

Those belong after the production foundation is proven.
