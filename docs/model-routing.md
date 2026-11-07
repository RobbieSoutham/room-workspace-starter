# Model routing and provider setup

Keep model routing as an explicit, inspectable operations concern. Separate the model catalogue, routing rules, authentication, benchmark evidence and observed runtime so that a marketing page or stale setup note cannot silently change live behaviour.

## Science-backed routing policy

The policy is evidence-informed and deliberately task-specific. It is not a claim that this workspace uses the single best model, or that any public benchmark establishes scientific validity.

| Policy | Evidence basis | Operational rule |
|---|---|---|
| A model is selected for a task and its error costs, not for a global rank | [HELM](https://arxiv.org/abs/2211.09110) reports multi-scenario, multi-metric evaluations; [AstaBench](https://arxiv.org/abs/2510.21652) evaluates distinct scientific tasks and notes the need to control tools, cost and baselines | Maintain task lanes and locally test important work; do not collapse unlike tasks to one score |
| Model scores travel with the harness and tools | [AgentBench](https://arxiv.org/abs/2308.03688), [PaperBench](https://arxiv.org/abs/2504.01848) and [Terminal-Bench](https://tbench.ai/) evaluate agents in defined environments; terminal benchmark reports show agent-pair results vary by scaffold | Record model + agent/tool stack, settings, retries and environment; prefer like-for-like comparisons |
| Advertised context length is not evidence of usable long-context performance | [RULER](https://arxiv.org/abs/2404.06654), [LongBench v2](https://aclanthology.org/2025.acl-long.183/) and [MRCR](https://arxiv.org/abs/2409.12640) test different retrieval/reasoning demands over long inputs | Evaluate the actual document types, positions, lengths and evidence density; retrieval/chunking is a candidate route, not an automatic downgrade |
| Static public benchmark scores can be contaminated, saturated or poorly scored | The benchmark maintainer's 2026 [SWE-bench Verified review](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) discusses contamination and test-oracle limitations | Keep a dated source register; use maintained/held-out/local tasks and inspect scoring rules before using a score in routing |
| A verifier model is a challenge, not ground truth | [SciVer](https://aclanthology.org/2025.acl-long.420/) evaluates a specific scientific claim-verification task; it does not validate screening or synthesis. A systematic review found task-dependent GenAI errors in evidence synthesis ([Clark et al., 2025](https://doi.org/10.1017/rsm.2025.16)). | Require source-level checks and human adjudication according to stakes; preserve disagreement and allow `ABSTAIN` |
| Use the simplest route that meets the need | Deterministic scripts provide exact, inspectable results for well-specified transformations; agent benchmarks measure different, interactive work | Prefer deterministic tools for counting, schema checks, searches, transformations and tests; use agents where language judgment or tool orchestration adds measurable value |

These sources motivate design rules, not automatic local thresholds. Local evaluation and policy adoption remain necessary. See [Model evaluation and benchmarks](model-evaluation-and-benchmarks.md) for the repeatable comparison method and [References](references.md) for scope notes.

## Canonical layers

| Layer | Owns | Keep out of this layer |
|---|---|---|
| Model catalogue | Provider model IDs, capabilities, context, modalities, tool support, lifecycle and known constraints | User-specific account status or recommendations inferred from benchmark rank |
| Routing policy | Task lanes, eligibility, fallbacks, privacy classes, escalation rules, hard blocks and cost controls | API keys and passwords |
| Provider/auth configuration | Secrets, login state, quota and product entitlements | Public documentation and Git |
| Benchmark evidence | Dated links, task/metric, model version, harness and limits | Executable routing policy |
| Runtime receipt | Requested model, observed model where available, route, time, usage/cost and outcome | Claims about quality without evaluation |

Use the machine-readable catalogue and routing policy as operational authority when the host has them. The generic starter does not ship a live provider configuration. Record host-specific paths in a private overlay.

## Task-lane register

Define lanes by work and risk, not by brand preference. A useful initial register might include:

| Lane | Primary route | Fallback/abstain | Data class | Public benchmark prior + checked date | Local evaluation |
|---|---|---|---|---|---|
| Deterministic checks and transforms | Script/tool | Stop on invalid input | Approved local | Not applicable | Fixture/regression checks |
| Routine public-text synthesis | Cost-appropriate model | Human or stronger route for uncertainty | Public | `<benchmark/task and date>` | Claim/source accuracy sample |
| Literature discovery/screening | Retrieval system plus selected model | Preserve candidates for human decision | Public or approved | `<benchmark/task and date>` | Recall/precision by decision stage |
| Claim verification | Independent source lookup or verifier model | Abstain/escalate | Approved for route | `<benchmark/task and date>` | Claim-support adjudication |
| Long-context synthesis | Model tested on long-document tasks | Chunk/retrieve or human review | Approved for route | `<benchmark/task and date>` | Evidence recall and position/length robustness |
| Coding/agentic implementation | Coding model plus controlled tools | Deterministic checks and human review | Repository-approved | `<benchmark/task and date>` | Issue/task suite, acceptance and regression results |
| Sensitive or restricted work | Approved local/institutional route | No external call | Restricted | `<benchmark/task and date>` | Privacy and task-specific evaluation |

Keep a simple deterministic baseline. Use fixed task-to-route rules for stable recurring jobs; reserve model-based routing for decisions where task classification adds measured value. Escalate or abstain when the task, identity, permissions, quota or data class is uncertain.

## Route-change procedure

1. State the reason for change and affected tasks.
2. Check provider/model availability, terms, privacy, quota, rate limits and cost from current authoritative sources.
3. Review public benchmarks as priors, then run the [local model evaluation](model-evaluation-and-benchmarks.md) against the current route under matched conditions.
4. Prepare a change record with exact catalogue and policy edits, expected outcome, failure modes, owner, validation steps and rollback.
5. Verify the configured route and observed execution using an approved smoke task that contains no sensitive data.
6. Monitor errors, output quality, cost and latency after rollout; revert when the stated trigger is met.

Do not route solely because a model leads a public benchmark. Do not add an inaccessible or unverified model to the route table. Treat quota and credits as volatile; a subscription tier or saved login label does not prove current entitlement. For multi-model review, use a separate context and preserve independent critiques before synthesis; different model names alone do not establish independence.
