# Workspace instructions for Claude

This repository coordinates shared work through three rooms: Operations, Research and Projects. Treat these instructions as the workspace operating rules. Adapt names and examples to the host environment without adding personal, account-specific or machine-specific details.

## Identity and user preferences

At the start of a session in this workspace, read `SOUL.md` and `USER.md`. Read this file as well. Apply the values and preferences throughout the task; do not merely acknowledge them.

- `SOUL.md` describes the assistant's working values and default behaviour.
- `USER.md` records concise, stable preferences of the current user.
- Room `CONTEXT.md` and `CURRENT.md` define the domain boundary and active state.
- `SOURCE_OF_TRUTH.md` maps durable information to its canonical home.

System and safety requirements take precedence. Follow the user's explicit instruction for the current task, then the applicable workspace and room rules. Use `SOUL.md` and `USER.md` as defaults where no more specific instruction applies. Do not infer missing personal details or treat `USER.md` as an authority for project status.

Be direct, resourceful and accurate. Investigate available context before asking questions. State what is observed, inferred or unknown; never claim a check or action that did not happen. Surface material risks in proportion to the task. Keep private information private and report the useful result, not a transcript of the work.

## Room routing

### Resolve the room before acting

First honour any room binding supplied by the host environment. If your agent identity or conversation is bound to a room, work there and reply through that same conversation. Do not switch rooms unless the user asks or the task genuinely requires cross-room work. Your first room-specific read is that room's `CONTEXT.md`.

If there is no binding, route by the work's primary owner:

| Work | Room |
|---|---|
| Shared workspace, tools, reliability, security and operating procedures | `workflows/operations/` |
| Research questions, evidence, methods, analysis and scholarly outputs | `workflows/research/` |
| Product, business and project intake or delivery coordination | `workflows/projects/` |

A host may use room-specific agent clones and an unbound coordinator. Keep the mapping from host agent identifiers to these room names in the host's own configuration or its local `AGENTS.md`; do not put private account IDs, chat IDs or machine paths in this generic repository. The coordinator routes by task type, and hands off to a room owner only when delegation is useful and available.

For cross-room work, identify the affected rooms, keep each artifact in its owning source and update ownership documentation if the canonical owner changes. Do not copy one room's whole context into another.

### Load context selectively

Use this order, skipping items that are irrelevant to the task:

1. `AGENTS.md` for host or repository-specific entry instructions.
2. `CLAUDE.md`, `SOUL.md` and `USER.md` for workspace rules, assistant behaviour and user preferences.
3. `ROOMS.md` and the selected room's `CONTEXT.md` for room ownership and boundaries.
4. That room's `CURRENT.md` when active work, prior decisions or next actions matter.
5. `SOURCE_OF_TRUTH.md` before creating or changing durable information.
6. `SKILLS.md` and only the skill or skills directly relevant to the task.
7. The specific knowledge files, protocols, project records or references needed to do the work.

`CONTEXT.md` is a stable room definition. `CURRENT.md` is a concise active-state note, not a history dump. Read `MEMORY.md`, room memory, `PROTOCOLS.md` or a `HEARTBEAT.md` only when relevant. Do not recursively load all rooms, memory, skills or repositories by default. Prefer targeted search and bounded reads. For long work, keep a compact checkpoint of scope, evidence, changes, open questions and next steps in the room's working area when one exists.

## Decision rules

Use the lightest reliable process. Make reversible, low-impact choices directly when the user has authorised the task. Slow down for decisions involving safety, privacy, research integrity, substantial cost, shared services, publication, access or irreversible effects.

### Ordered engineering and process review (Elon's five-step heuristic)

For design, engineering and operational-process changes, use this sequence when it fits:

1. **Question the requirement.** Identify the intended outcome, who owns each constraint and why it exists. Separate a genuine requirement from inherited convention or an untested assumption.
2. **Delete unnecessary parts or steps.** Remove work that does not serve the outcome. Preserve required safety controls, legal obligations, research evidence and recovery mechanisms.
3. **Simplify or optimise what remains.** Reduce complexity only after confirming the remaining parts are needed.
4. **Accelerate the cycle.** Shorten feedback and delivery time only after the process is valid and sufficiently simple.
5. **Automate stable repetition.** Automate only when the steps, inputs, outcomes, ownership and failure recovery are understood.

### Reasoning, risk and delegation

- Match effort to uncertainty, impact and reversibility. Routine lookups and small edits need a direct pass; architecture, policy, security, high-stakes or ambiguous-cause work needs deeper analysis and explicit verification.
- Before a consequential plan, consider its most plausible failure modes, hidden assumptions, early warning signs and rollback or stop conditions. Use the global `premortem` skill when a structured review is useful.
- Delegate only when subtasks are meaningfully separable, parallel expertise matters, or independent review will improve confidence. Do not spawn agents for ceremony. Give each delegate a bounded role, scope, success criterion, return budget and structured output contract. Keep reviewers independent and read-only where appropriate; use a different model family when that materially improves independence and one is available.
- Prefer a deterministic script over an agent for mechanical checks such as counts, schemas, links and diffs. Review the returned artefact and evidence, not a delegate's hidden reasoning or raw transcript.
- Verify important claims and changes against primary records or reproducible checks. For high-impact shared changes, use an independent review when available.
- If a required tool, dependency, credential or environment is missing, do not bluff or silently skip the check. Use existing project tooling when possible; otherwise state what is blocked and the precise next setup step.

## Source-of-truth and file placement

Follow `SOURCE_OF_TRUTH.md`. Keep one canonical home for each fact; link to it elsewhere instead of maintaining competing copies.

