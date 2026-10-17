# PP-01 — Production Foundation

This is the current project milestone.

## Purpose

Build the minimum production system needed to begin a vertical slice responsibly.

PP-01 is complete when we can create, test and review gameplay content through a repeatable pipeline.

## Deliverables

### Documentation

- [x] repository README
- [x] AGENTS.md
- [x] Game Vision v0.1
- [x] Game Bible v0.1
- [x] System Bible v0.1
- [x] Technical Bible v0.1
- [x] Art Bible framework
- [x] Production Roadmap
- [x] AI Production System
- [ ] approved visual reference set
- [ ] concrete first-biome brief
- [ ] concrete first-player brief

### Repository / tooling

- [ ] initialize Unity 6 URP project
- [ ] add appropriate Unity .gitignore
- [ ] define Unity folder conventions
- [ ] integrate Odin Inspector & Serializer
- [ ] integrate Feel/MMFeedbacks
- [ ] integrate GeNa Pro when world work begins
- [ ] select and connect Unity MCP/tooling
- [ ] validate agent can compile/run/tests
- [ ] establish CI smoke validation

### Gameplay foundation

- [ ] create CombatLab
- [ ] implement movement/camera prototype
- [ ] implement damage/health/death
- [ ] implement melee primitive
- [ ] implement projectile primitive
- [ ] implement AoE primitive
- [ ] implement dash/dodge
- [ ] implement initial feedback profiles
- [ ] evaluate game feel

### Data/system foundation

- [ ] ability data definition v0
- [ ] effect primitive architecture v0
- [ ] status system v0
- [ ] enemy configuration v0
- [ ] enemy capability composition v0
- [ ] elite modifier v0
- [ ] encounter configuration v0

### Playgrounds

- [ ] ContentLab
- [ ] AnimationVFXLab
- [ ] EncounterLab
- [ ] PerformanceLab
- [ ] NetworkLab only if multiplayer becomes a committed pillar

### Content pipeline benchmark

Produce Enemy #1 end-to-end.

Record:
- human time;
- agent runtime;
- API/cloud cost;
- iterations;
- rework;
- amount of new code;
- reused primitives;
- failures/lessons.

Then produce Enemy #2 and Enemy #3 from the same family.

Success condition:
the later enemies require materially less human effort and bespoke code.

### Ability pipeline benchmark

Produce at least three meaningfully different abilities using the same underlying grammar.

Success condition:
ability #3 is primarily data/composition rather than another custom implementation.

## PP-01 exit criteria

All must be true:

### Gameplay
Primitive combat feels promising enough to invest further.

### Systems
Abilities/enemies can be composed from reusable primitives.

### Production
Repeated content shows measurable acceleration.

### Technical
Unity project, tests and agent tooling are stable enough for continuous work.

### Knowledge
Important successful workflows are recorded as reusable skills.

## Not required for PP-01

Do not expand scope to:
- several finished biomes;
- final UI;
- full story;
- full progression economy;
- large enemy roster;
- final multiplayer;
- final mobile build;
- marketing polish.

Those can hide unresolved foundational problems.
