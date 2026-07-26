# Winning Post 01 — "28 leads/month recovered" (case-study / build-in-public)

- **Skeleton:** A (Case study, result-first) · **Pillar:** P1 build-in-public / P3 ROI
- **Hook formula:** Specific-number / result · **Format:** Text case study (~1,450 chars)
- **CTA:** genuine operator question + soft consultative first comment (no bait, no body link)
- **QA:** 95/100 PASS · projected engagement: HIGH (save-worthy build + comment-driving question)

---

## THE POST

A client was quietly losing 28 leads a month in their own WhatsApp.

I built a 6-node n8n agent that answers every one of them in under 60 seconds.

Here's the situation I walked into.

A 2-person agency. Genuinely good at the work. Leads coming in steady, mostly through WhatsApp and a GoHighLevel form.

But a normal month looked like this: ~50 enquiries in, ~22 ever got a reply. The other 28 just sat there. Seen, no answer, because both founders were in client calls all day.

By the time they replied, the lead had already booked with whoever answered first.

So we didn't touch their lead gen. We fixed the follow-up.

The build (6 nodes in n8n):

1. Trigger — a new WhatsApp message or GHL form hits a webhook.
2. Classify — an LLM node reads it: buyer, supplier, or noise?
3. Enrich — pull the contact and any past history from GHL.
4. Draft — write a reply in the founder's own voice, with the next step (a booking link).
5. Guardrail — anything low-confidence gets held for a human instead of auto-sent.
6. Log + notify — write it back to GHL and ping the founder in Slack.

Response time went from ~6 hours to under 60 seconds.

Month one: 28 previously-dead leads got a real reply. 4 of them closed.

The lesson isn't "AI replaces your team."

It's that most agencies don't have a lead problem. They have a "nobody answered in time" problem. And that one is cheap to fix.

The hardest node wasn't the AI. It was node 5, the guardrail. An agent that confidently sends the wrong thing to a real buyer is worse than no agent at all.

What's the one part of your follow-up you still wouldn't hand to an agent yet?

---

## FIRST COMMENT (post right after — adds cost detail + invites the technical thread)
Cost to run this for them: ~$50/month all in (n8n on a $5 VPS, an LLM key, the rest they already had). Happy to go node-by-node on the guardrail logic if that's the useful part. It's the bit everyone skips.

## QA — Agent 5 (upgraded scorecard): 95/100 → PASS, no red flags
Hook 17 · Show-the-work 16 · Comment-trigger 15 · Save-worthy 9 · Pillar/authority 12 · Dwell 9 ·
Format fit 8 · Hashtags 4 · Voice 5. Projected engagement HIGH: the 6-node breakdown is save-bait
(good kind), the build invites "how did you do that?" comments, the closing question is answerable
from experience. Client is the hero; reliability angle (node 5) ties to Usama's wedge.

## CAROUSEL VARIANT (optional, ~4x engagement)
Same content as 8 slides: 1 cover ("28 leads/month, recovered") · 2 the problem (50→22→28) ·
3–8 one node per slide · 1 result + "save this / what would you never hand to AI?". Build from
`../../carousels/` + `../../brandkit.html`.

## HOW TO POST
Tue/Wed/Thu 7:30–10:00 AM. No hashtags, no body link. Don't edit for 60 min. Reply to every comment
in the first 90 min (the question is built to pull operator replies — that's your reach engine).
