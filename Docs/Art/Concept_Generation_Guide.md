# Concept Generation Guide

Status: v0.2 — production-oriented concepting rules.

Required companions: [Asset Sheet Standard](Asset_Sheet_Standard.md), [Concept Readiness](Concept_Readiness.md), [Concept Register](Concept_Register.md), and [Evidence Dossier](../../References/Act_I_Evidence_Dossier.md).

A prompt is executable only after its brief is selected. Source constraints and unresolved assumptions must be included; generic date/region language is not enough.

## Goal

Use AI concepts to design reusable 3D systems, not standalone illustrations.

Every concept must help answer a production question:
- what is the shared base mesh?
- what is modular?
- what is a material/state change?
- what changes only through VFX?
- does it remain readable from the actual top-down camera?

## Mandatory style statement

Use language equivalent to:

> Folkhero: simple modular 3D for a top-down action RPG; historically grounded late-16th-century Belarusian/Ruthenian/Lithuanian/Polish material culture; dark fairytale mood; large readable forms; flat/soft-shaded materials; restricted palette; minimal texture noise; mobile-readable silhouettes; system-driven variants.

Avoid asking for:
- painterly key art as a production target;
- photorealism;
- dense cinematic clutter;
- miniature/toy diorama;
- highly textured PBR;
- hundreds of tiny props.

## Camera

### Gameplay concepts
- true 3D top-down/isometric view;
- expected gameplay angle;
- objects shown at realistic gameplay scale;
- include a reduced mobile-size example where useful.

### Asset sheets
- 3/4 orthographic-like 3D presentation;
- neutral dark background;
- consistent object scale;
- repeat the same base mesh across variants.

## Detail limiter

Always request:
- large simple shapes;
- few color blocks;
- minimal surface noise;
- minimal small props;
- no individual leaf detail;
- no dense debris;
- no dense flower carpet unless specifically needed;
- no baked painterly light;
- no tiny embroidery beyond one or two large readable bands;
- no tiny bags/belts unless role-critical.

If the output is still too detailed, explicitly request:
> simplify another 30–40%; reduce prop count and color count; use broad flat materials; every object must look like a reproducible game-ready 3D mesh.

## Historical grounding

Gather Evidence references before generating culture-specific production concepts.

For architecture preserve:
- construction type;
- roof pitch/material;
- openings;
- functional proportions;
- settlement/farmstead logic.

For clothing preserve:
- garment layering;
- social role;
- material;
- headwear;
- footwear;
- plausible ornament placement.

Generated images are not evidence.

## Reuse rule

A prompt should explicitly state what must remain the same underlying asset.

Example:
> Show one historically plausible rural house base mesh reused in six conditions. Keep wall geometry identical. Variation may come from two roof modules, porch/chimney attachments, palette, wetness, snow, damage and curse masks.

## Character concept template

Show:
- one standard humanoid-rig base;
- family exploration views as needed; every selected object then gets the complete individual modeling packet required by Asset_Sheet_Standard.md;
- 4–8 head/hair/headwear options;
- 3–5 torso options;
- 2–4 lower-body options;
- cloak/outerwear options;
- role weapons/tools;
- palette examples;
- gameplay-size silhouette row.

Rules:
- realistic/mildly stylized anatomy;
- simple rounded facial planes;
- rounded/broad nose language;
- large clothing masses;
- restrained accessories;
- ordinary human first, class/faction second.

Do not design each NPC as a unique bespoke costume.

## Environment-kit template

Every environment concept sheet should show:
1. core geometry;
2. modular attachments/connections;
3. material variants;
4. season/weather variants;
5. gameplay blockers/traversal modules;
6. one assembled gameplay example;
7. one reduced top-down readability example.

Label:
- reusable base;
- optional module;
- material-only state;
- VFX-only state;
- gameplay prop;
- decoration.

## State variant template

For the exact same base mesh, where applicable, show:
- Normal;
- Wet/Rain;
- Autumn;
- Winter/Snow;
- Frozen;
- Burned;
- Poisoned;
- Damaged;
- Cursed.

Do not accidentally redesign the asset between states.

## VFX template

For each VFX show:
- persistent state look;
- short reaction burst;
- gameplay-scale footprint;
- primary/supporting colors;
- light-background test;
- dark-background test;
- gameplay information communicated.

Persistent effects must remain restrained.

## UI/gameplay screenshot template

Use the PC gameplay frame as the primary deliverable. Add a separate mobile readability/touch-layout comparison; do not overlay touch controls on every PC scene.
- fixed/limited-rotation top-down action-RPG framing;
- PC action/cooldown prompts appropriate to the selected input scheme;
- touch comparison only: left movement joystick and right attack/skill cluster;
- compact minimap;
- compact quest/objective panel;
- target HP/status;
- player HP and cooldowns; no mana/stamina/rage bars under the current design;

Test:
- village/non-combat;
- regular combat;
- status/reaction combat;
- boss;
- co-op;
- rain/snow;
- corruption.

UI must not cover telegraphs or systemic surfaces.

## Recommended prompt order

1. Production purpose.
2. Shared base geometry.
3. Historical subject/date/region.
4. Simple 3D visual language.
5. Camera.
6. Modular/material/state variants.
7. Mobile readability.
8. Explicit exclusions.

## Example — historical systemic house

> Production concept sheet for Folkhero. Show one historically plausible late-16th-century rural GDL/Belarus-region log house as a simple real 3D game asset, not an illustration. Use the approved evidence packet for log construction, roof form, openings and farmstead proportions. Do not invent a chimney or porch to satisfy a generic fantasy house template. Large simple geometry, flat/soft shading, restricted palette, minimal texture noise. Reuse the same base structure with two roof modules, only source-supported attachments and heating/smoke outlet configuration selected in the brief, summer, rain/wet, winter/snow, damaged and cursed states. Maximum 3–4 material families. No generic fantasy cottage, no dense props, no tiny carvings. Include a small top-down gameplay-scale comparison.

## Example — modular human system

> Modular humanoid production sheet for Folkhero. One standard humanoid rig and base body, realistic/mildly stylized proportions, simple rounded facial planes and broad rounded nose language. Show modular head/hair/headwear, torso, lower body, cloak, weapon/tool modules. Assemble farmer, village woman, hunter, Warrior, Vedun and authority soldier from the same system. Historically grounded late-16th-century regional clothing silhouettes, restricted linen/earth/red palette, minimal tiny accessories, large color blocks, mobile-readable silhouettes. Real 3D asset appearance, not 2D character illustration.

## Review checklist

Reject/revise when:
- too many unique meshes are required;
- variants change geometry without need;
- historical silhouette is lost;
- too many colors are used;
- texture detail dominates form;
- mobile silhouettes merge;
- VFX hides units;
- it works only as key art;
- it cannot plausibly be reproduced in Unity.

Approve only when the concept makes the next implementation decision easier.

## Generation constraints
- User sequence: complete gap research/documentation, discuss and select, then try generation. No automatic batch generation.
- Every object inherits explicit metric scale from the shared human ruler. A family image is not a modeling sheet.
- High-resolution final layouts may be composed from multiple native views; preserve native files and disclose upscaling.
- Separate evidence, game assumption and approved visual treatment. Missing evidence must not be hidden by detailed rendering.
- A01 is consolidated from selected calibration objects; early outputs are provisional, not final style locks.
