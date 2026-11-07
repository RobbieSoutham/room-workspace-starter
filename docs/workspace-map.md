# Workspace map

Keep this map shallow: it records stable ownership and placement rules, not every file or runtime state. File existence alone does not prove that a file is loaded, current or authoritative.

## Suggested layout

| Path | Purpose | Authority |
|---|---|---|
| `CLAUDE.md`, `AGENTS.md` | Shared workspace and host/agent entry instructions | Exact instruction files |
| `SOUL.md`, `USER.md` | Assistant defaults and optional stable preferences | Exact file; do not duplicate personal preferences in generic system docs |
| `ROOMS.md`, `SOURCE_OF_TRUTH.md` | Room ownership and canonical topic-to-file map | Maintained with room boundaries |
| `PROTOCOLS.md` | Shared procedures and decision rules | Named canonical procedure documents |
| `docs/` | Human-readable system/workflow explanations | Docs index and cited source-of-truth files |
| `skills/` | Cross-room procedures | Each `SKILL.md`, indexed in `SKILLS.md` |
| `tools/` | Shared deterministic tools and adapters | Implementation and relevant operating docs |
| `workflows/<room>/` | Room context, current state, knowledge, skills and work areas | Room `CONTEXT.md`, `CURRENT.md` and domain authorities |
| `projects/<name>/` | Independent project source/evidence repository or Git submodule | Project repository and project records |
| `memory/`, `MEMORY.md` | Dated observations and brief cross-room durable pointers | Memory policy and canonical room sources |
| external approved storage | Large, restricted, generated or private data | Data owner and access policy |

## Placement rules

- Put task work in its owning room, normally a dated or named directory under `working/`.
- Put global reusable skills under `skills/<name>/SKILL.md`; room skills under `workflows/<room>/skills/<name>/SKILL.md`.
- Put project code, protocols, results, decisions and project-specific references in the project repository. The workspace tracks a submodule URL and commit pointer, not a second copy of the project contents.
- Keep credentials, private exports, participant or customer data, caches, virtual environments, dependency trees, database files and generated bulk output out of Git by default.
- Configure storage thresholds and external mount paths locally. Do not publish host paths or presume another machine has the same mount.
- Update `SOURCE_OF_TRUTH.md` when ownership changes; elsewhere, link to the canonical record instead of copying it.

## Host-specific overlay

Keep room-agent bindings, CLI invocation paths, authentication instructions, storage mounts, scheduler inventory, secrets handling and active project paths in a private host overlay or local configuration. Do not put personal account IDs or remote-access details in this generic starter.
