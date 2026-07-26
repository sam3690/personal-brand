# Post 1 — "Your LLM is not a sales agent" (Contrarian)

- **Skeleton:** B (Data-backed contrarian) · **Pillar:** P2 Contrarian
- **Hook formula:** Contrarian claim · **Format:** Text (~1,450 chars)
- **CTA:** genuine operator question + follow/conversation (no magnet forced)
- **SEO keywords (woven in):** AI sales agent, lead qualification, n8n, lead scoring, sales pipeline
- **Slot:** Monday 9:00–11:00 AM (wildcard)
- **Sources:** cost-per-qualified-opportunity and ramp-time stats from `../../research/week-of-2026-07-06.md`
  (Digital Applied AI SDR Statistics 2026 / State of AI SDR Industry 2026 report)
- **QA (self-scored against Agent 5 rubric):** 91/100 PASS · red flags: none
  - Hook 17/18 (claim in line 1, contrarian formula) · Specificity 15/16 (real sourced stat + named tool)
  - Comment-trigger 15/16 (specific experience question) · Save-worthiness 8/10 · Pillar fit 12/12
  - Dwell 9/10 · Format fit 8/8 · Hashtags 4/4 (zero) · Voice 6/6 (no em dash, no banned phrases)
  - Projected engagement: HIGH (fresh 2026 data + contrarian claim + concrete 3-step framework)

---

Your LLM is not a sales agent. It's a very fast intern with no memory of yesterday's conversation.

New industry data backs this up: cost per qualified opportunity is about $487 in human-only sales pods vs about $224 in hybrid AI+human pods. A real 54% drop. But fully autonomous AI SDRs still haven't replaced human sales teams at any meaningful scale. Companies keep reverting to hybrid.

I've built 500+ AI workflows for founders and agencies, and the pattern is always the same. The workflows that actually save money have three things wrapped around the model that the model itself doesn't have:

1. A qualify step (does this lead match the ICP, yes or no)
2. A score step (0 to 100, with a reason, never a bare number)
3. A route step (above threshold, a human books the call, below, it goes to nurture)

I wire all three in n8n. Strip them out and what's left is a chatbot with excellent grammar. It'll happily chat with a lead for 20 minutes and never once ask about budget.

The model is the engine. Qualify, score, route is the car. That data above is basically the whole industry finding this out the hard way.

What's the one "AI agent" pitch you've seen that was really just a chatbot with a system prompt?

---

**FIRST COMMENT (post 10-15 min after publishing):**
"The full breakdown of that 3-step wiring (qualify, score, route) is basically a mini playbook. Happy to share the exact prompt structure if anyone wants it, just ask below."
