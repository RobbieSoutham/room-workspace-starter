# Protocol register

This register indexes active, reusable protocols in the workspace. They may apply across rooms or to one room; each scope is stated below. Every entry identifies its owner, version, effective date and canonical instructions. The detailed rule lives at the linked source; this file does not maintain a competing copy.

**Last reviewed:** 2026-11-06

## Active protocols

| Protocol | Owner | Version / effective date | Canonical instructions | Scope |
|---|---|---|---|---|
| Requirement-first engineering and process review | Workspace maintainers | 1.0.0 / 2026-11-06 | [`CLAUDE.md` — Ordered engineering and process review](CLAUDE.md#ordered-engineering-and-process-review) | Design, engineering and operational process changes; apply proportionately and preserve required safeguards |
| Research design, evidence and integrity | Research room owner | 1.0.0 / 2026-11-06 | [`research-principles.md`](workflows/research/knowledge/research-principles.md), [`evidence-and-claims.md`](workflows/research/knowledge/evidence-and-claims.md), [`reproducibility-and-integrity.md`](workflows/research/knowledge/reproducibility-and-integrity.md) | Claim-bearing research across methods; project protocols and evidence stay in their project repository |
| Literature search and synthesis | Research room owner | 1.0.0 / 2026-11-06 | [`evidence-and-claims.md`](workflows/research/knowledge/evidence-and-claims.md) and [`evidence-led-review`](workflows/research/skills/evidence-led-review/SKILL.md) | Search scope, query records, eligibility, evidence extraction and synthesis; follow current field standards |
| Science-backed model routing and evaluation | Operations and research owners | 1.0.0 / 2026-11-07 | [`docs/model-routing.md`](docs/model-routing.md), [`docs/model-evaluation-and-benchmarks.md`](docs/model-evaluation-and-benchmarks.md) | Public benchmarks are task-bound priors; route changes require current access checks and suitable local evaluation; verifier outputs remain fallible |
| Canonical memory and source-of-truth updates | Workspace maintainers | 1.0.0 / 2026-11-06 | [`CLAUDE.md` — Source-of-truth and file placement](CLAUDE.md#source-of-truth-and-file-placement) and [`CLAUDE.md` — Memory, concurrency and write-back](CLAUDE.md#memory-concurrency-and-write-back) | Durable shared or room knowledge; keeps active state, memory and policy distinct |
| Delegation and independent review | Task owner | 1.0.0 / 2026-11-06 | [`CLAUDE.md` — Reasoning, risk and delegation](CLAUDE.md#reasoning-risk-and-delegation) | Cross-room delegation and review; task owners choose suitable available agents and deterministic checks |
| Project repository boundaries | Project owner | 1.0.0 / 2026-11-06 | [`CLAUDE.md` — Project Git submodules](CLAUDE.md#project-git-submodules) | Project code and records live in independent Git repositories; the workspace tracks submodule pointers |

## Updating this register

1. Change the canonical source first and record the decision, owner and rationale there when appropriate.
2. Increment the affected protocol version, set its effective date and update this register in the same change.
3. Check linked skills, room contexts, templates and other references for alignment.
4. Mark a proposal `candidate` until it has been reviewed and deliberately adopted. Do not call a dated experiment or project-only protocol active for every room.
5. Review time-sensitive protocols against their current implementation and evidence. If freshness is unknown, mark the entry `needs review` instead of implying it is current.

This generic starter excludes host-specific routing/model policy, personal data, project-only protocols and experimental procedures that have not been promoted. Add only rules a future user can safely apply after adapting the named owner and project boundaries.
