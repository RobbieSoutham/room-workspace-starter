---
name: semantic-gatekeeper
description: Inspect the structure of a large or unfamiliar file before deciding whether to read it in full.
---

# Semantic gatekeeper

Use when a file is large enough that loading all of it would obscure the task or consume disproportionate context.

1. Identify file type, size, headings, table of contents, definitions and relevant sections using bounded tools.
2. Inspect small, high-value excerpts around the task's question.
3. Decide whether the full file is needed. If so, read only the sections that bear on the answer before expanding scope.
4. Preserve exact source locations for claims that depend on the file.

Do not use a size threshold as a substitute for judgement. Never run an unbounded recursive scan over sensitive or bulk storage to avoid opening one known file.
