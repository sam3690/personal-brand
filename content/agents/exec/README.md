# Exec layer — the decision team that runs the business

The content/outreach teams generate work. This layer DECIDES what work to do and checks it.
Built in the same pattern as everything else: markdown instruction files, invoked by scheduled routines.

## Org chart
```
CEO (0-ceo.md, opus)                  owns niche/offer/price/positioning; "no blind offers, no skipped weeks"
 ├─ Content Director (1-content-director.md, opus)   supervises + QA-grades the content teams
 │    └─ LinkedIn team (../0..6, sonnet) + X team (../x/x0..x3, sonnet)   ← the doers
 └─ Growth Lead (2-growth-lead.md, opus)             owns outbound funnel, cadence, pipeline
      └─ cold-email routine + prospecting (sonnet)   ← the doers
```
CFO is not a separate agent yet (pre-revenue = nothing to account). Its job — "watch the money, is this
actually working" — lives inside the CEO's weekly review as a CFO lens. Split it out at real MRR.

## The coordination mechanism
`content/strategy/current-strategy.md` is the single source of truth. The CEO writes it; every routine
reads it FIRST and obeys the current niche / offer / price / positioning / this-week directives.
Nothing about strategy is hardcoded in a routine anymore.

## Model routing
Deciders/strategists/researchers → opus 4.8, max thinking effort. Task executors → sonnet 5, max effort.

## How a week runs
1. Sun ~3pm PKT — `weekly-ceo-review` (CEO, opus): read the truth (perf logs + send logs + pipeline),
   grade last week, decide, update current-strategy.md + this-week directives.
2. Sun ~5pm PKT — `weekly-linkedin-zernio-drafts`: Content Director briefs + supervises the LinkedIn team.
3. Mon & Thu 6pm PKT — `cold-email-outreach`: Growth Lead enforces niche/offer/cadence, routine sends.
4. Daily ~1pm PKT — `daily-x-trending-posts`: Content Director keeps X on-strategy; Agent 6 feeds metrics.
5. Agent 6 performance logs feed the next CEO review. Loop closes.
