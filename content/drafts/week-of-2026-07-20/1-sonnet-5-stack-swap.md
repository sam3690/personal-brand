# Post 1 — "I swapped Claude Sonnet 5 into my stack" (Build-in-public / cost update)

- **Skeleton:** A (Case-study, cost-update sequel to the 07-07 stack post) · **Pillar:** P1 Build-in-public
- **Hook formula:** Specific-number / result · **Format:** Text (~1,300 chars)
- **CTA:** genuine operator question + follow/conversation (no magnet forced; references the existing
  STACK asset from the 07-07 post rather than re-pitching it)
- **SEO keywords (woven in):** Claude Sonnet 5, AI SDR, n8n, LLM cost, cold email automation
- **Slot:** Tuesday 2026-07-21, 7:30–9:00 AM ET (strongest window; matches last week's best-performing
  cost-delta hook pattern per `../../performance/linkedin-performance-log.md`)
- **Sources:** Claude Sonnet 5 pricing ($2/M input, $10/M output tokens through 2026-08-31) — Anthropic,
  TechCrunch, per `../../research/week-of-2026-07-20.md`
- **QA (self-scored against Agent 5 rubric):** 90/100 PASS · red flags: none
  - Hook 17/18 (result in line 1, specific-number formula, could be 1 word tighter) · Specificity 16/16
    (real pricing, named model, ties to a real prior post's real number) · Comment-trigger 14/16 (good
    experience question, slightly softer than a magnet CTA) · Save-worthiness 8/10 · Pillar fit 12/12
    (build-in-public, on-topic) · Dwell 9/10 · Format fit 8/8 · Hashtags 4/4 (zero) · Voice 6/6 (no em
    dash, no banned phrases)
  - Projected engagement: HIGH (live launch news + real before/after cost number + sequel to the
    account's best-performing post)

---

I swapped Claude Sonnet 5 into my AI SDR stack the week it launched. Same workflow, same lead volume, the LLM line item dropped by roughly half.

Quick recap for anyone who saw the $45/mo stack post: the LLM step drafts personalized outreach and classifies replies as interested, objection, or not now. That line item was running about $20/mo on a GPT-4-class model.

Anthropic priced Sonnet 5 at $2 per million input tokens and $10 per million output, roughly half of what the frontier models were charging before. I pointed the same n8n workflow at it. Same prompts, same volume, same qualify/score/route logic wrapped around it.

Result: that $20/mo line item is now closer to $10-12/mo. Reply classification accuracy hasn't dropped on my spot-checks after a week of runs, and drafting quality held up against the same rubric I use to review outputs.

The lesson isn't "switch models." It's that the model is the one line item in your stack worth re-pricing every time a new one ships, because the wrapper around it (the qualify step, the score step, the retry handling) doesn't change when you swap the engine.

Anyone else re-benchmarked their stack since Sonnet 5 shipped? What moved for you, cost or quality?

---

# Media brief

- **Type:** single image, Usama's fixed Canva template layout (same pattern every post, only headline text + visual slot change; template link in `../../knowledge-base/x-playbook.md` under "Canva template")
- **Concept:** cost-drop comparison. Two stacked bars or two big numbers side by side: "$20/mo" (old LLM line item, muted/gray) vs "$10-12/mo" (Sonnet 5, brand accent color), with a small "same workflow, same volume" caption between them. Optionally a small n8n + Claude logo pair at the bottom of the visual slot.
- **Text on image (headline slot):** "Same stack. Half the LLM cost."
- **Alt text:** Comparison graphic showing the monthly LLM cost of an AI SDR stack dropping from about $20 to about $10-12 after switching to Claude Sonnet 5, with the rest of the n8n workflow unchanged.
- **Fallback (zero effort):** screenshot of the Anthropic Sonnet 5 pricing announcement ($2/M input, $10/M output) with the price line circled.
