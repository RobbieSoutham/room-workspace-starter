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

These sources motivate design rules, not automatic local thresholds. Local evaluation and policy adoption remain necessary. See [Model evaluation and benchmarks](model-evaluation-and-benchmarks.md) for live leaderboards, the repeatable comparison method and the papers behind the benchmark choices.

## Canonical layers

| Layer | Owns | Keep out of this layer |
|---|---|---|
| Model catalogue | `config/ai/model_catalog.yaml`: installed model IDs, access surfaces, routing roles, blocks and known constraints | Account status, endpoints, credentials or recommendations inferred from rank |
| Routing policy | `config/ai/routing_policy.yaml`: task lanes, escalation, protected routes, data limits and hard blocks | API keys and passwords |
| Provider/auth configuration | Private runtime config: secrets, login state, quota and product entitlements | Public documentation and Git |
| Benchmark evidence | Dated links, task/metric, model version, harness and limits | Executable routing policy |
| Runtime receipt | Requested model, observed model where available, route, time, usage/cost and outcome | Claims about quality without evaluation |

The repository ships the current room-based setup's model catalogue and routing policy as editable files. The native Codex default is `openai-codex/gpt-5.5` with no automatic fallback. GPT-6.1 Sol is the explicit high-end Codex route for architecture, complex planning, red-team and senior synthesis; GPT-6 Astra is an explicit same-family alternative, not an independent verifier. Opus 5.5 is the protected specialist/adjudication route requiring fresh admission and exact-model evidence; Sonnet 5.5 provides bounded cross-family redundancy when GPT usage is high. GPT-5.4 handles source gathering, GPT-5.4 Mini handles routine scoped code and GPT-5.4 Nano handles first-pass extraction. Kimi K2.6 and DeepSeek V3.2 Speciale are manual Azure verifier routes restricted to public, non-sensitive work. Groq and Vercel are opt-in public-data grunt lanes; AgentRouter is a third-party relay for public code only and is never a verifier. Gemini 4 Argon is for direct use in the official Google AI/Antigravity product, not a headless agent route unless current provider terms explicitly permit that use. These are roles and policies, not guarantees of current account quota. Check the catalog and runtime before launch.

## Task-lane register

An additional explicit public-text lane uses Experiential Labs DeepSeek V4.1 Flash with the `:free` suffix, a one-attempt cap and provider fallback disabled. It stops at the free allowance; finite wallet credits do not make other models free. Fable 5.1 remains prohibited. Follow the [setup guide](providers/experiential-labs.md) for credentials, balance units, privacy limits and verification. This lane does not change the native default or promote a final judge.

Define lanes by work and risk, not by brand preference. A useful initial register might include:

| Lane | Primary route | Fallback/abstain | Data class | Public benchmark prior + checked date | Local evaluation |
|---|---|---|---|---|---|
| Deterministic checks and transforms | Script/tool | Stop on invalid input | Approved local | Not applicable | Fixture/regression checks |
| Architecture, complex planning, final red-team | GPT-6.1 Sol, explicit high-end route; GPT-6 Astra is a same-family alternative | GPT-5.5 current default; do not switch automatically | Approved for route | [AA Intelligence Index](model-evaluation-and-benchmarks.md#live-benchmark-board); local evaluation required | Plan quality, error discovery, cost and downstream acceptance |
| Heavy implementation and tool-heavy execution | GPT-5.5 via native Codex | Explicit GPT-6.1 Sol escalation after access check | Repository-approved | [Terminal-Bench and Arena coding boards](model-evaluation-and-benchmarks.md#live-benchmark-board); local task suite | Acceptance, regression, safety, cost and latency |
| Research source gathering | GPT-5.4 plus explicit retrieval tools | GPT-6.1 Sol synthesises retrieved evidence | Public or approved route | [AstaBench literature boards](model-evaluation-and-benchmarks.md#live-benchmark-board) | Retrieval recall, source identity and claim/source accuracy |
| Routine scoped code | GPT-5.4 Mini | Deterministic checks and human review | Repository-approved | [Coding-agent boards](model-evaluation-and-benchmarks.md#live-benchmark-board) | Issue/task suite, acceptance and regression results |
| First-pass extraction and summaries | GPT-5.4 Nano | Source sampling and schema checks | Approved for route | Task-matched public board plus local sample | Missing-field rate, fidelity and downstream correction rate |
| Independent audit when GPT usage is high | Claude Sonnet 5.5 | Compare source-level disagreement; abstain as needed | Approved for route | [Arena and relevant task board](model-evaluation-and-benchmarks.md#live-benchmark-board) | Independent disagreement review and human adjudication |
| Protected adjudication | Claude Opus 5.5, deliberate specialist call | Human adjudication | Approved for route | No public score overrides the protected-call gate | Exact model admission, evidence quality and adjudication record |
| Fourth-family verification | Kimi K2.6 or DeepSeek V3.2 Speciale via manual Azure route | Primary-source checks and deterministic validation | Public, non-sensitive only | [AstaBench scientific agent boards](model-evaluation-and-benchmarks.md#live-benchmark-board) | Challenge only; outputs remain fallible |
| Low-cost public-data work | Groq gpt-oss-120b/Qwen3.8 or Vercel AI Gateway gpt-oss-120b; separate AgentRouter lane for public code | Higher-capability native route when uncertain; no silent provider failover | Public, non-sensitive only | [Free API terms and limits](model-access-and-offers.md#current-free-api-tiers-and-model-access) | Task-specific accuracy, rate-limit and privacy check |
| Direct Google AI access | Gemini 4 Argon in the official Google product | Do not drive subscription quota via a different agent unless current terms permit it | Direct interactive use only | [Offer and access terms](model-access-and-offers.md#current-promotions-and-research-programmes) | Product access is not proof of an API or headless-agent entitlement |
| Sensitive or restricted work | Approved local/institutional route | No external call without approval | Restricted | No public benchmark changes the data gate | Privacy and task-specific evaluation |

Keep a simple deterministic baseline. Use fixed task-to-route rules for stable recurring jobs; reserve model-based routing for decisions where task classification adds measured value. The native default is deliberately flat: no automatic model fallback. Explicit specialist, research and verifier lanes keep their own admission and data rules. Escalate or abstain when the task, identity, permissions, quota or data class is uncertain.

## Route-change procedure

1. State the reason for change and affected tasks.
2. Check provider/model availability, terms, privacy, quota, rate limits and cost from current authoritative sources; the current offer register is [here](model-access-and-offers.md).
3. Review the [live benchmark board](model-evaluation-and-benchmarks.md#live-benchmark-board) as a shortlist prior, then run the [local model evaluation](model-evaluation-and-benchmarks.md) against the current route under matched conditions.
4. Prepare a change record with exact catalogue and policy edits, expected outcome, failure modes, owner, validation steps and rollback.
5. Verify the configured route and observed execution using an approved smoke task that contains no sensitive data.
6. Monitor errors, output quality, cost and latency after rollout; revert when the stated trigger is met.

Do not route solely because a model leads a public benchmark. Do not add an inaccessible or unverified model to the route table. Treat quota and credits as volatile; a subscription tier or saved login label does not prove current entitlement. For multi-model review, use a separate context and preserve independent critiques before synthesis; different model names alone do not establish independence.
