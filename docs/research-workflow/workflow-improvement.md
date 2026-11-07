# Evidence-led workflow improvement

Treat a reusable workflow as a versioned intervention. A plausible improvement is a candidate until a comparison shows that it helps for the intended tasks without unacceptable regressions, cost or friction.

1. Collect recurring failures or friction with examples, including first-check failures and recoveries. Separate observed recurrence from a one-off preference.
2. State the proposed change, target users/tasks, expected benefit, risks and evidence that would disconfirm it.
3. Freeze a small representative evaluation set. Keep hidden or held-out cases where feasible; document provenance, rights and leakage risks.
4. Compare current and candidate versions under the same model/tool budget, prompts, inputs and scoring rubric. Include a simple baseline and human review for judgment-heavy outcomes.
5. Score task outcomes and error types, evidence traceability, robustness, safety/privacy, latency, cost and user effort. Report sample size, uncertainty and known limits; do not rely only on an LLM judge or success rate.
6. Obtain an independent critique for consequential changes. Keep raw outputs and disagreements needed to reproduce the decision.
7. Promote only through a recorded owner decision. Version the procedure, publish the change, define migration and rollback, and monitor early use.

Never let a workflow edit and promote itself without review. Improvements should be reversible and should preserve previous versions and failures. A benchmark result is evidence for the tested task and setup, not proof of general superiority.
