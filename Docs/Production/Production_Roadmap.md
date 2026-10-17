# Production Roadmap

Status: v0.2.

## Development principle

Each phase removes a different risk.

The project should prove the **game factory** before scaling content.

Sequence:

Vision Lock
-> AI Production Foundation
-> Gameplay + Network Risk Prototypes
-> System Grammar
-> Procedural Region / Content Pipeline
-> Production Playgrounds
-> Vertical Slice
-> MVP / Closed Alpha
-> Early Access
-> Full Campaign Growth
-> Expansions / Long-Term Support.

## Phase 0 — Vision Lock

### Purpose
Make sure two independent agents reading the repository describe approximately the same product.

### Locked direction
- story-driven systemic action RPG / hack-and-slash;
- persistent progression, not roguelite run resets;
- Warrior + Vedun initial classes;
- systemic status/surface/weather combat;
- ornament affinity build system;
- 3 regions / 5 acts for the first full campaign;
- host-based campaign co-op;
- PC-first, mobile-aware;
- premium buy-to-play;
- one-region Act I Early Access launch target.

### Remaining work
- approved art references;
- exact networking technology;
- exact first enemy roster;
- detailed Act I quest scripting;
- numeric balance.

## Phase 1 — PP-01: Production Foundation

Prove:
- agents have reliable source-of-truth documents;
- Unity can be edited/tested through a closed loop;
- core combat primitives are reusable;
- networking can support the committed 2-player slice;
- successful workflows can be captured as skills.

Deliverables:
- AGENTS.md and source-of-truth docs;
- Unity 6 URP initialization;
- Odin + Feel/MMFeedbacks integration;
- CombatLab;
- System/ContentLab;
- NetworkLab;
- initial data schemas;
- CI smoke validation;
- production metrics.

## Phase 2 — Gameplay + Network Risk Prototypes

Use primitive art.

Validate:
- movement;
- fixed/limited-rotation camera + zoom;
- Warrior basic melee;
- Vedun basic ranged;
- cooldown skills;
- smart/manual aiming experiment;
- health/healing/death;
- Downed/revive;
- hit feedback;
- 2-player host/join;
- status synchronization;
- loot/progression ownership semantics.

Do not require production-quality art.

Exit:
the basic solo + 2-player combat loop is promising and technically credible.

## Phase 3 — System Grammar

Implement initial reusable primitives.

Required gameplay foundation:
- Physical;
- Wet;
- Fire/Burning;
- Cold/Frozen;
- Shock/Lightning;
- Poison;
- Curse.

Required reactions:
- Wet + Cold;
- Wet + Lightning;
- Wet + Fire;
- Wet + Poison;
- Frozen + heavy impact;
- Curse overlays.

Implement:
- ability grammar;
- enemy capability grammar;
- boss-safe status responses;
- ornament affinity totals/thresholds;
- one-primary/one-secondary build model;
- simple Armor + resistances;
- weather/system modifiers.

Exit:
Warrior and Vedun can create meaningfully different builds mostly from shared primitives.

## Phase 4 — Procedural Region + Content Pipeline

Build the first-region production grammar.

Target:
Upper Berezina / forest-marsh region.

Prove:
- authored gameplay modules;
- rule-based assembly;
- mandatory quest anchors;
- repeatable wilderness/dungeon generation;
- weather/season overlays;
- GeNa-assisted dressing where useful.

State targets include:
- baseline/summer;
- rainy/autumn;
- winter;
- flood or another wet extreme.

Not every state must be production-complete before the Vertical Slice, but the architecture must support them.

## Phase 5 — Content Production Benchmarks

Produce one folklore enemy end-to-end:
research
-> gameplay role
-> concept
-> approval
-> model/asset
-> cleanup
-> rig/animation
-> Unity
-> behavior
-> VFX/SFX
-> test
-> documentation.

Then produce related Enemy #2 and Enemy #3.

Track:
- human time;
- agent runtime;
- API/cloud cost;
- rework;
- new code;
- reused primitives;
- defects.

Exit:
later related content is materially cheaper/faster to produce.

## Phase 6 — Production Playgrounds

