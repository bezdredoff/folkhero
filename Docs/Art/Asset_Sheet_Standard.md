# Asset Sheet Standard
Status: v0.1 — production documentation standard, 2026-10-18.
Applies to Concept_Generation_Guide.md and every Act I object. This defines deliverables, not approval of any unchosen visual design.

## Three deliverables
1. Exploration: a small number of alternatives answering a named design question.
2. Modeling packet: one selected object, consistent views and dimensions.
3. System/context sheet: module reuse, state variants and actual gameplay-camera readability.

A family board does not replace individual modeling packets. Every distinct modeled object gets a separate high-resolution sheet; states of the same object remain linked to that object. An inseparable assembly may share one packet, but independently modeled attachments need their own IDs and sheets. Terrain, VFX, UI and layout studies use their own templates rather than forced six-view object turnarounds.

## Identity and naming
Use parent backlog ID + object suffix, e.g. B01-HOUSE-A, B02-BARN-A, C01-BIRCH-A.
File convention: <object-id>_<deliverable>_<revision>.<ext>.
Each packet records parent, purpose, source IDs, dependencies, revision, approval status and outputs. A changed silhouette/dimension/module needs a new revision and another consistency review.

## Scale
- Unity convention: 1 unit = 1 metre; Y up. Show the front direction and footprint axes explicitly.
- Reuse an upright neutral 1.80 m adult mannequin, measured barefoot, in all object comparisons. This is a production ruler, not a claim about historical average stature.
- The mannequin shares the object's ground plane and projection; never enlarge it independently to fill a panel.
- Record width/depth/height in metres (small props may also show cm), door and opening dimensions, tool grip dimensions, and attachment heights.
- Dimensions are sourced where evidence exists; otherwise label them GAME ASSUMPTION. A measurement drawn by an image generator is not evidence.
- Humans and creatures show their actual chosen height beside the same reference ruler. Do not force every character to 1.80 m.
- Buildings must accommodate the chosen human dimensions and functional use. A gameplay exaggeration must be named.

## Modeling views
For an ordinary standalone object: front, back, left, right, top and 3/4 overview. Include underside only where it resolves construction.
- Orthographic views use equal pixels per metre, aligned baselines and matching geometry.
- The perspective 3/4 view is clearly separated from orthographic views.
- Keep asymmetry: left and right cannot be silently mirrored.
- Show concealed structure through an extra cutaway/exploded view when needed.
- Buildings: footprint/plan, roof geometry, opening locations, wall/roof junction and foundations; mark interior as unspecified when not designed.
- Characters: front/back/both sides in the same neutral rig-compatible pose, plus 3/4; no perspective anatomy changes. Separate tools, detachable clothing and equipment.
- Trees/foliage: show volume, trunk, canopy construction and approximate gameplay occlusion; do not draw every leaf.
- Small props: show thickness, joints, grip and functional interfaces.
All views must be checked against one another. Where AI invents inconsistent views, resolve the construction in a simple blockout and render the blockout; do not ask a modeler to reconcile contradictions.

## Resolution and files
- Final composed master: PNG, sRGB, 6144 x 4096 px landscape by default; use 4096 x 6144 portrait when appropriate.
- Separate orthographic view images: aim for at least 2048 px on the long edge of the subject bounding box.
- If six readable views do not fit, create numbered continuation sheets for the SAME object. No unrelated objects to fill space.
- Preserve native generation images and record their true dimensions. The final master can be assembled from separate views; do not claim native 6K generation when unavailable.
- Upscaling does not qualify missing construction detail as resolved.
- Keep labels/dimensions as editable text in a companion SVG or source layout; clean view PNGs must also be available.
- Optional PDF is a review export, not a replacement for clean images/source.
This is a delivery target, not a demand to generate all views in a single call.

## Production annotations
Record base mesh, detachable modules, sockets/contact points, material families, material masks and collision/traversal intent. State what can be shared across the family.
Normal/dry is the baseline. Show only applicable states; use N/A with a reason for irrelevant ones.
Weather/status versions preserve geometry unless an explicit attachment/swap is identified. Do not show every possible combination: baseline plus individual changes and one stress-test combination are enough.

## Review
Two independent checks:
1. Historical/material logic: provenance, chronology, region, social role, explicitly marked extrapolations.
2. Production/visual logic: approved style, scale, view agreement, reuse, gameplay readability.
A high-resolution sheet with contradictory views fails. An attractive historically unsupported silhouette fails historical acceptance.
Image dimensions and scale annotations do not certify engineering/CAD accuracy.

## Output checklist
Object ID; brief; evidence/assumptions; selected design; dimension table; required views; clean images; editable labels; module/material map; gameplay-size comparison; status and reviewer/date.
