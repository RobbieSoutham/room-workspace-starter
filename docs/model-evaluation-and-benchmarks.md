# Model evaluation and benchmarks

No general model leaderboard can tell a team which model is best for its research work. Public benchmarks are useful for shortlisting; local, task-representative evaluation is needed before relying on a model or agent in a workflow. Treat published scores as dated evidence tied to a task, prompt, model version, tools, scaffold and scoring method.

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
| Broad public model comparisons | [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) | A dated third-party comparison across selected tasks and settings | It is a provider-independent aggregator, not a primary scientific benchmark; inspect individual measures and methodology |

This is a curated starting shelf, not an exhaustive or permanent “SOTA” list. Check each benchmark's current version, paper, official leaderboard, license, data access and submission rules. Prefer primary papers and benchmark maintainers over copied leaderboard summaries.

Keep a dated benchmark register with one row per source: benchmark name/version; maintainer and primary paper; task/metric; last checked; model and agent scaffold; task fit; known contamination or saturation risk; and the local decision it informs. Store official links and update date rather than manually transcribed scores that will go stale. Refresh at a regular interval and after relevant model or benchmark releases.

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
