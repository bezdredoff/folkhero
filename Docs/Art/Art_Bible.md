# Art Bible

Status: v0.5 — systemic 3D direction and concept delivery standards for pre-production.

## Purpose

Folkhero needs a visual language that allows a very small team to build a large systemic action RPG from a small number of reusable 3D assets.

The art direction must support:
- historical and ethnographic grounding;
- Belarusian / Ruthenian / Lithuanian / Polish regional identity;
- top-down mobile readability;
- modular reuse;
- seasonal and weather transformation;
- gameplay status states;
- AI-assisted concepting;
- affordable 3D production;
- mobile-class performance.

The target is not a painted illustration recreated in 3D. It is a simple, deliberate 3D game language whose variation comes from systems.

## Core visual thesis

**Flat dark-fairytale systemic 3D.**

Working formula:

historically grounded shapes  
+ simple readable 3D geometry  
+ large flat color masses  
+ restricted regional palette  
+ modular parts  
+ data-driven materials/states  
+ restrained VFX  
= Folkhero

The game should clearly read as 3D:
- real volume;
- stable lighting;
- readable silhouettes;
- simple modeled forms;
- consistent camera-space proportions.

Avoid:
- detailed 2D-illustration appearance in gameplay;
- painterly concept detail treated as final asset specification;
- noisy realistic PBR;
- miniature/toy diorama aesthetics;
- high-frequency fantasy decoration.

## Production-first art principle

The primary question is not “How many beautiful variants can we draw?” but:

> How many useful game variants can one base asset produce?

Prefer:
- one house mesh + modular roof/porch/chimney + palette/state parameters;
- one tree family + foliage/material/state variants;
- one humanoid base + modular heads/clothing/equipment;
- one enemy chassis + attachments/materials/animation/VFX states;
- one terrain family + dry/wet/snow/ice/poison/curse states.

Avoid separate unique assets when a shared base can express the same distinction.

## Visual pillars

1. **Systemic before bespoke** — reuse geometry and let modules, materials, weather, status and world state create variation.
2. **Large forms before texture detail** — objects must read at top-down mobile scale.
3. **Historically grounded silhouette** — architecture, clothing, tools and weapons come from late-16th-century GDL / early PLC material culture.
4. **Dark fairytale through palette and atmosphere** — uncanny and restrained without monochrome grimdark.
5. **Folk identity through real material culture** — textiles, dress, architecture, tools and ritual objects beat generic fantasy symbols.
6. **Limited clean accents** — white linen, red ornament, healthy green, clean water and selected warm light carry meaning because they are not everywhere.
7. **Readable system states** — Wet, Frozen, Burning, Shocked, Poisoned and Cursed remain distinct without covering the screen in effects.

## Camera and readability

Target:
- 3D top-down / isometric;
- fixed or very limited rotation;
- controlled zoom;
- gameplay-first composition.

A game object must remain legible:
- at phone size;
- partially occluded;
- in rain/fog;
- next to VFX;
- among several units.

### Readability hierarchy

At gameplay distance:
1. traversable / blocked space;
2. player characters;
3. enemies and tactical role;
4. attack telegraphs;
5. systemic surfaces and status states;
6. interactables/objectives;
7. decoration.

Decoration must never compete with 1–6.

## Detail budget

### Environment
Prefer a few large forms.

Typical forest composition:
- 2–4 strong tree masses;
- 1 undergrowth mass;
- 1–2 rock/log shapes;
- 0–1 gameplay prop.

Typical swamp module:
- one water/ground shape;
- 1–3 reed/sedge clumps;
- one dead tree/root mass;
- one bank/island shape;
- one crossing/gameplay prop.

### Characters
At gameplay distance, a humanoid should read as roughly 5–8 major visual masses:
- head/skin;
- hair/headwear;
- shirt/tunic;
- lower body;
- outer layer;
- one cultural color/ornament accent;
- weapon/tool;
- optional class-specific prop.

Avoid accessories and embroidery visible only in close-up.

### Architecture
A rural house should read through:
- wall mass;
- roof mass;
- openings;
- one trim/accent family;
- 0–2 optional attachments.

## Shape language

### People
- realistic or mildly stylized human proportions;
- standard humanoid-rig compatibility;
- animation-library friendly;
- simple facial planes;
- slightly softened/rounded folk-fairytale character;
- rounded, somewhat broad noses can be a recurring shape-language trait;
- avoid fashion-model faces as the default.

Local population can visually lean toward fair/light hair and light eyes while retaining believable variation. Minority groups may appear where historically and narratively appropriate and should be represented as people, not costume archetypes.

### Buildings
Rural structures remain historically grounded even when simplified.

Preserve:
- plausible log/timber construction;
- believable roof pitch/material logic;
- functional doors/windows;
- barns, sheds, granaries, wells and fences;
- regional farmstead organization.

Simplify:
- joinery detail;
- plank count;
- surface noise;
- small carving.

