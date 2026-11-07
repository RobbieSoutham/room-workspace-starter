# Research workflow

This workflow is a set of connected checkpoints, not a claim that all research follows one linear recipe. Choose the level of documentation to fit the question, method and consequences. For a systematic review, use the relevant review standards and seek information-specialist input where appropriate.

## 1. Frame the question

State the question, why it matters, the target contribution, what evidence could change the current view, and important scope limits. Separate established facts from assumptions. Use the research-frame and research-question-development skills before committing to costly data collection or code.

## 2. Choose the method and record the plan

Select a method that can answer the question. Record eligibility rules, search sources and dates, analysis decisions, expected outputs and known limitations before claim-bearing work begins. Use a protocol for systematic or otherwise consequential work. Record later deviations with the reason and date; do not quietly rewrite the original plan. [PRISMA 2020](https://www.prisma-statement.org/prisma-2020-statement), [PRISMA-S](https://www.prisma-statement.org/prisma-search) and the [Cochrane Handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04) provide reporting and methods guidance within their stated review scopes; they are not substitutes for a sound method.

## 3. Find and manage evidence

Combine suitable database searches with citation searching or other justified sources. Keep each database query, date, result count, deduplication rule and screening decision. Treat discovery tools and ranking signals as ways to find candidates, not as evidence of quality or completeness. Retain stable identifiers and source links, and distinguish records found from records assessed and included.

## 4. Assess and synthesise

Read sources at the level needed to support the intended claim. Extract claim-level evidence with page or section locators, source identity and limitations. Compare findings, methods and disagreement across sources; do not convert absence of evidence into evidence of absence. Keep automated suggestions separate from human decisions and record the model, version, prompt or settings when an AI output affects the research. A 2025 systematic review found substantial errors across GenAI evidence-synthesis tasks and concluded that the evidence did not support use without human oversight ([Clark et al., 2025](https://doi.org/10.1017/rsm.2025.16)); its results are task- and study-dependent, not a guarantee about every tool or future model.

## 5. Analyse or implement

For data or code work, preserve input provenance, environment and version, decision rules, run identifiers and outputs needed to reproduce the result. The [FAIR principles](https://doi.org/10.1038/sdata.2016.18) provide a framework for data findability, accessibility, interoperability and reuse; they do not require making restricted data public. Validate the implementation separately from the scientific interpretation. A successful program run is not by itself evidence that the research claim is correct.

## 6. Write and communicate

Build each claim from its evidence and qualify it to the study design, scope and uncertainty. Use a claim-evidence audit before submission. Adapt presentations, figures, posters and manuscripts to their real audience while keeping source attribution, uncertainty and limitations legible. Verify venue requirements from the venue's current official guidance.

## 7. Review, revise and release

Use independent critique when stakes or uncertainty justify it. Resolve comments one by one and keep a response trail. Preserve the initial check result, including failures, when a revised version later passes. Before sharing, check rights, privacy, secrets, large generated files, reproducibility instructions and the exact released version.

## 8. Archive and learn

Keep canonical documents in one source-of-truth location, working drafts in their dated or project area, and project code/evidence in its own repository. Capture reusable lessons only after checking that the pattern is supported by the work. Link retrospective notes to the artifact and decision they describe.

## Suggested room layout

`papers/` holds bibliographic records and permitted source files; `literature/` holds structured notes and evidence summaries; `notes/` holds working research notes; `planning/` holds questions, protocols and decision records; `presentations/` and `posters/` hold communication drafts; `figures/` holds source and export files; `meetings/` holds dated minutes; `working/` holds temporary runs and drafts; `references/` holds citation-manager exports or pointers. Use `projects/<slug>/` submodules when a project needs its own Git history or remote. Do not commit private source documents, credentials, caches, environments or generated bulk data by default.

## Evidence states

Use explicit states such as `NOT_STARTED`, `IN_PROGRESS`, `PASS`, `PASS_WITH_LIMITATIONS`, `FAIL`, `BLOCKED` and `NOT_APPLICABLE`. Record which check was performed, against which artifact/version, by whom or what, when, the evidence and the next action. Failed and blocked states remain visible after revision. See [Evidence and failure records](evidence-and-failure-records.md).
