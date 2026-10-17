# Folkhero

**Folkhero** is a systems-driven hack-and-slash / roguelike RPG inspired by Belarusian and broader Slavic folklore.

The project is designed for a very small human team working with AI agents. The goal is not to compensate for team size by generating large amounts of disposable content. The goal is to build a reusable **content factory**: data-driven gameplay systems, repeatable asset pipelines, specialized AI agents, automated QA, and strong human approval gates.

## Current phase

**Pre-production — PP-01: Production Foundation**

The first milestone is intentionally not a vertical slice. Before scaling content, the project must prove that:

1. combat can become fun quickly;
2. gameplay systems combine into meaningful emergent interactions;
3. new content becomes cheaper and faster to produce after the first implementation;
4. AI agents can safely work inside repeatable, testable workflows.

See:
- [AGENTS.md](./AGENTS.md)
- [Production Roadmap](./Docs/Production/Production_Roadmap.md)
- [PP-01 Production Foundation](./Docs/Production/PP-01_Production_Foundation.md)
- [Game Bible](./Docs/GameDesign/Game_Bible.md)
- [System Bible](./Docs/GameDesign/System_Bible.md)
- [AI Production System](./Docs/Production/AI_Production_System.md)

## Product philosophy

Folkhero is developed as two products at once:

### 1. The game

A replayable action roguelike / hack-and-slash built around:
- expressive combat;
- systemic interactions;
- build experimentation;
- Belarusian folklore identity;
- strong replayability rather than a large linear campaign.

### 2. The content factory

A production system built around:
- reusable combat primitives;
- data-driven enemies, abilities, encounters and loot;
- reusable animation / VFX / feedback libraries;
- AI-assisted Unity and Blender workflows;
- automated test playgrounds;
- production metrics;
- explicit human approval points;
- successful workflows being promoted into reusable AI skills.

## Target development ladder

```text
Vision Lock
    ↓
AI Production Foundation
    ↓
Combat Prototypes
    ↓
System Grammar
    ↓
Content Pipelines
    ↓
Production Playgrounds
    ↓
Vertical Slice
    ↓
MVP / Alpha
    ↓
Early Access
    ↓
Folklore Chapters / Live Service
```

## Initial technology direction

- **Engine:** Unity 6, URP
- **Authoring:** Odin Inspector & Serializer
- **World / biome tooling:** GeNa Pro
- **Game feel:** Feel / MMFeedbacks
- **AI-assisted development:** Codex / Claude-style CLI agents, Unity MCP, Blender / Mixar-style agent tooling
- **Image production:** local ComfyUI where efficient; cloud APIs when they clearly save human time
- **Source control:** GitHub
- **Lead platform for Early Access:** PC first; controller/mobile constraints considered architecturally, but not allowed to block the vertical slice

Multiplayer remains a design decision gate: if co-op becomes a core product promise, networking must be validated early rather than postponed to the end.

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

Empty folders are represented by README files until implementation begins.

## Working principle

A fast AI-generated implementation is not automatically progress.

A feature is considered successful when it:
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

If every new enemy, weapon or encounter costs the same as the first, the production system is failing even if visible content is increasing.

## Status

This repository currently contains the pre-production foundation derived from project planning and AI-production research. Gameplay implementation starts after PP-01 is sufficiently defined and the Unity project is initialized.
