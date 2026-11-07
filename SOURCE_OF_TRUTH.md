# Source-of-truth map

Each topic should have one canonical home. Other documents should link to it rather than keep competing copies.

| Information | Canonical location | Update rule |
|---|---|---|
| Assistant working values and behaviour defaults | `SOUL.md` | Update when shared agent behaviour expectations change; does not override higher-priority instructions or explicit user requests |
| Stable user preferences | `USER.md` | Keep brief and non-sensitive; update when preferences change; do not use for active project status |
| Room purpose, boundaries and conventions | `workflows/<room>/CONTEXT.md` | Change when the room's remit or conventions change |
| Active work and next steps | `workflows/<room>/CURRENT.md` | Update as work starts, changes or completes |
| Durable room knowledge | `workflows/<room>/knowledge/` | Add only reusable facts, decisions and procedures |
| Global reusable agent procedures | `skills/<skill>/SKILL.md` | Keep cross-room skills here and list them in `SKILLS.md` |
| Room-specific agent procedures | `workflows/<room>/skills/<skill>/SKILL.md` | Keep scoped skills in their room; list each in that room's `CONTEXT.md` and in `SKILLS.md` |
| Research principles and standards | `workflows/research/knowledge/research-principles.md`, `evidence-and-claims.md`, `reproducibility-and-integrity.md`, and `communication-and-visual-design.md` | Canonical research-room practice; change these before changing a skill that implements them |
| Research procedures for agents | `workflows/research/skills/<skill>/SKILL.md` | Skills operationalise the research source-of-truth docs; link back instead of maintaining competing policy text |
| Model/agent benchmark guidance and local evaluation records | `docs/model-evaluation-and-benchmarks.md` and the relevant project repository | Recheck benchmark versions and source dates; keep project-specific evaluation data, results and decisions with the project |
| Model routing policy, evidence interpretation and change procedure | `docs/model-routing.md` | Separate public product facts, policy, execution receipts and local evaluation; version host-specific machine policy separately |
| Model access types and offer comparison method | `docs/model-access-and-offers.md` | Verify current eligibility and terms at provider sources; keep personal account status and secrets local and untracked |
| Project question, protocol, evidence and deviations | The relevant project repository, using `workflows/research/templates/` | Copy and complete records in project context; do not store project data or findings in this generic starter |
| Cross-room durable memory | `MEMORY.md` | Keep brief; link to room-owned sources |
| Shared procedures and decision rules | `PROTOCOLS.md` | Version material changes and record the effective date |
| Cross-room workflow explanations and source-based guidance | `docs/` | Keep maintained explanations here; cite primary or authoritative sources and label guidance by scope |
| Room names and ownership | `ROOMS.md` | Update when rooms are added, renamed or re-scoped |
| Project code, data references, evidence and delivery records | `projects/<project-name>/` Git submodule and its own repository records | Commit and push project work to its own remote; this repository tracks only the submodule pointer |

If ownership is unclear, do not silently create a second canonical copy. Resolve the owner, then update this map.
