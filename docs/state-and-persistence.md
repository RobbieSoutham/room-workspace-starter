# State and persistence

Different records answer different questions. Keep active state, durable knowledge, policy, evidence and session telemetry separate so that one cannot silently masquerade as another.

| Record | Answers | Update pattern |
|---|---|---|
| `CURRENT.md` | What is active now, blocked and next? | Short, mutable pointer; link to detailed receipts |
| `MEMORY.md` / room memory | What durable context is likely to matter later? | Small, curated facts with links and provenance |
| `knowledge/` | What stable domain guidance or decision is reusable? | Canonical documents; revise with evidence and ownership |
| `PROTOCOLS.md` | Which shared procedures are in force? | Version/effective date; link to canonical procedure |
| Project evidence/decision records | What happened, under which method/data/version, and what was concluded? | Preserve provenance and history; update through explicit receipts |
| Session/task registry | Which processes, agents, handoffs and runs exist? | Machine-maintained lineage/liveness; not quality or truth |
| Dashboard/index | What should be surfaced for navigation? | Derived view; rebuild from canonical records where possible |

## Memory write-back

After meaningful work, decide whether a reusable fact belongs in an existing canonical file. Search before adding. Choose `ADD`, `UPDATE`, `SUPERSEDE` or `NOOP`; retain dates and rationale where they affect interpretation. Keep volatile service, model, price and offer state in a dated live register, not permanent memory. Link to evidence rather than copying it into several summaries.

## Session and handoff records

For long-running or delegated work, retain objective, authorized scope, owner room, in-flight artifacts, process/session identity when useful, blockers, next action and canonical pointers. Registration and liveness are operational evidence only. A successful CLI exit or agent response does not prove correctness, scientific validity, model identity or approval.

Use a database or event log when multiple writers, lineage, audit history or concurrent updates require it. Keep derived indexes rebuildable and avoid storing unique authority only in an ephemeral chat or dashboard. Restrict telemetry that may contain prompts, data paths or provider details.
