# Decision Log

This file records high-impact product decisions so they do not exist only in chat.

## 2026-10-17 — Design lock pass

### Genre / progression
**Decision:** Folkhero is a story-driven systemic co-op action RPG / hack-and-slash with persistent progression.

**Rejected direction:** primary roguelite/run-reset structure.

### Initial classes
**Decision:** Start with only two foundational archetypes:
- Warrior;
- Vedun.

Future classes are out of current scope.

### Warrior weapons
**Decision:** Initial weapon families are axe and spear.

Rogatina and scythe/battle-scythe are saved for later variation.

### Skill controls
**Decision:** Basic attack + up to 4 active skills.

Initial class resource model is cooldown-only.

No mana/stamina/rage at first.

### Universal dodge
**Decision:** No universal dodge/roll requirement.

Mobility/defense can come from class/weapon/skills.

### Physical damage
**Decision:** Physical is one undivided damage type.

Do not split into slash/pierce/blunt.

### Core status/system set
**Decision:**
- Wet;
- Fire/Burning;
- Cold/Frozen;
- Shock/Lightning;
- Poison;
- Curse.

Bleed is deferred.

### Initial reactions
**Decision:**
- Wet + Cold -> Frozen;
- Wet + Lightning -> stronger Shock/Chain;
- Wet + Fire -> suppress/extinguish;
- Wet + Poison -> contaminated water/spread;
- Frozen + Heavy -> Shatter;
- Curse can modify/combine with any core direction.

### Environment
**Decision:** Limited but important systemic surfaces:
- water/wet ground;
- snow/ice;
- fire;
- poisoned water.

Weather materially changes combat.

### Weather
**Decision:** Rain, heat, cold, blizzard/deep snow and fog are gameplay modifiers, not only visuals.

### Ornament model
**Decision:** Hybrid learned-recipe model.

Find/learn an ornament once -> it becomes permanent knowledge -> community craftsman can apply it for resources.

### Ornament slots
**Decision:** Baseline one primary ornament per equipment item.

Possible rare/unique double-ornament exception later.

### Affinity totals
**Decision:** Ornament affinities are summed across the entire equipped build.

Thresholds can change skill behavior/type.

### Build specialization
**Decision:** Baseline build supports one primary + one secondary affinity.

Future magic classes may intentionally break this rule.

### Item longevity
**Decision:** Weapons are long-lived platforms and can remain useful for a large part of the game.

Avoid constant stat-stick replacement.

### Rarity
**Decision:** Use fewer rarity tiers because loot is less frequent/more meaningful.

Exact naming remains open.

### Crafting
**Decision:** Eventual actions:
1. apply/change ornament;
2. upgrade base stats;
3. rare special modification.

Implementation priority is ornament first, upgrades later, special modification much later.

### Inventory
**Decision:** Minimal inventory friction; separate ornament library; shared hub stash.

### Economy
**Decision:** 1 normal currency, 1–2 common materials, few rare regional/folklore materials.

### Loot/farming
**Decision:** Best rewards often come from bosses/quests/dungeons/exploration/events, but repeatable farming in dungeons and wilderness is intentionally supported.

### Procedural generation
**Decision:** Use a Path-of-Exile-like philosophy:
authored modules + rule-based assembly + authored anchors + procedural route/encounter/event/weather variation.

### Enemy categories
**Decision:** Four major content categories:
1. humans;
2. neutral/territorial spirits;
3. inherently dangerous supernatural creatures;
4. cursed/corrupted beings.

### Boss count
**Decision:** First full game target ~10–12 bosses.

At least one meaningful main-quest boss per act plus selected side/dungeon bosses.

### Boss status rules
**Decision:** Bosses participate in the same status/reaction system.

Strong crowd-control maps to boss-safe reduced effects rather than broad immunity.

### Defense
**Decision:** Armor for Physical plus individual Fire/Cold/Lightning/Poison/Curse resistances.

### Healing
**Decision:** Limited healing charges, safe-point recovery, later build-based healing.

### Death
**Decision:** Moderate checkpoint penalty; keep level/equipment; lose some temporary outing resources; partial enemy reset.

