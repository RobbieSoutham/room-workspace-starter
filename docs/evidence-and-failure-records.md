# Evidence and failure records

Research records should let a colleague tell what was checked, what was observed and which version the conclusion applies to. Keep method quality, data integrity, implementation behaviour and scientific interpretation as separate questions.

## Minimum record

For each consequential check, capture:

- check name and the requirement or criterion;
- artifact identifier, version or content hash;
- check date and reviewer/tool;
- status: `PASS`, `PASS_WITH_LIMITATIONS`, `FAIL`, `BLOCKED`, `NOT_RUN` or `NOT_APPLICABLE`;
- evidence observed and its source;
- limitation or uncertainty;
- action taken and the next check.

Keep the first result immutable. When a later version changes, append a new row that links to the earlier one. Do not replace a failed result with a passing result or make the later version appear to have passed the earlier check. Report both the failure and the recovery.

## Failure versus limitation

- **Fail:** a required criterion was tested and not met.
- **Blocked:** the check could not run because a named dependency, permission or input was unavailable.
- **Not run:** no check was attempted.
- **Pass with limitations:** the criterion was met within a stated scope, but known limits remain.

These states are not interchangeable. A missing full text is a retrieval limitation or block, not a reason to mark a paper excluded. A quote found in an abstract confirms only that the text occurs there; claim support requires a separate semantic assessment and often full-text reading.

## Example: preserve the first failed check

The following record is fictional and illustrates chronology only:

| Version | Check | Result | Evidence | Next action |
|---|---|---|---|---|
| Draft 0 | Citation locator audit | **FAIL** | 3 of 12 in-text citations lacked a matching reference entry | Resolve identifiers and recheck the affected claims |
| Draft 1 | Citation locator audit | **PASS** | All 12 citations resolve; 2 source limitations remain documented | Independent claim-support review |
| Draft 1 | Claim-support review | **BLOCKED** | One cited source could not be accessed | Obtain permitted full text or narrow the claim |
| Draft 2 | Claim-support review | **PASS_WITH_LIMITATIONS** | 11 claims checked against full text; one claim narrowed to the available abstract | Retain limitation in the manuscript |

Draft 0 remains recorded as failed. Draft 2 passing its later checks does not change that history.

## Templates and use

Start from [`templates/check-log.md`](../workflows/research/templates/check-log.md) for a check trail. For systematic reviews, align reporting with the applicable [PRISMA guidance](https://www.prisma-statement.org/prisma-2020-statement) and preserve search/screening records. For AI-assisted work, record where AI influenced the workflow, what human checks were applied and what was not validated; a 2025 review reports substantial task-level error and supports human oversight ([Clark et al., 2025](https://doi.org/10.1017/rsm.2025.16)). The [PRISMA-AIM project](https://equator-network.org/reporting-guidelines/under-development/prisma-aim/) is currently listed as under development; do not present it as a final reporting standard.
