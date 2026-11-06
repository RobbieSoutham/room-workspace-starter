---
name: service-health-review
description: Assess a service using bounded, current evidence and report health, uncertainty and next checks.
---

# Service health review

Use for a bounded review of a service, system or recurring operational process.

1. Define the service, question, time window and acceptable impact. Read its current owner, runbook and recent incident record.
2. Inspect authoritative health signals for that window: availability, errors, latency, resource use, dependencies and user-visible outcomes as relevant.
3. Separate direct observations, reported symptoms, hypotheses and unavailable evidence. Do not call a service healthy solely because a process is running.
4. Compare signals with documented objectives or a recent baseline. If neither exists, state that limitation and avoid inventing an SLO.
5. Report findings, impact, confidence, immediate action and a specific follow-up owner or check. Link to evidence and keep secrets or personal data out of the report.
