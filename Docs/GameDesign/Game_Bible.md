# Game Bible

Status: v0.2 — player-facing design direction after design-lock discussion. Exact values remain prototype hypotheses unless marked as committed.

## Genre

- story-driven cooperative action RPG / hack-and-slash;
- persistent Diablo-like character progression;
- systemic combat and buildcraft;
- alternate-history folklore fantasy;
- authored campaign supported by procedural/replayable wilderness and dungeons.

This is **not a run-reset roguelite**.

## Player fantasy

The player is not a member of a professional monster-hunting order.

The initial playable archetypes are people from the same remote village and nearby khutors who are forced into a wider conflict after the local political and supernatural order collapses.

Working archetypes:

### Warrior
- returned/retired soldier or veteran;
- melee/cold weapons;
- strong Physical baseline;
- initial weapons: axe and spear.

### Vedun
- folk-magic practitioner / hermit from a nearby khutor;
- ranged attacks and ritual/zone magic;
- interacts more directly with statuses, areas and environmental reactions.

## Core combat controls

Mobile-first simplicity is a design constraint.

Baseline player kit:
- 1 basic attack;
- up to 4 active skill slots;
- early progression may use only 1–2 active skills.

Initial resource model:
- basic attack;
- cooldown-driven active abilities;
- no mana, stamina or rage bars at first.

There is no universal dodge/roll button as a required baseline system.

Mobility and defense can come from:
- class tools;
- weapon behavior;
- specific skills;
- positioning.

## Targeting/input direction

Current prototype direction:
- left virtual stick / movement input;
- large basic-attack action;
- skill buttons;
- tap for smart targeting;
- hold/drag/release for manual aiming where relevant;
- soft auto-targeting for basic attacks and quick casts.

Exact implementation is a technical spike, not yet a dependency choice.

## Damage and defense

### Damage families

Committed baseline:
- Physical;
- Fire;
- Cold;
- Lightning;
- Poison;
- Curse.

Wet is a state, not a damage type.

Physical remains one undivided damage type. Do not split it into slash/pierce/blunt damage.

### Defense

Keep defensive stats simple:
- Armor mitigates Physical;
- separate resistance values for Fire, Cold, Lightning, Poison and Curse.

Avoid early complexity such as:
- armor penetration layers;
- armor classes;
- many overlapping mitigation stats.

## Core statuses and interactions

Initial core set:
- Wet;
- Burning / Fire;
- Cold / Frozen;
- Shock / Lightning;
- Poison;
- Curse.

Initial important reactions:
- Wet + Cold -> Frozen;
- Wet + Lightning -> stronger Shock / Chain behavior;
- Wet + Fire/Burning -> extinguish or suppress Burning;
- Wet + Poison -> poisoned/contaminated water and poison spread;
- Frozen + heavy physical impact -> Shatter;
- Curse can combine with any other core status as a supernatural overlay/modifier.

Bleed may exist later as an additional status but is not a foundational pillar.

## Surfaces

The initial environmental simulation should be deliberately bounded.

Important surface/state families:
- water / wet ground;
- snow / ice;
- fire;
- poisoned water.

Do not attempt full material simulation in the first implementation.

## Weather and seasons

Weather must materially change gameplay.

Examples:
- rain increases Wet prevalence and weakens/suppresses Burning;
- heat/drought dries surfaces faster and increases fire risk/spread;
- cold makes freezing easier;
- deep snow and blizzards affect movement/visibility;
- fog reduces detection and long-range visibility.

Seasonal/weather states are a major content-reuse mechanism.

## Ability progression

Avoid a huge active-skill tree.

Preferred structure:
- abilities unlock through character levels and/or important quests;
- each ability may gain a small number of meaningful modifiers;
- ornament affinity thresholds can transform the systemic type/behavior of abilities.

Example:
the same projectile foundation may become Cold-, Shock- or Curse-oriented depending on the build.

Respec/reconfiguration should be low-friction compared with a hard permanent skill-tree commitment.

## Ornament build system

Ornaments are a central progression layer.

Acquisition model:
1. discover, learn or earn an ornament/pattern in the world;
2. it becomes a permanent recipe/known pattern;
3. an appropriate community craftsman can apply it to compatible equipment for resources.

Baseline:
- one primary ornament per equipment item;
- rare/unique equipment may later support two, if needed.

Ornaments contribute build-wide affinity points/weight.

Reaching affinity thresholds can:
- unlock a skill variant;
- change a skill's systemic type;
- add a reaction behavior;
- strengthen an existing specialization.

Baseline build expectation:
- one primary affinity;
- one secondary affinity.

Future magic-focused classes may intentionally break this rule, but the first two classes do not need that complexity.

Belarusian ornament should be mechanically meaningful, not merely cosmetic.

The Slutsk belt should eventually have a culturally important gameplay role, likely as a high-value accessory/relic or special ornament-bearing item category.

