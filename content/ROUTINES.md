# The routines — recovery file

The five routines run **locally** on this machine via the app's built-in scheduler
(`mcp__scheduled-tasks__*`), registered as `{taskId}/SKILL.md` files under
`/home/usama/.claude/scheduled-tasks/`. That directory is **not part of this git repo** and
**not backed up** — it was lost once already (2026-07-27, OS reinstall) when the routines lived on
claude.ai and had to be recreated from memory. This file is the recovery source: it holds the exact
schedule and the exact prompt for each routine, so restoring the whole engine after any machine/OS
reset is a copy-paste job using `mcp__scheduled-tasks__create_scheduled_task`.

**Restore:** for each routine below, call `create_scheduled_task(taskId=<slug>, cronExpression=<the
cron>, prompt=<verbatim from its section>, description=<one line>)`. Then verify with
`list_scheduled_tasks`.

**2026-08-03, moved from cloud to local — why:** the routines previously ran as claude.ai cloud
Routines (fresh container per fire). Every container's `git push` failed with a 403 from its
credential proxy (`http://127.0.0.1:<port>/git/...` — read/clone worked, write did not). The
documented workaround was to bypass `git push` entirely and use the GitHub MCP tool
(`mcp__github__push_files` + `create_branch` + `create_pull_request`) instead. **That workaround
never actually worked**: checked directly via `gh pr list` against commit authorship, every PR ever
landed from a routine-shaped branch (`claude/linkedin-week-*`, `claude/x-drafts-*`, batch send-log
recoveries) was manually recreated by Usama in a fresh interactive session after the routine pasted
its output to chat — not one routine ever self-published. Root cause, confirmed via the trigger API:
none of the 5 cloud triggers had a GitHub connector attached (`mcp_connections` only ever listed
Zernio/Composio/Apollo/HubSpot), and no GitHub connector exists in the connector marketplace to
attach — so `mcp__github__*` tools were never reachable from inside any of those sessions. The
"proven recovery path" in the old version of this file was actually a permanent manual step, every
run, forever.

