# DM reply skeletons, week of 2026-08-03

> Four posts, four different asks. Without these, four CTAs turn into four bespoke replies written
> under time pressure, which is the one failure a reliability offer cannot afford. Set-review edit 18.
> Voice rule: no em dashes. US English. Mirror their message length. One question per reply.

**Standing rules for all four.** Reply inside the hour if you can, same day at worst. Never open with
the offer. Never send a booking link in the first reply. Answer the technical question first and
completely, then ask the one question that moves it forward. If the answer is "nothing needs doing,"
say that and stop; it costs one lead and buys the reputation the whole positioning rests on.

---

## Post 1 (Tue) — they asked for the Error Workflow + heartbeat JSON

**The asset exists:** `content/lead-magnets/n8n-error-workflow-heartbeat/error-workflow-heartbeat.json`
Five nodes: Error Trigger, Build Alert (Set), a placeholder send node, Heartbeat Schedule, Heartbeat Ping.
**Before sending:** swap `SEND NODE GOES HERE` for their channel and wire `{{ $json.alertText }}` into it.
That is the wiring the post promised, so do it, do not send the placeholder.

```
Sending it over. Two things I set before I export it, so it lands working:

The send node is [Slack/Telegram/Twilio]. The alert carries the failing node name and a direct link
to the execution, because an alert that just says something failed gets muted inside a week.

The ping URL and the two window fields are blank on purpose, those are yours. Period is your schedule
interval, grace is one more interval on top of it. Grace of zero pages you at 3am on one slow run.

One thing worth checking before you import: how many workflows are you planning to point at this?
```

**Why that question:** the number splits the segments in one reply. One or two means Segment B, keep
teaching. Five or more means Segment C, and the audit rung is the natural next move.

**If they said Gmail:** ask what credentials are in the workflow it watches, first. If Google auth is
in there, the alert cannot go out through Gmail. That is the mechanism 2 conversation and it is a
good one to have.

---

## Post 2 (Wed) — they gave two numbers (workflows built / workflows they can name as running)

```
Thanks. Three questions that usually find the gap between those two numbers:

1. Sort your Credentials page by how many workflows use each one. What is the top row, and what is
   the number next to it?
2. Of the ones you can name as running, how many have an Error Workflow set in Workflow Settings?
3. When something last broke, who noticed first, you or the person paying for it?

The credential I would check today is [the top one / whichever is on the client-facing build]. One
string holding up that many workflows is a blast radius nobody picked.

Which of those three was hardest to answer?
```

**The escalation:** whichever question they could not answer is the audit's opening slide. If they
answered all three cleanly, they are more organized than the post assumed, so say so and ask what
their maintenance actually costs them per month.

---

## Post 3 (Thu) — they told you what their last node does + webhook or poll

```
Got it. For a [webhook/poll] trigger firing a [what the send node does]:

Dedupe key: [the stable field, usually email or an external ID]. Remove Duplicates, in the mode that
removes items seen in previous executions. A retried POST is not a retry, it is a second POST.

[If poll] The pointer goes in $getWorkflowStaticData('global'), written after the last successful
item. Trap worth knowing: static data persists on production executions and not on manual ones, so it
looks broken the whole time you are testing it.

[If webhook] You do not need a pointer, you need idempotency. Same key, different reason: senders
retry, and a retry looks identical to a new lead.

The one business rule I would put a Stop and Error node on: [the field whose absence makes the send
embarrassing, e.g. no name, empty model response].

Is the send node still off, or did you turn it on and it is the confidence that is missing?
```

**Why that question:** it separates "not built" from "built but not trusted." The second one is the
takeover conversation.

---

## Post 4 (Fri) — they sent their list of waits

**If the list has numbers:** name which one you would build first and why, in two sentences. The
ordering rule is wait length times frequency, not how annoying the task is.

**If the list has no numbers:**
```
Take these three and go get the numbers, in this order:

1. How long it sits. This is the one people are always wrong about, and always in the same direction.
2. How often it happens. A week of counting beats a guess.
3. What it is worth when it goes well.

You can estimate 2 and 3. Do not estimate 1, go and look at timestamps.

Send them back and I will tell you which one I would build first.
```

**Do not** pitch on this reply. Segment A is reach, not near-term revenue. The job here is to be the
person who gave them the decision they were stuck on. The sale, if it comes, comes after they ship
something and hit the reliability wall, which is when they become Segment B.
