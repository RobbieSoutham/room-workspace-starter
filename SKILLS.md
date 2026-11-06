# Skills index

This is the complete index of reusable agent procedures shipped in this starter. Read the relevant skill before using its workflow. Skills provide task steps; canonical policies and records remain in the locations listed in `SOURCE_OF_TRUTH.md`.

## Global skills

| Skill | Use it for |
|---|---|
| [`adversarial-refinement`](skills/adversarial-refinement/SKILL.md) | Pressure-testing a consequential proposal and comparing realistic alternatives |
| [`premortem`](skills/premortem/SKILL.md) | Failure paths, assumptions and tripwires before a consequential plan |
| [`retrospective`](skills/retrospective/SKILL.md) | Capturing supported, reusable lessons after substantial work |
| [`safe-release-review`](skills/safe-release-review/SKILL.md) | Reviewing repository contents, secrets, size and rights before an authorised release |
| [`semantic-gatekeeper`](skills/semantic-gatekeeper/SKILL.md) | Bounded inspection of large or unfamiliar files |
| [`skill-maintenance`](skills/skill-maintenance/SKILL.md) | Creating, updating or retiring reusable skills |

## Operations room

| Skill | Use it for |
|---|---|
| [`capacity-and-cost-review`](workflows/operations/skills/capacity-and-cost-review/SKILL.md) | Comparing capacity, cost and operating burden before a resource decision |
| [`change-planning`](workflows/operations/skills/change-planning/SKILL.md) | Scoping an operational change, validation, authority and rollback |
| [`incident-review`](workflows/operations/skills/incident-review/SKILL.md) | Recording impact, evidence, cause, remediation and follow-up |
| [`service-health-review`](workflows/operations/skills/service-health-review/SKILL.md) | Assessing current service health and evidence quality |

## Research room

| Skill | Use it for |
|---|---|
| [`claim-evidence-audit`](workflows/research/skills/claim-evidence-audit/SKILL.md) | Checking whether evidence supports specific research claims |
| [`evidence-led-review`](workflows/research/skills/evidence-led-review/SKILL.md) | Planning and conducting traceable literature searches and reviews |
| [`literature-synthesis`](workflows/research/skills/literature-synthesis/SKILL.md) | Comparing an identified set of sources into themes and disagreements |
| [`manuscript-review`](workflows/research/skills/manuscript-review/SKILL.md) | Developmental review of argument, methods reporting and claim calibration |
| [`research-communication`](workflows/research/skills/research-communication/SKILL.md) | Adapting established evidence for an audience or format |
| [`research-frame`](workflows/research/skills/research-frame/SKILL.md) | Framing or revising a research question before substantial work |
| [`research-protocol`](workflows/research/skills/research-protocol/SKILL.md) | Specifying methods and reproducibility before claim-bearing work |
| [`research-question-development`](workflows/research/skills/research-question-development/SKILL.md) | Turning a broad topic into a focused, answerable question |

## Projects room

| Skill | Use it for |
|---|---|
| [`delivery-planning`](workflows/projects/skills/delivery-planning/SKILL.md) | Planning milestones, ownership, dependencies and review points |
| [`launch-readiness`](workflows/projects/skills/launch-readiness/SKILL.md) | Reviewing support, documentation, risk and authorisation before release |
| [`opportunity-validation`](workflows/projects/skills/opportunity-validation/SKILL.md) | Testing uncertain opportunities before investing heavily |
| [`project-intake`](workflows/projects/skills/project-intake/SKILL.md) | Establishing project ownership, scope, records and first decision |

## Scope and maintenance

Global skills apply across rooms. Room skills are kept beside the room that owns the work and are also listed in that room's `CONTEXT.md`. A skill should point to canonical knowledge rather than duplicate policy. To add, change or retire one, follow [`skill-maintenance`](skills/skill-maintenance/SKILL.md), then update this index and the owning room context.
