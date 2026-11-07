---
name: experiment-lifecycle
description: Specify, implement and close out a claim-bearing computational experiment with evidence gates.
---

# Experiment lifecycle

This is an optional candidate workflow. Adopt it only when its gates match the research design and local governance.

1. Freeze question, estimand or target, falsifier, data, exclusions, baselines and analysis plan.
2. Record code version, environment, input hashes, random seeds and expected outputs.
3. Implement the smallest run; validate inputs, outputs and invariants before scaling.
4. Execute under declared limits. Preserve failed runs and diagnostics; never overwrite the first result.
5. Independently verify key metrics and reproduce at least one claim from retained artifacts.
6. Close with deviations, unresolved checks and a disposition: supported, unsupported, inconclusive or blocked.

Return a run receipt and claim-to-output map. Passing software checks is not scientific validation. Do not treat this candidate lifecycle as an approved or universal standard.
