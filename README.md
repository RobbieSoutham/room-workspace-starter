# Room-based workspace starter

A small template for keeping agent instructions, room context, current work and durable knowledge in one Git repository.

## Start here

1. Read `AGENTS.md`, `CLAUDE.md`, `SOUL.md` and `USER.md`.
2. Replace the prompts in `USER.md` with only the stable preferences that are useful to this workspace; remove unused fields.
3. Rename, add or remove the example rooms under `workflows/` to fit your work.
4. Give each room a short `CONTEXT.md` and a frequently updated `CURRENT.md`.
5. Record durable facts in that room's `knowledge/`; keep dated working material elsewhere in the room.
6. Update `ROOMS.md` and `SOURCE_OF_TRUTH.md` when ownership changes.

## Layout

```text
AGENTS.md                 Entry point for coding agents
CLAUDE.md                 Workspace rules, context-loading and ownership
SOUL.md                   Assistant values and working defaults
USER.md                   Editable, non-sensitive user preferences
ROOMS.md                  Room names, purpose and boundaries
SOURCE_OF_TRUTH.md        Canonical location for each kind of information
SKILLS.md                 Complete global and room-local skill index
MEMORY.md                 Small, durable cross-room facts
PROTOCOLS.md              Versioned procedures and decision rules
docs/                     Cross-room workflow documentation and source-backed guidance
config/ai/
  model_catalog.yaml       Model IDs, access surfaces, current roles and hard constraints
  routing_policy.yaml      Active task lanes, escalation, protected routes and promotion gates
skills/<skill>/SKILL.md   Reusable procedures available across rooms
workflows/<room>/
  CONTEXT.md              Room identity, conventions and boundaries
  CURRENT.md              Active state and next actions
  knowledge/README.md     Index and rules for room-owned knowledge
  skills/<skill>/SKILL.md  Room-local procedures for agents
  memory/                 Room-specific durable notes
  research/               Research examples, planning, papers, notes and outputs
projects/<project>/       Independent project repository as a Git submodule
```

The example rooms are `operations`, `research` and `projects`. They are placeholders; adapt them freely.
Each room has its own context, source-of-truth knowledge and relevant skills. Global skills in `skills/` apply across rooms; `SKILLS.md` indexes both sets. The starter preserves the working setup: flat native Codex default with no automatic fallbacks, explicit task lanes for planning, implementation, source gathering, extraction and independent review, a protected specialist gate, a manual fourth-family verifier, hard data-class boundaries, live task-matched leaderboards, local evaluation gates, and a weekly human-reviewed offer-source watch. `config/ai/` records the concrete routing shape; `docs/` explains the policies, benchmarks and current public offers. Remove names, account identities, private endpoints, credentials, balances and host paths when adapting the setup; keep the operating design intact.

For the current setup, start with [`config/ai/model_catalog.yaml`](config/ai/model_catalog.yaml) and [`config/ai/routing_policy.yaml`](config/ai/routing_policy.yaml), then read [Model routing](docs/model-routing.md), the [live leaderboard and benchmark board](docs/model-evaluation-and-benchmarks.md#live-benchmark-board) and the [current promotions/free-tiers register](docs/model-access-and-offers.md).

## Principles

- Keep one canonical home for each fact and link to it elsewhere.
- Keep project source in `projects/<name>/` Git submodules; each project has its own history and remote. See `CLAUDE.md` for the workflow.
- Load `SOUL.md` and `USER.md` and apply them throughout the task.
- Load the relevant room context before acting; load other rooms only when needed.
- Keep credentials, personal data and machine-specific state out of Git.
- Prefer short, maintained source-of-truth documents over duplicated summaries.
- Record changes to important decisions and procedures with dates and rationale.
