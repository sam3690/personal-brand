# Lead List Quality

Lesson from 2026-07-09: a domain-level check is not a mailbox-level check, and skipping the
distinction cost real bounces on the [[Cold Outreach Engine]].

## What happened
Before sending cold-email batch 02, an MX record check confirmed all 10 domains had a live mail
server. That only proves the *domain* can receive mail, not that the specific *mailbox* exists.
4 of 20 sends that day bounced (550 5.1.1, address not found): 2 in batch 02 (fresh, uncatchable
by MX check alone) and 2 in batch 01 (Ty Smith, Ray Ali — these had already bounced on Touch 1
three days earlier, sitting unread in the inbox, and got followed up anyway because the Touch 2
task checked for *replies* but not *bounces* first).

## The fix, going forward
1. Every send task now runs a bounce sweep (`from:mailer-daemon`) as step one, before the reply
   check, before any follow-up goes out.
2. Bounced addresses get marked in HubSpot (`hs_email_status: BOUNCED`) and flagged in the send
   log's own file, so future drafting (which reads the log first) excludes them automatically.
3. Apollo's "verified" tag on [[Cold Outreach Engine|batch 01]] had a ~20% real bounce rate.
   Gmail starts distrusting a sender above ~5%; two batches like that back to back would hurt
   deliverability on the *good* addresses too. Before scaling past batch 2, run the remaining list
   through a real mailbox-level verifier (MillionVerifier / ZeroBounce free-credit tiers cover the
   ~86 leftover leads) rather than trusting the source tag alone.

Related: [[Cold Outreach Engine]]