- `workflows/<room>/CONTEXT.md`: room purpose, boundaries, conventions and pointers.
- `workflows/<room>/CURRENT.md`: current priorities, status and next actions.
- `workflows/<room>/knowledge/`: durable, reusable facts and decisions owned by that room.
- `workflows/<room>/skills/` and `skills/`: room-local and cross-room task procedures.
- `PROTOCOLS.md`: procedures shared across rooms, with version and effective date for material changes.
- `MEMORY.md`: brief, durable facts shared across rooms, linked to their canonical sources.
- `workflows/<room>/memory/` or `memory/`: durable room-level or dated session memory, according to the local convention. Keep it concise and do not use it as a task-status duplicate.
- `projects/<project-name>/`: project repositories included as Git submodules. Their code, project-specific evidence, data references, decisions and delivery records belong in the project repository.

`workflows/projects/` coordinates project intake and portfolio-level status; it is not a substitute for the project repository. Research templates under `workflows/research/templates/` are copied into the relevant project submodule and completed there. Keep restricted data in approved storage and link to it only where access is appropriate.

### Project Git submodules

Each project is an independent Git repository with its own remote, history, access controls and release decisions. Add it to this workspace as a submodule under `projects/<project-name>/`. The workspace repository tracks the submodule URL and commit pointer; it does not absorb the project's files or history.

- Clone the workspace with submodules using `git clone --recurse-submodules <workspace-url>`; for an existing clone use `git submodule update --init --recursive`.
- Add a project with `git submodule add <project-repository-url> projects/<project-name>` after confirming the intended remote and access.
- Commit and push project changes from inside the project repository to its own remote. Then update and commit the submodule pointer in the workspace repository.
- Before updating a submodule pointer, confirm the referenced project commit exists on the intended remote and is accessible to the workspace's intended users.
- Never store credentials in submodule URLs. Do not push either repository unless authorised; publishing the workspace pointer does not publish an unpushed project commit.
- Check the submodule's own status and diff. A clean workspace status does not prove submodule contents are committed or pushed.

## Skills

`SKILLS.md` is the complete skills index. Canonical skills live in `skills/<name>/SKILL.md` (global) and `workflows/<room>/skills/<name>/SKILL.md` (room-local). Read the relevant skill before following a recurring procedure. Skills implement policy; they do not override higher-priority instructions or replace canonical knowledge documents.

When adding, renaming or retiring a skill, use `skill-maintenance`, then update `SKILLS.md` and the owning room's `CONTEXT.md`. If a platform needs native skill registration or symlinks, keep the workspace skill as the single source and document the bridge in host-specific instructions.

## Data, storage and safety

- Keep credentials, tokens, private personal or customer data, restricted research data, raw private exports, virtual environments, dependency caches, databases, generated builds and machine-specific state out of this public starter repository.
- Store project-specific code and records in the project's submodule. Put large or restricted data in approved storage and keep only permitted references, metadata or reproducible acquisition instructions in Git.
- Before committing, inspect status, staged changes, file sizes, binary files and submodule pointers. Use `.gitignore` as a supplement, not as a substitute for reviewing staged content. Run secret scanning when available, especially before publication.
- Respect third-party licences and attribution. Do not add a blanket licence unless all contributors have authority to grant it.
- Treat publication, external messages, purchases, account changes, permission changes and destructive actions as requiring explicit user authorisation. A plan or checklist is not approval.
- Prefer scoped and reversible changes. Preserve unrelated work, historical records, user data and active sessions. Do not terminate access paths or services unless the task authorises it.

## Memory, concurrency and write-back

After meaningful work, update the owning room's `CURRENT.md` when active status or next actions changed. Add durable room or cross-room memory only when it will matter again; link to detailed evidence rather than duplicating it. Skip trivial edits and transient search noise.

Before adding a durable fact, search its canonical store and choose one action: **ADD** a new fact, **UPDATE** a changed fact in place, **SUPERSEDE** an outdated fact with a link to its replacement, or **NOOP** when it is already represented. Do not leave contradictory active claims in separate files.

Set review timing by fact type. Recheck volatile live state before relying on it; keep it in `CURRENT.md` or another live source rather than durable memory. Project decisions change more slowly and should retain their dated evidence. Stable policy needs no routine expiry, but should be revised when its owner changes it.

Before editing a shared or append-only record, reread it immediately before the change and check for concurrent updates. Use the repository's locking or atomic-write helpers if provided for shared state. Preserve history when revising a decision; mark superseded material rather than silently erasing it.

## Writing and final handoff

Use the language, spelling and formatting requested by the user or recorded in `USER.md`. If neither specifies a preference, match the user's language and use clear, consistent spelling. Keep prose direct and make technical terms understandable in context.

In the final handoff, state what changed, where the canonical result lives, what checks actually ran, material limits or uncertainty, and any decision still needed. Do not repeat the whole work log.

## Heartbeats and scheduled work

For a heartbeat request, read `HEARTBEAT.md` and perform only the checks or actions it specifies or clearly implies. If no action is needed, return the host's designated no-op response. Use scheduled jobs for exact timing; use heartbeat work only for lightweight periodic review. Do not start a service or scheduled process merely to make a check appear green.

## Repository map

- `workflows/operations/` owns shared workspace operations.
- `workflows/research/` owns reusable research principles, templates and research skills.
- `workflows/projects/` owns project intake and shared delivery coordination.
- `projects/<project-name>/` contains independently maintained project repositories as Git submodules.
- `SOURCE_OF_TRUTH.md` and `SKILLS.md` map canonical ownership and reusable procedures.
