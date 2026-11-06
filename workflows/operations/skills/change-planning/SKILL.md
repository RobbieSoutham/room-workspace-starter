---
name: change-planning
description: Plan a consequential operations change with scope, validation, authorisation and rollback.
---

# Change planning

Use before a change that can interrupt shared services, alter access or data, incur ongoing cost, or affect multiple rooms.

1. Name the desired outcome, affected resources, current state and dependencies.
2. Identify the authorised operator and any approvals required; planning is not approval.
3. Capture the minimum baseline needed to detect regression.
4. Define an ordered change, success checks, stop conditions and a rollback that restores the prior state.
5. Include users, timing, expected outage, costs and data-preservation needs.
6. After execution, compare observed results with the baseline and record deviations.

Do not combine unrelated changes into one unreviewable step. Keep secrets out of change records and link to their approved storage.
