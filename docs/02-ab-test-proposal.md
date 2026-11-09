# A/B test proposal: single-screen partner invitation

## Hypothesis

If new users see a single-screen invitation with one primary action and a live status, more of them will send an invite and more couples will pair on day 1, because there is less to read and decide and the result of their action is visible.

## Variants

- **Control:** current multi-option invite page.
- **Treatment:** single-screen invite from `prototype/index.html`.

## Metrics

| Role | Metric | Definition |
|---|---|---|
| Primary | D1 partner-pairing completion | Users whose pairing is completed within 24 hours of registration / users registered |
| Secondary | Invite send rate | Users with `invite_sent` / users who viewed the screen |
| Secondary | Median time from send to pairing | `pairing_completed.time_since_sent_sec` |
| Guardrail | D1 uninstall rate | Must not rise by more than 1 point |
| Guardrail | Skip rate | `pairing_skipped` / screen views, watched for a sharp rise |

## Sample size

Baseline D1 pairing rate 30%, minimum detectable effect +4 points absolute, alpha 0.05 (two-sided), power 80%.

```
python scripts/sample_size.py --baseline 0.30 --mde 0.04
```

This gives about **2,134 users per arm**. At 300 registrations a day the test needs about 15 days, rounded up to **two full weeks** so every weekday is covered twice.

## Design rules

- Randomize at the user level, 50/50, sticky assignment.
- Run for the full pre-planned duration. Do not call a winner early: peeking inflates false positives.
- Exclude internal and test accounts.
- Check sample-ratio mismatch before reading any result (expected 50/50).
- Log `local_hour` on every event so the late-evening segment can be cut afterwards.

## Decision rule

Ship if the primary metric improves with a 95% confidence interval above zero and no guardrail breaches. If the guardrail confidence interval includes the 1-point limit, extend the test or investigate before shipping.

## Segments to read after the main result

Platform (Android, iOS), invite channel, and registration hour (before 9 PM vs 9 PM to midnight). Segments are exploratory: findings there become new hypotheses, not conclusions.

## Event schema

See `events/posthog_event_schema.json` and `docs/03-event-schema.md`.
