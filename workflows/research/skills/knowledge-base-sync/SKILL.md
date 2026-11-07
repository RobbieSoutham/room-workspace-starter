---
name: knowledge-base-sync
description: Maintain a research knowledge base without creating competing copies or overwriting local work.
---

# Knowledge-base sync

1. Identify the canonical note and destination before writing.
2. Check for an existing note by stable source ID and title; prefer linking or updating one canonical record.
3. Preserve provenance, date, authorship and local metadata. Do not expose private paths or credentials.
4. Compare destination content before overwriting; merge only the requested, supported changes.
5. Verify the saved note and any configured sync status. Record sync failure without claiming success.

Return the destination, files changed and sync result. If no sync system is configured, keep the note local and say so.
