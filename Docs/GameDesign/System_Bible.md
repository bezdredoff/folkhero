# System Bible

Status: v0.2.

The System Bible defines the reusable grammar from which player abilities, enemies, environments, loot and encounters are assembled.

## Core rule

A new content item should normally be configuration/composition of known primitives.

New runtime code is justified when the requested behavior is:
- genuinely new;
- readable;
- reusable by several future content pieces.

The game should not require a unique architecture for every weapon, enemy, boss or quest.

## Damage grammar

Primary damage families:
- Physical;
- Fire;
- Cold;
- Lightning;
- Poison;
- Curse.

Wet is a state, not a damage family.

Physical remains one unified type.

Do not split Physical into slash/pierce/blunt damage.

## Status grammar

Initial core states:
- Wet;
- Burning;
- Cold / Frozen;
- Shock;
- Poison;
- Curse.

Bleed is deferred as a possible later status.

Where useful, Burning, Poison and future Bleed may share generic damage-over-time runtime primitives while preserving different tags, visuals and interactions.

## Core interaction matrix

Do not require every state to react with every other state.

Prioritize a small number of readable, intentional interactions.

### Wet + Cold
Result:
- Frozen target and/or ice surface;
- Cold thresholds can be easier to reach when already Wet.

### Wet + Lightning
Result:
- stronger Shock behavior;
- chaining/spread through valid nearby wet targets/surfaces.

### Wet + Fire/Burning
Result:
- extinguish;
- suppress Burning;
- reduce fire persistence where appropriate.

### Wet + Poison
Result:
- contaminated/poisoned water;
- poison spreads through valid wet surfaces/targets.

Poison does not need broad chemistry interactions with every element in the first version.

### Frozen + Heavy impact
Result:
- Shatter;
- increased burst/stagger/secondary effect depending on target type.

### Curse + any core system
Curse is a supernatural overlay.

It may modify:
- Wet;
- Fire;
- Cold;
- Lightning;
- Poison;
- Physical effects.

Avoid treating Curse as only another colored damage element.

## Boss-safe reactions

Bosses participate in the same systemic grammar.

Do not use broad immunities to invalidate builds.

Strong control reactions map to reduced boss-safe outcomes such as:
- stagger;
- interrupt;
- vulnerability window;
- partial duration;
- meter contribution.

## Surface grammar

Initial surface families:
- Water / Wet Ground;
- Snow / Ice;
- Fire;
- Poisoned Water.

Surface state must be:
- readable;
- bounded in simulation cost;
- useful to both combat and weather.

Avoid simulating every material in the environment.

## Weather grammar

Weather is a ruleset modifier.

Examples:

### Rain
- increases Wet application/prevalence;
- creates/maintains wet surfaces;
- weakens fire persistence;
- changes encounter assumptions.

### Heat / drought
- dries surfaces faster;
- increases fire risk/spread;
- changes vegetation/material state.

### Cold
- makes freezing easier;
- increases snow/ice persistence;
- changes route/surface behavior.

### Blizzard / deep snow
- reduces visibility;
- affects movement;
- changes encounter ranges.

### Fog
- reduces perception/detection;
- reduces effective long-range visibility.

The exact numeric effects are data, not bespoke weather code in every system.

## Ability grammar

Candidate delivery primitives:
- melee;
- projectile;
- area;
- cone;
- line;
- chain;
- aura;
- movement/dash when a specific skill needs it;
- summon later if required.

Candidate effects:
- damage;
- apply status;
- spawn surface/entity;
- push / movement;
- modify state;
- heal;
- shield;
- trigger secondary effect.

Candidate triggers:
- OnHit;
- OnCrit;
- OnKill;
- OnDamageTaken;
- OnCast;
- OnStatusApplied;
- OnReaction;
- OnEnterArea.

Candidate modifiers:
- count;
- size;
- range;
- speed;
- duration;
- trajectory;
- affinity/system type;
- trigger condition;
- repeat;
- chaining;
- targeting rule;
- scaling rule.

Conceptual formula:

Delivery + Shape + Effect(s) + Status/Affinity + Trigger(s) + Modifier(s) + Feedback Profile.

## Player-class use of the grammar

### Warrior

Primary identity:
- melee;
- Physical damage;
- weapon reach/cadence;
- stagger;
- heavy impact;
- Shatter;
- optional elemental/curse overlays from ornaments.

A Warrior must remain viable as a mostly Physical build.

Initial weapon families:
- axe;
- spear.

Weapon differentiation should come from:
- reach;
- speed;
- attack shape;
- stagger;
- moveset;
- tags;
- special behavior;

not separate slash/pierce damage systems.

### Vedun

Primary identity:
- ranged/ritual control;
- projectile;
- persistent area;
- more direct application/manipulation of systemic states.

Both classes may use the same affinities but create different tactical patterns.

## Skill-slot and cooldown grammar

Baseline:
- one basic attack;
- up to four active skills;
- cooldowns as the first resource model.

Do not add mana/stamina/rage until playtesting proves a need.

A class-specific resource may be introduced later only if it adds meaningful rhythm/depth.

## Ornament affinity grammar

An ornament contributes affinity weight to the entire equipped build.

Example conceptual totals:
- Cold Affinity;
- Lightning Affinity;
- Poison Affinity;
- Curse Affinity;
- Fire Affinity.

Thresholds can activate:
- skill conversion;
- extra status application;
- reaction amplification;
- conditional triggers;
- secondary behavior.

Baseline build shape:
- one primary affinity;
- one secondary affinity.

This is a design norm, not an engine hard-limit for all future classes.

