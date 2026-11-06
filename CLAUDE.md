# Workspace instructions

## Room model

This repository separates work into rooms under `workflows/`. Route each task to the closest room using `ROOMS.md`. A room owns its context, active status and durable domain knowledge.

## Reading order

Read `ROOMS.md` and the selected room's `CONTEXT.md` first. Read its `CURRENT.md` for active tasks, and consult `SOURCE_OF_TRUTH.md` before updating facts that may have another canonical home. Load only the additional material needed for the task.

## Writing rules

- Keep `CONTEXT.md` stable: purpose, boundaries, conventions and file locations.
- Keep `CURRENT.md` concise and current: active priorities, status and next steps.
- Put durable domain facts in `knowledge/`; put dated drafts and experiments in a room-local working area.
- Keep cross-room memory short and link to room-owned sources.
- Do not duplicate canonical material; link to its source instead.
- Do not store secrets, credentials or private personal data in this repository.

## Source precedence

Use the ownership map in `SOURCE_OF_TRUTH.md`. If two sources disagree, prefer the named canonical source, record the conflict and update secondary summaries only after resolving it.
