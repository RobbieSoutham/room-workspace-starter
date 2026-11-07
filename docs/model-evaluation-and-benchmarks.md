# Model evaluation, live leaderboards and benchmarks

No general model leaderboard can tell a team which model is best for its research work. Public benchmarks are useful for shortlisting; local, task-representative evaluation is needed before relying on a model or agent in a workflow. Treat published scores as dated evidence tied to a task, prompt, model version, tools, scaffold and scoring method. The operational inventory and lane policy live in [`config/ai/model_catalog.yaml`](../config/ai/model_catalog.yaml) and [`config/ai/routing_policy.yaml`](../config/ai/routing_policy.yaml).

## Live benchmark board

**Snapshot checked: 7 November 2026.** These live boards inform candidate selection in [`model-routing.md`](model-routing.md); the links are the live source and the snapshot below is only a dated reading. Reopen the source before a routing decision. Public rank is a prior, not a promotion rule.

| Routing question | Live board and checked result | How this setup uses it | Main limitation |
|---|---|---|---|
| Broad intelligence, cost and speed across current frontier models | [Artificial Analysis LLM leaderboard](https://artificialanalysis.ai/leaderboards/models) and [Intelligence Index v5.0.1](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index). On 7 Nov the live Index led with Gemini 4 Carbon (high), 60; Claude Opus 5.5 (max), 59; Gemini 4 Carbon (medium), 58; GPT-6 Astra (max), 57; GPT-6.1 Sol (max), 55. It reports cost and time per task beside score. | Shortlist current high-capability models and compare quality/cost trade-offs; inspect component evaluations rather than following the composite score. | Composite weights and model effort settings matter. A broad index is not an evaluation of our research workflow or data controls. Artificial Analysis notes its Index is independently run and updates its model data; its data API is not publicly available. |
| Human preference and interactive agent quality | [Arena live leaderboard](https://arena.ai/leaderboard?tab=arena-elo). On 7 Nov its “Best Overall Agents” board ranked Claude Opus 5.5 (Max), Gemini 4 Carbon (High), Claude Sonnet 5.5 (Max), then GPT-6 Astra (Max). | Use the separate text, coding, web-development and agent tabs to see which systems users prefer for a similar interaction type. | Crowd preference is not factuality, citation accuracy, reproducibility or research-task success; compare the matching sub-board, not only “overall”. |
| Literature discovery, evidence retrieval and synthesis | [AstaBench literature leaderboards](https://allenai-asta-bench-leaderboard.hf.space/), maintained as part of [Ai2 AstaBench](https://allenai.org/asta/bench). The suite includes PaperFindingBench, LitQA2 FullText Search, ScholarQA-CS2 and literature-table tasks. | This is the closest public board for SciBench-style discovery and literature-workflow candidates. Match the exact retrieval or synthesis task before using a result to shortlist. | Corpus coverage, access to full text, citation metrics, tool setup and agent harness vary across tasks. AstaBench itself describes an evolving multi-benchmark suite, not one universal rank. |
| Scientific code, data analysis and end-to-end research agents | The AstaBench board also has coding/execution, data-analysis and end-to-end discovery leaderboards. For project-level computational science, see [ASI-Bench](https://asibench.apexin.ai/leaderboard/). | Compare model **and** agent harness on implementation, reproducibility and research-lifecycle tasks; use the B1–B4 guidance levels to distinguish assisted execution from more autonomous work. | ASI-Bench describes current results as supplied aggregates and its FAQ says a final official baseline has not yet been published. Treat those scores as exploratory. |
| Terminal coding and scientific execution | [Terminal-Bench](https://tbench.ai/) and the Terminal-Bench-Science component in the [live Artificial Analysis Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index). | Inform coding-agent and reproducible-science shortlist decisions, then run the proposed harness on held-out local tasks. | Results depend on container, scaffold, tools and test oracle. A coding leaderboard is not evidence for literature screening or scientific claim validity. |

The 7 Nov Artificial Analysis snapshot illustrates why scores should stay beside the task: Gemini 4 Carbon leads the composite, while Artificial Analysis reports GPT-6 Astra leading Terminal-Bench-Science and other models leading other component benchmarks. It also reports materially different task costs. This implies there is no single leader to route every job to; choose the board matching the task, check whether the model is available in the configured routes, then use local evidence.

Maintain these live links and dated snapshots. Update the snapshot after material board/model changes and at least monthly. Do not scrape or redistribute leaderboard datasets unless the source's licence and API terms permit it; Artificial Analysis states that it does not offer a public API for its model leaderboard data.

## Benchmark families to consult

| Need | Useful starting points | What they can tell you | Limits to record |
|---|---|---|---|
| Broad capabilities and risk dimensions | [HELM](https://crfm.stanford.edu/helm/) | Multi-scenario, multi-metric capability and risk coverage | Scenario mix and supported models change; averages hide task-specific performance |
| Scientific research tasks | [AstaBench](https://allenai.org/asta/bench), [PaperBench](https://arxiv.org/abs/2504.01848) | Literature tasks, scientific workflows, or research replication performance | Task coverage, discipline, corpus access, tools, rubric and human baseline differ |
| Interactive tool-using agents | [AgentBench](https://arxiv.org/abs/2308.03688) and task-specific tool benchmarks | Behaviour in defined interactive environments | Results are sensitive to scaffold, tools, retries and environment state |
| Coding agents | [Terminal-Bench](https://tbench.ai/), [SWE-bench Pro](https://www.swebench.com/) | Agent-plus-model performance in terminal tasks or issue resolution | Report the full model+harness+tool setup; public static issues risk contamination and test oracles may be imperfect |
| Coding benchmark caution | [SWE-bench Verified](https://www.swebench.com/) | Historical widely used fixed issue set | OpenAI has stopped reporting it because of contamination and scoring-oracle concerns ([2026 explanation](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)); do not treat its score as a current routing rule |
| Claim verification | Scientific-claim datasets such as [SciVer](https://aclanthology.org/2025.acl-long.420/) | Whether a system can verify the benchmark's defined scientific claims | Dataset modality and task definition may differ sharply from screening, synthesis or citation support |
| Tool use / function calling | [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html), [τ-bench](https://taubench.com/) | Structured tool-call accuracy or simulated user-facing task completion | Tool schemas, simulated environment and task distribution define the result |
| Long-context retrieval | [RULER](https://arxiv.org/abs/2404.06654), [LongBench v2](https://aclanthology.org/2025.acl-long.183/), [MRCR v2](https://arxiv.org/abs/2409.12640) | Retrieval and reasoning over long inputs under benchmark conditions | Input window size is not effective recall; test the actual document type, position and evidence density |
| Broad public model comparisons | [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) and the live [model leaderboard](https://artificialanalysis.ai/leaderboards/models) | A dated third-party comparison across selected tasks and settings, including cost and speed | Independent evaluation is useful for shortlisting, not a primary scientific benchmark; inspect individual measures and methodology |

This is a maintained starting shelf, not an exhaustive or permanent “SOTA” list. Check each benchmark's current version, paper, official leaderboard, licence, data access and submission rules. Prefer primary papers and benchmark maintainers over copied leaderboard summaries. Key methods behind these defaults include HELM's multi-scenario, multi-metric approach ([Liang et al., 2022](https://arxiv.org/abs/2211.09110)); AstaBench's scientific-agent suite ([Liao et al., 2025](https://arxiv.org/abs/2510.21652)); long-context tests RULER ([Hsieh et al., 2024](https://arxiv.org/abs/2404.06654)), LongBench v2 ([Bai et al., ACL 2025](https://aclanthology.org/2025.acl-long.183/)) and MRCR ([Google DeepMind, 2024](https://arxiv.org/abs/2409.12640)); agent evaluation ([AgentBench, ICLR 2024](https://arxiv.org/abs/2308.03688)); research replication ([PaperBench, 2025](https://arxiv.org/abs/2504.01848)); and scientific claim verifiability ([SciVer, ACL 2025](https://aclanthology.org/2025.acl-long.420/)). These benchmarks measure different constructs and should not be averaged into one score.

Keep a dated benchmark register with one row per source: benchmark name/version; maintainer and primary paper; task/metric; last checked; model and agent scaffold; task fit; known contamination or saturation risk; and the local decision it informs. Store official live links and an explicitly dated snapshot; refresh after relevant model or benchmark releases and at least monthly. The 2026 [SWE-bench Verified review](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) describes contamination and scoring-oracle concerns, a reminder that a familiar fixed benchmark can stop being a dependable routing signal.

## Local evaluation protocol

1. **Name the decision.** Specify the workflow task and acceptable error tradeoffs: e.g. recall-first candidate screening, exact citation identity, passage-grounded claim support, structured extraction, or figure/code review.
2. **Make a representative set.** Sample real permitted tasks, include edge cases and known failures, define gold labels with qualified human adjudication, and preserve a held-out subset. Document data rights and prevent evaluation data from being sent to unapproved providers.
3. **Fix the conditions.** Record provider/model/version, date, prompt and system instructions, tools/data, agent scaffold, sampling parameters, retries, context limits and human intervention. Separate requested model from observed execution when the platform exposes that evidence.
4. **Choose task metrics.** Report denominators and uncertainty. Examples: precision/recall and abstention for screening; citation identity and claim-support accuracy for evidence work; extraction agreement and missing-field rate; reproducibility/acceptance tests for code. Measure disagreement, subgroup/edge-case failures, latency and total cost.
5. **Compare fairly.** Include the current workflow, a human or simple baseline, and candidate models under matched conditions. Use paired tasks and repeated runs when stochasticity matters. Blind reviewers to model identity where practical.
6. **Inspect errors.** Classify harmful and recoverable failures; inspect a sample of successes too. For model-graded outputs, validate the judge against human ratings and report judge limitations.
7. **Decide and revisit.** State the scope of any adoption, residual human gate, thresholds, review date and rollback trigger. Re-evaluate after material model, prompt, tool, corpus or policy changes.

Never use provider self-reported benchmarks as the only selection evidence. Do not combine unlike scores into a single rank without a justified, predeclared decision model. Preserve raw outputs and an evaluation manifest, subject to rights, privacy and retention rules.

## Minimal evaluation record

```yaml
evaluation_id: <stable-id>
task_and_decision: <what this evaluation will inform>
dataset: <version, provenance, rights, sample size, held-out policy>
model_and_provider: <requested and observed identity, if available>
prompt_tools_scaffold: <versions and settings>
date_and_environment: <when and how it ran>
baseline: <human/current/simple baseline>
metrics_and_thresholds: <predeclared measures, denominators, uncertainty>
results_and_failures: <aggregate plus error categories and examples>
cost_latency: <total, retries and human review effort>
reviewer_and_adjudication: <who checked labels and disagreements>
decision_scope: <adopt, trial, reject, or collect more evidence>
limitations_and_recheck_trigger: <what could invalidate this result>
```
