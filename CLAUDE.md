# CLAUDE.md — Usama's Content Engine (LinkedIn + X.com)

Personal-brand content system for **Usama Ayoub** (AI sales automation: n8n, AI SDRs,
GTM agents, CRM). Two engines, two goals:
- **LinkedIn** (niche, 4 pillars): grow a cold account into audience + clients.
- **X.com** (generic trending AI topics, NOT niche-locked): grow a broad AI audience fast.

This file is auto-loaded every session (including the scheduled routines' fresh sessions). Read the
linked files only as needed — do not re-derive what is already captured here.

## Start here (in order, only what the task needs)
0. `content/strategy/current-strategy.md` — the CEO-owned SINGLE SOURCE OF TRUTH: current niche, offer, price, positioning, this-week directives. Every routine reads this FIRST and obeys it. Never hardcode strategy into a routine; change it here. Maintained by the exec team in `content/agents/exec/` (CEO + Content Director + Growth Lead).
1. `content/README.md` — full map + how to run
2. `content/knowledge-base/brand-profile.md` — voice, ICP, offer, the 4 content pillars
3. `content/knowledge-base/winning-post-patterns.md` — the 100+ engagement swipe file (DEFAULT register)
4. `content/knowledge-base/linkedin-algorithm-2026.md` — the rulebook (phases, signals, timing, hooks)
5. `content/brain/` — Obsidian second brain (atomic concept notes, start at `LinkedIn Brain Index.md`)
6. `content/knowledge-base/brand-design-system.md` — the Green Room visual kit (colors, type,
   components) for carousels/banners/CTA images; renderable decks in `carousels/green-room/`

## The managed teams (run in order)
**Exec layer (decides + supervises, opus):** `content/agents/exec/` — **CEO** (`0-ceo.md`: owns niche/offer/price/positioning, weekly review, enforces no-skipped-weeks + no-blind-offers), **Content Director** (`1-content-director.md`: supervises + QA-grades the content teams below), **Growth Lead** (`2-growth-lead.md`: owns outbound funnel + cadence + pipeline). They read/write `content/strategy/current-strategy.md`. CFO is folded into the CEO's weekly review until there is real MRR. Model routing: deciders run **opus** (max thinking); the doer teams below run **sonnet** (max effort).

**LinkedIn:** `0 Research Scout → 1 Strategist → 2 Hook → 3 Post → 4 CTA → 5 QA` — files in `content/agents/`.
- Run it with **`/linkedin-post [topic]`** (add "week" for a full week).
- For recognition / no-CTA inbound posts, use the **`the-payslip-post`** skill instead ("run the payslip post"). That is the exception; the 6-agent winning register is the default.

**X.com:** `X0 Trend Scout → X1 Post Writer → X2 Media Brief → X3 QA` — files in `content/agents/x/`,
register in `content/knowledge-base/x-playbook.md`.
- Run it with **`/x-post [optional topic]`** → 2-3 drafts in `content/drafts/x/<date>/`.
- Publish approved drafts with **`/x-publish`** (Composio; confirms each post in-session first).

**Cold email (outbound):** 3-touch sequence (day 0 / day 3 / day 7) run out of `content/business/`,
templates in `outreach-scripts.md`, prospects in `prospects/*.csv`, permanent bounce exclude list in
`prospects/dead-addresses.md`. Sent via Composio Gmail, logged to `batch-NN-send-log.md` files.
Runs automatically twice a week (scheduled tasks `cold-email-outreach` Mon and `cold-email-outreach-thu`
Thu, both 6pm PKT / 9am ET): sends whatever's due (new batch touch 1, or touch 2/3 follow-ups),
sources more prospects via Apollo when the list runs low, verifies MX before first contact, checks
for bounces/replies after sending. LinkedIn connection requests stay manual (Usama's own account,
~10/day, no note) — the routine queues names into `linkedin-connect-todo.md` but never sends them.

**Both:** `Agent 6 Performance Analyst` (`content/agents/6-performance-analyst.md`) closes the loop:
daily for X (Apify scrapes public metrics — the X free API is write-only), Sunday for LinkedIn
(Zernio analytics). Learnings append to `content/performance/*.md`; writing agents read those logs
first — **what the data says beats the playbook**.

**Model routing:** pipeline/agentic work runs on **sonnet**; deep thinking (Agent 6 analysis,
complex strategy) runs on **opus** (spawn subagents with the model override).

## Hard rules (enforced by Agent 5 QA on LinkedIn, Agent X3 on X; pass = ≥80, zero red flags)
- **Voice (both platforms):** Usama's — direct, specific, no fluff. No "game-changer / revolutionary / unlock". Every line a claim or a proof. **No em dashes in any content.**
- **LinkedIn register:** lead with the result or claim, **show the work** (named tools + real numbers), end with a **genuine operator question**. ≤3 hashtags (default 0). Stay on the 4 pillars. Never post off-topic reposts or certificate/badge humblebrags (they suppress reach).
- **X register:** hook line first (number / bold claim / curiosity gap), ≤280 chars per post, threads only when earned, **zero hashtags**, generic trending AI topics are in scope.
- **Both:** no links in the post body (LinkedIn: first comment; X: first reply). No engagement bait. No fabricated stats — cite real sources.

## Publishing = Zernio, DRAFTS ONLY, human gate
LinkedIn is connected to Zernio as **"Usama Ayoub", accountId `6a3cf3529d9472faaedefbd5`**.
Create every post as a **draft** — never auto-publish.

**`posts_create_post` is NOT a directly-exposed MCP tool.** The Zernio server exposes a simplified
`posts_create` (single `platform` string, `schedule_minutes`, no `scheduled_for`/`timezone`) which
CANNOT express an absolute slot time. The full API tool is reachable only through the passthrough.
Exact call:
```
call_tool(
  name = "posts_create_post",
  arguments = {
    "is_draft": true,
    "content": <full post body incl. any CTA/P.S.>,
    "title": "<short label> [slot: <day> <time> - ADD IMAGE before publishing]",
    "scheduled_for": "<the slot's date+time as ISO with +05:00 offset>",
    "timezone": "Asia/Karachi",
    "platforms": [{"platform":"linkedin","accountId":"6a3cf3529d9472faaedefbd5"}]
  }
)   # no publish_now, no media_items
```
Verified 2026-07-27: `is_draft: true` **wins over** `scheduled_for` — the post comes back
`status: 'draft'` with the slot time stored but NOT armed to publish. The human gate holds.
Use `search_tools` to discover other full-API tools; `call_tool` executes them.
`scheduled_for` MUST be the intended posting slot, NEVER the routine's run time.
Slot times are US Eastern (audience US/EU). Convert to Karachi: 7:30am ET = 4:30pm PKT,
8am ET = 5pm PKT, 10am ET = 7pm PKT. Example: Tue 8am ET slot = "2026-07-07T17:00:00+05:00".
Usama adds the image and approves before it goes live. The image step is the human guardrail.

## X.com publishing = Composio, disk drafts, human gate
X is connected via **Composio** (free tier: 500 posts/month, write-only API — metrics come from
Apify scraping, never the API). Flow: daily routine writes drafts to `content/drafts/x/<YYYY-MM-DD>/`
with frontmatter (`status: pending-approval`, `media: []`, `first_reply`, `qa_score`) → Usama
reviews, drops media path(s) into `media:` → runs **`/x-publish`**, which confirms each post
in-session, then posts via COMPOSIO_SEARCH_TOOLS + COMPOSIO_MULTI_EXECUTE_TOOL (thread parts are
dependent calls: post in reply-chain order, never parallel; source link goes as a reply).
**Never publish a draft Usama has not confirmed in-session. Agents never attach or generate media.**

## Preflight (every scheduled routine, before step 0)
Routines run in **fresh sessions**. Two things have failed there before; check both first.

1. **Repo present?** If there is no `content/` directory in the working directory, the repo was not
   cloned into this session. Self-heal, do not abort:
   ```
   git clone https://github.com/sam3690/personal-brand.git /home/user/personal-brand
   cd /home/user/personal-brand
   ```
   Git is proxied with an `insteadOf` rewrite, so the https URL works with no credentials. Re-read
   this file after cloning.
2. **Connectors callable?** A connector can be connected org-wide yet still be off for the fired
   session (`enabledInChat: false`). Confirm the ones this routine needs respond before doing the
   work: Zernio → `accounts_list`, Composio → `COMPOSIO_SEARCH_TOOLS`. Check `ListConnectors` if a
   call fails.

If a required connector is genuinely unavailable, **stop and say so precisely**. Never fabricate
strategy, performance data, or drafts to paper over a missing tool, and never report a draft as
created when no API call succeeded.

## The routines (the agentic loops)
Exact schedules + the full prompt of every routine: **`content/ROUTINES.md`** (the recovery file —
routines live server-side on claude.ai, so recreate them from there after any machine/OS reset).
- **`daily-x-trending-posts`** — every day ~1pm PKT: Agent 6 reviews yesterday's X metrics (opus) →
  X0 scouts today's trending AI topics → X1/X2/X3 write, brief, QA 2-3 posts → drafts + notify.
  Posting windows: 9am-12pm ET, posts spaced 2+ hours.
- **`weekly-linkedin-zernio-drafts`** — Sunday ~5pm PKT: Agent 6 reviews last week via Zernio
  analytics (opus) → research → 4 posts → Zernio drafts + a `# Media brief` section at the end of
  EACH draft markdown file (same format as the X drafts: Type · Concept · Text on image · Alt text ·
  Fallback; Canva template link in `x-playbook.md`; carousel posts get slide-by-slide direction) →
  notify. Best slots: Tue 7:30-9am, Wed 8-10am, Thu 7:30-9am ET, + one wildcard
  Mon 9-11am or Fri before 9am. Golden-hour ritual after posting: `content/templates/golden-hour-checklist.md`.

## Efficiency notes (keep runs cheap + smooth)
- **Reuse before inventing:** pull angles from the latest brief in `content/research/`, then
  `ai-sales-automation-content-angles.md` (100 angles). Reuse brand assets in `carousels/` + `brandkit.html`.
- **Skip redundant research:** if a fresh brief (< 7 days) already exists in `content/research/`, use it; do not re-scout.
- **Save drafts** to `content/drafts/<folder>/` in the same structure as existing drafts (X posts: `content/drafts/x/<YYYY-MM-DD>/`).
- **Check the performance logs** (`content/performance/`) before writing; they are small and they are the improvement loop.
- **Keep sessions short and scoped.** The engine + brain live on disk; a fresh session + one command
  is enough. Do not reload research already captured in `knowledge-base/`.
- **Batch file writes** in one command when creating several files (a GateGuard hook prompts per new file).
