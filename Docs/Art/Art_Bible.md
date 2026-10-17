# Art Bible

Status: v0.2 pre-production direction. Visual references still need approval.

## Purpose

Define constraints that let human artists and AI-assisted pipelines create assets that belong to the same game while remaining readable, reusable and affordable for a very small team.

## Visual direction

The game should be **deliberately stylized rather than photorealistic**.

The style should be selected partly for production practicality:
- reliable AI-assisted concept generation;
- modular modeling;
- shared rigs;
- shared materials;
- procedural reuse;
- readable silhouettes;
- scalable PC/mobile performance.

Historical/folk grounding matters, but strict museum reconstruction is not the goal.

## Folklore first

Visual identity should communicate Belarusian and wider regional culture through:
- silhouette;
- textiles and ornament;
- clothing;
- tools/weapons;
- ritual objects;
- architecture;
- landscape;
- creature anatomy;
- environmental storytelling.

Avoid generic fantasy with folklore names pasted onto it.

## Historical frame

The world is alternate-history late-16th-century Grand Duchy of Lithuania / early Polish–Lithuanian Commonwealth.

Use recognizable historical material culture as a foundation, then allow supernatural divergence.

Real historical references should support plausibility without preventing stylization.

## Gameplay readability

Combat readability beats detail.

At gameplay camera distance the player should quickly read:
- enemy role;
- attack telegraph;
- status state;
- dangerous surface;
- elite/boss state;
- interactable objective.

Do not spend detail budget on elements invisible from the top-down/isometric camera.

## Camera-driven production

Camera is fixed or very limited-rotation with controlled zoom.

Environment production can therefore optimize for:
- expected viewing angles;
- combat readability;
- modular composition;
- occlusion control;
- performance.

Do not assume every asset must survive unrestricted third-person inspection.

## Character/class identity

Initial player archetypes:

### Warrior
- practical physical silhouette;
- axe and spear foundations;
- veteran/returned-soldier grounding;
- should read as capable without looking like a generic high-fantasy knight.

### Vedun
- folk-magic practitioner;
- ranged/ritual identity;
- should read as belonging to the same rural world rather than a separate wizard-school fantasy.

Final naming, clothing details and proportion guides require visual reference approval.

## Ornament language

Belarusian ornament patterns are a gameplay system and must be legible as more than decoration.

Art direction should support:
- recognizable pattern families;
- application to equipment/accessories;
- clear visual distinction without excessive UI noise;
- color/material variation tied to affinity where useful.

The Slutsk belt is a required culturally important reference for later high-value equipment/relic design.

## Creature production philosophy

Prefer reusable visual grammar.

Conceptual monster construction:
Body/Rig Family
+ Head/Face
+ Attachments
+ Material
+ VFX
+ Status/Corruption State.

Where practical, build around a small number of foundational rigs/chassis and produce variants through:
- proportions;
- attachments;
- materials;
- animation layers;
- VFX;
- damage/corruption states.

Do not assume every folklore creature requires a unique rig.

## Gameplay-driven visual states

Gameplay tags should drive presentation.

Examples:
- Wet -> wetness/material response;
- Frozen -> frost/ice response;
- Burning -> flame/ember response;
- Shocked -> electrical response;
- Poisoned -> contamination response;
- Cursed -> supernatural/corruption overlay.

These visual states should work across multiple characters/enemies where possible.

## Environment production

Regions are modular systems, not one-off scenes.

A production kit may contain:
- gameplay geometry modules;
- terrain/material rules;
- vegetation;
- rocks;
- structures;
- props;
- decals;
- weather;
- lighting profiles;
- hazard/surface elements;
- seasonal material/prop variants.

GeNa Pro should apply authored rules, not replace level design.

## Seasonal reuse

One strong region kit should support distinct gameplay/readability states:
- summer;
- rainy/autumn;
- winter;
- flood.

Seasonal work should reuse geometry and assets where possible while visibly changing:
- ground state;
- foliage;
- water level;
- snow/ice;
- lighting;
- fog/precipitation;
- traversal cues;
- combat surfaces.

## Initial region direction

The first region is based on an Upper Berezina / Berezinsky-reserve-like forest-marsh landscape:
- forest;
- bog;
- river headwaters;
- springs;
- lakes;
- villages;
- khutors;
- wet clearings;
- seasonal snow/flood states.

It must support the Vertical Slice and first Early Access act.

## VFX

VFX should be stylized, readable and reusable.

Build shared presentation for:
- hit impact;
- Physical heavy hit/Shatter;
- Wet;
- Burning;
- Cold/Frozen;
- Shock;
- Poison;
- Curse;
- status reaction;
- elite appearance;
- Downed/revive;
- boss phase;
- objective completion.

Feel/MMFeedbacks should provide reusable feedback profiles around these events.

## AI-assisted asset pipeline

AI generation is a production tool, not an art director.

Preferred flow:
brief
-> cheap concept/reference
-> human approval
-> production asset
-> cleanup
-> rig/material/animation as needed
-> Unity validation
-> gameplay-camera review.

Generated output must be checked for:
- style consistency;
- anatomy;
- topology;
- UV quality;
- material correctness;
- animation compatibility;
- licensing/usage constraints;
- performance.

Avoid depending on random one-off generated 3D assets that cannot be reproduced or maintained.

## Local vs cloud

Use local ComfyUI where it provides good quality at low marginal cost and iteration speed.

Use paid/cloud tools when they clearly save meaningful human time.

Optimize for accepted production output per human hour, not minimum API cost.

## Art Bible TODO before Vertical Slice

Add:
- approved visual reference board;
- final shape language;
- palette principles;
- material language;
- Warrior reference;
- Vedun reference;
- first enemy-family reference;
- first-region reference;
- ornament reference set;
- UI direction;
- polygon/texture/VFX budgets;
- animation timing examples.
