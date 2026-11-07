# Independent verification

Independent review is a challenge process, not a substitute for source evidence or human accountability. Use it when uncertainty, consequences or the cost of an unnoticed error justify the extra work. For low-risk routine tasks, a targeted self-check may be sufficient.

## Prepare an outcome-blind packet

Give the verifier the question/frame, protocol, relevant source material, code and data identity, environment, acceptance criteria, tolerances and commands needed to reconstruct the result. Exclude the implementer's preferred conclusion, draft narrative, expected result values and prior verdicts until reconstruction is complete. Remove credentials and minimise sensitive data; an external model call can disclose packet contents.

## Two-phase check

1. **Reconstruct:** verifier independently interprets the method and runs or traces the check without seeing the target result.
2. **Compare:** reveal the sealed result; compare source interpretation, method, values and tolerances.
3. **Record:** preserve packet identity, verifier identity/context as allowed, exact checks, evidence, disagreements, limitations and verdict.

Use a different model family when it materially increases independence and is appropriate for the data. Model diversity alone does not ensure independence: models may share training data, tools, assumptions or failure modes. Keep individual critiques before synthesis and retain unresolved disagreement.

## Verdicts

Use scoped states such as `CONFIRMED`, `CONFIRMED_WITH_CAVEATS`, `NOT_CONFIRMED`, `BLOCKED` or `ABSTAIN`. State what was checked. A citation-format check is not claim support; schema validation is not semantic verification; a model's agreement is not ground truth. A verifier must not silently edit the implementation it is reviewing or certify its own output.
