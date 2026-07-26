# Cold Outreach Engine

The revenue-side counterpart to [[The Five Agents]]: automated cold email + LinkedIn connection
requests for the Speed-to-Lead offer. Built 2026-07-06 through 2026-07-09.

## Architecture
- **Sending:** Composio's Gmail connector (`GMAIL_SEND_EMAIL` / `GMAIL_REPLY_TO_THREAD`) from
  usamabinayoub@gmail.com. HubSpot cannot send on the free tier (no send-email tool in its
  connector; real send is a paid Marketing Hub feature), so it never touches the send path.
- **Tracking:** every send is logged as a HubSpot EMAIL engagement against a Contact record
  (portal 246685260), created via `manage_crm_objects`. This gives a CRM timeline per lead
  without HubSpot ever sending anything, so no cold-outreach deliverability penalty from HubSpot's
  infrastructure.
- **Scheduling:** one-time scheduled tasks (`scheduled-tasks` MCP) fire at the send window and
  execute the whole send → log → append-to-file loop unattended. Editing a task's prompt can
  silently clear its `fireAt` and disable it — always re-run `list_scheduled_tasks` after any edit
  to confirm it's still armed.
- **Source of truth:** `content/business/prospects/batch-01-2026-07-03.csv` (100 leads, A/B/X
  tier from Apollo via Apify). Send logs live next to the drafts, e.g.
  `content/business/monday-batch-01-send-log.md`.

## Cadence
- **Cold email:** max 10 new prospects/day, ~20 total sends/day (new + follow-ups) while on plain
  Gmail. Touch 1 → Touch 2 (day 3, in-thread reply) → Touch 3 (day 7, "closing the loop", breakup
  email). Templates in `content/business/outreach-scripts.md`.
- **Send window:** 5–7pm PKT = 8–10am US Eastern, when the prospect is at their desk. Karachi is
  9 hours ahead of NY in summer; a 4–6pm PKT idea maps to 7–9am ET, still morning, not evening —
  worth double-checking the offset before picking a window.
- **LinkedIn connection requests:** 5/day on weekdays while under ~500 connections (a burst of 3+
  invites tripped the weekly limit on a 9-week-old, 267-connection account). Same 4:30–7pm PKT
  window. Prospects already in the email sequence get a one-line note; everyone else gets a blank
  invite (accepted at the same or higher rate, doesn't burn the personalized-note quota).

Related: [[Lead List Quality]] · [[The Five Agents]] · [[Usama Brand Profile]]
