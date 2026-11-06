# Reproducibility and research integrity

**Owner:** Research room · **Status:** Canonical source of truth for protocols, deviations, integrity boundaries and release checks.

## Plan before outcome-driven work

For work intended to evaluate or support a claim, record the design before examining outcome data where feasible. The project protocol should identify its version and date, question, data/materials, inclusion rules, units, comparisons, outcomes or analytic questions, analysis order, planned checks, exclusions and stopping rules. Record software, method and input versions, environment, random seeds where relevant, and expected outputs.

Exploratory work may adapt as understanding develops. Label it exploratory and preserve when and why the design changed. A later claim-bearing use needs a stronger plan and review; it must not be presented as if that plan governed the earlier exploration.

## Preserve deviations and inconvenient findings

Keep the initial plan. Log material changes with date, reason, evidence available at the time, effects on interpretation and any review or approval. Copy [`../templates/deviation_log.md`](../templates/deviation_log.md) into the project repository.

Preserve relevant null, negative, inconclusive, invalid and non-estimable outcomes, as well as failed controls and unexpected observations. Do not select a result or measure after the fact without identifying that choice as exploratory.

## Keep execution and result judgements separate

Report separately:

- whether the planned work was ready and executed;
- whether the method was implemented faithfully and checked;
- what the evidence showed and with what uncertainty;
- what an independent reviewer concluded.

A successful run is not confirmation of a hypothesis. A technical failure is not evidence for the opposite hypothesis. Scale independent review and verification to the consequence of error; give reviewers the evidence and a specific question without implying a desired verdict.

## Ethics, privacy and intellectual property

Before collection, access or release, identify the ethics approvals, consent, privacy, security, copyright, licensing, retention and data-access rules that apply. Do not assume that online availability permits unrestricted reuse. Follow relevant institutional, funder, publisher, provider and jurisdictional requirements.

Keep personal, confidential or restricted materials out of public repositories and general-purpose notes. Share data or derivatives only when permission and safeguards allow it. Record boundaries and approval points in the project plan.

## Tools and reporting

For iterative computational experiments, identify each reported metric and its units or scale, run/version, observation time and completed step. Keep the latest observation distinct from a best or selected result. Preserve unavailable historical values as gaps; do not infer them or rerun archived work merely to backfill a report without the project owner's authority.

For computational work, make a fresh run from documented inputs where practical and check important outputs against an independent calculation, baseline or scientific oracle when available. For interpretive work, make the path from source material to interpretation inspectable within the permissions that apply.

If AI or automated tools assist research, verify their output against sources and actual results. Verify every citation, protect confidential input, and follow institutional, funder and publisher rules on disclosure and use. Record enough detail for the project to explain how tool output was checked.

Before releasing a paper, report, presentation or software, check that claims remain within the evidence, meaningful negative or uncertain findings are represented, citations are verified, and included files have been checked for permissions, secrets, personal data, machine-specific paths and generated artefacts.

## Maintenance

This is the policy source for the Research room. Skills should link here rather than duplicate these rules. Project protocols, approvals, deviations and release decisions are project records, not shared workspace policy.
