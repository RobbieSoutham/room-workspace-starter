# Workspace instructions for Claude

This repository is a shared work environment organised into three rooms: **Operations**, **Research** and **Projects**. It is a generic starter: adapt the room names, owners and procedures to the people using it, and keep private or machine-specific material out of the repository.

## 1. Choose the room and respect its boundary

If your host explicitly binds you to a room, follow that binding. Otherwise route by the work's primary owner:

| Work | Room |
|---|---|
| Shared tools, reliability, security and operating procedures | `workflows/operations/` |
| Research questions, methods, evidence and scholarly outputs | `workflows/research/` |
| Products, delivery and projects without a more specific owner | `workflows/projects/` |

Read that room's `CONTEXT.md` before acting. Stay in the selected room unless the user requests cross-room work or the work genuinely affects another room. For cross-room work, name the rooms and keep each fact in its owning source.

## 2. Load context in this order

1. `AGENTS.md` for the repository entry point and environment-specific rules.
2. `ROOMS.md` and the selected room's `CONTEXT.md` for ownership and boundaries.
3. The selected room's `CURRENT.md` when active status, prior decisions or next actions matter.
4. `SOURCE_OF_TRUTH.md` before creating or editing durable information.
5. `SKILLS.md`, then only the one or two skills relevant to the task.
6. The referenced knowledge, protocol, template or project record needed to do the work.

Do not load every room, memory file or skill by default. A room's `CONTEXT.md` explains its remit; `CURRENT.md` is its short-lived active state, not a durable policy document.

## 3. Preserve canonical ownership

Use `SOURCE_OF_TRUTH.md` to resolve where information belongs. The normal pattern is:

- `workflows/<room>/CONTEXT.md`: stable purpose, boundaries, conventions and pointers.
- `workflows/<room>/CURRENT.md`: concise active work, status and next actions.
- `workflows/<room>/knowledge/`: durable reusable facts, decisions and room procedures.
- `workflows/<room>/skills/<skill>/SKILL.md`: task workflows specific to that room.
- `skills/<skill>/SKILL.md`: reusable workflows that apply across rooms.
- `PROTOCOLS.md`: procedures shared by multiple rooms.
- `MEMORY.md`: brief cross-room facts that link to the canonical record.
- Project repositories: project-specific code, datasets, evidence and delivery records; see `REPOSITORIES.md`.

Prefer a link to the canonical source over a copied summary. When a source-of-truth owner changes, update `SOURCE_OF_TRUTH.md` and the relevant room context in the same change. Skills explain how to do recurring work; they do not override user instructions or replace policy documents.

## 4. Use the starter and skills consistently

`SKILLS.md` is the complete index. Global skills are stored under `skills/`; room skills are under the owning room's `skills/` directory and should also be listed in that room's `CONTEXT.md`. Read a skill before invoking its procedure. If a task does not match a skill, proceed with ordinary judgement rather than forcing a workflow.

When adapting this starter for a new team:

1. Rename, add or remove rooms and update `ROOMS.md`.
2. Set each room's purpose, boundaries, canonical files and skills in `CONTEXT.md`.
3. Keep `CURRENT.md` focused on active items, with owners and next actions where useful.
4. Put durable facts and procedures into the correct `knowledge/` or shared protocol file.
5. Update `SOURCE_OF_TRUTH.md`, `SKILLS.md` and links affected by the change.
6. Remove example material that is not appropriate to the team's work; keep fictional examples clearly labelled.

## 5. Protect data and repositories

Do not place credentials, tokens, private personal or customer data, restricted research data, raw private exports, virtual environments, dependency caches, databases, generated builds or machine-specific state in this starter. Keep project artifacts in their approved storage and use `.gitignore` as a supplement, not a substitute for checking the staged files.

Before committing, inspect `git status`, the full staged diff, file sizes and binary additions. Use available secret scanning for repository changes, especially before a public release. Keep third-party licences and attribution; do not grant a blanket licence unless contributors can do so. Follow `safe-release-review` before preparing an authorised release.

Treat publication, external communications, purchases, account changes and destructive actions as requiring explicit user authorisation. A plan or checklist does not grant that authorisation. Prefer reversible, scoped changes and leave unrelated work untouched.

## 6. Make work reviewable

Use the lightest process that fits the task. Preserve prior records when changing durable decisions; record rationale and effective dates for shared procedures. Verify outcomes using checks suited to the change and report only checks actually performed. In the final handoff, state what changed, the canonical files involved, verification results, remaining uncertainty and any next decision.

## Repository map

- `workflows/operations/` owns shared workspace and service operations.
- `workflows/research/` owns reusable research practice, with generic templates and a fictional example.
- `workflows/projects/` owns shared project intake and delivery coordination.
- `REPOSITORIES.md` explains when project work belongs in a separate repository.
- `SOURCE_OF_TRUTH.md` and `SKILLS.md` are the authoritative indexes for file ownership and reusable procedures.
