# Research lifecycle and gates

Rigour should follow the intended claim, use and risk. Keep exploration inexpensive; add controls when an output will support a decision, publication, public release or durable research claim.

```text
Evidence → Frame → (Argument + Protocol) → Implement → Validate → Interpret
     ↑                  │                       │                    ↓
     └──── targeted search/reframe ← deviation ─┘          Communicate → Close
```

## Work levels

| Level | Use | Minimum record | Escalation trigger |
|---|---|---|---|
| Exploratory | Feasibility, debugging, early sense-making | Question/decision, location, exploratory label, brief close/park note | An output is reused as a claim or decision input |
| Claim-bearing | Paper, report, presentation, thesis, or consequential decision | Frame, protocol appropriate to method, evidence/claim trace, validation and limitations | External release or reliance by others |
| Release | Public code, data, model, or formal research artefact | Claim-bearing evidence plus rights, privacy, reproducibility, security and release review | New data or material change after review |

These levels are a practical scaffold, not an ethics or funder classification. Field-specific risk review, preregistration, consent, data governance and institutional approvals remain separate requirements.

## Gates

1. **Evidence adequacy:** identify the closest relevant work, unresolved disagreement and important unknowns. If the search is incomplete, label the gap provisional.
2. **Frame:** define the question, target contribution, plausible falsifier, intended use, unit/population, scope and stop condition.
3. **Design join:** ensure the argument asks a question the protocol can answer and the protocol produces the promised evidence. If not, revise before implementation.
4. **Implementation faithfulness:** bind load-bearing source requirements and design choices to code, data and tests. Log deviations rather than silently changing the method.
5. **Validation:** separate software correctness, scientific validity, statistical design, reproducibility and independent verification. Missing required evidence is `BLOCKED`, not `PASS`.
6. **Claim promotion:** state what the evidence supports, its uncertainty and its boundary. Keep null, ambiguous, failed and withdrawn outcomes visible.
7. **Release and close-out:** check rights, privacy, provenance, exact artifact version and reproducibility; record what is safe to claim and what remains open.

Use the [evidence and failure record](../evidence-and-failure-records.md) for states and receipts. A single global “pass” must not stand in for all gates.
