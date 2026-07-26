# Usama's LinkedIn Content Engine

A managed-agent system that writes LinkedIn posts engineered for the **2026 algorithm** — built to
grow a cold, ~9-week-old account (271 followers) into an audience of founders and agency owners who
become clients.

## Why your posts weren't landing (the diagnosis)
See `knowledge-base/profile-audit.md`. Short version: off-topic reposts + certificate humblebrags
told the algorithm you're not an AI-automation expert, so your real posts (0–6 reactions) got
throttled to the wrong audience — on a seed audience already tiny from a new account. This system
fixes all of it.

## Do this FIRST (30 min, multiplies everything)
1. `knowledge-base/profile-audit.md` → add Featured section, turn on Services, stop the reposts/badges.
2. Read `knowledge-base/linkedin-algorithm-2026.md` once. It's the rulebook.

## How the engine works (5 managed agents, chained)
```
/linkedin-post "<optional topic>"
        │
        ▼
1. Topic & Keyword Strategist  → picks pillar + angle (+ trend check) + SEO keywords   [agents/1]
2. Hook Writer                 → 3 hooks via the 6 formulas, picks the winner          [agents/2]
3. Post Writer                 → full body in Usama's voice, chosen format             [agents/3]
4. CTA Writer                  → comment-magnet or follow CTA + first comment          [agents/4]
5. Algorithm QA & Scorer       → scores /100, blocks <80 or any red flag, returns fixes [agents/5]
        │
        ▼
   Scored draft saved to  drafts/  → you run the golden-hour checklist → publish
```

## Run it
- **In Claude Code:** `/linkedin-post` (optionally with a topic). It executes all 5 agents and writes
  a finished, scored draft into `drafts/`.
- **Manually:** open `agents/1`…`agents/5` in order and follow each. Same result, slower.

## Cadence
4 posts/week (Tue/Wed/Thu Tier-1 windows + one wildcard). Weekly mix and pillars in
`knowledge-base/brand-profile.md`. Posting ritual in `templates/golden-hour-checklist.md`.
**Consistency is the lever** — a missed week costs 20–40% reach.

## File map
```
content/
├─ README.md                      ← you are here
├─ knowledge-base/
│  ├─ linkedin-algorithm-2026.md  ← the rulebook (4-phase model, signals, timing, hooks)
│  ├─ brand-profile.md            ← voice, ICP, offer, 4 content pillars
│  └─ profile-audit.md            ← diagnosis + exact profile fixes (do first)
├─ agents/                        ← the 5 managed agents (the pipeline)
├─ templates/                     ← post-format skeletons + golden-hour checklist
├─ lead-magnets/                  ← real assets your comment-keywords deliver (STACK, PLAYBOOK)
└─ drafts/week-01/                ← 4 ready-to-post, scored drafts
```

## Reuse
Topic bank: `../ai-sales-automation-content-angles.md` (100 angles). Carousel/brand assets:
`../carousels/`, `../brandkit.html`. n8n auto-posting (later): `../PLAN.md`.

## ⚡ Winning patterns (added after web research)
- `knowledge-base/winning-post-patterns.md` — the **100+ engagement swipe file**: 6 winning hooks,
  format→engagement table (carousel ~4x text), 5 body skeletons (case-study, data-contrarian,
  build-in-public carousel, 5-lessons, soft showcase), AI-automation rules. **Agents 2/3/5 write to
  it by default.** Brain note: `brain/Winning Post Patterns.md`.
- `drafts/winning/` — posts in the winning result-first / build-in-public style (the default now).
- `drafts/payslip-posts/` — recognition / no-CTA posts (the exception, via the the-payslip-post skill).

- `agents/0-research-scout.md` + `research/` — the Research Scout (agent 0) that scouts trending + winning posts each week and feeds the Strategist. Wired into the Sunday routine.

## 🎨 Brand design system (Green Room kit)
- `knowledge-base/brand-design-system.md` — full visual spec (colors, type, components, slide
  anatomy) for carousels, banners, CTA/featured-post images. Synced from Usama's Claude Design
  project. Brain note: `brain/Brand Design System.md`.
- `../carousels/green-room/` — the actual renderable `.dc.html` decks + runtime, including this
  week's finished carousel (`carousel-multichannel-outbound.dc.html`). See that folder's README
  for the render pipeline and one open manual step (two image assets need manual download).

## 🐦 X.com engine (daily, generic trending AI topics)
- `agents/x/` — the X team: `x0-trend-scout → x1-post-writer → x2-media-brief → x3-qa`.
- `agents/6-performance-analyst.md` — the monitoring loop (daily X via Apify, Sunday LinkedIn via Zernio); learnings land in `performance/`.
- `knowledge-base/x-playbook.md` — X register, formats, timing, Canva template link.
- Run: `/x-post` (drafts to `drafts/x/<date>/`) → add media → `/x-publish` (Composio, human-confirmed).
- Automated: scheduled task `daily-x-trending-posts` runs the whole loop every day ~1pm PKT.
