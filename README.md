# Folkhero

**Languages:** English (canonical) · [Русский](./ru/README.md)

**Folkhero** is a story-driven cooperative systemic action RPG / hack-and-slash inspired by Belarusian and wider Slavic folklore, set in an alternate-history late Grand Duchy of Lithuania / early Polish–Lithuanian Commonwealth world.

The project is designed for a very small human team working with AI agents. The goal is not to compensate for team size by generating large amounts of disposable content. The goal is to build a reusable **content factory**: data-driven gameplay systems, modular procedural regions, repeatable asset pipelines, specialized AI agents, automated QA, and strong human approval gates.

## Current phase

**Pre-production — PP-01: Production Foundation**

The first milestone is intentionally not a production-heavy vertical slice. Before scaling content, the project must prove that:

1. combat can become fun quickly;
2. Warrior and Vedun can share reusable systems while feeling distinct;
3. status/surface/weather interactions create meaningful decisions;
4. ornament-driven buildcraft changes behavior rather than only numbers;
5. 2-player co-op is technically credible early;
6. procedural region/content pipelines make repeated content cheaper to produce;
7. AI agents can safely work inside repeatable, testable workflows.

See:
- [AGENTS.md](./AGENTS.md)
- [Game Vision](./Docs/Vision/Game_Vision.md)
- [World and Narrative Bible](./Docs/Vision/World_and_Narrative.md)
- [Game Bible](./Docs/GameDesign/Game_Bible.md)
- [System Bible](./Docs/GameDesign/System_Bible.md)
- [Progression and Itemization](./Docs/GameDesign/Progression_and_Itemization.md)
- [Vertical Slice Specification](./Docs/GameDesign/Vertical_Slice_Spec.md)
- [Technical Bible](./Docs/Technical/Technical_Bible.md)
- [Art Bible](./Docs/Art/Art_Bible.md)
- [Production Roadmap](./Docs/Production/Production_Roadmap.md)
- [PP-01 Production Foundation](./Docs/Production/PP-01_Production_Foundation.md)
- [Decision Log](./Docs/Production/Decision_Log.md)
- [Early Access and Long-Term Support](./Docs/LiveOps/Early_Access_and_Live_Service.md)
- [AI Production System](./Docs/Production/AI_Production_System.md)
- [Documentation Translation](./Docs/Production/Documentation_Translation.md)

## Product direction

### The game

A persistent-progression hack-and-slash built around:
- expressive combat;
- systemic status/surface/weather interactions;
- ornament-based build experimentation;
- authored story with variable procedural journeys;
- Belarusian folklore identity;
- cooperative play;
- reusable regions that change through season, weather and world state.

The game is **not primarily a roguelite**. Character level, equipment, skills and learned ornaments persist.

### The content factory

A production system built around:
- reusable combat primitives;
- data-driven enemies, abilities, encounters and loot;
- authored modules assembled by procedural rules;
- reusable animation / VFX / feedback libraries;
- AI-assisted Unity and Blender workflows;
- automated test playgrounds;
- production metrics;
- explicit human approval points;
- successful workflows promoted into reusable AI skills.

## First playable scope

Initial player archetypes:
- **Warrior** — Physical-first melee foundation, starting from axe/spear;
- **Vedun** — ranged folk-magic foundation using projectile and persistent ritual/area tools.

Initial systemic layer:
- Physical;
- Wet;
- Fire/Burning;
- Cold/Frozen;
- Shock/Lightning;
- Poison;
- Curse.

The first region is an Upper-Berezina-like forest-marsh landscape with meaningful rain, winter, flood and other systemic state variation.

## Target development ladder

```text
Vision Lock
    ↓
PP-01 Production Foundation
    ↓
Gameplay + Network Risk Prototypes
    ↓
System Grammar
    ↓
Procedural Region / Content Pipeline
    ↓
Production Playgrounds
    ↓
Vertical Slice
    ↓
MVP / Closed Alpha
    ↓
Early Access — 1 Region / Complete Act I
    ↓
Full 3-Region / 5-Act Campaign Growth
    ↓
Expansions / Long-Term Support
```

## Vertical Slice target

A 20–30 minute representative scenario with:
- Warrior + Vedun;
- solo + 2-player co-op;
- basic attack + 2 skills per class;
- systemic status reactions;
- ornament affinity thresholds;
- meaningful weather;
- a small procedurally assembled forest/swamp route;
- one authored quest anchor;
- normal enemies, elite and boss;
- Downed/revive;
- a familiar community NPC mini-hub;
- replay with a different build/weather state.

## Early Access direction

- PC first;
- one complete region is enough;
- one complete Act I;
- ~2–3 hours main story plus side/farm/replay content;
- co-op from launch;
- persistent progression;
- seasonal/weather reuse;
- premium buy-to-play.

Mobile remains a later target, but architecture, input and performance must stay mobile-aware.

## Initial technology direction

- **Engine:** Unity 6, URP
- **Authoring:** Odin Inspector & Serializer
- **World / biome tooling:** GeNa Pro
- **Game feel:** Feel / MMFeedbacks
- **AI-assisted development:** structured Unity/Blender tooling and project-local agent workflows
- **Image production:** local ComfyUI where efficient; cloud APIs when they clearly save human time
- **Source control:** GitHub
- **Lead platform for Early Access:** PC
- **Networking:** committed requirement; exact stack still to be selected by spike

## Repository layout

```text
/Docs
  /Vision
  /GameDesign
  /Technical
  /Art
  /Production
  /Research
  /LiveOps

/AI
  /Roles
  /Skills
  /Checklists
  /Knowledge

/References
/Experiments
/Tools
/UnityProject
```

## Working principle

A fast AI-generated implementation is not automatically progress.

A feature is successful when it:
- fits the game vision;
- reuses existing primitives where possible;
- is testable;
- is documented;
- does not introduce avoidable bespoke architecture;
- makes the next similar piece of content easier to produce.

The desired trend is:

```text
Enemy #1: expensive learning
Enemy #2: faster
Enemy #3: substantially faster
```

If every new enemy, weapon, quest or encounter costs the same as the first, the production system is failing even if visible content is increasing.
