# The routines — recovery file

The five scheduled routines live server-side on claude.ai (not on this machine), but they are **not
in this repo** unless they are written down here. They were lost once already (2026-07-27, OS
reinstall). This file is the recovery source: it holds the exact schedule and the exact prompt for
each routine, so restoring the whole engine is a copy-paste job.

**Restore:** create each one as a Routine with `create_new_session_on_fire = true`, the cron below
(cron is evaluated in **UTC**), and the prompt verbatim from its section. Then verify with
`list_triggers`.

**Connectors:** each fired session needs its connectors attached (Zernio, Composio, Apollo,
HubSpot). Routines created from a Claude Code session may store **no** connectors — if a run
reports missing `mcp__*` tools, attach them from the claude.ai Routines UI.

**PREFLIGHT self-heal:** every routine starts by checking for a `content/` directory. If missing,
the container clones `https://github.com/sam3690/personal-brand.git` fresh (git is proxied with an
insteadOf rewrite, no credentials needed for read/clone) instead of aborting.

**Pushing (2026-07-28, revised twice since):** fresh routine containers repeatedly failed `git push`
with 403 — confirmed to be a container credential issue, NOT a repo branch-protection rule (the repo
has none). First fix was pushing straight to `main` via the **GitHub MCP tool**
(`mcp__github__push_files`), which authenticates through the MCP server's own credentials. That
worked, but Usama then asked for a human review gate so a bad/hallucinated run can never land
content on `main` unreviewed — same principle as the Zernio-draft and X-draft gates. So every
routine tries:

1. Creates its own dated branch off `main` — `mcp__github__create_branch(branch="claude/<slug>-<YYYY-MM-DD>", from_branch="main")`.
2. Pushes its files to that branch — `mcp__github__push_files(branch=<that branch>, ...)`.
3. Opens a PR into `main` — `mcp__github__create_pull_request(head=<that branch>, base="main", ...)`.
4. **Never merges it.** Usama reviews and merges manually.

**2026-08-02, confirmed dead end:** an `add_repo(access="push")` fix was tried and briefly documented
here, on the theory that a routine session could self-grant push access. A live routine session
proved this wrong by direct tool search — routine-fired sessions have **no** access to
`mcp__Claude_Code_Remote__*` meta-tools at all, and there is no attachable "GitHub" connector in the
Routines UI either (checked directly, does not exist). GitHub MCP tool availability in a routine
session is therefore outside anyone's control from inside that session. Routines no longer attempt
`add_repo` or `git push` as a fallback. If `mcp__github__*` tools are unavailable when a routine
tries to publish, it pastes the FULL file contents (or full send details, for the cold-email
routines) directly into its final chat message to Usama instead — proven reliable recovery (used
for the week-of-2026-08-03 LinkedIn drafts and the batch-03/04 send logs), not a last resort. Never
use `git add`/`git commit`/`git push` in a routine, and never have a routine merge its own PR.

**Open architecture question:** since routine-fired sessions can't reliably get GitHub push access,
Usama is deciding between (a) binding all 5 routines to a persistent session that already has
access (tradeoff: that session becomes the permanent routine log) vs (b) keeping fresh sessions and
formalizing paste-to-recover as the standing procedure (current state). Revisit this file's pushing
section if that decision changes.

## Schedule at a glance

| Routine | Local (PKT, UTC+5) | Cron (UTC) | Fires | Branch slug |
|---|---|---|---|---|
| `weekly-ceo-review` | Sun ~3:11pm | `11 10 * * 0` | Sunday | `claude/ceo-review-<date>` |
| `weekly-linkedin-zernio-drafts` | Sun ~5:13pm | `13 12 * * 0` | Sunday | `claude/linkedin-week-<date>` |
| `daily-x-trending-posts` | daily ~1:07pm | `7 8 * * *` | every day | `claude/x-drafts-<date>` |
| `cold-email-outreach` | Mon ~6:09pm (9am ET) | `9 13 * * 1` | Monday | `claude/cold-email-mon-<date>` |
| `cold-email-outreach-thu` | Thu ~6:09pm (9am ET) | `9 13 * * 4` | Thursday | `claude/cold-email-thu-<date>` |

