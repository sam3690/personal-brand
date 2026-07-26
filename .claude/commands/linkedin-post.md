---
description: Generate 2026-algorithm-optimized LinkedIn post(s) via the managed agent team
argument-hint: [optional topic/pillar, or "week" for a full week]
---

You are running Usama's LinkedIn Content Engine. Produce finished, scored, ready-to-post draft(s).

Topic seed (optional): $ARGUMENTS

## Load context (read first)
- content/knowledge-base/brand-profile.md, linkedin-algorithm-2026.md, winning-post-patterns.md
- content/templates/post-formats.md
- content/lead-magnets/ (which comment-keywords have real assets)
- ai-sales-automation-content-angles.md (100-angle reuse bank)
- content/research/ (latest weekly research brief, if present)

## Run the agent team in order
0. content/agents/0-research-scout.md — scout trending topics + currently-winning LinkedIn posts in the niche (100+ engagement); write/refresh the weekly brief in content/research/. Skip only if a fresh brief (under 7 days old) already exists.
1. content/agents/1-topic-keyword-strategist.md — using the brief, pick pillar + angle + SEO keywords.
2. content/agents/2-hook-writer.md — 3 hooks, pick the winner.
3. content/agents/3-post-writer.md — full body in the chosen format.
4. content/agents/4-cta-writer.md — CTA (comment-magnet only if the keyword maps to a real magnet file, else follow/conversation) + first comment.
5. content/agents/5-algorithm-qa.md — score /100; if <80 or any red flag, fix and re-score until PASS.

## Output
Write finished draft(s) to content/drafts/<folder>/<n>-<slug>.md (same structure as content/drafts/winning/). Show the post body and QA score in chat.

Keep Ponytail discipline: specific over generic, <=3 hashtags, no links in body, no engagement bait.
