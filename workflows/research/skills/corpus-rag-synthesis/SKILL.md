---
name: corpus-rag-synthesis
description: Answer a research question from a bounded, user-supplied paper corpus with claim-level citations.
---

# Corpus-grounded synthesis

Use only when the corpus and its inclusion scope are known.

1. Define the corpus snapshot, question and evidence fields available (for example, abstract versus full text).
2. Retrieve passages for each subquestion and bind them to source IDs and page or section locators.
3. Draft claims only from retrieved evidence; quote accurately and separate source statements from interpretation.
4. Compare agreement, contradiction, method and population differences. Mark unanswered questions explicitly.
5. Recheck every citation against the underlying source and state retrieval limits.

Return a concise synthesis with claim-to-source links, disagreement and missing evidence. Retrieval over a corpus does not establish that corpus completeness or source quality.
