# Production Metrics

The project must measure whether AI and reusable systems are actually making production cheaper.

## Content production benchmark

For each benchmark item record:

| Field | Meaning |
| --- | --- |
| Item | enemy / ability / VFX / encounter / biome module |
| Human time | active human effort |
| Agent runtime | approximate execution time |
| API cost | paid generation/processing cost |
| Attempts | number of meaningful iterations |
| Rework | manual correction effort |
| New code | new runtime code required |
| Reused primitives | existing systems reused |
| Accepted | yes/no |
| Defects | regressions discovered later |
| Lessons | links to skill/knowledge updates |

## Core production KPIs

Track over time:
- time to create a new ability;
- time to create a new enemy;
- time to create a new encounter;
- percentage of reused systems;
- bespoke code per content item;
- agent task acceptance rate;
- human correction time;
- regression rate;
- cost per accepted asset;
- time from concept approval to playable result.

## Gameplay KPIs

Later, once telemetry exists:
- run completion;
- death causes;
- build diversity;
- weapon pick rate;
- upgrade pick rate;
- encounter duration;
- boss success rate;
- repeat-run intent;
- abandon point.

## Interpretation

A high amount of produced content is not success by itself.

Warning signs:
- every new enemy takes the same effort;
- repeated one-off scripts;
- rapidly growing bug count;
- agents frequently need full rewrites;
- human review time increases with every feature;
- build diversity looks large on paper but converges in player choices.

Positive signs:
- repeated content becomes materially faster;
- new content mainly uses data/composition;
- tests catch regressions early;
- old systems gain value when new systems are added;
- agent corrections become smaller over time.