## Ornament acquisition grammar

Ornaments are learned patterns, not disposable sockets.

Flow:
discover/earn pattern
-> pattern added to permanent knowledge
-> craftsman can apply pattern
-> player reconfigures equipment/build.

Baseline item rule:
- one primary ornament per item.

Possible later exception:
- selected rare/unique items support two.

## Item grammar

An equipment item should be understood as:

Base Item
+ Weapon/Armor Behavior
+ Base Stats
+ Ornament
+ later Upgrade Level
+ much-later Special Modification.

Do not make rarity the main identity of equipment.

Use fewer rarity tiers than classic loot-rainbow systems.

## Progression grammar

Persistent progression:
- character level;
- equipment;
- skills;
- ornaments/recipes;
- resources;
- story/world state.

Skills unlock through:
- levels;
- important quests;
- potentially class milestones.

Skill depth should come from a small number of meaningful modifiers rather than a huge active-skill list.

## Defense grammar

- Armor -> Physical mitigation.
- Fire Resistance.
- Cold Resistance.
- Lightning Resistance.
- Poison Resistance.
- Curse Resistance.

Wet has no resistance stat because it is a state.

## Healing/death grammar

### Healing
- limited healing charges;
- safe-point restoration;
- possible partial between-fight recovery;
- build-based healing later.

### Death
- respawn at safe point/checkpoint/hub;
- keep persistent character progression;
- lose some temporary outing resources;
- partial encounter recovery/reset.

### Co-op Downed
- ally revive before full respawn.

## Enemy grammar

Candidate composition:

Chassis
+ Locomotion
+ Battlefield Role
+ Attack Package
+ Defense Package
+ Perception/Targeting
+ Status/Affinity
+ Elite Modifier
+ Feedback Profile.

Initial battlefield role candidates:
- melee pursuer;
- fast flanker;
- ranged pressure;
- tank/blocker;
- support;
- disruptor/summoner.

## Enemy family categories

Content/lore categories:
1. humans;
2. neutral/territorial spirits;
3. inherently dangerous supernatural creatures;
4. cursed/corrupted beings.

These categories should reuse gameplay primitives rather than require separate architecture.

## Elite modifier grammar

Candidate elite modifiers:
- affinity/status mutation;
- explosive death;
- enraged below threshold;
- aura/support;
- shielded;
- summoner;
- duplicating/spawning;
- movement mutation;
- cursed overlay.

Modifiers must remain readable.

## Boss grammar

A boss may use:
- shared movement primitives;
- shared status/reaction rules;
- shared attack/effect primitives;
- one or two bespoke twists;
- a unique presentation/arena when justified.

Major story bosses may justify more bespoke content than side/dungeon bosses.

## Encounter grammar

Encounter configuration:
- enemy roster;
- role mix;
- spawn timing;
- arena tags;
- environmental surfaces;
- weather state;
- optional objective;
- difficulty budget;
- reward tier;
- world-state modifiers.

Variation should come from composition, not one script per encounter.

## Quest grammar

Reusable objective primitives may include:
- Find;
- Track;
- Hunt/Kill;
- Protect;
- Escort;
- Collect;
- Investigate;
- Cleanse;
- Survive;
- Perform Ritual;
- Deliver;
- Rescue;
- Choose;
- Return.

Main quests use authored narrative anchors.

Repeatable/low-cost content may combine primitives more aggressively.

## World-state grammar

Candidate persistent variables include:
- HumanInfluence;
- SpiritInfluence;
- Corruption;
- Flooding;
- ForestHealth;
- VillageSafety;
- LocalSpiritDisposition;
- PoliticalHeat;
- LocalSupport.

Content should react declaratively.

Examples:
- high Corruption -> cursed modifiers, visual corruption, altered events;
- high Flooding -> more Wet surfaces, water spirits, blocked/alternate paths;
- high LocalSupport -> hidden routes, shelter, cheaper/special services;
- high PoliticalHeat -> checkpoints, patrols, bounty hunters.

## Procedural-region grammar

A generated wilderness/dungeon is not arbitrary noise.

Composition:

Authored Modules
+ Connectivity Rules
+ Required Anchors
+ Route Rules
+ Encounter Tables
+ Event Tables
+ Weather/Season State
+ World-State Modifiers
+ Dressing Rules
+ Reward Rules.

This follows a Path-of-Exile-like philosophy:
- authored pieces;
- rule-based assembly;
- coherent identity;
- meaningful variation.

## Biome/region grammar

Region content:

Geometry Kit
+ Vegetation/Prop Kit
+ Material State
+ Decals
+ Lighting
+ Weather
+ Seasonal State
+ Environmental Rules
+ Encounter Rules
+ Creature Pool
+ World-State Overlay.

One good kit should create several visually and mechanically distinct states.

## Feedback grammar

Feel/MMFeedbacks should provide reusable profiles for:
- hitstop;
- camera impulse/shake;
- flash;
- scale punch;
- damage audio;
- death;
- projectile impact;
- status application;
- reaction trigger;
- elite spawn;
- boss phase;
- objective completion;
- level-up.

Content should reference profiles rather than rebuild feedback logic.

## Evaluation test

The grammar is working if:
- several abilities can be authored without new parallel architectures;
- Warrior and Vedun use the same primitives but feel tactically different;
- bosses respect the player's systemic build without being trivialized;
- the same region plays differently under rain, winter and flood states;
- changing ornaments changes skill behavior;
- enemies reuse substantial code/assets while remaining tactically distinct;
- new world-state variables alter existing content;
- authoring becomes measurably faster with repeated content.
