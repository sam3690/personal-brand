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
| 2026-08-21 | 4 | | | | | |
| 2026-08-24 | 3 | | | | | |
| 2026-08-25 | 2 | | | | | |

## People

Stages: `queued` → `requested` → `accepted` → `messaged` → `replied` → `call booked` → `won` / `dead`.
Never re-source a name that appears here in any state.

| Name | Company | Profile | Stage | Shape | Last touch | Next action | Notes |
|---|---|---|---|---|---|---|---|
| Claire Arnaud-Aubour | SpLAshPR Agency | [linkedin.com/in/claire-arnaud-aubour](https://www.linkedin.com/in/claire-arnaud-aubour/) | queued | A | 2026-08-21 | Usama sends blank connect | PR/events agency, Santa Monica, ~6 people |
| Jamie Lamonde | Kindship Group | [linkedin.com/in/jamie-lamonde](https://www.linkedin.com/in/jamie-lamonde/) | queued | A | 2026-08-21 | Usama sends blank connect | Fractional CMO/brand consultancy, Madison WI, 4 people |
| Mandy McEwen | Mod Girl Marketing | [linkedin.com/in/mandymcewen](https://www.linkedin.com/in/mandymcewen/) | queued | A | 2026-08-21 | Usama sends blank connect | B2B LinkedIn prospecting consultancy, San Diego, 7 people |
| Kilee Hughes | Six One Agency | [linkedin.com/in/kileehughes](https://www.linkedin.com/in/kileehughes/) | queued | A | 2026-08-21 | Usama sends blank connect | PR/brand strategy, beauty/wellness, Denver, 7 people |
| Amanda Christoff | Bloom Talent | [linkedin.com/in/amandachristoff](https://www.linkedin.com/in/amandachristoff/) | queued | B | 2026-08-24 | Usama sends blank connect | Boutique recruiting agency (EAs, Chiefs of Staff, People Ops), SF Bay Area, ~6 people |
| Sue Ebrahim | Hire Talent | [linkedin.com/in/sueebrahim](https://www.linkedin.com/in/sueebrahim/) | queued | B | 2026-08-24 | Usama sends blank connect | Interim/executive recruitment, Houston TX, 2-9 people (Clutch) |
| Mary Lou Bunn | Flower Shop | [linkedin.com/in/mary-lou-bunn-643192b](https://www.linkedin.com/in/mary-lou-bunn-643192b/) | queued | B | 2026-08-24 | Usama sends blank connect | Creative ad agency, NYC, team of 8, Adweek Creative 100 2026 |
| Susan Major | Major Executive Search | [linkedin.com/in/susanmajor](https://www.linkedin.com/in/susanmajor/) | queued | B | 2026-08-25 | Usama sends blank connect | Executive search firm, San Diego, ~8 people, places C-suite for tech companies but not itself technical |
| Mike Knapp | Incrementa (un)consulting | [linkedin.com/in/mikevknapp](https://www.linkedin.com/in/mikevknapp/) | queued | B | 2026-08-25 | Usama sends blank connect | Business strategy/execution coaching, Vancouver BC, 2-4 people |

## Read at day 7 of the first 100 requests

Acceptance rate against the 28.5% platform benchmark (Expandi, 13.2M requests). **Below 15% means
the profile is the blocker, not the targeting.** Fix the profile before sending more.

## Gate: CLEARED

The profile rewrite in `profile-rewrite-2026-08-10.md` went live the night of 2026-08-10. It sat
recorded as unchecked in this repo for ten days, which is why the lane looked blocked when it was not.
**Lesson: a gate that is only tracked in a file nobody updates is not a gate, it is a rumour.** When a
human-side action completes, the file gets updated in the same session or the routine reads a lie.

Profile published: ☑ headline ☑ banner ☑ About (all three live 2026-08-10, confirmed by Usama 2026-08-20)