Do not replace historical silhouettes with generic fantasy cottages.

### Supernatural
Prefer:
base body/rig  
+ head/face module  
+ attachment family  
+ material state  
+ VFX state  
+ animation layer.

## Settlement and landscape grammar

Permanent settlement normally sits on:
- comparatively dry ground;
- low ridges;
- terraces;
- gentle hills/rises;
- forest edges above wet ground.

Default gradient:

**village / khutor on dry rise**  
→ yards / gardens / small fields  
→ hay meadow / pasture / livestock routes  
→ wet meadow / floodplain  
→ marsh / bog / water.

Lowland near wetlands is more likely to contain haymaking, pasture, livestock routes, fishing access and flood-prone paths than permanent homes.

## Historical and ethnographic policy

Reference priority:
1. primary-period / near-primary evidence;
2. archaeology, inventories, surviving objects;
3. museum/scholarly reconstruction with documented basis;
4. later ethnography explicitly marked as continuity evidence;
5. films/games only as artistic inspiration.

For approved references record where possible:
- source;
- approximate date;
- region;
- social context;
- confidence;
- evidence-based vs game extrapolation.

Generated images are never historical evidence.

### Ornament
Do not use random “Slavic pattern”.

Use:
- documented motif families;
- documented placement logic;
- real textile construction;
- restrained application at gameplay scale.

At gameplay distance ornament often reads as one red/white band, border or chest/sleeve/hem accent rather than dense micro-pattern.

## Religious layer

Christianity is present but visually restrained in the home region.

Remote villages / wilderness:
- occasional cross;
- local icon;
- small chapel/church where appropriate.

Polotsk:
- stronger institutional Christian layer;
- churches;
- crosses;
- clergy;
- icons;
- urban/institutional architecture.

## Color language

### Base families
- peat/earth brown;
- dark weathered wood;
- linen white / warm off-white;
- charcoal / iron gray;
- desaturated forest green;
- moss/olive;
- cold blue-gray water;
- fog gray.

### Controlled accents
- textile red;
- clean white;
- healthy green;
- clean-water blue-green;
- warm fire/lamplight;
- rare supernatural colors.

A scene should not use every accent simultaneously.

## Material model

Use a small number of shared material families:
- wood;
- cloth;
- leather;
- metal;
- stone;
- terrain;
- foliage;
- water.

Shared parameters where useful:
- BaseColor / PaletteIndex;
- SecondaryColor;
- Roughness;
- Wetness;
- SnowAmount;
- FrostAmount;
- BurnAmount;
- PoisonAmount;
- CurseAmount;
- DamageAmount;
- OrnamentMask;
- DirtAmount.

Prefer:
- low-frequency albedo;
- low texture noise;
- shared tiling/trim textures;
- masks;
- atlasable decals;
- simple normals only where needed.

Avoid unique high-resolution texture sets for ordinary repeated assets and baked painterly lighting.

## Modular architecture system

Act I village kit should use a small vocabulary:
- House A;
- House B / wealthier house;
- barn;
- shed;
- granary;
- animal shelter;
- well;
- fence/gate;
- haystack;
- bridge/boardwalk;
- small ritual/church object.

Variation:
- roof module;
- porch/lean-to;
- chimney;
- windows/doors;
- fence style;
- palette;
- weather/season;
- damage;
- curse.

A concept is successful when it demonstrates many believable outcomes from few modules.

## Modular character system

Use:
- few body bases;
- shared humanoid rig;
- interchangeable heads/hair/headwear;
- interchangeable torso/lower-body/outerwear;
- modular weapon/tool;
- limited bags/accessories;
- ornament masks/decals.

Identity should come mainly from silhouette, role prop, large clothing colors, headwear, posture/animation and one or two cultural accents.

### Warrior
- ordinary human first;
- returned-soldier/veteran grounding;
- strong weapon silhouette;
- practical regional clothing/armor;
- shares the civilian/soldier system where possible.

### Vedun
- ordinary human first;
- rural clothing foundation;
- identity through staff/tool, ritual object, herbs/material bundle and restrained supernatural VFX;
- not wizard-school fantasy.

## Enemy production grammar

### Human family
One shared human foundation can support:
- bandit;
- authority soldier;
- officer;
- cursed human;
- militia/local fighter.

### Folklore families
Prefer a small number of body/rig families. Each creature should answer:
1. what makes the folklore identity recognizable?
2. what can remain shared?

Do not assume each named creature needs a unique rig.

## Seasons, weather and world states

Core seasonal states:
- summer;
- autumn/rain;
- winter;
- spring flood.

World/system states:
- dry;
- wet;
- snow-covered;
- frozen;
- burned;
- poisoned;
- cursed;
- damaged.

Preferred transformation order:

**material parameter**  
→ **reusable overlay/attachment**  
→ **geometry swap only when necessary**.

## Status presentation

### Wet
- darker material;
- controlled highlights;
- puddle/water response;
- very light particles.

