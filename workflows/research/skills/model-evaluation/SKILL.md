---
name: model-evaluation
description: Compare candidate models or research agents on representative, task-specific work before relying on them in a research workflow.
---

# Model evaluation

Use for model selection, agent/workflow comparisons or material model/prompt changes. Follow the canonical [evaluation and benchmark guidance](../../../../docs/model-evaluation-and-benchmarks.md).

1. Define the task and decision, including acceptable errors and whether the task is consequential.
2. Assemble a permitted representative set with human-checked references, edge cases and a held-out portion where practical.
3. Fix and record model/version, prompt, tools, scaffold, retries, date, access route and output handling.
4. Compare against the current method and a human or simple baseline; use paired examples and repeat runs when randomness affects the result.
5. Report task-specific quality, uncertainty, abstentions, error types, latency, monetary cost and human review effort.
6. Inspect failures and a sample of apparent successes. Validate any automated judge against human assessment.
7. Record a bounded decision, limitations, remaining human checks, re-evaluation trigger and rollback route. Do not declare general model superiority from one benchmark or task.