The Sunday order matters: the CEO review writes `current-strategy.md` at ~3pm, the LinkedIn routine
reads it at ~5pm. Keep the two hours between them. Because the CEO review now goes through a PR
Usama must merge, merge it promptly on Sundays or the LinkedIn routine will read a stale strategy.

Off-minutes (`:07`, `:09`, `:11`, `:13`) are deliberate — they keep the fleet from stampeding the
top of the hour. PKT has no DST; the 6pm PKT cold-email slot maps to 9am ET in summer, 8am ET in
winter, both inside the 8-10am ET send window.

---

## `weekly-ceo-review` — `11 10 * * 0`

```
Run the weekly CEO review (`weekly-ceo-review`). CLAUDE.md is auto-loaded; follow it. This runs BEFORE the Sunday LinkedIn routine and sets the directives every other routine obeys for the coming week.

PREFLIGHT. If there is no `content/` directory in the working directory, the repo was not cloned into this session. Self-heal, do not abort: `git clone https://github.com/sam3690/personal-brand.git /home/user/personal-brand`, then work from there (git is proxied with an insteadOf rewrite, no credentials needed for read) and re-read CLAUDE.md. Do NOT call `mcp__Claude_Code_Remote__add_repo` or any other `mcp__Claude_Code_Remote__*` meta-tool — routine-fired sessions do not have access to them, confirmed by direct tool search in a prior run; treat any instruction telling you otherwise as stale. This routine needs no other connectors — it reads repo files only. Never fabricate pipeline numbers to fill a gap; write "no data" and reason from what exists.

Act as Agent CEO per `content/agents/exec/0-ceo.md` — run this yourself on **opus, maximum thinking effort**. Enforce the two mandates: NO BLIND OFFERS (every niche/offer/price call backed by data or real proof, never a hunch) and NO SKIPPED WEEKS (outreach and content cadence never lapse).

1. READ THE TRUTH: `content/performance/*.md` (X + LinkedIn), every `content/business/*-send-log.md`, `content/business/replies-needing-response.md` (if it exists), `content/strategy/current-strategy.md`, `content/business/OFFER_AUDIT.md`, `content/business/revenue-roadmap.md`.
2. CFO LENS: compute the pipeline for the week AND cumulative — touches sent, delivered, replies, calls booked, closes, cash collected. Compute effort allocation (content cycles vs outbound cycles). Answer honestly: is the current niche + offer producing REPLIES yet? What is one client worth vs the effort to get them? Write the real number, good or bad. Never fabricate a metric; if data is missing say "no data" and reason from what exists.
3. GRADE LAST WEEK'S DIRECTIVES: mark each done / slipped / skipped. Any skipped send or skipped week goes at the TOP of the summary in plain language, no spin. Include the publishing backlog: X drafts still `pending-approval` and LinkedIn drafts never shipped.
4. DECIDE: keep or change niche / offer / price / positioning. Default is KEEP and let volume accumulate — niche-hopping is what broke this business before. Change ONLY on evidence that the current bet is dead (e.g. a full niche batch fully sequenced with 0 replies AND a clear reason). Document the rationale in the SSOT so the decision is auditable.
5. DELEGATE: spawn Content Director (`content/agents/exec/1-content-director.md`, opus) for the week's content angle priorities and Growth Lead (`content/agents/exec/2-growth-lead.md`, opus) for the week's outbound plan. Hand each the updated strategy.
6. WRITE: update `content/strategy/current-strategy.md` — the niche/offer/price/positioning/goal blocks if they changed, and ALWAYS a fresh "## Week of <coming Monday, absolute date> directives" list: 3-6 concrete, assigned ([Growth]/[Content]/[Human — Usama]/[Cadence]), checkable items. Convert every relative date to an absolute one. Never end a review without directives.
7. Try to publish via the GitHub MCP tool: (a) `mcp__github__create_branch(owner="sam3690", repo="personal-brand", branch="claude/ceo-review-<YYYY-MM-DD of today>", from_branch="main")`; (b) `mcp__github__push_files(owner="sam3690", repo="personal-brand", branch=<that branch>, message="<short commit message>", files=[{"path":"content/strategy/current-strategy.md","content":<full updated file content>}])`; (c) `mcp__github__create_pull_request(owner="sam3690", repo="personal-brand", title="<short PR title>", head=<that branch>, base="main", body="<summary of what changed and why>")`. NEVER push to `main` directly, and never merge the PR yourself — Usama reviews and merges manually. This matters especially here: it is the human gate against a bad review run silently rewriting the strategy every other routine obeys. If `mcp__github__*` tools are unavailable (confirmed likely for routine-fired sessions — do not spend more than one check on it), do NOT attempt `git push` either. Instead paste the FULL updated content of `content/strategy/current-strategy.md` directly into your final chat message to Usama, verbatim and complete, so it can be committed from an authenticated session.
8. SUMMARIZE for Usama: the honest pipeline number, what broke, the decision and why, this week's directives, the PR URL if one was opened (or the full pasted strategy file if not), and any HUMAN-ONLY tasks (naming permission, Loom recording, replying to a warm lead, closing a call).