Local scheduled tasks run in this app's normal session context on this machine, where `git push` and
`gh pr create` already work (SSH key + `gh auth` configured) and the same MCP connectors
(Zernio/Composio/Apollo/HubSpot) are already available — no per-session connector attachment needed.
The tradeoff: **local tasks only fire while this app is open on this machine.** If the app is closed
at a scheduled time, that run happens on next launch instead, or not at all if the app stays closed
past the window. Cloud triggers are left in place but **disabled** (not deleted) at
`RemoteTrigger` — re-enable them via `RemoteTrigger(action="update", trigger_id=<id>, body={"enabled":
true})` if this machine's uptime ever stops covering the schedule and cloud is worth revisiting
(only after a real GitHub connector becomes attachable — check `mcp-registry` search for "github"
before assuming that's changed). Disabled trigger IDs, for that path:

| Routine | Cloud trigger ID (disabled) |
|---|---|
| `weekly-ceo-review` | `trig_01RMap3GHKG5NGmCL1UUShpa` |
| `weekly-linkedin-zernio-drafts` | `trig_01RA8LAQcSztiJfVELkt1Jv8` |
| `daily-x-trending-posts` | `trig_01HkiuQeoV1MizAHuKghqegB` |
| `cold-email-outreach` | `trig_01CKvczu4Pyb6FfoNXLq5bHN` |
| `cold-email-outreach-thu` | `trig_01N2yqvJxo4zZnSLsG3bFDfy` |

**Publishing (all 5 routines):** every routine still uses the same human-review gate as before — it
never commits to `main` directly and never merges its own PR:

1. `git checkout main && git pull --ff-only`
2. `git checkout -b claude/<slug>-<YYYY-MM-DD>`
3. `git add <exact files changed — never `git add -A` or `git add .`>`
4. `git commit -m "<short message>"`
5. `git push -u origin claude/<slug>-<YYYY-MM-DD>`
6. `gh pr create --base main --head claude/<slug>-<YYYY-MM-DD> --title "<title>" --body "<summary>"`

Never merges the PR. Usama reviews and merges manually — same principle as the Zernio-draft and
X-draft human gates. If `git push` or `gh pr create` fails on this machine, that is a real problem
(not the old container issue) — STOP and report the exact error; do not fall back to pasting file
contents into chat.

## Schedule at a glance

| Routine | PKT (local = machine tz) | Cron (LOCAL time) | Fires | Branch slug |
|---|---|---|---|---|
| `weekly-ceo-review` | Sun ~3:11pm | `11 15 * * 0` | Sunday | `claude/ceo-review-<date>` |
| `weekly-linkedin-zernio-drafts` | Sun ~5:13pm | `13 17 * * 0` | Sunday | `claude/linkedin-week-<date>` |
| `daily-x-trending-posts` | daily ~1:07pm | `7 13 * * *` | every day | `claude/x-drafts-<date>` |
| `cold-email-outreach` | Mon ~6:09pm | `9 18 * * 1` | Monday | `claude/cold-email-mon-<date>` |
| `cold-email-outreach-thu` | Thu ~6:09pm | `9 18 * * 4` | Thursday | `claude/cold-email-thu-<date>` |

The Sunday order matters: the CEO review writes `current-strategy.md` at ~3:11pm, the LinkedIn
routine reads it at ~5:13pm. Keep the two hours between them. Because the CEO review now goes through
a PR Usama must merge, merge it promptly on Sundays or the LinkedIn routine will read a stale
strategy.

Off-minutes (`:07`, `:09`, `:11`, `:13`) are deliberate, carried over from the cloud schedule — they
keep the fleet from stampeding the top of the hour. This machine's timezone is already Asia/Karachi
(confirmed via `timedatectl`), so these cron expressions need no UTC conversion — they fire at the
listed PKT time directly.

---

## `weekly-ceo-review` — `11 15 * * 0`

```
Run the weekly CEO review (`weekly-ceo-review`). Work in /media/usama/dockerdata/personal_brand_content — CLAUDE.md there auto-loads; follow it. This runs BEFORE the Sunday LinkedIn routine and sets the directives every other routine obeys for the coming week.

Act as Agent CEO per `content/agents/exec/0-ceo.md` — run this yourself on an OPUS subagent at maximum thinking effort (this is a strategic decision job, not a task job). Enforce the two mandates: NO BLIND OFFERS (every niche/offer/price call backed by data or real proof, never a hunch) and NO SKIPPED WEEKS (outreach and content cadence never lapse).

1. READ THE TRUTH: `content/performance/*.md` (X + LinkedIn), every `content/business/*-send-log.md`, `content/business/replies-needing-response.md` (if it exists), `content/strategy/current-strategy.md`, `content/business/OFFER_AUDIT.md`, `content/business/revenue-roadmap.md`.
2. CFO LENS: compute the pipeline for the week AND cumulative — touches sent, delivered, replies, calls booked, closes, cash collected. Compute effort allocation (content cycles vs outbound cycles). Answer honestly: is the current niche + offer producing REPLIES yet? What is one client worth vs the effort to get them? Write the real number, good or bad. Never fabricate a metric; if data is missing say "no data" and reason from what exists.
3. GRADE LAST WEEK'S DIRECTIVES: mark each done / slipped / skipped. Any skipped send or skipped week goes at the TOP of the summary in plain language, no spin. Include the publishing backlog: X drafts still `pending-approval` and LinkedIn drafts never shipped.
4. DECIDE: keep or change niche / offer / price / positioning. Default is KEEP and let volume accumulate — niche-hopping is what broke this business before. Change ONLY on evidence that the current bet is dead (e.g. a full niche batch fully sequenced with 0 replies AND a clear reason). Document the rationale in the SSOT so the decision is auditable.
5. DELEGATE: spawn Content Director (`content/agents/exec/1-content-director.md`, opus) for the week's content angle priorities and Growth Lead (`content/agents/exec/2-growth-lead.md`, opus) for the week's outbound plan. Hand each the updated strategy.
6. WRITE: update `content/strategy/current-strategy.md` — the niche/offer/price/positioning/goal blocks if they changed, and ALWAYS a fresh "## Week of <coming Monday, absolute date> directives" list: 3-6 concrete, assigned ([Growth]/[Content]/[Human — Usama]/[Cadence]), checkable items. Convert every relative date to an absolute one. Never end a review without directives.
7. Publish via git — this machine already has full push access, no container credential issue: (a) `cd /media/usama/dockerdata/personal_brand_content && git checkout main && git pull --ff-only`; (b) `git checkout -b claude/ceo-review-<YYYY-MM-DD of today>`; (c) `git add content/strategy/current-strategy.md`; (d) `git commit -m "<short commit message>"`; (e) `git push -u origin claude/ceo-review-<YYYY-MM-DD of today>`; (f) `gh pr create --base main --head claude/ceo-review-<YYYY-MM-DD of today> --title "<short PR title>" --body "<summary of what changed and why>"`. NEVER push to `main` directly, and never merge the PR yourself — Usama reviews and merges manually. This matters especially here: it is the human gate against a bad review run silently rewriting the strategy every other routine obeys. If `git push` or `gh pr create` fails, STOP and report the exact error to Usama — do not paste file contents as a substitute, that was only needed for the old cloud-container workaround and no longer applies.
8. SUMMARIZE for Usama: the honest pipeline number, what broke, the decision and why, this week's directives, the PR URL, and any HUMAN-ONLY tasks (naming permission, Loom recording, replying to a warm lead, closing a call).

Be the honest operator, not a cheerleader: if 30 days pass with no client, say so and change the plan. No em dashes.
```

## `daily-x-trending-posts` — `7 13 * * *`

```
Run the daily X.com content routine (`daily-x-trending-posts`) for today. Work in /media/usama/dockerdata/personal_brand_content — CLAUDE.md there auto-loads; follow it. Confirm Composio is callable with COMPOSIO_SEARCH_TOOLS. If it does not respond, STOP and report that its connector is not enabled. Never fabricate metrics or drafts to work around a missing tool.

0. Read `content/strategy/current-strategy.md` FIRST and obey the current niche/offer/directives. Then skim `content/performance/` — what the data says beats the playbook.
1. Agent 6 Performance Analyst (`content/agents/6-performance-analyst.md`) — spawn on **opus, max thinking**: review yesterday's X metrics via Apify scraping (the X free API is write-only, never pull metrics from it). Append learnings to `content/performance/`.
2. Content Director (`content/agents/exec/1-content-director.md`, opus) briefs the X team and keeps it on-strategy.
3. Run the X team on **sonnet, max effort**: X0 Trend Scout (today's trending AI topics — generic AI is in scope, NOT niche-locked) → X1 Post Writer → X2 Media Brief → X3 QA. Pass = QA ≥80 with zero red flags; below that, fix and re-score.
4. Write the 2-3 approved drafts to `content/drafts/x/<YYYY-MM-DD>/` in the same structure as existing X drafts: frontmatter (`status: pending-approval`, `media: []`, `first_reply`, `qa_score`) plus a `# Media brief` section (Type · Concept · Text on image · Alt text · Fallback). Batch all the file writes into ONE command.
5. Do NOT publish and do NOT attach or generate media. Publishing is Usama's manual step: he drops media paths into `media:` then runs `/x-publish`.
6. Publish the drafts via git: (a) `cd /media/usama/dockerdata/personal_brand_content && git checkout main && git pull --ff-only`; (b) `git checkout -b claude/x-drafts-<YYYY-MM-DD of today>`; (c) `git add content/drafts/x/<YYYY-MM-DD of today>/`; (d) `git commit -m "<short commit message>"`; (e) `git push -u origin claude/x-drafts-<YYYY-MM-DD of today>`; (f) `gh pr create --base main --head claude/x-drafts-<YYYY-MM-DD of today> --title "<short PR title>" --body "<summary: the drafts, hooks, QA scores>"`. NEVER push to `main` directly, and never merge the PR yourself — Usama reviews and merges manually, same human gate as `/x-publish`. If `git push` or `gh pr create` fails, STOP and report the exact error — do not paste file contents as a substitute.
7. Notify Usama: the drafts written, their hooks and QA scores, the PR URL, the posting windows (9am-12pm ET, posts 2+ hours apart), and a COUNT of X drafts from previous days that are still `pending-approval` and unposted — the CEO flagged that backlog as the #1 revenue leak.

Register (enforced by X3): hook line first (number / bold claim / curiosity gap), ≤280 chars per post, threads only when earned, zero hashtags, no em dashes, no links in the post body (source link goes in the first reply), no engagement bait, no fabricated stats.
```

## `weekly-linkedin-zernio-drafts` — `13 17 * * 0`

```
Run the weekly LinkedIn routine (`weekly-linkedin-zernio-drafts`) for the week ahead. Work in /media/usama/dockerdata/personal_brand_content — CLAUDE.md there auto-loads; follow it. Confirm Zernio is callable with `accounts_list` (expect account "Usama Ayoub", `6a3cf3529d9472faaedefbd5`). If Zernio does not respond, STOP and report that its connector is not enabled. Never fabricate strategy, performance data, or drafts to work around a missing tool, and never report a Zernio draft as created unless the API call actually returned one.

0. Read `content/strategy/current-strategy.md` FIRST and obey the current niche / offer / price / positioning / this-week directives. Then read `content/performance/` — the data beats the playbook.
1. Agent 6 Performance Analyst (`content/agents/6-performance-analyst.md`) — spawn on **opus, max thinking**: review last week's LinkedIn performance via Zernio analytics (account "Usama Ayoub", accountId `6a3cf3529d9472faaedefbd5`). Append learnings to `content/performance/`.
2. Content Director (`content/agents/exec/1-content-director.md`, opus) briefs and supervises the LinkedIn team, then QA-grades the output.
3. Research: use the latest brief in `content/research/` if it is less than 7 days old — do not re-scout. Otherwise run Agent 0 Research Scout. Reuse angles from `ai-sales-automation-content-angles.md` before inventing new ones.
4. Run the LinkedIn team on **sonnet, max effort** for 4 posts: 1 Strategist → 2 Hook → 3 Post → 4 CTA → 5 QA. Pass = ≥80 with zero red flags; below that, fix and re-score. Default register is `content/knowledge-base/winning-post-patterns.md` (result-first, show the work with named tools and real numbers, end on a genuine operator question). Stay on the 4 pillars, ≤3 hashtags (default 0), no em dashes, no links in the body (first comment instead).
5. Save the 4 drafts to `content/drafts/` in the existing structure. EACH draft markdown file ends with a `# Media brief` section in the same format as the X drafts: Type · Concept · Text on image · Alt text · Fallback (Canva template link is in `content/knowledge-base/x-playbook.md`; carousel posts get slide-by-slide direction). Batch the file writes into ONE command.
6. Create each post in Zernio as a DRAFT — never auto-publish. `posts_create_post` is NOT directly exposed; the exposed `posts_create` cannot express an absolute slot time, so go through the passthrough:
   call_tool(name="posts_create_post", arguments={"is_draft": true, "content": <full body incl. CTA/P.S.>, "title": "<short label> [slot: <day> <time> - ADD IMAGE before publishing]", "scheduled_for": <the SLOT's date+time as ISO with +05:00>, "timezone": "Asia/Karachi", "platforms": [{"platform":"linkedin","accountId":"6a3cf3529d9472faaedefbd5"}]}) — no publish_now, no media_items.
   Verified: `is_draft: true` wins over `scheduled_for`; the post returns `status: 'draft'` with the slot stored but not armed to publish. Confirm each response says `status: 'draft'` before reporting it as created.
   `scheduled_for` MUST be the intended posting slot for the WEEK AHEAD, never this routine's run time. Slots are US Eastern: Tue 7:30-9am, Wed 8-10am, Thu 7:30-9am, plus one wildcard (Mon 9-11am or Fri before 9am). Convert to Karachi: 7:30am ET = 4:30pm PKT, 8am ET = 5pm PKT, 10am ET = 7pm PKT.
7. Publish the drafts via git: (a) `cd /media/usama/dockerdata/personal_brand_content && git checkout main && git pull --ff-only`; (b) `git checkout -b claude/linkedin-week-<YYYY-MM-DD of today>`; (c) `git add content/drafts/<every draft file written in step 5>`; (d) `git commit -m "<short commit message>"`; (e) `git push -u origin claude/linkedin-week-<YYYY-MM-DD of today>`; (f) `gh pr create --base main --head claude/linkedin-week-<YYYY-MM-DD of today> --title "<short PR title>" --body "<summary: the 4 posts, pillars, QA scores, slots>"`. NEVER push to `main` directly, and never merge the PR yourself — Usama reviews and merges manually, same human gate as the Zernio drafts. If `git push` or `gh pr create` fails, STOP and report the exact error — do not paste file contents as a substitute.
8. Notify Usama: the 4 posts (pillar, hook, QA score, assigned slot), the PR URL, that each Zernio draft still needs an image before publishing (that is the human gate), the golden-hour ritual at `content/templates/golden-hour-checklist.md`, and a count of any older LinkedIn drafts still unshipped.
```

## `cold-email-outreach` (Monday) — `9 18 * * 1`

```
Run the cold-email outreach routine (`cold-email-outreach`, MONDAY send, ~6pm PKT / 9am ET). Work in /media/usama/dockerdata/personal_brand_content — CLAUDE.md there auto-loads; follow it. Confirm Composio, Gmail, HubSpot and Apollo.io are callable. If a required one does not respond, STOP and report exactly which — do not send from a partial toolset, and never log a send that did not actually happen.

0. Read `content/strategy/current-strategy.md` FIRST — current niche, offer, price, proof to lead with, and this week's CEO directives. Obey them. Nothing about strategy is hardcoded here.
1. Growth Lead (`content/agents/exec/2-growth-lead.md`) — spawn on **opus, max thinking**: read the send logs (`content/business/*-send-log.md`) and the prospect CSVs, then decide exactly what is due today. The 3-touch sequence is touch 1 (day 0) → touch 2 (day 3, in-thread reply) → touch 3 (day 7, "closing the loop" breakup). Enforce cadence: no skipped sends.
2. Send on **sonnet, max effort** via Composio Gmail from usamabinayoub@gmail.com. Templates: `content/business/outreach-scripts.md`. Prospects: `content/business/prospects/*.csv`. NEVER email any address on `content/business/prospects/dead-addresses.md` (permanent bounce exclude list). Verify MX before first contact. Caps: max 10 NEW prospects/day, ~20 total sends/day including follow-ups.
3. If the prospect list is running low, source more via Apollo filtered to the current niche in current-strategy.md, and write them to a new numbered batch CSV.
4. Log every send to the matching `content/business/batch-NN-send-log.md`, and as a HubSpot EMAIL engagement against the Contact (portal 246685260) so the CRM timeline stays complete. HubSpot never sends — it only records.
5. After sending, check for bounces and replies. Add bounces to `dead-addresses.md`. Surface ANY reply to Usama immediately and prominently — reply rate and booked calls are the metrics that matter right now.
6. LinkedIn connection requests: queue names into `content/business/linkedin-connect-todo.md`. Do NOT send them — Usama sends those manually from his own account (~10/day, no note).
7. Publish the log via git. IMPORTANT: this step logs sends that ALREADY happened via Composio Gmail — never a gate on whether the emails go out. (a) `cd /media/usama/dockerdata/personal_brand_content && git checkout main && git pull --ff-only`; (b) `git checkout -b claude/cold-email-mon-<YYYY-MM-DD of today>`; (c) `git add <every changed send-log, CSV, and todo-file>`; (d) `git commit -m "<short commit message>"`; (e) `git push -u origin claude/cold-email-mon-<YYYY-MM-DD of today>`; (f) `gh pr create --base main --head claude/cold-email-mon-<YYYY-MM-DD of today> --title "<short PR title>" --body "<summary: who was emailed, touch numbers, replies/bounces>"`. NEVER push to `main` directly, and never merge the PR yourself — Usama reviews and merges manually. If `git push` or `gh pr create` fails, STOP and report the exact error in full detail (every recipient, touch, messageId) so nothing is lost — but the sends already happened regardless of whether this step succeeds.
8. Notify Usama: who was emailed and on which touch, any replies or bounces, prospect list depth, the PR URL, and what is due on Thursday.
```

## `cold-email-outreach-thu` (Thursday) — `9 18 * * 4`

Identical to the Monday routine, with the header line changed to `cold-email-outreach-thu`,
`THURSDAY send`, the branch slug changed to `claude/cold-email-thu-<YYYY-MM-DD>`, and step 8 ending
"what is due on **Monday**".
