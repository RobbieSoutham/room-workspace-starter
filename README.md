# Room-based workspace starter

A small template for keeping agent instructions, room context, current work and durable knowledge in one Git repository.

## Start here

1. Read `AGENTS.md`, then `CLAUDE.md`.
2. Rename, add or remove the example rooms under `workflows/` to fit your work.
3. Give each room a short `CONTEXT.md` and a frequently updated `CURRENT.md`.
4. Record durable facts in that room's `knowledge/`; keep dated working material elsewhere in the room.
5. Update `ROOMS.md` and `SOURCE_OF_TRUTH.md` when ownership changes.

## Layout

```text
AGENTS.md                 Entry point for coding agents
CLAUDE.md                 Shared workspace rules and room routing
ROOMS.md                  Room names, purpose and boundaries
SOURCE_OF_TRUTH.md        Canonical location for each kind of information
REPOSITORIES.md           How workspace and project repositories relate
MEMORY.md                 Small, durable cross-room facts
PROTOCOLS.md              Versioned procedures and decision rules
workflows/<room>/
  CONTEXT.md              Room identity, conventions and boundaries
  CURRENT.md              Active state and next actions
  knowledge/README.md     Index and rules for room-owned knowledge
  memory/                 Room-specific durable notes
```

The example rooms are `operations`, `research` and `projects`. They are placeholders; adapt them freely.
The Research room is also a practical example: [`PRACTICES.md`](workflows/research/PRACTICES.md) walks through an evidence-led project, a fictional worked example shows how the pieces fit, and copyable templates live in `workflows/research/templates/`.

## Principles

- Keep one canonical home for each fact and link to it elsewhere.
- Keep this workspace template separate from project source repositories; see `REPOSITORIES.md`.
- Load the relevant room context before acting; load other rooms only when needed.
- Keep credentials, personal data and machine-specific state out of Git.
- Prefer short, maintained source-of-truth documents over duplicated summaries.
- Record changes to important decisions and procedures with dates and rationale.
