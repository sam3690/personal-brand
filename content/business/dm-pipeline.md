# DM pipeline (opened 2026-08-20)

One file for the LinkedIn lane. Replaces the scattered tracking in `dm-lane-tracker.md`, which stays
as the historical record of the cold-email lane and the two matched batches.

Booking link: **https://calendly.com/usamabinayoub/30min** (never in message one).

## How this works

A scheduled agent sources and qualifies overnight and writes `dm-queue/queue.json`. Usama opens
`dm-queue/queue.html` in the morning, clicks through about 15 minutes of actions, and pastes the
end-of-day log back. **Nothing sends itself.** LinkedIn's Prohibited Software policy is the reason,
and the account is the asset being protected.

## Daily log

| Date | Queued | Requests sent | Accepts | First messages | Replies | Booked |
|---|---|---|---|---|---|---|
| 2026-08-20 | 0 | | | | | |

## People

Stages: `queued` → `requested` → `accepted` → `messaged` → `replied` → `call booked` → `won` / `dead`.
Never re-source a name that appears here in any state.

| Name | Company | Profile | Stage | Shape | Last touch | Next action | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Read at day 7 of the first 100 requests

Acceptance rate against the 28.5% platform benchmark (Expandi, 13.2M requests). **Below 15% means
the profile is the blocker, not the targeting.** Fix the profile before sending more.

## Gate: CLEARED

The profile rewrite in `profile-rewrite-2026-08-10.md` went live the night of 2026-08-10. It sat
recorded as unchecked in this repo for ten days, which is why the lane looked blocked when it was not.
**Lesson: a gate that is only tracked in a file nobody updates is not a gate, it is a rumour.** When a
human-side action completes, the file gets updated in the same session or the routine reads a lie.

Profile published: ☑ headline ☑ banner ☑ About (all three live 2026-08-10, confirmed by Usama 2026-08-20)
