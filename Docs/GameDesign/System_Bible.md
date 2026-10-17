# System Bible

Status: v0.1.

The purpose of the System Bible is to define the reusable grammar from which gameplay content is assembled.

## Core rule

A new content item should usually be configuration/composition of known primitives.

New code is justified when the requested behavior is genuinely new and reusable.

## Ability grammar

Candidate delivery primitives:
- projectile;
- area;
- cone;
- dash;
- orbit;
- trap;
- beam;
- summon.

Candidate effect primitives:
- damage;
- knockback;
- pull;
- apply status;
- spawn entity;
- transform state;
- shield;
- heal;
- modify movement;
- trigger secondary effect.

Candidate modifiers:
- count;
- size;
- range;
- speed;
- duration;
- trajectory;
- element;
- trigger condition;
- repeat;
- chaining;
- targeting rule.

Conceptual ability formula:

Delivery + Effect(s) + Modifier(s) + Feedback Profile.

The same mechanical primitive can support different fantasy through data, VFX, SFX and status behavior.

## Enemy grammar

Candidate layers:
- body/chassis;
- locomotion;
- battlefield role;
- attack package;
- defensive package;
- perception/targeting;
- status/element;
- elite modifier;
- feedback profile.

Example:
humanoid chassis + chase + melee role + leap attack + poison + exploding elite modifier.

A different enemy may reuse the same chassis but change movement, range pressure and status.

## Status / interaction grammar

Initial candidates:
- fire/burning;
- cold/freeze;
- wet/water;
- poison;
- physical force/knockback;
- curse.

These are hypotheses, not a locked list.

The important requirement is interaction.

Examples:
- wet + cold -> stronger freeze behavior;
- fire + flammable environment -> hazard;
- knockback + hazard -> environmental damage;
- poison + another effect -> special reaction if it improves readability and build depth.

Every added major system should be reviewed for:
- what old abilities it changes;
- what old enemies it changes;
- what old environments it changes;
- whether it creates new builds.

## Elite modifier system

Elite modifiers are a core content multiplier.

Candidate types:
- elemental;
- explosive on death;
- enraged below threshold;
- summoner;
- shielded;
- aura/support;
- duplicating/spawning;
- movement mutation.

Modifiers must remain readable. Combinatorial quantity is not useful if players cannot understand threats.

## Encounter grammar

Encounter configuration should include:
- enemy roster;
- role mix;
- spawn timing;
- arena tags;
- environmental hazards;
- optional objective;
- difficulty budget;
- reward tier.

The goal is to create encounter variation without bespoke scripting for every room.

## Loot / upgrade grammar

Prefer upgrades that modify behavior.

Low-value example:
+5% damage.

Higher-value examples:
- projectile returns;
- dash creates a trail;
- freeze creates an explosion;
- critical hit spreads curse;
- summons inherit player element;
- status consumption causes a secondary effect.

Simple numerical upgrades may exist but should not dominate build identity.

## Biome grammar

Candidate composition:

Geometry kit
+ vegetation/prop kit
+ material set
+ decals
+ lighting/weather
+ environmental system
+ encounter rules
+ creature pool.

One production kit should ideally produce several visually and mechanically distinct states.

## Feedback grammar

Feel/MMFeedbacks should provide reusable profiles for:
- hitstop;
- camera impulse/shake;
- flash;
- scale punch;
- damage audio;
- death feedback;
- projectile impact;
- level-up;
- elite spawn;
- status application.

Content should reference profiles rather than recreate the same feedback logic.

## Evaluation test

The grammar is working if:
- several different abilities are built without new gameplay architecture;
- several enemies share capabilities but feel tactically different;
- modifiers create readable variation;
- new systems alter old content;
- authoring becomes faster with each repeated task.
