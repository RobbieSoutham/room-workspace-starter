# Agent entry point

Before working in this repository:

1. Read `CLAUDE.md` for workspace rules and room routing.
2. Read `SOUL.md` and `USER.md`; apply their working values and stable preferences throughout the task.
3. Read the selected room's `CONTEXT.md`.
4. Read that room's `CURRENT.md` when the task depends on active work.
5. Check `SOURCE_OF_TRUTH.md` before creating or changing canonical information.

Keep work inside the selected room unless the user asks for a cross-room change. Do not copy private or machine-specific information into this template. Ask before actions that publish data, contact external services or destroy user data.

The workspace identity and user-preference files are `SOUL.md` and `USER.md`; do not infer missing personal details. The complete skills index is `SKILLS.md`. Global skills live at `skills/<skill-name>/SKILL.md`; room-local skills live at `workflows/<room>/skills/<skill-name>/SKILL.md` and are listed in the room's `CONTEXT.md`. Read a relevant skill before using it.
