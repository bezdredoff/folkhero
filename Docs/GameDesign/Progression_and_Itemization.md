# Progression and Itemization

Status: v0.1 — locked progression philosophy for pre-production.

## Core rule

Folkhero uses persistent character progression.

There is no mandatory roguelite build reset between quests/expeditions.

Persistent layers:
- character level;
- equipment;
- skills;
- learned ornaments;
- resources;
- story/world state.

## Character levels

Use ordinary character levels.

Current compact first-game target is approximately 20 levels, but this is a balance hypothesis rather than a locked number.

Levels should:
- unlock capabilities gradually;
- support campaign pacing;
- avoid making raw stat growth the only reason to level.

## Skill progression

Do not build a huge skill tree.

Preferred structure:
- small active kit;
- abilities unlocked through levels and/or important quests;
- 2–3 meaningful modifiers per ability where useful;
- ornament thresholds can change ability affinity/systemic behavior.

Baseline control budget:
- 1 basic attack;
- up to 4 active skills.

Early game / Vertical Slice:
- basic attack + 2 skills per class is sufficient.

## No resource bars initially

Warrior and Vedun begin with:
- basic attacks;
- cooldown-driven skills.

Do not add:
- mana;
- stamina;
- rage;

until prototype evidence shows they add useful rhythm/depth.

## Physical vs affinity builds

Physical is a full build direction, especially for Warrior.

A Warrior must not need an elemental ornament package merely to be viable.

Systemic affinities are overlays/strategies, not replacements for Physical combat.

## Ornament system

Ornaments are the central buildcraft layer.

### Discovery
A player first:
- finds;
- learns;
- earns;
- is taught;

a pattern in the world.

Possible sources:
- quests;
- folklore encounters;
- old textiles/relics;
- artisans;
- regional exploration;
- bosses/dungeons.

### Permanent knowledge
Once learned, a pattern becomes a permanent recipe/known ornament.

It is not a one-use socket gem.

### Application
A community craftsman applies/replaces an ornament for resources.

### Baseline item capacity
- 1 primary ornament per item.

Possible later exception:
- selected rare/unique items may support 2.

## Build-wide affinity

Ornaments contribute affinity weight across the entire equipped set.

The system checks totals, not only the ornament on the weapon currently attacking.

Conceptual example:
- Cold +1;
- Cold +2;
- Curse +1.

At thresholds, the build may gain:
- skill conversion;
- stronger status application;
- new reaction behavior;
- conditional triggers.

Exact numbers are not locked.

## Build shape

Baseline for the first classes:
- one primary affinity;
- one secondary affinity.

This is a balance/design expectation, not a universal engine rule.

Future magical classes may:
- specialize extremely hard into one affinity;
- support multiple primary affinities.

Do not build those classes now.

## Affinity families

Initial:
- Fire;
- Cold;
- Lightning;
- Poison;
- Curse.

Wet is primarily a state/environmental enabler rather than a conventional damage affinity.

Physical remains separate and fully valid.

## Equipment philosophy

Less loot, more meaning.

Equipment should be interesting because of:
- weapon family/behavior;
- ornament;
- systemic synergy;
- special identity;
- future upgrades;

not constant item-level replacement.

A favorite weapon may survive most or all of the campaign.

## Rarity

Use fewer rarity tiers than Diablo-style loot rain.

Working expectation:
- about 3 meaningful tiers;
- exact naming/presentation TBD.

Rarity should not override the more important questions:
- does this item support my build?
- what ornament can it carry?
- does it change behavior?

## Equipment slots

Keep slot count simple.

Current conceptual direction:
- weapon;
- armor;
- 2–3 accessories/talismans.

Exact slot count is not locked and should not block early implementation.

## Slutsk belt

The Slutsk belt must eventually have a meaningful place in the item system.

Possible role:
- culturally important high-value accessory/relic;
- special ornament-bearing item;
- base belt + weave/ornament + blessing/inscription.

Do not implement this before the basic ornament system works.

## Crafting

Only three eventual actions are needed:

1. Apply/change ornament.
2. Upgrade base item stats.
3. Rare special modification that changes/adds behavior.

Implementation order:
1. ornament application;
2. basic upgrades later;
3. special modifications much later.

Avoid broad crafting complexity.

## Inventory

Keep inventory friction low.

Use:
- small equipment storage;
- separate ornament knowledge/library;
- simple resource counters;
- shared stash in hubs.

Do not create an inventory-tetris subgame.

## Economy

Simple baseline:
- 1 regular currency;
- 1–2 common materials;
- a few rare regional/folklore materials.

Avoid:
- many currencies;
- dust;
- shards;
- seasonal token clutter.

## Reward sources

High-value rewards primarily come from:
- bosses;
- main quests;
- side quests;
- dungeons;
- exploration;
- rare events;
- specific craftsmen/merchants.

Ordinary enemies mostly provide:
- currency;
- common materials;
- occasional useful drops.

## Farming

Repeatable farming is intentional.

Important spaces:
- dungeons;
- deep forest / wilderness;
- elite/event encounters.

Farm rewards should emphasize:
- useful materials;
- target ornaments/pattern progress where appropriate;
- occasional meaningful equipment;
- rare regional materials.

Avoid floods of trash loot.

## Defense

Keep stats legible.

- Armor -> Physical.
- Fire resistance.
- Cold resistance.
- Lightning resistance.
- Poison resistance.
- Curse resistance.

No Wet resistance.

## Healing

Baseline:
- limited healing charges/flask-style resource;
- refill/recovery at safe points;
- possible partial health recovery between fights;
- build-based healing later.

Avoid a large potion/food inventory.

## Death penalty

Moderate, not punitive.

On full death:
- respawn at nearest safe point/checkpoint/hub;
- keep level/equipment/ornaments;
- lose some temporary outing resources/consumables;
- area enemies partially recover/reset.

No gear drop.

No run-reset progression loss.

## Co-op progression ownership

Every player keeps personal:
- level;
- equipment;
- ornaments;
- resources;
- XP;
- loot.

The host owns:
- quest state;
- world state;
- narrative consequences.

Guest progression is not lost, but their own campaign is not silently advanced.

## Validation goals

The progression system is successful if:
- changing ornaments meaningfully changes how the same skills play;
- a Physical Warrior remains viable;
- a player can keep a favorite weapon without falling behind purely because of item level;
- farming is rewarding without producing inventory clutter;
- the player can understand why their build is strong in Wet/Cold/Shock/etc.;
- co-op guests keep meaningful character progress without corrupting campaign ownership.
