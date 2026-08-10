---
type: teach (Playbook, structure #1)
framework: content/knowledge-base/winning-post-patterns.md, Teach format + Nate Herk standard
pillar: P3 ROI systems
audience: anyone with leads arriving and nobody answering them
slot: Wed 2026-08-12 8:00am ET / 5:00pm PKT
qa_score: 90
zernio: draft 6a75b1f5113480c933562b4f
cta: the real n8n export, in the first comment, no keyword bait
hashtags: 0
status: pending-approval (Usama adds carousel, publishes the Gist link in comment 1)
---

# Post 3 — "Answer every lead in under 60 seconds. Six steps, none skipped."

**This is the giveaway post.** Usama's instruction: gift something to people. The account has earned
**one save in its entire history** (`../../performance/linkedin-performance-log.md`) and the teach
format is the one that fixes that. `winning-post-patterns.md` has flagged Teach as "a first-class P3
format, currently underused" since 2026-07-22.

The Herk/Ottley standard is the bar: step-by-step, **zero skipped steps**, safe for a non-technical
founder to follow or at minimum to brief someone with. Vague teach is the worst of both worlds, no
save and no authority. So the steps below are the real ones, in the real order, with the real tools
named, including the step almost everybody skips.

## Hook-payoff integrity check

The hook promises **six steps of one build** (a process, not a list of six independent things), and
the body delivers exactly six ordered steps of that one build. Correct shape per the law in
`winning-post-patterns.md`. Do not renumber these into "6 automations": that would break it.

## PREREQUISITE before this posts (5 minutes, Usama)

The gift needs somewhere to live. `../../lead-magnets/n8n-error-workflow-heartbeat/error-workflow-heartbeat.json`
is a real five-node export and it is what step 6 describes.

1. Paste it into a **public GitHub Gist** under Usama's own account.
2. Put that Gist URL in the **first comment**, never the body (external links in the body cost ~60%
   reach, `../../knowledge-base/linkedin-algorithm-2026.md` Phase 1).
3. Nothing else needed. No keyword, no "comment HEARTBEAT", no DM gate. That is bait and 2026 penalizes
   it. The link is just there, free, for anyone who wants it. Free with no hoop is what gets a post
   shared by people who will never buy anything, which is how it leaves the network.

- **Sources:** the build is the interior-studio system from `proof-assets.md` #1, generalized into
  steps. The heartbeat in step 6 is the real JSON on disk. No invented tool, no invented number.
- **QA (self-scored):** 90/100 PASS, zero red flags. Hook 17/18 · Specificity 15/16 · Comment-trigger
  14/16 (a teach post earns saves more than comments, and that is the intent here) · Save-worthiness
  10/10 · Pillar 12/12 · Dwell 9/10 · Format 8/8 · Hashtags 4/4 · Voice 6/6.
  Hook-payoff integrity: PASS. Offer legibility: PASS. Bait check: CLEAN, no keyword CTA.
  Character count: 2,225 of 3,000. Longest of the week by design: a teach post is
  read, not skimmed, and dwell time is the 2026 ranking signal.

---

Answering a lead in under 60 seconds is not an AI problem. It is a plumbing problem.

Here is the whole build, six steps, in the order they have to happen. I have shipped this. Nothing below is skipped.

1. Pick the ONE place leads actually arrive.

Not everywhere they could arrive. The one that carries the most. Meta lead form, website form, WhatsApp, missed call. Pick it and ignore the rest until this works. Most people fail here by trying to catch all four on day one.

2. Get it out of your notifications and into a workflow.

A notification is not a system. It depends on you being awake, unbooked, and holding your phone. In n8n this is one trigger node: the Meta Lead Ads node, or a webhook the form posts to. That is the whole step, and it is the one that actually changes your life.

3. Write the first reply yourself. Four lines, maximum.

Do not generate it. Do not let a model improvise in front of a stranger who is about to spend money with you. You write it, you read it back, you approve it. The system's job is speed, not judgment.

4. Ask three qualifying questions in the same thread.

Not a form. Not a link to a form. Three questions inside the conversation they are already in. Scope, timeline, rough budget range. People answer questions in a chat they have already opened. They abandon forms.

5. Route both outcomes. Never leave silence.

Clears the bar, calendar link in the same thread, while they still have the phone in their hand. Does not clear the bar, still gets a real answer. Ghosting somebody politely is still ghosting them, and they remember it.

6. Add the heartbeat. This is the step everyone skips.

Errors alert you. Silence does not. A lead that simply sits there throws nothing, so your dashboard stays green the entire time nothing is happening. You need an alert that fires when the workflow has NOT run, not just when it fails. That is a five-node error workflow plus a scheduled check.

I have put that heartbeat export in the first comment. Free, no email, no keyword. Import it and point the send node at your own channel.

Steps 1 to 5 win you the lead. Step 6 is the only reason the thing is still working in March.

Which step is the one your current setup is missing?

**FIRST COMMENT:** Here is the n8n error-workflow heartbeat, importable as-is: [GIST LINK]. Five nodes. Wire the send node to your Slack or WhatsApp and it tells you when nothing happened, which is the failure nobody catches. Happy to answer questions on it here.

---

# Media brief

- **Type:** Carousel, 8 slides, 1080x1350, Green Room kit
  (`../../knowledge-base/brand-design-system.md`). Carousels run ~4x text engagement and this is the
  save-driver of the week, so this is the one to spend the effort on.
- **Slide 1 (cover):** BG-MAIN. Anton, Bone White: "ANSWER EVERY LEAD IN", then in Signal Green,
  larger: "UNDER 60 SECONDS." Small mono chip beneath: "6 STEPS. NONE SKIPPED."
- **Slides 2-7:** one step per slide, in order. Top: the step number in Signal Green mono, big. Middle,
  Bone White Anton: the step in four words or fewer ("GET IT OUT OF NOTIFICATIONS"). Bottom, smaller,
  body weight: the one sentence that makes it actionable, including the node name where there is one.
- **Slide 6 (step 5) needs no art beyond text. Slide 7 (step 6, the heartbeat) is the one slide that
  earns a real screenshot:** the actual five-node error workflow on the n8n canvas, cropped tight so
  all five nodes are legible. This is the one place in the week a canvas screenshot belongs, because
  here the wiring IS the gift.
- **Slide 8 (close):** "STEPS 1-5 WIN THE LEAD." / Signal Green: "STEP 6 IS WHY IT STILL WORKS IN
  MARCH." Then, small: "Export in the comments. Free." Author badge bottom-right.
- **Alt text:** "Eight slides showing a six-step build for answering every lead in under sixty
  seconds: pick one lead source, move it from notifications into an n8n workflow, write the first
  reply yourself, ask three qualifying questions in-thread, route both outcomes with no silence, and
  add a heartbeat alert that fires when nothing has run."
- **Fallback:** text-only with the Gist in the first comment. The post is complete without the deck.
  The deck is what earns the saves.
