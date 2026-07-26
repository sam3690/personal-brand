# Post 6 — "How to answer every lead in under 60 seconds (the n8n build, 5 steps)" (TEACH / Playbook)

- **Skeleton:** Teach / Playbook (the new first-class P3 format — "how to automate X, step by step")
- **Pillar:** P3 ROI systems / P1 build-in-public · **Format:** Text (~1,450 chars)
- **Hook formula:** relatable enemy → result → numbered teaser (Welsh trailer) + humbling real number (Saraev)
- **Why this angle:** the format Usama admires ("how to actually use/automate X"), currently underused. Teaches
  automation #1 from the 5-boring-automations carousel, so the two posts reinforce each other. Cloned skeleton:
  Nate Herk step-by-step (no skipped steps) + Welsh Trailer/Body/CTA. See `knowledge-base/winning-post-patterns.md`.
- **CTA:** genuine operator question (first-response-time confession) + follow. First comment offers the build.
- **Hook-Payoff check:** "5 steps" promises 5 ordered build steps → body delivers exactly 5 ordered build
  steps of ONE process (correct shape for a "how to build" hook). PASS.
- **Offer legibility:** the close states in plain words what this is ("the one that answers leads in 60 seconds
  so you stop losing deals to whoever replied first"). A non-technical founder gets it. PASS.
- **Slot:** next wildcard (Mon 9-11am or Fri before 9am ET). Reusable teach-format template.
- **NOTE ON NUMBERS:** "3 hours" first-response and any figure must be Usama's real number. Swap or cut. No invention.
- **QA (self-scored, new rubric incl. hard gates):** 92/100 PASS · gates: Hook-Payoff PASS · Offer-legibility
  PASS · Teach-delivers PASS · red flags: none. Hook 17 · Specificity 15 · Comment-trigger 15 · Save 10 (numbered
  build) · Pillar 12 · Dwell 9 · Format 8 · Hashtags 4 · Voice 6.

---

A lead fills out your form at 9pm. By the time you reply at 9am, they've already booked with someone who answered in 5 minutes.

That gap is the most expensive thing in your funnel, and it's the easiest one to close.

Here's the exact n8n build I use to answer every new lead in under 60 seconds, day or night. 5 steps, and you can ship the first version this week:

1. Catch the lead the second it lands.
A webhook node fires the moment someone submits (your site form, Typeform, a Meta lead ad). No polling, no 15-minute delay. This is the trigger everything else hangs off.

2. Enrich before you write a word.
Push the email through Clay or Apollo to pull name, company, role, and one specific detail. A reply that references their actual world books the call. A generic "Hi there" gets ignored.

3. Draft the reply with Claude, not a canned template.
Feed the enriched data in with one instruction: sound like a human who read their form, answer their real question, and offer two specific call times. One short paragraph. No pitch.

4. Send from a warmed inbox, then stop the moment they reply.
Fire it through the lead's own channel (email or WhatsApp). The second they respond anywhere, the sequence cancels itself. Nobody gets a "just following up" after they already answered.

5. Build the failure state before you go live.
This is what separates a demo from a system. Enrichment fails? Send a solid generic version, not silence. Send fails? Retry with backoff, then flag a human. A lead should never drop into a silent hole.

Ship steps 1 to 4 this week. Step 5 is what makes it safe to leave running while you sleep.

This is automation #1 of the five businesses actually pay for: the one that answers leads in 60 seconds so you stop losing deals to whoever replied first.

What's your honest average first-response time right now? Mine was 3 hours before I built this.

---

**FIRST COMMENT (post 10-15 min after publishing):**

Want the actual n8n canvas for this (the 5 nodes plus the stop-condition)? Comment BUILD and I'll send the walkthrough.

---

# Media brief

- **Type:** single image OR short 5-slide carousel. If carousel: render as 5 SEQUENTIAL numbered steps with
  connecting arrows (this IS a process, so a pipeline layout is correct here — the opposite of the
  boring-automations post, which was a list). One node/step per slide.
- **Concept:** clean n8n-style canvas, 5 nodes left to right: Webhook → Enrich (Clay/Apollo) → Draft (Claude)
  → Send + Stop-condition → Failure-state. Node 5 highlighted in the brand accent as the "what makes it safe"
  step. Dark Green Room kit (`knowledge-base/brand-design-system.md`).
- **Text on image (headline slot):** "Answer every lead in under 60 seconds."
- **Alt text:** Five-node n8n workflow that answers a new lead in under 60 seconds: webhook trigger, enrichment,
  a Claude-drafted reply, send from a warmed inbox with an auto-stop on reply, and a failure-state fallback.
- **Fallback (zero effort):** post text-only; the numbered 5-step body carries the save-worthiness on its own.
