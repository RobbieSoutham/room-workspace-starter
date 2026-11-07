# Example: failed first check stays visible

This is a fictional example showing how to preserve a failure and its repair.

| Version | Check | Status | Record |
|---|---|---|---|
| Search plan v0 | Seed relevance check | **FAIL** | Both seeds described a neighbouring topic and neither represented the target population. Search was not run. |
| Search plan v1 | Seed relevance check | **PASS_WITH_LIMITATIONS** | Three seeds now span the target population and method; one subtopic has no seed. |
| Search run v1 | Candidate identity check | **FAIL** | Two provider records shared a title but had different identifiers; one was incorrectly merged in the draft output. |
| Search run v2 | Candidate identity check | **PASS** | Merge rule now requires a stable identifier. The original failure and correction remain linked. |

The first pass is not edited to appear successful. The final report states that the seed check had a limited pass, the initial identity check failed, and the corrected run passed the revised check. See the [check-log template](../templates/check-log.md) and [evidence record guidance](../../../docs/evidence-and-failure-records.md).