## Equipment philosophy

Loot is less frequent and more meaningful than in Diablo.

Weapons are long-lived platforms.

A good axe or spear found early can remain useful if the player:
- changes ornaments;
- upgrades it later;
- changes build;
- adds later special modifications.

Do not make progression depend on replacing a weapon every few minutes because a new drop has a larger raw number.

Rarity should use fewer tiers than a classic common/magic/rare/legendary ladder. Exact names are still open.

## Crafting scope

Eventual actions:
1. apply/change ornament;
2. upgrade base item stats;
3. rare special modification that changes/adds behavior.

Development priority:
1. ornament application first;
2. ordinary upgrading later;
3. special modification much later.

Avoid a large crafting economy.

## Inventory and economy

Inventory management should be light.

Use:
- small equipment storage;
- separate learned-ornament collection;
- simple material tracking;
- shared stash in hubs.

Avoid inventory tetris and constant junk sorting.

Economy:
- 1 normal currency;
- 1–2 common crafting materials;
- a small number of rare regional/folkloric materials.

Avoid many currencies, dusts, shards and seasonal tokens.

## Loot sources and farming

High-value rewards should primarily come from:
- bosses;
- main and side quests;
- dungeons;
- exploration;
- rare events;
- specific craftsmen/merchants.

Ordinary enemies mostly provide:
- currency;
- materials;
- occasional useful drops.

There must still be deliberate repeatable farming space:
- dungeons;
- deep forest / wilderness;
- elite encounters;
- rare events.

Farm loops should emphasize useful materials, ornaments and occasional meaningful gear rather than floods of disposable items.

## Health, healing and death

### Healing
- limited healing charges/flask-style resource per outing/quest;
- recovery at safe points;
- possible limited between-fight recovery;
- later builds may add regeneration, healing or lifesteal.

Avoid a large consumable inventory.

### Solo/full death
On death:
- respawn at nearest safe point/checkpoint or hub;
- keep level and equipment;
- lose some temporary outing resources/consumables;
- enemies in the area partially recover/reset.

No gear-loss or roguelite progression reset.

### Co-op downed state
Before full death:
- player enters Downed;
- ally can revive after a short interaction;
- if revival fails, use normal respawn logic.

Revive pressure can be tuned later with timer/resource rules.

## Co-op progression

Long-term support target: 1–4 players.

Initial validation: solo + 2-player co-op.

Each player keeps:
- level;
- equipment;
- learned ornaments;
- resources;
- XP/loot earned in the session.

The host owns:
- quest progression;
- world state;
- narrative consequences.

A guest does not automatically advance the same quest in their personal campaign and may replay it later as host.

No friendly fire initially.

## Enemy families

Four major categories for the first game:

1. **Humans**
   - soldiers;
   - bandits;
   - mercenaries;
   - agents of the new authority / military program.

2. **Neutral/territorial spirits**
   - rule-bound;
   - may become hostile when boundaries, pacts or rituals are violated.

3. **Inherently dangerous supernatural creatures**
   - malicious or naturally harmful to humans.

4. **Cursed/corrupted beings**
   - produced or worsened by broken pacts, experiments and supernatural corruption.

## Bosses

Target for the first full game:
- approximately 10–12 bosses total;
- at least one meaningful main-quest boss in each act;
- additional bosses for selected side quests and dungeons.

Not all bosses need equal production cost.

Suggested mix:
- 3–4 major unique region/story-defining bosses;
- remaining bosses built more economically from shared systems plus 1–2 memorable twists.

Bosses must participate in the common status/reaction system.

Do not solve boss balance by making them immune to the player's build.

Control-heavy effects use boss-safe variants:
- brief stagger;
- interrupt;
- vulnerability window;
- reduced-duration response.

## World structure

First full game:
- 3 major reusable regions;
- 5 narrative acts.

Working structure:

### Act I — Home and exile
- ritual/pact conflict;
- sacred place destroyed;
- heroes resist;
- heroes become fugitives;
- community displacement begins.

### Act II — Wider crisis
- first outside region;
- discover similar failures have already happened elsewhere.

### Act III — War administration
- Polotsk / military-administrative space;
- deliberate supernatural exploitation becomes clear.

### Act IV — Escalation and altered familiar places
- revisit old systems/regions under changed war, season and world state.

### Act V — Final conflict and return
- resolve central campaign conflict;
- secure conditions for safe return home.

## Region structure

Working major regions:
1. **Home / Upper Berezina forest-marsh region**
   - inspired by the modern Berezinsky Biosphere Reserve / upper Berezina landscape;
   - springs, bogs, forests, lakes, river headwaters, villages and khutors.

2. **Polotsk region**
   - larger roads;
   - settlements;
   - trade;
   - military administration;
   - fortification.

