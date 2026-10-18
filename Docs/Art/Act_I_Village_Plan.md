# Act I village — accepted 23-household layout

Status: user-approved planning direction, 2026-10-18. Terrain schematic selected after rejecting the grid revision. Coordinates, dimensions, contours and water levels are illustrative, not a surveyed or gameplay-tested layout.

[Community roster](../Vision/Act_I_Community.md) · [Construction brief](Act_I_Village_Design.md) · [Concept review](Village_Concept_Review.md) · [Image gallery](../../References/Targets/Act_I_Village/README.md)

## Locked settlement decisions

- Exactly **23 residential households**: HH-01–HH-09 plus 14 additional local farming households, HH-10–HH-23. HH-01 is separate in this layout; do not count it again among the additional farms.
- No church in the village. No chapel is added by this plan.
- Burial ground outside the village, on a low hill beside a lake **beyond the forest**; reached by a footpath through woodland. Grave-marker forms and religious details are not approved by the generated illustration.
- Houses occupy a curved dry ridge and a lower dry terrace above wet meadow. Main and lower roads follow terrain and pass between entire estates, not through their gardens/buildings.
- Main route connects western market-town access and eastern fields; another field exit runs north. A lower branch serves residents and ends at the mill working area. Eastern livestock route and southern woodland footpath are separate functions.
- Northern fields continue beyond the visible map; gardens alone do not feed the settlement. Gardens, field access, grazing, hay, fuel, grain/seed storage and repairs all need spatial provision.
- Spring/ritual place is at the western marsh headwater, separate from everyday water collection. Stream flows toward the mill and downstream washing place. Lake is a separate water feature beyond the forest, not silently substituted as the river's source.
- Mill uses a natural local drop, without a large millpond. Miller's dwelling and woodworking shelter stand on a dry shelf, not in the flood channel.
- Existing return-home story remains: village becomes politically inaccessible; destruction of the village is not required.

## Plan authority and revisions

1. Initial four-house illustration: rejected as insufficient scope.
2. ASCII 23-yard proposal: composition/functions accepted; church excluded and cemetery location fixed by user.
3. Rectilinear interactive map: rejected because road crossed estates 11/14 and layout ignored terrain.
4. Terrain schematic: accepted. [Static map](../../References/Targets/Act_I_Village/Layout/village-terrain-selected.svg), [geometry](../../References/Targets/Act_I_Village/Layout/village-layout.json), [editable source fragment](../../References/Targets/Act_I_Village/Layout/village-terrain-selected.fragment.html).
5. Full generated village image: retained as provisional visual interpretation. Exact household count, positions and technical details have **not** been certified. The schematic and written roster override the image.

Schematic number denotes an entire estate with house, yard and associated functions, not just a house footprint. The symbol's repeated little buildings are a legibility convention, not a final identical outbuilding count for every family. Static export is for GitHub reading; Russian source labels preserve the reviewed discussion while canonical design prose stays English.

## Household assignments and spatial reasoning

| Yard | Residents | Provision and placement |
|---|---|---|
| 01 | Ordinary local reference pair | Small house, storage, garden, fuel; routine central village life; livestock shed only if needed |
| 02 | Weaver family, seven residents | Larger dwelling/work space for loom, storage, drying/work shelter, livestock; northern field access and nearby well |
| 03 | Smith, wife, teenage child | Ordinary residential estate; smithy K detached near western entry with open separation from dwellings |
| 04 | Miller/carpenter, wife, elderly father | Dry shelf above mill M; storage, shed, timber and woodworking shelter T |
| 05 | Hunter/fisher with Cossack past; family unspecified | Normal home and household economy, tackle storage/work shelter, access to eastern forest and fishing |
| 06 | Tatar family, four residents | House, storage, stable/shed, hay and horse enclosure P; dry northeastern edge with livestock/field access |
| 07 | Jewish family, four residents | House, shoe/leather repair work corner, dry materials storage, garden; western road for orders and town links |
| 08 | Roma healer family, four residents | Ordinary house, herb garden, drying/storage; lower western terrace integrated with neighbors |
| 09 | Starosta; family unspecified | Well-kept ordinary estate near road widening; storage and shed, no administrative palace |
| 10–11 | Two ordinary farming households | House, storage, shed as needed, garden; direct field access |
| 12–13 | Two larger farming households | More living/storage space and livestock capacity; possible multigenerational pattern, exact residents open |
| 14–16 | Three ordinary farming households | Shared basic modules in varied arrangements |
| 17–18 | Two small households | Small houses and modest stores, shared water access; large livestock sheds not automatic |
| 19–21 | Three ordinary households | Access to lower livestock route; exact family sizes and ages open |
| 22–23 | Two more livestock-oriented households | More shed/hay capacity and short access to meadow; dwellings remain on dry ground |

