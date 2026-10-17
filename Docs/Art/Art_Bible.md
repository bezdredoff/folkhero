# Art Bible

Status: pre-production framework. Visual direction is not yet locked.

## Purpose

The Art Bible defines constraints that let human artists and AI-assisted pipelines create assets that belong to the same game.

It should eventually include image references, not only text.

## Current principles

### Folklore first

Visual design should communicate Belarusian / regional folklore through:
- silhouette;
- materials;
- clothing;
- ritual objects;
- architecture;
- landscape;
- creature anatomy;
- environmental storytelling.

Avoid generic fantasy with folklore names pasted on top.

### Gameplay readability

Combat readability beats detail.

Enemy role, attack telegraph and interactable state must remain understandable at gameplay camera distance.

### Scalable production

Art direction should support:
- reusable rigs;
- modular environment kits;
- material variants;
- shared VFX primitives;
- controlled asset complexity;
- LODs where needed.

## Character / creature pipeline principles

For complex generated or AI-assisted assets:
1. concept first;
2. approve silhouette and gameplay role;
3. generate/model in logical parts when useful;
4. clean topology as required;
5. create predictable UVs/materials;
6. keep important functional parts separate when animation/VFX requires them;
7. rig;
8. animate;
9. import to Unity;
10. validate in gameplay camera.

A beautiful close-up asset that fails animation, readability or performance is not production-ready.

## Environment principles

Biomes should be produced from modular kits rather than one-off scenes.

A kit may contain:
- terrain/material rules;
- vegetation;
- rocks;
- structures;
- props;
- decals;
- weather;
- lighting profiles;
- hazard elements.

GeNa Pro should help apply and vary authored rules. It should not be used as a substitute for defining those rules.

## VFX

VFX development should follow:
concept -> approval -> implementation -> VFX/Animation playground -> reusable library.

Important actions deserve clear feedback:
- heavy hit;
- status application;
- elite appearance;
- level-up;
- boss phase;
- objective completion.

## AI-generated assets

AI generation is a production tool, not an art director.

Generated output must be checked for:
- style consistency;
- anatomy;
- topology;
- UV quality;
- material correctness;
- animation compatibility;
- licensing/usage constraints where relevant;
- performance.

## Local vs cloud

Use local ComfyUI when it provides good quality at low marginal cost and iteration speed.

Use paid/cloud tools when they clearly save meaningful human time, especially for specialized 3D/video/edit operations.

Optimize for accepted production output per human hour, not only API cost.

## Art Bible TODO

Before Vertical Slice, add:
- approved visual references;
- shape language;
- palette;
- material language;
- character proportion rules;
- environment density rules;
- VFX style rules;
- UI direction;
- target polygon/texture budgets;
- animation timing examples.