3. **Border / war zone**
   - forts;
   - camps;
   - damaged villages;
   - refugees;
   - military logistics;
   - most aggressive supernatural experiments.

## Hubs and community

Use compact authored hubs rather than enormous fully simulated cities.

The same core displaced village community moves through the campaign and settles into new regional spaces.

Familiar recurring NPCs include the people who provide:
- trade;
- ornament application;
- future item upgrades;
- services;
- quest and social continuity.

This should preserve the feeling of community and home while the player is displaced.

Do not build a full permanent companion-party system.

Some NPCs may temporarily accompany quests as support characters.

## Procedural wilderness and dungeons

Target philosophy is similar to Path of Exile's modular procedural approach:
- authored modules/tiles/rooms/clearings/landmarks;
- rule-based connectivity;
- procedural routing;
- encounter placement;
- events;
- weather/state selection;
- rewards;
- authored gameplay anchors.

Avoid noise-like fully random maps.

A region must remain recognizable and coherent across generated variants.

## Seasonal reuse

The same modular region should support meaningfully different states such as:
- summer;
- rainy/autumn;
- winter;
- flood.

Variants should change:
- available routes;
- surfaces;
- enemy mixes;
- events;
- weather;
- combat interactions;

not only textures and lighting.

## Quest structure

Main quests:
- authored story and anchor;
- variable journey.

Systemic/repeatable quest grammar can support:
- notice boards;
- random NPC requests;
- wilderness events;
- farming goals.

Useful quest primitives include:
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

## Campaign scope

Target:
- about 8–10 hours mandatory main story;
- about 12–15 hours typical first playthrough with optional content;
- around 3–4 authored main quests per act;
- roughly 15–20 main quests total.

Scope control is more important than campaign length.

## World-state consequences

Use three horizons:

### Local
Affects:
- current quest;
- nearby area;
- immediate NPC/event state.

### Regional
Persists across later visits/acts and changes:
- patrols;
- routes;
- enemies;
- merchants;
- quests;
- visuals;
- safety.

### Campaign
Only a small number, roughly 3–5, should materially alter:
- final conditions;
- political situation;
- epilogue.

Avoid huge branching campaign trees.

## Narrative premise

At home, a ritual at a spring beside a marsh where a river begins maintains an old pact with a local Bolotnik.

The Bolotnik is locally important but not globally unique; other places have their own spirits and agreements.

New authorities suppress/destroy the ritual site.

The heroes resist, but the site is still destroyed and the old balance breaks.

The heroes become fugitives.

As they travel, they learn:
1. this did not happen only to their village;
2. the pattern has existed elsewhere for some time;
3. authorities are breaking local supernatural agreements systematically;
4. higher levels are deliberately exploiting the resulting supernatural chaos/power for military goals.

Knowledge is tiered:
- local officials may sincerely believe the customs are superstition;
- higher levels know the supernatural is real.

The ruler knows and sanctions the broad military purpose, while a dedicated military organization runs the practical program and may hide methods/consequences even from political leadership.

## Return-home payoff

The campaign's emotional long-term goal is safe return.

Two major routes are sufficient:

1. **Patronage**
   - obtain protection from a powerful side able to guarantee safe return.

2. **Gray political change**
   - war or changing power makes return possible without a clean official vindication.

Both return the player to a home that has changed.

## Camera

3D top-down/isometric.

- fixed or very limited rotation;
- controlled zoom in/out;
- readability and performance over cinematic freedom.

## Vertical Slice target

A 20–30 minute representative scenario containing:
- Warrior and Vedun;
- solo and 2-player co-op;
- basic attack + 2 skills per class;
- Physical plus Wet/Fire/Cold/Lightning/Poison/Curse systems;
- at least 3–4 real reactions;
- ornament affinity thresholds;
- rain or snow that materially changes combat;
- small procedurally assembled forest/swamp space;
- one authored quest anchor;
- several normal enemies;
- one elite;
- one boss using boss-safe status reactions;
- downed/revive;
- one familiar community NPC in a mini-hub;
- reward + ornament swap;
- a second run with meaningfully different build/weather behavior.

The slice passes if replaying it with different ornaments and weather is genuinely interesting.

## First Early Access target

- PC-first premium release;
- one complete region;
- one complete Act I;
- about 2–3 hours main story;
- several additional hours of side content/farming/replay;
- two base classes;
- co-op from day one;
- procedural wilderness/dungeons;
- meaningful seasonal/weather states;
- ornament/status/progression systems;
- no planned progression wipe unless a technical necessity is discovered early.

## Current open items

These are not blockers for design lock and should be solved through prototype/research:
- exact rarity tier names and presentation;
- exact Warrior/Vedun final names and visual identity;
- exact networking technology;
- exact target-scoring/input implementation;
- exact status values and affinity thresholds;
- exact item slot count;
- exact first enemy roster;
- exact military occult service name;
- approved visual reference set;
- detailed Act I quest script.
