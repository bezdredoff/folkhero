# Research Notes — Stefan 3D AI Game Development Workflow

Research date: October 2026.

These notes capture useful production patterns from Stefan 3D AI's recent videos. They are not endorsements of every tool or claim.

## Primary video

"This Is How I Actually Make Games With AI - My Setup"
YouTube ID: czsNiALTgWQ
Published: 2026-10-12

## Core pattern

The important idea is not "one model makes a game".

The workflow is built around:
- a persistent local workspace/project folder;
- project context stored with the work;
- GitHub-backed knowledge;
- CLI agents;
- specialized task contexts;
- reusable processes/skills;
- tool integrations through MCP/API;
- visual/interactive reports;
- human review;
- successful experiments added back to project knowledge.

## Repeated workflow learning

A particularly useful habit:

1. attempt a task;
2. iterate until a result is good;
3. identify what made the successful approach work;
4. write that process into project knowledge/skills;
5. use the improved process on the next similar task.

This turns experimentation into cumulative production capability.

## Narrow agent contexts

Stefan separates work such as:
- Unity;
- animation;
- VFX;
- other production areas.

This reduces context noise while all roles still share project knowledge.

Folkhero adaptation:
shared source-of-truth docs + specialized agent roles.

## Unity

Stefan recommends structured Unity agent tooling/MCP instead of generic computer-use clicking.

Useful principle:
agent should be able to edit, compile, test, enter Play Mode, inspect output and iterate.

A Unity playground is especially valuable because agents can validate a bounded thing without navigating a full game.

## Blender / 3D

The same principle applies:
structured Blender/Mixar-style tools plus good task workflows are more efficient than generic GUI control.

A strong model without a production workflow can be slower and less reliable than the same model with task-specific skills.

## Concept-first workflow

In VFX and character work, Stefan often uses:

concept/reference -> review -> production -> playground -> library.

This is important because concept iteration is cheaper than implementing the wrong production direction.

Folkhero should use this for:
- creatures;
- bosses;
- VFX;
- environments;
- animation references;
- UI direction.

## Playgrounds

Observed examples include dedicated spaces for:
- unit/animation review;
- VFX testing.

Folkhero expands this into:
- CombatLab;
- ContentLab;
- AnimationVFXLab;
- EncounterLab;
- PerformanceLab.

## Long autonomous experiments

Related videos show 36–47 hour autonomous runs that can produce large playable prototypes.

The key caveat is preparation:
- detailed design brief;
- many references;
- project instructions;
- connected Unity/Blender/generation tools;
- existing workflows.

These experiments show capability, but they should not be mistaken for the safest daily production process.

Folkhero default:
small bounded tasks with review gates.

## Related videos reviewed

- Building My Game I've Dreamed of for 15 Years with AI - From Absolute Zero (mNjBBO1gWFI)
- Building My Dream Game With AI - Characters & Animations (UBjgJM6D18A)
- You're Using GPT-6 Astra Wrong - This Setup Is Insane (nHBNa2IKWvk)
- This Is What Opus 5.5 Max Built in 36 Hours for 2,175 USD (doR2RhsneRA)
- AI Built My Game in 47 Hours So I Can Destroy Everything (cJH4UgCWrT8)
- AI Can Now Create VFX For Your Game & Characters (ZksPNRPupWs)
- AI Can Do Everything in Blender Now - Mixar (Z8xhELifAVs)

## Tool ideas mentioned in the research

Potentially relevant:
- Unity MCP / Unity CLI-style structured control;
- Blender MCP;
- Mixar;
- Higgsfield MCP;
- fal.ai;
- Tripo;
- local ComfyUI.

Tool selection should be benchmark-driven. Folkhero already has strong local image-generation hardware/workflows, so blindly copying a cloud-heavy stack would be inefficient.

## Conclusion for Folkhero

The major roadmap change from this research is:

pre-production should not end with a GDD and a prototype.

It should end with a small but functioning production factory:
- knowledge;
- agent roles;
- reusable skills;
- data-driven systems;
- playgrounds;
- QA loop;
- content benchmarks;
- documented production velocity.
