# Post 2 - "Your CPL dashboard looks great. Your booked-calls number doesn't." (Teach / Audit)

> **Rewritten 2026-08-04.** The original version was a builder tutorial (Error Trigger, Workflow
> Settings, healthchecks.io) written to someone who personally maintains n8n workflows. That is the
> retired tribe (`../../strategy/tribe.md` header: "a tribe of builders cannot be sold a build").
> This version is written to the agency owner deciding whether their client's follow-up is actually
> happening, using only things they can already see or ask for: no build step, no tool install.

- **Skeleton:** Teach format #1, Audit. Three checks an agency owner can run this week using their
  own client relationship and existing dashboards. No step requires touching anyone's tech stack.
- **Pillar:** P3 ROI systems · **Shape:** A, their client's inbox (LEAD WITH THIS per `tribe.md` 8.0)
- **Hook formula:** Recognition object, reused verbatim from `tribe.md` §7 object #6 (already
  identified as a top-tier hook: "the gap is the whole business problem")
- **Format:** Text, 1,590 characters.
- **CTA:** the closing question doubles as the qualifier. No keyword, no link, no price.
- **Slot:** Wednesday 2026-08-05, 8:00-10:00 AM ET (5:00 PM PKT)
- **Zernio:** draft `6a70658f65c9da1a4f98ebc9` **(content changed, needs re-sync)**

## Tribe test (per `tribe.md` §10)

Two-plus items from sections 3.1 / 5 / 7 required. Present: recognition marker #4 ("You know your CPL
to one decimal place and cannot tell me your average reply time"), object #6 (CPL dashboard vs
booked-calls gap), the muted Slack Connect channel (marker #2 / object #7), and the enemy line
verbatim ("The leads are fine. Nobody called them.", §6). Vocabulary used: CPL, booked calls, the
account, churn. No n8n/Make/node language anywhere in the body.

- **Sources:** `tribe.md` §6 (the enemy), §7 objects #6 and #7, §5 marker #4. No client named, no
  invented statistic.
- **QA (self-scored):** 88/100 PASS, zero red flags. Hook 17/18 (recognition object, pre-validated in
  tribe.md) · Specificity 14/16 · Comment-trigger 15/16 · Save-worthiness 9/10 (three-step audit
  format) · Pillar 12/12 · Dwell 8/10 · Format 8/8 · Hashtags 4/4 · Voice 6/6. Hook-payoff integrity:
  PASS (promises the gap explained, delivers three checks). Tribe test: PASS.
  Character count: 1,590 of 3,000.

---

Your CPL dashboard looks great. Your booked-calls number doesn't.

That gap is not a media problem. The ads did their job. Somebody just never called the lead back, and by the time it shows up as churn, it is too late to prove it.

Here is the audit I run before I ever touch a client's account. Three checks. None of them need engineering access. You can do all three this week with what you already have.

1. Ask for reply time, not just close rate.

Almost every agency reports CPL and close rate. Almost none report how long a lead sat before anyone touched it. That is the number that predicts the churn conversation, not the CPL one. If your client cannot answer it in one sentence, neither of you actually knows what is happening after the lead lands.

2. Look at the contact timestamps, not the red flags.

Nothing errors when a lead just sits. Ask to see the CRM's last-contacted column for the last 20 leads. A three-day gap on a hot lead will not show up in any report your client is already looking at. It will show up in the next "the leads are garbage" message.

3. Find out where the alert goes, and whether anyone can mute it.

If a lead sits, someone needs to know before day three, not the day the account reviews the quarter. A Slack Connect channel that gets muted after week two is not a monitoring system. It is a habit of not looking.

None of this is a build. It is three questions and one CRM view.

What's your average CPL? Now, what's your average reply time? If you don't know the second number, that's the leak, and it was never the ads.

**FIRST COMMENT:** The push-back I get most: "my client would tell me if leads were sitting." They would not, because they do not know either. That is the entire gap. Whose job is it on your accounts to actually check the timestamp, not just the dashboard?

---

# Media brief

- **Type:** Single image, portrait 1080x1350, Green Room kit (`../../knowledge-base/brand-design-system.md`).
  A dashboard mockup, not a code screenshot.
- **Concept:** Two stat tiles side by side, BG-MAIN. Left tile: "CPL: $18" in Bone White, a small green
  up-arrow. Right tile: "BOOKED CALLS: 4" in Bone White, a small red down-arrow. Nothing else on the
  slide. The visual contradiction IS the post.
- **Text on image:** below the tiles, one line, Anton, Bone White, last two words in Signal Green:
  "ONE OF THESE **GETS YOU FIRED.**"
  Why this one: it refuses to explain the two tiles, so the reader has to look back at both numbers
  and work out which, and working it out IS the post. It is also a threat aimed precisely at the
  agency owner's real fear (fired over a number they do not control, `tribe.md` §6), which a neutral
  caption like "same month, same account" throws away.
  *Alternate if you want accusation over threat:* "YOU ONLY REPORT **ONE OF THESE.**"
- **Author badge:** bottom-right, avatar + "USAMA AYOUB", surname in Signal Green.
- **Alt text:** "Two stat tiles: a good cost-per-lead number next to a bad booked-calls number, same
  month, same account."
- **Fallback:** post text-only. The recognition-object hook carries the post without art.
