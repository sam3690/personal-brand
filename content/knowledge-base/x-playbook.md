# X.com Playbook — Usama Ayoub

Goal: grow a new X audience fast by riding daily trending AI topics (generic AI news is IN SCOPE,
unlike LinkedIn which stays on the 4 niche pillars). Voice stays Usama's: direct, specific, no fluff.

## Register
- Hook line carries the post. Number, bold claim, or curiosity gap in the first 8 words.
- ≤280 chars per post. Threads (2-5 posts) only when the story earns it.
- **No hashtags. No links in the post body** — source link goes in the first reply.
- **Every post's `first_reply` must be a real, specific link (Usama, 2026-08-11):** the news
  article for a news/story post, or the project's **GitHub repo or official site** for an
  open-source tool / release post. Never leave it blank or generic — this is the only citation
  the post carries and it doubles as the reader's next click.
- No em dashes ever. No fluff words. End with a take or a sharp question.
- **Media is optional, not required per post (Usama, 2026-08-11).** Skip the media brief/image
  when the post doesn't need one; don't hold a post back from posting for lack of an image.

## Formats that travel (2026)
1. **Builder/demo post (DEFAULT, per Usama 2026-07-07)**: build-something content — stunning AI/3D
   websites via Claude Code or Fable 5, agent teams, automated content pipelines, "how I built X"
   with the method shown. This is what trends on X and attracts the pro-AI buyer audience.
2. **Hot take** on today's AI story.
3. **Explainer thread**: "What actually happened + why it matters" in 3-5 posts.
4. **Number lead**: the one surprising stat from the story, then context.
5. **Operator angle**: the generic story + one line of "here's what this means if you build/sell".

**Audience rule (Usama, 2026-07-07):** target people who are EXCITED about AI, automation, and AI
agents (potential service buyers). Never lead with anti-AI backlash, doom, or compliance/regulation
angles. Every post should make the reader want to build or buy, not worry.

## Cadence & timing
2-3 posts/day, spaced 2+ hours apart. Best windows: 9am-12pm ET (6-9pm PKT) and 5-7pm ET.
Reply to comments in the first hour — replies are the strongest growth signal on X.

## Pipeline
`x0-trend-scout → x1-post-writer → x2-media-brief → x3-qa` (files in `../agents/x/`), then
Agent 6 (performance analyst) closes the loop daily. Drafts land in `content/drafts/x/<date>/`.

**Publishing (as of 2026-08-11):** Composio X writes are blocked (API credits depleted, see
`../performance/x-performance-log.md`). Usama approves each draft in-session, then Claude posts
it via the **Claude in Chrome extension** (his real, already-logged-in X session) — ad hoc, one
draft at a time, never a standing auto-post queue. Claude shows the exact composed post before
clicking Post; only an explicit per-draft yes triggers the publish. Do not batch-approve.

## Brand design system (replaces the earlier Canva-template plan)
LinkedIn/X post images use Usama's fixed visual system — not Canva, a Claude Design project:
"Brand system design for social media carousels" (the Green Room kit, v1.2).
Project link: https://claude.ai/design/p/5790bcce-f02c-4647-a1dd-9837aee8c75f
Full token spec: `../knowledge-base/brand-design-system.md`. Renderable decks synced locally:
`../../carousels/green-room/` (one deck built already — `carousel-multichannel-outbound.dc.html`).

## Performance memory
Writing agents read `../performance/x-performance-log.md` before every run. What the data says
beats what this playbook says.