### Co-op Downed
**Decision:** Downed/revive before full respawn.

### Camera
**Decision:** Fixed/limited-rotation 3D top-down/isometric camera with controlled zoom.

### Art direction
**Decision:** Deliberately stylized, chosen partly for AI-assisted/modular/procedural production and mobile scalability.

### World structure
**Decision:** First full game target:
- 3 major reusable regions;
- 5 acts;
- ~8–10 hours mandatory story;
- ~12–15 hours typical first playthrough.

### Main quest structure
**Decision:** Fixed story + variable journey.

### Consequences
**Decision:** Medium-strength systemic consequences with local, regional and a small number (~3–5) of campaign-level decisions.

### Narrative setting
**Decision:** Alternate-history late GDL / early PLC, using the Livonian War as historical skeleton.

Real historical names/events may be used.

### Inciting incident
**Decision:** A ritual at a spring/marsh maintains a pact with a local Bolotnik. New authority destroys/suppresses the site; heroes resist; pact breaks; heroes become fugitives.

### Military program
**Decision:** Higher leadership knows the supernatural is real and sanctions deliberate military exploitation; a dedicated military organization runs operations.

### Home/displacement
**Decision:** Home is not destroyed; it becomes politically inaccessible.

The displaced village community is a recurring hub/social anchor.

### Return-home ending
**Decision:** Only two major routes:
1. protection/patronage from an influential side;
2. gray political change that makes return possible.

### Companions
**Decision:** No permanent controllable companion-party system.

Temporary support NPCs are allowed.

### Hubs
**Decision:** The same core displaced community reappears in changing regional hubs.

### Platform
**Decision:** PC-first development/Early Access; mobile-aware architecture; iOS/Android later.

### Co-op commitment
**Decision:** Co-op is required in the first Early Access release and must be validated early.

Long-term target 1–4; initial focus solo + 2-player.

### Co-op campaign ownership
**Decision:** Character progression belongs to each player; quest/world-state progression belongs to the host.

### Early Access scope
**Decision:** One region is enough for first EA if it proves seasonal/weather/systemic reuse.

First EA includes a complete Act I with ~2–3 hours main story plus side/farm/replay content.

### Monetization
**Decision:** Premium buy-to-play.

No sale of power, ornaments, loot, energy or progression acceleration.

### Vertical Slice
**Decision:** 20–30 minute slice with:
- Warrior + Vedun;
- solo + 2-player co-op;
- basic attack + 2 skills/class;
- core statuses/reactions;
- ornament thresholds;
- meaningful weather;
- procedural forest/swamp;
- authored quest anchor;
- normal enemies + elite + boss;
- Downed/revive;
- community NPC mini-hub;
- reward/build swap;
- meaningful replay.

## Open prototype/research decisions

These are intentionally not locked yet:
- final class names;
- exact rarity names/colors;
- exact networking technology;
- exact target-selection algorithm;
- exact status/affinity numeric thresholds;
- exact equipment slot count;
- exact first enemy roster;
- exact military service name;
- final visual reference board;
- detailed Act I quest scripts.


## 2026-10-18 — Systemic 3D art-direction lock

### Rendering / production language
**Decision:** Folkhero uses simple modular 3D with large readable forms, flat/soft-shaded materials, restricted palette and low texture noise.

**Rejected as production target:** painterly/illustrative rendering that requires dense unique detail or makes gameplay assets read as 2D art.

### Asset multiplication
**Decision:** Prefer a small number of reusable base meshes multiplied through:
- modular attachments;
- palette/material parameters;
- weather/season states;
- damage;
- gameplay status;
- corruption.

### Historical silhouette
**Decision:** Simplification must preserve historically plausible late-16th-century regional silhouettes and construction logic, especially architecture and clothing.

### Mobile readability
**Decision:** Art is authored for top-down mobile readability first. Large shape/color masses outrank micro-detail.

### Corruption
**Decision:** The “Cursed Treasures” dark/corrupted visual language is a reusable overlay/state, not a separate base rendering style.

### VFX
**Decision:** Persistent state VFX stay restrained. Bright effects are primarily reserved for short gameplay reactions, attacks and telegraphs.