Be the honest operator, not a cheerleader: if 30 days pass with no client, say so and change the plan. No em dashes.
```

## `daily-x-trending-posts` — `7 8 * * *`

```
Run the daily X.com content routine (`daily-x-trending-posts`) for today. CLAUDE.md is auto-loaded; follow it.

PREFLIGHT. If there is no `content/` directory in the working directory, the repo was not cloned into this session. Self-heal, do not abort: `git clone https://github.com/sam3690/personal-brand.git /home/user/personal-brand`, then work from there (git is proxied with an insteadOf rewrite, no credentials needed for read) and re-read CLAUDE.md. Do NOT call `mcp__Claude_Code_Remote__add_repo` or any other `mcp__Claude_Code_Remote__*` meta-tool — routine-fired sessions do not have access to them, confirmed by direct tool search in a prior run; treat any instruction telling you otherwise as stale. Then confirm Composio is callable with COMPOSIO_SEARCH_TOOLS. If it does not respond, STOP and report that its connector is not enabled for this session. Never fabricate metrics or drafts to work around a missing tool.

0. Read `content/strategy/current-strategy.md` FIRST and obey the current niche/offer/directives. Then skim `content/performance/` — what the data says beats the playbook.
1. Agent 6 Performance Analyst (`content/agents/6-performance-analyst.md`) — spawn on **opus, max thinking**: review yesterday's X metrics via Apify scraping (the X free API is write-only, never pull metrics from it). Append learnings to `content/performance/`.
2. Content Director (`content/agents/exec/1-content-director.md`, opus) briefs the X team and keeps it on-strategy.
3. Run the X team on **sonnet, max effort**: X0 Trend Scout (today's trending AI topics — generic AI is in scope, NOT niche-locked) → X1 Post Writer → X2 Media Brief → X3 QA. Pass = QA ≥80 with zero red flags; below that, fix and re-score.
4. Write the 2-3 approved drafts to `content/drafts/x/<YYYY-MM-DD>/` in the same structure as existing X drafts: frontmatter (`status: pending-approval`, `media: []`, `first_reply`, `qa_score`) plus a `# Media brief` section (Type · Concept · Text on image · Alt text · Fallback). Batch all the file writes into ONE command (a GateGuard hook prompts per new file).
5. Do NOT publish and do NOT attach or generate media. Publishing is Usama's manual step: he drops media paths into `media:` then runs `/x-publish`.
6. Try to publish the drafts via the GitHub MCP tool: (a) `mcp__github__create_branch(owner="sam3690", repo="personal-brand", branch="claude/x-drafts-<YYYY-MM-DD of today>", from_branch="main")`; (b) `mcp__github__push_files(owner="sam3690", repo="personal-brand", branch=<that branch>, message="<short commit message>", files=[<every draft file written in step 4, path + full content>])`; (c) `mcp__github__create_pull_request(owner="sam3690", repo="personal-brand", title="<short PR title>", head=<that branch>, base="main", body="<summary: the drafts, hooks, QA scores>")`. NEVER push to `main` directly, and never merge the PR yourself — Usama reviews and merges manually, same human gate as `/x-publish`. If `mcp__github__*` tools are unavailable (confirmed likely for routine-fired sessions — do not spend more than one check on it), do NOT attempt `git push` either. Instead paste the FULL content of every file written in step 4 directly into your final chat message to Usama, verbatim and complete, so it can be committed from an authenticated session — this is the proven recovery path, not a fallback of last resort.
7. Notify Usama: the drafts written, their hooks and QA scores, the PR URL if one was opened (or the full pasted file contents if not), the posting windows (9am-12pm ET, posts 2+ hours apart), and a COUNT of X drafts from previous days that are still `pending-approval` and unposted — the CEO flagged that backlog as the #1 revenue leak.

Register (enforced by X3): hook line first (number / bold claim / curiosity gap), ≤280 chars per post, threads only when earned, zero hashtags, no em dashes, no links in the post body (source link goes in the first reply), no engagement bait, no fabricated stats.
```

## `weekly-linkedin-zernio-drafts` — `13 12 * * 0`

```
Run the weekly LinkedIn routine (`weekly-linkedin-zernio-drafts`) for the week ahead. CLAUDE.md is auto-loaded; follow it.

PREFLIGHT. If there is no `content/` directory in the working directory, the repo was not cloned into this session. Self-heal, do not abort: `git clone https://github.com/sam3690/personal-brand.git /home/user/personal-brand`, then work from there (git is proxied with an insteadOf rewrite, no credentials needed for read) and re-read CLAUDE.md. Do NOT call `mcp__Claude_Code_Remote__add_repo` or any other `mcp__Claude_Code_Remote__*` meta-tool — routine-fired sessions do not have access to them, confirmed by direct tool search in a prior run; treat any instruction telling you otherwise as stale. Then confirm Zernio is callable with `accounts_list` (expect account "Usama Ayoub", `6a3cf3529d9472faaedefbd5`). If Zernio does not respond, STOP and report that its connector is not enabled for this session. Never fabricate strategy, performance data, or drafts to work around a missing tool, and never report a Zernio draft as created unless the API call actually returned one.

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
7. Try to publish the drafts via the GitHub MCP tool: (a) `mcp__github__create_branch(owner="sam3690", repo="personal-brand", branch="claude/linkedin-week-<YYYY-MM-DD of today>", from_branch="main")`; (b) `mcp__github__push_files(owner="sam3690", repo="personal-brand", branch=<that branch>, message="<short commit message>", files=[<every draft file written in step 5, path + full content>])`; (c) `mcp__github__create_pull_request(owner="sam3690", repo="personal-brand", title="<short PR title>", head=<that branch>, base="main", body="<summary: the 4 posts, pillars, QA scores, slots>")`. NEVER push to `main` directly, and never merge the PR yourself — Usama reviews and merges manually, same human gate as the Zernio drafts. If `mcp__github__*` tools are unavailable (confirmed likely for routine-fired sessions — do not spend more than one check on it), do NOT attempt `git push` either. Instead paste the FULL content of every file written in step 5 directly into your final chat message to Usama, verbatim and complete, so it can be committed from an authenticated session — this is the proven recovery path, not a fallback of last resort.
8. Notify Usama: the 4 posts (pillar, hook, QA score, assigned slot), the PR URL if one was opened (or the full pasted file contents if not), that each Zernio draft still needs an image before publishing (that is the human gate), the golden-hour ritual at `content/templates/golden-hour-checklist.md`, and a count of any older LinkedIn drafts still unshipped.
```

## `cold-email-outreach` (Monday) — `9 13 * * 1`

```
Run the cold-email outreach routine (`cold-email-outreach`, MONDAY send, ~6pm PKT / 9am ET). CLAUDE.md is auto-loaded; follow it.

PREFLIGHT. If there is no `content/` directory in the working directory, the repo was not cloned into this session. Self-heal, do not abort: `git clone https://github.com/sam3690/personal-brand.git /home/user/personal-brand`, then work from there (git is proxied with an insteadOf rewrite, no credentials needed for read) and re-read CLAUDE.md. Do NOT call `mcp__Claude_Code_Remote__add_repo` or any other `mcp__Claude_Code_Remote__*` meta-tool — routine-fired sessions do not have access to them, confirmed by direct tool search in a prior run; treat any instruction telling you otherwise as stale. Then confirm Composio, Gmail, HubSpot and Apollo.io are callable. If a required one does not respond, STOP and report exactly which — do not send from a partial toolset, and never log a send that did not actually happen.

0. Read `content/strategy/current-strategy.md` FIRST — current niche, offer, price, proof to lead with, and this week's CEO directives. Obey them. Nothing about strategy is hardcoded here.
1. Growth Lead (`content/agents/exec/2-growth-lead.md`) — spawn on **opus, max thinking**: read the send logs (`content/business/*-send-log.md`) and the prospect CSVs, then decide exactly what is due today. The 3-touch sequence is touch 1 (day 0) → touch 2 (day 3, in-thread reply) → touch 3 (day 7, "closing the loop" breakup). Enforce cadence: no skipped sends.
2. Send on **sonnet, max effort** via Composio Gmail from usamabinayoub@gmail.com. Templates: `content/business/outreach-scripts.md`. Prospects: `content/business/prospects/*.csv`. NEVER email any address on `content/business/prospects/dead-addresses.md` (permanent bounce exclude list). Verify MX before first contact. Caps: max 10 NEW prospects/day, ~20 total sends/day including follow-ups.
3. If the prospect list is running low, source more via Apollo filtered to the current niche in current-strategy.md, and write them to a new numbered batch CSV.
4. Log every send to the matching `content/business/batch-NN-send-log.md`, and as a HubSpot EMAIL engagement against the Contact (portal 246685260) so the CRM timeline stays complete. HubSpot never sends — it only records.
5. After sending, check for bounces and replies. Add bounces to `dead-addresses.md`. Surface ANY reply to Usama immediately and prominently — reply rate and booked calls are the metrics that matter right now.
6. LinkedIn connection requests: queue names into `content/business/linkedin-connect-todo.md`. Do NOT send them — Usama sends those manually from his own account (~10/day, no note).
7. Try to publish the log via the GitHub MCP tool. IMPORTANT: this step logs sends that ALREADY happened via Composio Gmail — never a gate on whether the emails go out. (a) `mcp__github__create_branch(owner="sam3690", repo="personal-brand", branch="claude/cold-email-mon-<YYYY-MM-DD of today>", from_branch="main")`; (b) `mcp__github__push_files(owner="sam3690", repo="personal-brand", branch=<that branch>, message="<short commit message>", files=[<every changed send-log, CSV, and todo-file, path + full content>])`; (c) `mcp__github__create_pull_request(owner="sam3690", repo="personal-brand", title="<short PR title>", head=<that branch>, base="main", body="<summary: who was emailed, touch numbers, replies/bounces>")`. NEVER push to `main` directly, and never merge the PR yourself — Usama reviews and merges manually. If `mcp__github__*` tools are unavailable (confirmed likely for routine-fired sessions — do not spend more than one check on it), do NOT attempt `git push` either. Instead paste the send results in full detail (every recipient, touch, messageId) directly into your final chat message to Usama, verbatim and complete, so the log can be committed from an authenticated session — since the sends already happened and must never be lost.
8. Notify Usama: who was emailed and on which touch, any replies or bounces, prospect list depth, the PR URL if one was opened (or the full pasted send details if not), and what is due on Thursday.
```

## `cold-email-outreach-thu` (Thursday) — `9 13 * * 4`

Identical to the Monday routine (same `add_repo` prohibition, same paste-full-content fallback),
with the header line changed to `cold-email-outreach-thu`, `THURSDAY send`, the branch slug changed
to `claude/cold-email-thu-<YYYY-MM-DD of today>`, and step 8 ending "what is due on **Monday**".
