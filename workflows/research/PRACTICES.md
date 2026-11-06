# Research practices: from question to defensible claim

This guide shows a practical research workflow that colleagues can adapt. It is discipline-neutral: a laboratory study, interview project, literature review, mathematical proof and software evaluation need different methods, but all benefit from making important choices visible and keeping claims connected to evidence.

The aim is not to create paperwork. Record the decisions that would otherwise be easy to change after seeing the results.

## The workflow at a glance

1. **Frame** the question, its importance and what could change your mind.
2. **Understand** existing evidence and the gap your work will address.
3. **Design** a method that can produce the kind of evidence the question needs.
4. **Protect** participants, data, collaborators and research integrity.
5. **Record** what was done, what changed and what the evidence shows.
6. **Check** whether the analysis and interpretation hold up.
7. **Communicate** a bounded claim that readers can trace back to evidence.

For a small exploratory task, some steps may fit on one page. For a larger or higher-risk project, each may need its own protocol, approval, data plan or review. Use the lightest process that protects the validity of the answer.

## 1. Frame a question that evidence can answer

Start with the problem or observation, then state the question. A useful frame makes clear:

- **Question:** What do you want to learn, about which people, objects, texts, systems or events, and in what setting?
- **Why it matters:** What decision, explanation or body of knowledge could the answer affect?
- **Current alternatives:** What plausible answers or explanations are live?
- **Decision rule:** What result would support, weaken or leave the claim unresolved?
- **Output:** What will a reader inspect to judge the answer: a figure, comparison table, proof, synthesis, dataset, code release or other artefact?

Write a falsifier or stopping rule before collecting or analysing outcome data when the work is meant to test a claim. This does not mean every study needs a numeric threshold. Qualitative and interpretive work can instead state what evidence would challenge the interpretation, what rival readings will be considered and how the researcher will document judgement.

Distinguish **exploratory** work, which discovers possibilities, from **confirmatory** work, which evaluates a specified claim. Exploration is valuable; label it honestly. If exploration leads to a new confirmatory question, frame that as a new question rather than rewriting the earlier plan.

Use [`templates/research_frame.md`](templates/research_frame.md) to capture the first version of the frame.

## 2. Learn the evidence landscape

Before committing to a method, find out what is already known and how it was established.

- Search sources appropriate to the field. Keep the query, databases or archives, date searched and scope limits.
- Set inclusion and exclusion rules before screening when the review needs to be reproducible. Record why borderline material was kept or removed.
- Read sources closely enough to separate what the authors observed from what you infer.
- Compare methods, populations, measures, assumptions and limitations, not just headline conclusions.
- Look for disagreement, null findings and relevant work that challenges your preferred explanation.
- Keep bibliographic details with the notes so a reader can find the source again.

A literature review should explain how the body of evidence bears on your question. A list of summaries is usually not enough: show where findings agree, where they differ and whether the differences could follow from method, context or measurement.

## 3. Make the method follow the question

Choose a method by asking what kind of observation would answer the question. Check that the unit of analysis, comparison, measures or interpretive framework fit the claim you hope to make.

| Research mode | Choices to make visible |
|---|---|
| Quantitative or experimental | Units, treatment or comparison, outcomes, controls, exclusions, missingness and analysis plan |
| Qualitative or interpretive | Sampling, setting, researcher role, data-generation process, coding or interpretive approach, and how alternative readings are handled |
| Literature review | Sources searched, search date, scope, eligibility rules, screening process and synthesis method |
| Computational or data science | Data lineage, preprocessing, baselines, splits, metrics, software and environment versions, seeds where relevant, and failure cases |
| Theoretical or mathematical | Definitions, assumptions, scope, proof strategy and what a counterexample would look like |
| Design or software research | Intended use, requirements, comparison or evaluation criteria, test cases and limits on generalisation |

For each mode, ask the same question: does this design produce evidence that can support the kind of conclusion I intend to draw? A tool working as specified establishes an engineering result; it does not by itself establish a scientific claim about the world.

## 4. Plan integrity, ethics and data handling

Before gathering data or accessing restricted material, identify the applicable approvals, consent, privacy, security, copyright, licensing and data-retention requirements. A dataset being available online does not automatically mean it is unrestricted or suitable for every use. Follow the rules of the institution, funder, publisher, data provider and jurisdiction that apply to the project.

