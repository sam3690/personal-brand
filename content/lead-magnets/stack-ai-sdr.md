# Lead Magnet — "STACK": The $50/mo AI SDR Stack

> Delivered when someone comments **STACK** (or DMs you). This is the actual asset — paste it as a
> DM, a Google Doc link, or a carousel. Keep it tight and real. Update prices as they change.

**One-line promise:** The exact tools, costs, and wiring to run an autonomous AI sales rep for under
$50/month — the same architecture I use for clients instead of $1,500–$2,000/mo tools.

---

## The stack (under $50/mo)

| Layer | Tool | Cost/mo | Job |
|---|---|---|---|
| Workflow engine | **n8n** (self-hosted on a $5 Hetzner VPS) | ~$5 | Orchestrates everything. Unlimited runs. |
| Brain | **LLM API** (Claude / GPT) | ~$20 | Drafts personalized outreach, classifies replies. |
| Sending | **3 warmed mailboxes** (Instantly) | ~$15 | Deliverability without burning your main domain. |
| Leads + enrichment | **Apollo / Clay** (free–starter tier) | $0–10 | Pulls + enriches the lead list. |
| **Total** | | **~$45–50** | vs Artisan ($1.5–2k) / 11x ($1.5k) |

## How it's wired (the pipeline)
1. **Ingest** leads from Apollo/Clay → 2. **Enrich** with company context →
3. **Draft** a personalized cold email with the LLM → 4. **Send** through a warmed inbox →
5. **Classify** replies (interested / objection / not now) → 6. **Hand off** hot leads to a human,
auto-book the call. Everything logged.

## Why it beats the $2k tools
- Self-hosting = unlimited runs, ~$0 marginal cost per lead after setup.
- n8n's AI Agent node has native tool-calling + persistent memory across executions.
- You own the logic, so you can fix it when a provider changes — not wait on a vendor.

## The catch (be honest — it builds trust)
The model is just the engine. The moat is the workflow design, lead-scoring logic, and reply
classification. A generic LLM dropped into sales scores *negative* on prospecting (GTM-Bench). The
$50 is the floor; the build quality is what makes it work.

---
**DM follow-up line:** "Want me to map this to your exact lead flow? Tell me your current stack and
I'll show you the 2–3 nodes that'd save you the most time."