### Frozen
- cold/pale shift;
- edge frost;
- limited ice attachment;
- status icon.

### Burning
- small flame/ember layer;
- char;
- short strong reaction burst.

### Shock
- brief arcs;
- chain line only when mechanically relevant.

### Poison
- contamination tint;
- limited vapor/particles;
- surface propagation when systemic.

### Curse
- darker/cooler palette;
- selected unnatural accent;
- restrained emissive marking;
- shape corruption only where necessary.

## VFX rules

Two tiers:

### State VFX
Persistent and low intensity:
- Wet;
- Poison;
- Frozen;
- Curse;
- Burning.

### Reaction VFX
Short and high intensity:
- Shatter;
- Wet + Shock chain;
- steam/extinguish;
- critical ritual trigger;
- boss reaction.

Bright effects should usually signal a gameplay event. Avoid rainbow clutter.

## Corruption / “Cursed Treasures” overlay

This is a reusable state, not the base rendering style.

Possible components:
- material palette shift;
- desaturated/dark vegetation;
- selected violet/unnatural accent;
- corruption decals;
- sparse emissive markings;
- dead/bent foliage attachment;
- fog profile;
- VFX/audio profile;
- enemy posture/animation layer.

The cursed version must remain recognizably the same underlying asset/location.

## Mobile/performance constraints

Prefer:
- few material families;
- instancing;
- atlases/trim sheets;
- low overdraw;
- limited transparency;
- low particle count;
- simple foliage;
- reusable LODs;
- camera-dependent detail.

Avoid:
- excessive unique props;
- dense alpha foliage;
- overlapping transparent VFX;
- tiny geometry detail;
- high-frequency textures invisible from gameplay camera.

Exact poly/texture budgets will be set from prototype profiling.

## AI-assisted concept pipeline

AI concepting must test production rules.

Every concept should answer:
- what are the reusable base assets?
- what are modular swaps?
- what changes by material parameters?
- what changes by weather/status?
- what is readable at gameplay distance?

Reject concepts that:
- rely on micro-detail;
- add dozens of one-off props;
- read as 2D rather than game-ready 3D;
- cannot plausibly be assembled from reusable assets;
- replace historical construction with generic fantasy.

See Docs/Art/Concept_Generation_Guide.md.

## Reference taxonomy

- **Evidence** — historical/museum/scholarly factual support.
- **Inspiration** — artistic treatment only.
- **Target** — approved visual/production direction.
- **Anti-reference** — what to avoid.

## First-region target

Upper Berezina / home region:
- dry elevated village/khutor;
- fields/gardens;
- hay meadow/pasture;
- forest edge;
- wet meadow;
- river/spring;
- marsh/bog;
- rain/snow/flood.

The same module kit should create:
- safe village;
- rainy route;
- winter route;
- flooded route;
- corrupted route;

without requiring a separate environment set for each.

## Current target summary

Folkhero is:

**historically grounded late-16th-century regional forms**  
rendered as  
**simple modular 3D with flat/soft shading and a limited palette**  
supporting  
**system-driven weather, status, season, corruption and procedural recombination**.

The direction succeeds only if it is:
- distinctive;
- readable on mobile;
- cheap to multiply;
- historically recognizable;
- compatible with ordinary 3D production;
- strong enough that simple assets feel intentional.

## Concept documentation standards
See Asset_Sheet_Standard.md for mandatory individual object sheets, human-relative metric scale, consistent multi-view modeling references and high-resolution delivery.
See Concept_Readiness.md and Concept_Register.md for stage tracking and unresolved choices. Historical claims require scoped evidence; use ../../References/Act_I_Evidence_Dossier.md.
PC-first release planning and mobile-readable art are compatible: primary PC HUD and separate touch/readability comparisons. Current classes use HP/cooldowns without mana/stamina/rage.
Written rendering direction is locked; actual target images must be stored/referenced and explicitly identified before they are treated as approved visual targets.

## Selected exploration targets — 2026-10-18
Use [Act I Pilot Review](Concept_Pilot_Review.md) and the [native target gallery](../../References/Targets/Act_I_Pilot/README.md) for the current five-subject visual calibration. Selected targets now exist; earlier missing-target notes are preparation history. Simplified alder/terrain/civilian revisions define the detail ceiling; do not copy every texture mark or winter twig. House A uses round logs, moss chinking, tar-dark corners and a continuous irregular partly buried fieldstone foundation. Curse uses local plum/violet stains and rare lilac activity across seasonal surfaces. All targets remain explorations, with construction, scale and historical limits recorded per object.

## 2026-10-18 — Village layout and concept continuation

[Village assets and reviews](Village_Concept_Review.md) and [accepted 23-household terrain plan](Act_I_Village_Plan.md): no church, cemetery on hill at lake beyond forest, roads outside estate footprints. New native image gallery preserves selected, superseded and unreviewed studies. Schematic overrides village illustration; simplify texture before production.
