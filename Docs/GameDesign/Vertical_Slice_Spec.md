# Vertical Slice Specification

Status: v0.1 — committed scope target.

## Purpose

The Vertical Slice is not a miniature version of every planned feature.

It is a **20–30 minute representative scenario** that proves the central product claim:

> The same compact set of systems can create meaningfully different combat, build and replay experiences through class behavior, ornaments, status reactions, weather, procedural layout and co-op.

## Required player classes

### Warrior
- basic Physical melee attack;
- 2 active skills;
- one weapon implementation sufficient for the slice, with axe/spear direction represented;
- strong Physical baseline;
- access to systemic affinity through ornaments.

### Vedun
- basic ranged attack;
- projectile-oriented skill;
- persistent area/ritual skill;
- access to the same systemic affinity framework.

No additional classes.

## Controls

Required:
- movement;
- basic attack;
- 2 skill buttons per class;
- cooldowns;
- smart targeting prototype;
- manual aim for at least one directional/area skill.

No mana/stamina/rage.

No universal dodge requirement.

## Combat systems

Required damage/state foundation:
- Physical;
- Wet;
- Fire/Burning;
- Cold/Frozen;
- Shock/Lightning;
- Poison;
- Curse.

At least 3–4 interactions must be active and clearly readable.

Priority reactions:
- Wet + Cold;
- Wet + Lightning;
- Wet + Fire;
- Frozen + Heavy -> Shatter.

Wet + Poison and Curse overlays should be supported by the architecture even if not all are equally prominent in the first scenario.

## Ornament buildcraft

Required:
- equipment can carry one ornament;
- equipped ornaments contribute build-wide affinity;
- at least one affinity threshold changes a skill or attack behavior;
- player can change an ornament after the scenario/reward;
- second playthrough can use a meaningfully different affinity setup.

## Environment

Theme:
Upper Berezina-like forest/swamp.

Required:
- small procedural/module-assembled route;
- authored quest anchor;
- wet ground/water;
- at least one additional systemic surface;
- weather state that changes combat.

Use either rain or winter/snow as the primary first demonstration.

## Procedural generation

Required:
- authored modules;
- rule-based assembly;
- mandatory start/end/quest anchor;
- variable route or encounter arrangement;
- repeatable seed for debugging.

The map must remain coherent and recognizable.

## Enemies

Required:
- several normal enemies;
- at least two tactical roles;
- one elite;
- one boss.

Enemy content should demonstrate shared capability composition.

The boss must:
- participate in status/reaction systems;
- map hard control to boss-safe effects;
- avoid broad immunity that invalidates the build.

## Co-op

Required:
- solo works;
- 2-player host/join works;
- both classes can play together;
- status/reaction interactions are synchronized;
- Downed/revive works;
- rewards/progression ownership is correct.

The slice should include at least one moment where co-op systemic sequencing is useful, for example:
one player applies Wet/Cold and the other exploits Shock/Shatter.

## Mini-hub/community

Required:
- one familiar recurring community NPC;
- one simple service relevant to the loop, preferably ornament application/change;
- quest setup/return point.

The hub is deliberately tiny.

It exists to prove community continuity, not to simulate a city.

## Reward loop

End of scenario:
- meaningful reward;
- ornament or ornament-related unlock/material;
- opportunity to change build;
- replay invitation.

## Weather/replay requirement

Second playthrough should differ through at least two of:
- different weather;
- different ornament affinity;
- different procedural route;
- different encounter composition.

## Success criteria

The slice passes only if:

### Combat
Both classes are fun enough with placeholder/early art.

### Buildcraft
A different ornament setup changes decisions, not only DPS.

### Systems
Reactions are readable and intentionally exploitable.

### Weather
Weather changes tactics rather than only visuals.

### Procedural world
Repeated layouts feel coherent but not identical.

### Co-op
Two players create useful systemic combinations.

### Production
The scenario is built mostly from reusable systems that can produce the next quest/region content faster.

### Replay
Playtesters have a reason to run the same slice again with a different build/weather state.

## Explicitly out of scope

- full Act I;
- multiple finished regions;
- more than 2 classes;
- full 1–4 player production networking;
- giant loot catalogue;
- final rarity naming;
- complex crafting;
- special item modification;
- full historical city;
- permanent companion party;
- final mobile build;
- 10–12 production bosses.