Decide where raw data, identifiers, consent records and working files belong. Keep confidential or personal material out of public repositories, issue trackers and general-purpose notes. Share data or derived materials only when the relevant permissions and protections allow it.

For work with material risks, specify who can approve access, analysis, external services, resource use and release. State what will not be uploaded or shared. Use a project-specific data management plan when required.

## 5. Preserve the plan and the research trail

Before execution, record enough detail to understand the design and repeat the work where permitted:

- protocol or analysis-plan version and date;
- data sources, sampling and inclusion rules;
- materials, measures, code and software versions;
- environment, random seeds and analysis order where relevant;
- primary outcomes or interpretive questions;
- planned exclusions, missing-data handling and stopping rules;
- intended outputs and where they will be stored.

Keep the original plan. If an unexpected issue forces a change, log the date, reason, affected decision and likely consequence. Do not quietly replace the plan after seeing results. [`templates/deviation_log.md`](templates/deviation_log.md) provides a simple record.

Keep an evidence ledger for claim-bearing sources or observations. Each entry should let a reviewer locate the source, see what it supports or challenges, and understand its limits. Mark the difference between a quotation, a paraphrase and your own interpretation. The blank [`templates/evidence_ledger.csv`](templates/evidence_ledger.csv) can be copied into a project.

## 6. Analyse without hiding inconvenient outcomes

Check data and methods before interpreting the headline result. Preserve denominators, exclusions, missing or invalid cases, failed controls, negative findings and non-estimable results where they affect the answer.

Keep these judgements separate:

- **Execution:** Was the planned work carried out, and were deviations recorded?
- **Validity:** Does the method support the proposed interpretation?
- **Finding:** What did the evidence show, including uncertainty or ambiguity?
- **Review:** What did another reader or verifier conclude?

An execution pass does not mean the hypothesis was confirmed. A run that fails technically is not evidence for the opposite hypothesis. Report both kinds of outcome accurately.

For computational work, make a fresh run from the documented inputs where practical. Check key outputs against an independent calculation, baseline or scientific oracle when one exists. For interpretive work, examine rival readings and make the route from source material to themes or conclusions inspectable without exposing restricted content.

## 7. Match claims to evidence

Before sharing a result, list the main claims and check each one:

1. What exact evidence supports it?
2. What evidence or alternative explanation challenges it?
3. What assumptions connect the evidence to the claim?
4. For which population, setting, time period or conditions should it hold?
5. What uncertainty or limitation must travel with it?

Use cautious language when the design is observational, the sample is limited, measures are indirect or results are uncertain. Do not turn association into causation, a tool demonstration into broad effectiveness, or absence of evidence into evidence of absence without a justified design.

For each important number or figure, preserve a route back to the underlying calculation or source. Verify citations against the original sources; do not rely on generated summaries or citation suggestions without checking them.

## 8. Use independent review and tools responsibly

Ask someone who was not responsible for the key implementation or analysis to review the parts where an error would change the conclusion. Give them a bounded question and the evidence needed to answer it, not a desired verdict. Record substantive disagreements and how they were resolved.

If AI or other automated tools assist with searching, coding, analysis or writing, check their output against primary sources and actual results. Verify every citation. Follow institutional, funder and publisher rules on disclosure, authorship, confidentiality and permitted use. A generated answer is a lead to check, not a source of evidence.

## 9. Share a useful, honest output

A paper, report, presentation or software release should help its audience inspect the reasoning. Include the methods and limits needed to interpret the result. Link claims to sources or artefacts, distinguish planned from post-hoc analyses, and report meaningful negative or inconclusive findings.

Before releasing code, data or materials, check licences, third-party notices, privacy and consent, secrets, machine-specific paths and generated files. Add a licence only for material whose rights you are authorised to license. Keep project-specific or restricted evidence in its approved home; this workspace template should contain generic process material only.

## A short close-out check

- Can a reader state the question and what would have challenged the answer?
- Is the method suited to the question and described well enough to assess?
- Are sources, data, exclusions and changes traceable within the permissions that apply?
- Are negative, uncertain and invalid outcomes represented honestly?
- Does each headline claim stay within what the evidence supports?
- Have citations, ethics, privacy, licences and release contents been checked?
- Is the next step or remaining uncertainty clear?

## Worked example

See [`examples/search-strategy-evaluation.md`](examples/search-strategy-evaluation.md). It is fictional and demonstrates how to make a small evaluation inspectable; it reports no real findings.
