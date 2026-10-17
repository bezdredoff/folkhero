# AI Skills

This directory stores repeatable project-specific workflows.

A skill is not a general prompt. It is a learned production procedure for Folkhero.

## When to create a skill

Create or update a skill when:
- a task will repeat;
- the team found a reliable solution after experimentation;
- prerequisites are easy to forget;
- review checkpoints are important;
- there is a common failure mode;
- a tool needs project-specific configuration.

## Skill template

Use this structure:

# Skill name

## Purpose
What recurring task this solves.

## Inputs
Required files, references, data and approvals.

## Prerequisites
Tools, scene setup, packages or configuration.

## Procedure
Numbered repeatable steps.

## Review checkpoints
Where human or QA review is required.

## Acceptance criteria
What must be true at the end.

## Failure modes
Common problems and how to detect them.

## Cost / performance notes
Only when relevant.

## Lessons / revisions
Important changes to the procedure over time.

## Initial skills to create after implementation begins

Likely:
- create-new-ability;
- create-enemy-from-existing-chassis;
- import-rigged-character;
- create-vfx-profile;
- add-elite-modifier;
- create-encounter;
- validate-content-item;
- run-unity-agent-qa-loop;
- prepare-generated-3d-asset;
- profile-enemy-stress-test.

Do not write fake detailed procedures before the project has actually proven them. Skills should represent learned practice.
