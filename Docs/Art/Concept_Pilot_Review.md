# Act I Concept Pilot — Selection Review
Status: selected exploration directions, 2026-10-18. No modeling-ready packet or engine benchmark delivered.

[Native image gallery](../../References/Targets/Act_I_Pilot/README.md) · [Machine-readable manifest](../../References/Targets/Act_I_Pilot/manifest.json) · [Evidence dossier](../../References/Act_I_Evidence_Dossier.md) · [Sheet standard](Asset_Sheet_Standard.md)

## Scope of acceptance
The user approved five base subjects through individual review, followed by winter variants and a terrain Curse test. Approval concerns the recorded form, palette and simplification; it is not historical certification, measured geometry or proof of engine feasibility. No inferred mass-production authorization.

All 17 available native PNGs are preserved: 11 selected images and six rejected/superseded iterations. They are 1536 × 1024, not final 6144 × 4096 masters. Exact early prompts/seeds/model versions were not exported; the manifest records known edit lineage and original filenames rather than inventing reproducibility.

## Selected object/state matrix
| Object | Base | Winter | Curse | Winter + Curse | Main remaining work |
|---|---|---|---|---|---|
| B01-HOUSE-A | summer r03 | r01 | Not tested | Not tested | Plan, dimensions, joins, openings and smoke route; simplify surface noise |
| C01-ALDER-A | summer r02 | r01 | Not tested | Not tested | Reduce winter twig complexity; consistent branch blockout and scale |
| D01-GROUND-WATER-A | summer r02 | r01 | r01 | r01 | Water depth/traversal and mask implementation; gameplay camera test |
| F03-PAIR-M | summer r02 | r01 | Not tested | Not tested | Costume evidence, boots/cap/cut, neutral orthographic views and clothing modules |
| I02-BOLOTNIK-A | base r02 | Not tested | Not tested | Not tested | Choose actual height, repair ruler comparison, neutral rig-compatible turnaround |

Rain/wet response, an assembled route, gameplay-size readability and implementation/performance remain untested. The matrix is not a request to fill every empty cell.

## House construction correction
The selected image supersedes the earlier isolated-support treatment for House A. Use a continuous low line of irregular fieldstones beneath the walls, including several much larger boulders, partly and unevenly buried. Close the wall-to-ground gap; no floating house. This is not a tall dressed-masonry plinth.
Round logs, visible broad moss chinking, tar-dark corners/log ends. Boards mainly at functional door/shutters; no plank-dominated walls or gable. Preserve few tiny membrane openings and the simple thatched gable roof.
Evidence R01/R02 gives broad construction context; R11 is adjacent-period context. The exact continuous foundation, moss/tar treatment and this arrangement are accepted game extrapolations, not a newly verified XVI-century reconstruction.
Winter retains the same base, closes shutters, and adds snow over roof/stone surfaces plus a trodden door approach. Snow is a candidate removable overlay, not a new house mesh.

## Simplified vegetation and ground
Summer alder uses a few large canopy masses and a faceted trunk. Winter removes foliage and exposes branches, with restrained snow caps. The selected winter illustration has more thin branches than the production target needs: consolidate into a few reusable secondary-branch/twig modules, then check silhouette in the gameplay camera. Tiny seed/flower details are not mandatory geometry.
The ground patch uses broad soil/grass masks, a gentle bank and two simple sedge clumps. Winter adds snow coverage, dry/bent sedge and a thin shore-ice strip with open brown water. This is one partial-freezing state, not a rule that every stream stays open or freezes completely. Habitat basis R19/R20/R22 does not supply exact seasonal ice geometry or plant model dimensions.

## Human and Bolotnik
Selected civilian: ordinary mildly stylized anatomy, simple rounded facial planes and clumped hair/beard; cream linen shirt, restrained belt, brown trousers, wraps and plain footwear. The simplified second variant is the rendering/proportion target. Winter preserves identity under a sheepskin coat with fleece inward and limited exposed edges, warm cap, mittens and boots. Exact historical pattern, headwear and footwear remain provisional (R01 material context; R03 later ethnography; R04 catalogue lead only).
Bolotnik: barefoot, heavy human torso, full human limbs, plain shirt/trousers/belt and concealed eyes. The revised target adds visibly olive-green hair/beard and larger moss coverage on clothing. Keep moss in broad masses rather than many separate leaves or strands. Clothing/green treatment is authored adaptation; R08 is scoped folklore context, not evidence of this exact costume or a former-human origin.
The image's ruler/height relationship is inconsistent: do not derive a 2.1 m lock from the generated label. The previously suggested 2–2.2 m range remains provisional. Repair scale in a blockout before modeling.

## Curse grammar validated in concept only
Localized plum/inky-violet stains link ground, shallow water and affected vegetation. Sparse lighter lilac veins suggest activity; ordinary summer/winter colors remain visible. Winter uses dark stain values against snow and beneath shore ice, with the same cue shapes. No obligatory geometry distortion, crystals or persistent particle cloud.
Proposed production composition: base terrain + season parameters/overlays + shared Curse mask. Snow/ice coverage and Curse must compose without hiding depth, traversal or combat telegraphs. These pictures support visual selection only; shader count, blend order, accessibility and URP cost require a prototype.

## Review lessons
| Earlier issue | Selected correction / future check |
|---|---|
| House looked suspended on separated stones | Continuous grounded irregular stone line with buried boulders |
| Tree/terrain/civilian details exceeded target | Fewer broad masses; simplified second variants |
| Bolotnik hair/moss lacked green | Olive hair/beard and broad moss coverage |
| Winter tree has excessive twigs | Reduce reusable modules before final packet |
| Generated scale labels and views imply precision | Blockout, measure and render consistent views; no pixel-derived dimensions |

## Next production gates
1. Reconcile plan/anatomy/scale in simple blockouts; resolve the named historical details or mark accepted extrapolations explicitly.
2. Produce separate coherent modeling packets with required views, dimensions, clean renders and editable labels under Asset_Sheet_Standard.md.
3. Test rain/wet response and one assembled scene at actual gameplay zoom, then consolidate A01/A02/A03.
4. Profile reusable materials, foliage, snow and water in URP before broad production.
Human effort/API cost/reuse speed were not measured reliably in this conversation; no throughput claim or invented benchmark is recorded.
