# Source-of-truth map

Each topic should have one canonical home. Other documents should link to it rather than keep competing copies.

| Information | Canonical location | Update rule |
|---|---|---|
| Room purpose, boundaries and conventions | `workflows/<room>/CONTEXT.md` | Change when the room's remit or conventions change |
| Active work and next steps | `workflows/<room>/CURRENT.md` | Update as work starts, changes or completes |
| Durable room knowledge | `workflows/<room>/knowledge/` | Add only reusable facts, decisions and procedures |
| Research principles and standards | `workflows/research/knowledge/research-principles.md`, `evidence-and-claims.md`, and `reproducibility-and-integrity.md` | Canonical research-room practice; change these before changing a skill that implements them |
| Research procedures for agents | `workflows/research/skills/<skill>/SKILL.md` | Skills operationalise the research source-of-truth docs; link back instead of maintaining competing policy text |
| Project question, protocol, evidence and deviations | The relevant project repository, using `workflows/research/templates/` | Copy and complete records in project context; do not store project data or findings in this generic starter |
| Cross-room durable memory | `MEMORY.md` | Keep brief; link to room-owned sources |
| Shared procedures and decision rules | `PROTOCOLS.md` | Version material changes and record the effective date |
| Room names and ownership | `ROOMS.md` | Update when rooms are added, renamed or re-scoped |
| Project repository boundaries and component versioning | `REPOSITORIES.md` and the project's own repository metadata | Keep project source out of this workspace template |

If ownership is unclear, do not silently create a second canonical copy. Resolve the owner, then update this map.
