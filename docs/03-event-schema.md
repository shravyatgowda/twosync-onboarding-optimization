# Event schema

Source of truth: `events/posthog_event_schema.json`. This page explains the funnel the events build.

```
pairing_screen_viewed -> invite_channel_selected -> invite_sent -> invite_opened -> partner_registered -> pairing_completed
                                   \-> invite_send_failed          (server-side events: invite_opened, partner_registered, pairing_completed)
                                   \-> pairing_skipped
```

## Why some events are server-side

The last three events happen on the partner's device or in the backend. Logging them server-side avoids losing them to ad blockers, offline clients or app version gaps, and keeps Android and iOS counts consistent.

## Validation checks (run daily)

1. Android and iOS event counts per 1,000 users stay within 10% of each other.
2. Every `pairing_completed` has a matching earlier `invite_sent` with the same `invite_id`.
3. No duplicate (user, event, invite_id) rows inside a 5-second window.
4. `local_hour` is present on 100% of events.
