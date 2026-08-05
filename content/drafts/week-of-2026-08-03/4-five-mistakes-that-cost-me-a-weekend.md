# Post 4 - "Five mistakes I made building automations people paid for. All five cost me a weekend." (Teach / Mistakes list)

- **Skeleton:** Teach format #3, Mistakes List. "[N] mistakes I made building [X]", each mistake one
  line plus the fix. `../../knowledge-base/winning-post-patterns.md` names this as the best format for
  SAVES. Crossed with the Saraev shape: a humbling outcome, told as the "I got this wrong" version
  rather than the flex.
- **Pillar:** P3 ROI systems · **Segment:** A on the way in (mistake 1), C on the way out (mistake 5)
- **Hook formula:** Specific-number promise + humbling frame (Formulas 2 and 3 crossed)
- **Format:** Text, 1,530 characters
- **CTA:** the closing question is the qualifier. Anyone who answers "the fifth" is a maintenance-debt
  buyer telling you so in public.
- **Slot:** Friday 2026-08-07, before 9:00 AM ET (5:00 PM PKT), wildcard slot
- **Zernio:** draft `6a7065a4dd5235c08d65dc62` (is_draft = true; the slot lives in the title, Zernio drafts cannot carry a scheduled time on the current API)

## Why a mistakes list is safe under the "do not lead with failure" rule

The CEO instruction is that vulnerability ships **with the fix attached**, never as an open scar. A
mistakes list is that rule in its purest form: every item is past tense, every item resolves in the
same breath, and the cumulative read is "this person has been through it and came out with a
standard," not "this person is struggling." It is also the single most relatable thing in the week.
Every operator reading it has paid for at least two of these.

Note on mistake 5: it names pricing maintenance, which is the takeover rung of the offer ladder
(`../../strategy/current-strategy.md`). It sells nothing and states no price. It just puts the idea in
the reader's head that the Thursday has a cost, which is the entire argument for the retainer.

- **Sources:** the reliability stack in `../../strategy/tribe.md` 8.2 and the wait-versus-task rule.
  No client named, no statistic, no credential flex. Every mistake is a real category of thing that
  goes wrong in n8n and Make and is described accurately.
- **QA (self-scored):** 88/100 PASS, zero red flags. Hook 16/18 · Specificity 15/16 · Comment-trigger
  16/16 (the close asks for a confession that costs nothing to give) · Save-worthiness 10/10 · Pillar
  11/12 · Dwell 8/10 · Format 8/8 · Hashtags 4/4 · Voice 6/6. Hook-payoff integrity: PASS, promises
  five, delivers five. Character count: 1,530 of 3,000.

---

Five mistakes I made building automations that people paid for.

All five cost me a weekend.

1. I built the interesting one first.

Content agents and research agents are visible. They look like work, so they get built. The expensive problem is almost always a wait: something sitting still because a person has not got to it yet. A wait does not look like work, so it never makes the list. Rank by how long something sits, not by how interesting it is to build.

2. I put error handling on one branch out of nine.

The branch I happened to be testing. One shared error handler, pointed at every workflow, set once, is a twenty minute job that I put off for months.

3. I let the alert go out through the account it was watching.

Google auth expired, so the alarm about Google auth could not send. The alert path gets its own credential. Always.

4. I treated a retry as a retry.

It is not. A retried POST is a second POST. One lead quietly became three records, and nothing anywhere reported an error, because nothing had failed. Dedupe on something stable before anything writes.

5. I quoted the build and never quoted the Thursday.

The build is a week. Keeping it alive is every week after that, and I had priced exactly none of it.

The first four are technical and you can fix them this afternoon.

The fifth one decides whether this is a business or an expensive hobby, and it took me the longest to learn.

Which of the five have you already paid for?

**FIRST COMMENT:** Number four is the one people argue with, so here is the tell: if you cannot say out loud what field you are deduping on, you are not deduping. "It has not happened yet" is not a mechanism, it is a run of luck. What is your key?

---

# Media brief

- **Type:** Carousel, 7 slides, 1080x1350, Green Room kit. Mistakes lists are save-driven and a
  carousel doubles the dwell signal per swipe.
- **Slide 1:** BG-MAIN. Anton, Bone White: "5 MISTAKES", underneath in Signal Green: "ALL FIVE COST ME
  A WEEKEND."
- **Slides 2-6:** one mistake per slide. Top half in Bone White, the mistake, past tense. Bottom half
  in Signal Green, the fix, one line. JetBrains Mono for anything that is a real setting or field name.
  Each slide must stand alone as a screenshot.
- **Slide 7:** the two closing lines, then the question. Author badge bottom-right.
- **Alt text:** "Seven slides listing five mistakes made building automations, each with its fix:
  building the interesting workflow first, error handling on one branch, the alert sharing a
  credential with what it watches, treating a retry as a retry, and never pricing maintenance."
- **Fallback:** text-only. It reads fine without the deck and the slot matters more than the art.