Required:
- CombatLab;
- Content/SystemLab;
- AnimationVFXLab;
- EncounterLab;
- ProceduralRegionLab;
- PerformanceLab;
- NetworkLab.

Exit:
a human or agent can test one enemy/status/build/weather/network interaction without playing the whole campaign.

# Gate A — Ready for Vertical Slice

Required:
- promising primitive combat;
- 2-player networking proven at core-loop level;
- core reaction grammar works;
- ornament thresholds alter builds;
- weather changes gameplay;
- procedural region assembly is coherent;
- content production acceleration is measurable;
- no core slice feature depends on an unreviewed one-off architecture.

# Vertical Slice

Target duration: **20–30 minutes**.

Required:
- Warrior;
- Vedun;
- solo;
- 2-player co-op;
- basic attack + 2 skills per class;
- Physical + six core status/system families;
- at least 3–4 meaningful reactions;
- ornament affinity thresholds;
- rain or snow materially changing combat;
- small procedurally assembled forest/swamp zone;
- one authored quest anchor;
- several normal enemies;
- one elite;
- one boss using boss-safe reactions;
- Downed/revive;
- one familiar community NPC in a mini-hub;
- reward + ornament swap;
- meaningful second playthrough with a different build/weather state.

Success:
- the second run is interesting for systemic reasons;
- Warrior and Vedun feel distinct;
- co-op adds interaction rather than only more damage;
- the architecture survives content growth;
- additional content has increasingly predictable cost.

# Gate B — Ready for MVP / Closed Alpha

Required:
- repeat-play intent;
- meaningful build differences;
- stable 2-player co-op foundation;
- procedural region generation reliable enough for repeated testing;
- save ownership semantics proven;
- smoke/regression tests;
- reproducible builds;
- bounded AI production tasks can be validated with evidence.

# MVP / Closed Alpha

Purpose:
prove a small end-to-end campaign loop inside the first region before public Early Access.

Should include:
- both classes;
- persistent level/equipment/ornament progression;
- hub/community loop;
- several main/side quests;
- repeatable wilderness/dungeon farming;
- weather/season variation;
- meaningful loot/economy;
- multiple boss encounters;
- save migration baseline;
- telemetry;
- 2-player co-op.

Exact content counts should be set after Vertical Slice production benchmarks.

# Gate C — Ready for Early Access

Required:
- stable PC build/release pipeline;
- first region content factory works;
- complete Act I narrative;
- co-op stable enough to be a product promise;
- save migration;
- telemetry;
- performance budgets;
- progression economy;
- repeatable farming loop;
- at least several meaningful weather/season states.

# Early Access Launch

Target:
- PC-first premium release;
- 1 complete region;
- 1 complete Act I;
- about 2–3 hours of main story;
- several additional hours of side content, farming and replay;
- Warrior + Vedun;
- co-op from launch;
- persistent progression;
- ornaments;
- core status/reaction system;
- procedural wilderness/dungeons;
- seasonal/weather variation;
- multiple bosses.

The Early Access launch is sold on depth/reuse of one region, not raw biome count.

# Post-EA campaign growth

Grow toward the first full campaign target:
- 3 regions;
- 5 acts;
- about 8–10 hours mandatory story;
- about 12–15 hours typical first playthrough;
- approximately 10–12 bosses;
- about 15–20 main quests;
- systemic consequences across local/regional/campaign horizons.

Add new regions/acts only when the content factory makes them sustainable.

# Long-term support / expansions

The project may continue for several years.

New chapters/expansions should ideally add:
- a new systemic variable or interaction;
- new enemy family;
- new boss;
- new ornaments/build possibilities;
- new region/state;
- new quest/event combinations.

Prefer additions that also remix old content.

Business model:
- premium base game;
- substantial paid expansions;
- optional cosmetics if useful;
- no sale of power/progression.

## Scope discipline

Do not expand to:
- many classes before Warrior + Vedun are proven;
- many regions before the first region factory works;
- complex crafting before ornaments work;
- deep item rarity ladders;
- large companion-party systems;
- giant handcrafted cities;
- networking postponed until late production.
