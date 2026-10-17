# Game Bible

Status: v0.1 pre-production.

This document describes the intended player-facing structure. Exact values are placeholders until prototypes and playtests validate them.

## Genre

- action roguelike / hack-and-slash;
- systemic buildcraft;
- folklore fantasy;
- run-based progression with meta progression.

## Core loop

Moment to moment:
move -> position -> attack -> react -> exploit statuses/environment -> collect reward -> choose next threat.

Encounter loop:
enter encounter -> identify pressure -> combine build tools -> defeat enemies -> select reward.

Run loop:
start run -> build character -> traverse regions/encounters -> defeat boss -> receive persistent reward/unlock -> start a new run with new possibilities.

## Run duration targets

Vertical Slice: approximately 20–30 minutes.

MVP: approximately 40–60 minutes for a full run.

These are hypotheses to test rather than promises.

## Combat principles

- readable danger;
- responsive input;
- meaningful movement;
- limited but strong defensive options;
- good hit feedback;
- enemies differentiated by battlefield role;
- player power increases should change decisions, not only damage numbers.

## Player build structure

Likely layers:
- character/archetype;
- weapon family;
- active abilities;
- passive modifiers;
- status/element specialization;
- run upgrades;
- persistent unlocks.

Build variety should come from combinatorial behavior.

## Enemy design

Enemies should be created from reusable capabilities where possible.

High-level enemy formula:

Body/chassis
+ locomotion
+ combat role
+ attack package
+ defense package
+ status/element
+ elite modifier

Initial role candidates:
- melee pursuer;
- fast flanker;
- ranged pressure;
- tank/blocker;
- support;
- disruptor/summoner.

## Encounter design

Encounters should be configurations of:
- enemy roles;
- spawn patterns;
- terrain;
- hazards;
- objectives;
- modifiers.

Avoid treating every encounter as a bespoke script.

## Bosses

Bosses should test understanding of systems already introduced and add one or two new rule twists.

Boss production should not be benchmarked as ordinary enemy production; bespoke mechanics are acceptable when justified.

## Biomes

A biome is not only an art set.

A biome should define:
- encounter grammar;
- traversal/hazard rules;
- system emphasis;
- art kit;
- lighting/weather;
- creature families;
- music/audio identity;
- reward tendencies.

## Progression

### In-run progression

Primary purpose: change build behavior during the run.

### Meta progression

Primary purpose:
- unlock possibilities;
- provide long-term goals;
- reveal folklore/world;
- widen viable strategies.

Avoid making permanent stat grinding the sole long-term progression.

## Narrative

Narrative structure is not yet locked.

Current preference:
- concise run-compatible storytelling;
- worldbuilding through places, creatures, rituals and item context;
- enough narrative identity to make folklore meaningful without requiring long interruptions to combat.

## Vertical Slice target

Approximate content:
- 1 playable hero;
- 1 biome family with 3 visual/subsystem states;
- 3 weapon families;
- about 6 base enemy roles;
- 5–8 elite modifiers;
- 1 miniboss;
- 1 boss;
- around 20 upgrades;
- 3–4 systemic interactions;
- 20–30 minute run.

Success is not "all content exists".

Success is:
- player wants another run;
- another build plays differently;
- production of additional content is demonstrably faster than the first content.

## MVP target

Approximate content:
- 2 playable archetypes;
- 2 biomes;
- 4–5 weapon families;
- 12–15 enemy archetypes/variants;
- 3–4 bosses/minibosses;
- 40–60 meaningful upgrades;
- meta progression;
- save system;
- telemetry;
- controller support;
- full 40–60 minute run.

## Open design decisions

- exact camera perspective and movement feel;
- exact death/respawn structure;
- how much procedural generation versus authored layout;
- multiplayer/co-op commitment;
- persistent progression economy;
- narrative framing;
- character roster and hero fantasy;
- exact first biome and first folklore enemy family.
