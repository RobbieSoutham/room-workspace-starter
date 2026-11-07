# Autonomy and scheduling

Scheduled automation can improve reliability only when ownership, inputs, permissions, expected outputs and recovery are clear. Start with an inventory and explicit trigger model; do not add a timer merely to make work look autonomous.

## Schedule inventory

Common installations may have multiple independent schedulers, for example an agent gateway scheduler, user/system `cron`, and user/system `systemd` timers. Inventory each source, record its owner and timezone, and define which source is authoritative for every job. A generated effective-schedule view is useful, but it does not replace the scheduler's live state.

For each job, record: stable ID; purpose; owning room; source schedule and timezone; command/entry point; credentials and data boundary; timeout/retry policy; expected artifact and location; alert route; last success/failure; and disable/rollback procedure.

## Safety and reliability gates

- Run read-only or dry-run mode first where available. Bound runtime, retries, output size and spend.
- Grant only the permissions required for the job. External messages, publication, purchases, financial actions, permissions changes and destructive edits require explicit authority.
- Make jobs idempotent or record deduplication keys. Preserve an execution receipt and actionable failure state.
- Alert on missed schedules, stale inputs, failed output validation and repeated retries. A timer being enabled does not prove the job ran.
- For sensitive data, keep processing in an approved boundary and do not forward payloads to external models without authorization.
- Monitor cost, provider changes, rate limits and downstream format/schema changes. Define a stop condition.
- Before changing a critical schedule, capture current config and prepare a rollback. Disable one owner at a time and verify no duplicate job remains.

## Promotion of unattended work

Start with supervised runs on representative inputs. Expand autonomy only after measuring quality, failure recovery, latency and cost, including quiet failures and no-op runs. Keep human gates at high-consequence decisions. Document observed performance and review dates; an untested schedule or workflow remains a proposal.
