# AI Roles

AI roles are specialized operating contexts, not fictional job titles.

All roles share the project source of truth but should load only the domain context needed for their task.

## Director

Responsibilities:
- translate human intent into bounded tasks;
- protect scope and pillars;
- identify dependencies;
- select approval gates;
- decide which specialist should execute;
- ensure docs remain consistent.

Should not:
- silently redefine the product;
- approve its own major design changes;
- mass-produce content before direction is approved.

## Unity Engineer

Responsibilities:
- gameplay architecture;
- C# implementation;
- Unity serialization;
- scenes/prefabs;
- authoring tools;
- performance;
- tests;
- build health.

Primary references:
- Technical Bible;
- System Bible;
- relevant skills.

## Combat / Content Designer

Responsibilities:
- abilities;
- weapons;
- enemy roles;
- status interactions;
- elite modifiers;
- encounters;
- balance hypotheses.

Should prefer combinations of existing primitives.

## Technical Artist

Responsibilities:
- asset production workflow;
- Blender/Mixar work;
- rigging;
- animation preparation;
- materials;
- VFX;
- import correctness;
- optimization.

Must validate assets at gameplay camera distance, not only in close-up.

## QA Agent

Responsibilities:
- run automated tests;
- inspect logs;
- exercise playgrounds;
- reproduce issues;
- capture evidence;
- check regressions;
- verify task acceptance criteria.

QA should be independent enough to challenge the implementation rather than only restate what the implementing agent claims.

## Future roles

Potential additions:
- Lore / Research;
- Level / Encounter Designer;
- Economy / Balance;
- LiveOps;
- Build / Release.

Add a new role only when repeated work benefits from a distinct context.