The last 14 household patterns are approved planning assignments, not fully written biographies. Twenty local households and three minority-family households do not establish a resident population percentage; 80–90% target still needs an actual census. Do not invent hero homes: Warrior's precise household remains open, Vedun's nearby khutor is outside these assigned yards unless later changed explicitly.

## Utility network

| Code | Function and constraints |
|---|---|
| K | Separate smithy near western entrance; accessible to carts, with free work apron; prevailing wind/fire arrangements to validate |
| T / M | Woodworking shelter / mill; dry timber storage and grain/cart approach; water feed → wheel → transmission → stones must be resolved |
| P | Stronger horse enclosure for yard 06; shared rail/post modules and diagonal board construction |
| G1–G5 | Distributed **groups** of individually assigned harvest/threshing/storage buildings near dry field margins; not five automatically communal barns |
| W1 / W2 | Windlass-well planning anchors on upper terrace |
| W3 / W4 | Sweep-well planning anchors on lower dry terrace |
| S | Sacred spring at marsh headwater; separate ritual approach |
| V | Livestock watering approach downstream of source |
| L | Washing approach farther downstream, below mill |

Four well symbols are planning anchors, not proof that four wells suffice. Existing rule of shared sweep wells for 2–3 simple households and neighbor-accessible wells at larger livestock estates remains; determine additional wells, catchments and travel distance during metric blockout. Surface elevation does not alone determine groundwater depth or well mechanism.

Every estate needs living/heating provision, food/seed storage, garden and field access, fuel, water access, useful workspace and livestock/feed provision where applicable. Plan waste/manure areas after checking drainage, groundwater and separation from wells; the schematic does not certify water safety.

Simple estate grammar: dwelling near road with door toward working yard; storage and livestock buildings to side/rear; garden behind; harvest buildings farther toward field access. No obligatory perimeter fence: wattle protects gardens, stronger rails contain animals, cart routes remain open. Poor/small estates omit modules; larger estates add shared modules rather than unique asset families.

## Landscape and production checks before blockout approval

- Heights shown as +8–12 m ridge / +3–6 m terrace / water ±0 are drawing hypotheses, not measured design commitments. Mill image's pronounced rocky drop must not force exaggerated terrain.
- Prove sufficient flow and head downstream from the spring/marsh catchment for mill function. Additional wetland inflow is a hypothesis, not an approved hydrological simulation.
- Check seasonal high water, drainage, gradients, cart turning, entrances, livestock routes, fire spacing and gameplay-camera readability.
- Main road polygons must not intersect any complete estate footprint. Geometry check in Tools/validate_village_concepts.py covers road width against rotated estate polygons; it does not prove all gates, service paths or 3D traversal.
- Reconcile full image to numbered plan; do not infer 23 distinct households by counting arbitrary roofs in the image.
- Reuse house A/B, storage/shed/threshing/shelter, fence/gate, utility and shared vegetation modules. 23 households does not authorize 23 bespoke buildings or mass production.
- Simplify roofs, ground and vegetation to approved large forms. Final dimensioned coherent object sheets and Unity validation remain open.

## Historical scope

R02 (Yakimovich, 1991) supplies regional architectural/planning context, including sixteenth-century settlement reorganization. This is an original alternate-history village, not a traced historical map. No specific Upper Berezina parcel survey, water model, religious arrangement or demographic census is claimed. Later ethnographic plans must not silently become sixteenth-century proof.
