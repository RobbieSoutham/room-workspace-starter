# System overview

This starter uses a room-based filesystem as the coordination layer for people and agents. Rooms define ownership and context; skills define repeatable task procedures; project repositories hold project code and evidence; root documents establish shared rules. The filesystem is the source of truth. Dashboards, agent memory, chat history and generated indexes are views or working aids unless a named authority says otherwise.

## Main components

| Component | Role |
|---|---|
| `AGENTS.md` | Short repository entry point and host integration notes |
| `CLAUDE.md` | Full workspace rules, context loading, room routing and decision practices; other agents may use a correspondingly named shared instruction file |
| `SOUL.md`, `USER.md` | Assistant behaviour defaults and optional stable user preferences |
| `ROOMS.md`, `SOURCE_OF_TRUTH.md` | Room ownership and canonical file map |
| `PROTOCOLS.md` | Versioned shared procedures and decision rules |
| `SKILLS.md`, `skills/` | Skill index and reusable cross-room procedures |
| `workflows/<room>/` | Room context, active state, knowledge and room-specific skills |
| `projects/<project>/` | Independent project Git repositories, commonly included as submodules |
| `tools/` | Deterministic shared tools and CLI bridges, when used |

## Runtime patterns

- A host may bind a room-specific agent to a room. On a bound conversation, first load that room's `CONTEXT.md` and remain in its ownership boundary unless the user expands scope.
- An unbound coordinator routes by task type using the room map. It may delegate separable work, but the owning room remains responsible for the durable result.
- Global skills are available across rooms; room-local skills live beside their owner. A skill bridge can expose canonical skill files to multiple CLIs without copying each skill's contents.
- Cross-CLI launchers can provide consistent invocation, session registration, lineage and usage records. These records show what was launched; they do not establish output quality or prove which model actually executed unless runtime evidence records that.
- Dashboards summarize canonical records and live services. They must link back to the source record and avoid becoming a second place to maintain status.
- Scheduled work may use more than one scheduler. Keep one declared source of truth for schedules, reconcile effective cron/systemd/gateway state, and monitor missed or failed runs.

## Boundaries

Keep provider routing and secrets in local configuration, not in a public starter. Keep machine-specific agent IDs, chat IDs, remote hostnames, personal contacts and current project status in the host workspace. Keep project methods and results in their project repository. Use least privilege for tools and data; delegation does not transfer human accountability for research, external release or spending decisions.

This document describes a reusable architecture pattern. Implementations vary; check the host's current configuration before assuming any component is installed or active.
