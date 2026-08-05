# Post 2 - "Your workflow has not thrown an error in four days. That is not evidence it is working." (Teach / Playbook)

- **Skeleton:** Teach format #1, Playbook. "How to [outcome] in [N] steps", 3 concrete do-it-today
  steps, each naming the exact move and tool, ending in what you get if you run all three.
  (`../../knowledge-base/winning-post-patterns.md`, The Teach format.)
- **Pillar:** P3 ROI systems · **Segment:** B, the reliability gap
- **Hook formula:** Counterintuitive claim (Formula 1) aimed at a thing the reader is currently
  reading as good news
- **Format:** Text, 1,690 characters. Teach posts win on SAVES, which this account has earned exactly
  one of in its whole history. This format is the fix.
- **CTA:** the closing question doubles as the qualifier. No keyword, no link, no price.
- **Slot:** Wednesday 2026-08-05, 8:00-10:00 AM ET (5:00 PM PKT)
- **Zernio:** draft `6a70658f65c9da1a4f98ebc9` (is_draft = true; the slot lives in the title, Zernio drafts cannot carry a scheduled time on the current API)

## Why this post exists

Usama's note: the week was missing guide and teaching posts, which attract attention. Correct, and the
repo already said so: `winning-post-patterns.md` calls the Teach format "a first-class P3 format,
**currently underused**", and names Nate Herk and Liam Ottley as the people who own it in this niche by
teaching step by step with zero skipped steps. The teach rule is the bar: **the reader must be able to
DO the thing from the post alone.** All three steps here are executable today with free tools.

- **Sources:** the reliability stack in `../../strategy/tribe.md` section 8.2. Every node name, setting
  and field verified there. No client, no statistic, no credential flex.
- **Technical check:** Error Trigger output fields, Workflow Settings as the Error Workflow location,
  and the credential-separation rule are all correct as written. The heartbeat is scoped to scheduled
  workflows on purpose, since a webhook has no window to measure.
- **QA (self-scored):** 89/100 PASS, zero red flags. Hook 16/18 · Specificity 16/16 · Comment-trigger
  14/16 · Save-worthiness 10/10 (this is the point of the post) · Pillar 12/12 · Dwell 9/10 · Format
  8/8 · Hashtags 4/4 · Voice 6/6. Hook-payoff integrity: PASS (promises a correction, delivers the
  mechanism plus three steps). Character count: 1,690 of 3,000.

---

Your workflow has not thrown an error in four days.

That is not evidence it is working. It is evidence that nothing has run and failed, which is a different sentence.

An error only exists if something ran. A trigger that quietly stopped firing produces no executions, so it produces no errors, so every alarm you built stays silent. On that screen, a healthy system and a dead one look identical.

Three checks. Ten minutes. Do them today.

1. Look at the gaps, not the reds.

Open your executions list and sort by newest. If the workflow runs hourly and your last three timestamps are eight hours apart, you just found it. Red rows are loud. Gaps are the ones that cost you money.

2. Set an Error Workflow, and do not let it share a credential with what it watches.

In n8n: Workflow Settings, Error Workflow, every workflow pointed at one shared handler. Put the failing node name and the execution link in the alert, or you will mute it inside a week. And if Google auth is the thing that broke, an alert sent through Gmail cannot reach you. That is the single most common reason a correctly built alarm never rings.

3. Add a heartbeat.

The last node on the success path pings a dead man's switch. healthchecks.io, Cronitor and Better Stack are all free at your size. If the ping does not land inside the window, the monitor tells you, and nothing inside your own instance had to be alive for that to happen.

Only the third one catches a trigger that simply stopped. The first two need something to have run.

An alarm that rings when something fails cannot tell you that nothing is happening. You need one that rings at silence.

Which of the three do you have on the workflow you would be most embarrassed to find dead?

**FIRST COMMENT:** The window is the part people get wrong. Period is your run interval, grace is one more interval on top of it, not zero. Set grace to zero and one slow run pages you at 3am, and you will have muted the monitor by Friday. What are you running yours at?

---

# Media brief

- **Type:** Carousel, 5 slides, 1080x1350, Green Room kit. Carousels are the only format that has
  broken 7% engagement rate on this account and they earn double the comments of text at the same
  reach (`../../performance/linkedin-performance-log.md`, 2026-07-19).
- **Slide 1:** BG-MAIN. Anton, Bone White: "NO ERRORS IN FOUR DAYS" then underneath, smaller, Signal
  Green: "IS NOT GOOD NEWS."
- **Slide 2:** the mechanism, JetBrains Mono. Two mock execution lists side by side, one healthy, one
  with an 8-hour timestamp gap, both showing zero red rows. Caption: "Same screen. One of these is dead."
- **Slide 3:** "1. LOOK AT THE GAPS, NOT THE REDS." One line of instruction under it.
- **Slide 4:** "2. ERROR WORKFLOW. SEPARATE CREDENTIAL." Small diagram: watched workflow in Bone
  White, alert path in Signal Green, visibly not touching the same credential box.
- **Slide 5:** "3. HEARTBEAT." A ping arrow leaving the instance to an outside monitor. Caption:
  "The only one that fires when nothing ran." Author badge bottom-right.
- **Alt text:** "Five slides explaining why an automation with no errors may not be running, and three
  checks: look at timestamp gaps, set an error workflow on a separate credential, and add a heartbeat."
- **Fallback:** single image of slide 1, or text-only. Do not miss the slot for the deck.
