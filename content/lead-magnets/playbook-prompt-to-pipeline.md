# Lead Magnet — "PLAYBOOK": Prompt → Pipeline (lead qualification in under 60 seconds)

> Delivered when someone comments **PLAYBOOK** (or DMs you). The real framework for turning a manual
> lead workflow into an automated qualify-score-route pipeline. No coding background needed.

**One-line promise:** Go from a single prompt to a fully automated lead-qualification pipeline in
6–8 weeks — response time from days to under 60 seconds, cost per lead from ~$180 to ~$65.

---

## The 5 steps

**1. Map your current lead workflow.**
Write down every step from "lead arrives" to "call booked." Most teams have 6–9 manual steps and
lose hours between them. You can't automate what you haven't mapped.

**2. Tag which steps AI can own.**
Mark each step: AI-owns / human-owns / hybrid. AI owns: research, enrichment, drafting, scoring,
routing. Humans own: the actual call, judgment calls, edge cases.

**3. The qualify → score → route prompt structure.**
- **Qualify:** does this lead match the ICP? (firmographics + intent signals)
- **Score:** 0–100 on fit + urgency, with a reason string (never a bare number).
- **Route:** ≥ threshold → book/notify a human; below → nurture sequence.

**4. Set safeguards so nothing breaks in production.**
Retry on API failure (exponential backoff). A human-review gate for low-confidence scores. Log every
decision. This is the difference between a demo and a system you bet your pipeline on.

**5. Measure real numbers.**
Track: response time, qualified-leads/month, cost per lead, and ROI. Targets seen in the field:
3x qualified leads/month, response 3 days → <60 sec, CPL $180 → $65.

---

## Build timeline
Week 1–2: map + tag. Week 3–5: build qualify/score/route in n8n. Week 6–8: safeguards, testing,
go live. Most of the risk is in step 4 — skip the safeguards and it breaks the first time an API
rate-limits you.

---
**DM follow-up line:** "Send me your current lead flow and I'll mark exactly which 3 steps to
automate first for the fastest ROI."
