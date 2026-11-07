# Implementation standard for claim-bearing research code

Use this when code or analysis will support a paper, presentation, durable research claim, shared artifact or consequential decision. Adapt it to the method; it is not a requirement to create a separate package for every exploratory script.

## Implementation card

Before claim-bearing implementation, record the research question and intended claim/use; target quantity and units; method/source basis; inputs, outputs and invariants; baseline and controls; acceptance criteria and tolerances; data, privacy and resource boundaries; reuse decision; validation plan; and expected result bundle. Log changes after inspecting results in a deviation record.

## Project structure

Use the smallest structure that supports inspection and reproduction. A reusable computational project will commonly have:

```text
project/
  README.md                 purpose, scope, status, setup, run, validation, outputs
  environment manifest      direct dependencies and versions
  src/                      reusable scientific logic
  tests/                    software and scientific-oracle checks
  docs/                     protocol, source/code map, deviations, verification
  scripts/                  thin entry points
  outputs/                  generated and ignored or explicitly curated
```

Keep notebooks useful for readers, but make them call the canonical implementation path. Separate generated outputs from source. Keep credentials, restricted/raw data, caches, virtual environments, dependency downloads and provider logs out of version control.

## Source-to-code trace

Maintain a compact ledger for each load-bearing requirement:

| ID | Source section/equation/spec | Interpretation | Code path/symbol | Test/oracle | Result or claim | Status/deviation |
|---|---|---|---|---|---|---|

Keep source text and your interpretation distinct. State substitutions, assumptions and unavailable details. A line number is only a snapshot; also record a stable symbol and code revision. Do not claim equivalence without a differential check or bounded explanation of what is equivalent.

## Validation layers

- **Structure:** imports, schemas, configuration, entry points and declared side effects.
- **Software behaviour:** unit/integration checks, failure and abstention paths, deterministic outputs where expected.
- **Scientific oracle:** analytical/reference values, independent implementations, metamorphic properties, positive/negative controls, known-truth simulations or exact source tracing. Choose tolerances, units, denominators and failure meanings before inspecting results.
- **Study/statistical design:** leakage, splits, baselines, uncertainty, multiplicity, sensitivity and subgroup checks appropriate to the claim.
- **Reproduction:** code identity, environment, input/output identity, clean execution and trace from run to reported result.
- **Independent review:** fresh-context verification for important claims, scoped to risk and feasible access.

Tests establish only the behaviours they exercise. A green software suite does not establish scientific validity. Preserve failed checks and state which limitations narrow or block the claim.

## Reuse decision

Before implementing, decide whether to reuse, wrap, fork, vendor or reimplement an existing method. Record source, version/commit, licence, semantic assumptions and needed differential checks. Prefer duplication over a shared abstraction when consumers have different units, estimands, timing or failure semantics; prefer shared code when it has stable semantics, multiple consumers and regression coverage.
