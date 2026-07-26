# Winning Post 02 — "Chatbot with a markup" (data-contrarian / authority)

- **Skeleton:** B (Data-backed contrarian) · **Pillar:** P2 Contrarian
- **Hook formula:** Contrarian / unpopular opinion · **Format:** Text (~1,650 chars)
- **CTA:** operator question + soft consultative first comment (no bait, no body link)
- **Slot:** Wed (today) 8:00–10:00 AM · **QA:** 96/100 PASS · projected engagement: HIGH (debate + saves)

---

## THE POST

Most "AI agents" agencies are selling right now are just a chatbot with a markup.

Here's how to tell the difference before you pay for one.

I've built over 500 workflows. The gap between a demo and a system that survives production is enormous, and it's exactly where most "AI agents" quietly fall apart.

A wrapper looks identical to a real agent for about five minutes. Then a lead sends something weird, an API rate-limits, and it confidently does the wrong thing.

Here's what actually separates the two.

A chatbot with a markup:
→ One prompt, one model, no memory.
→ Sends whatever it generates. No confidence check.
→ Breaks silently the first time an API returns a 429.
→ Looks great in the demo, costs you a real client in week one.

A real agent:
→ Classifies the input before it acts: buyer, supplier, or noise.
→ Holds memory across the conversation, not just the last message.
→ Routes low-confidence outputs to a human instead of guessing.
→ Retries on failure. Logs every decision. Fails loud, not silent.

The benchmark backs this up. In the largest sales-AI test run so far (GTM-Bench), four of six general agents scored negative. The purpose-built one scored +26,615. The model was barely the difference. The system around it was.

Same lesson I learned building backend for healthcare years ago: nobody claps for the guardrail. But the guardrail is the product.

So if you're buying an AI agent, ask one question: what happens when it's not sure?

If the seller doesn't have a clean answer, you're buying a chatbot with a markup.

What's the worst demo-to-production gap you've seen on an "AI agent"?

---

## FIRST COMMENT (post right after — adds detail, invites the technical thread)
That "what happens when it's not sure?" check is usually one node: a confidence gate that routes to a human instead of auto-sending. Least glamorous part of the build, the one that saves the client relationship. Happy to break down how I wire it if that's the useful bit.

## QA — Agent 5 (upgraded): 96/100 → PASS, no red flags
Hook 17 · Show-the-work 16 · Comment-trigger 15 · Save-worthy 10 · Pillar/authority 12 · Dwell 9 ·
Format fit 8 · Hashtags 4 · Voice 5. Projected HIGH: the wrapper-vs-agent checklist is save-bait,
the claim drives debate (comments = top signal), the "ask one question" line is quotable, and the
close pulls operator war stories. Reliability angle ties to the healthcare/Axios wedge.

## HOW TO POST
Today (Wed) 8:00–10:00 AM. No hashtags, no body link. Don't edit for 60 min. Post the first comment
right after. Reply to every comment in the first 90 min — this one is built to start arguments (the
good kind), so be there to feed the thread.

## IMAGE (optional)
A simple two-column compare graphic: "Chatbot with a markup" (red ✗ list) vs "Real agent" (emerald ✓
list), brand colours from `../../brandkit.html`. Clean, legible, no clutter.
