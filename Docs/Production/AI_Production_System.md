# AI Production System

Status: v0.1.

## Goal

Use AI to increase validated production throughput, not to maximize generated artifacts.

The preferred operating model is a persistent project workspace:
- repository context;
- specialized agents;
- explicit tools/APIs;
- reusable skills;
- cheap concept iteration;
- human approval;
- automated validation;
- lessons written back into the project.

## Core loop

Human intent
-> director/spec
-> reference/concept
-> human approval
-> specialist implementation
-> Unity/Blender/other tool execution
-> tests/playground
-> logs/screenshots
-> human review
-> merge
-> successful method becomes a reusable skill.

## Agent roles

Initial roles:
- Director;
- Unity Engineer;
- Combat/Content Designer;
- Technical Artist;
- QA.

Later:
- Lore/Research;
- Level/Encounter Designer;
- Economy/Balance;
- LiveOps.

See AI/Roles/README.md.

## Context strategy

Do not create one giant agent context containing everything.

Use:
- shared source-of-truth docs;
- specialized task context;
- project-local skills;
- linked references.

A Unity agent does not need the full lore corpus for a serialization bug. A lore agent does not need all Unity API details.

## Concept -> Approve -> Produce

For expensive or subjective work:
1. define intent;
2. produce cheap alternatives;
3. choose one direction;
4. only then spend time/credits on production;
5. validate in context.

Examples:
- boss concept before production model;
- VFX concept before Shader/VFX implementation;
- animation reference before rig/animation iteration;
- biome reference board before large environment generation.

## Tool policy

Prefer structured tools over GUI automation.

Examples:
- Unity MCP/CLI over clicking Unity through generic computer control;
- Blender/Mixar agent tools over manual GUI computer use when suitable;
- generation APIs/MCPs for reproducible calls;
- local ComfyUI when it is faster/cheaper for the required quality.

## Local vs paid generation

Optimize for accepted result per human hour.

A paid call is good if it saves meaningful time and produces a controllable result.

A free local workflow is bad if it consumes many hours of debugging for a minor saving.

Conversely, repeated image iteration may be ideal locally when the GPU/workflow already exists.

## Skills

A skill should be created when:
- a task is likely to repeat;
- a successful approach required learning;
- there are non-obvious prerequisites;
- review checkpoints matter;
- a previous failure should not recur.

Each skill should contain:
- purpose;
- prerequisites;
- inputs;
- steps;
- expected output;
- review checkpoints;
- failure modes;
- cost notes if relevant.

## Playgrounds as AI interfaces

Playgrounds are not only developer conveniences. They make the game legible to agents.

An agent can more reliably test:
- one enemy;
- one status;
- one VFX;
- one animation;
- one encounter;

when it does not need to navigate a complete run.

## Closed feedback loop

Target Unity loop:
edit -> compile -> run automated checks -> enter Play Mode -> capture evidence -> inspect -> fix.

Evidence should include some combination of:
- test output;
- Unity console;
- screenshots;
- short captures when needed;
- profiler metrics;
- serialized config diff.

## Long autonomous runs

Long autonomous agent runs are experiments, not the default quality workflow.

They are appropriate when:
- the brief is precise;
- tools are stable;
- scope is bounded;
- intermediate artifacts are recoverable;
- failure cost is acceptable.

Daily production should prefer smaller reviewable tasks.

## Failure policy

Do not erase failed approaches from project knowledge when the failure is likely to repeat.

Record:
- what was tried;
- why it failed;
- what fixed it;
- how to detect failure earlier next time.

## Production velocity

AI value must be measured.

Track:
- human minutes/hours;
- agent runtime;
- API cost;
- accepted output;
- rework;
- bespoke code;
- reuse percentage;
- defects/regressions.

The desired pattern is falling human effort for repeated content categories.

## Research origin

This operating model was informed by analysis of Stefan 3D AI's October 2026 game-development workflow videos, especially his use of:
- persistent local project workspace;
- GitHub-backed knowledge;
- narrow task chats/agents;
- MCPs for Unity/Blender;
- concept-first VFX/asset development;
- playground scenes;
- converting successful experiments into reusable processes.

The project adapts the underlying production principles rather than copying his exact tool stack.
