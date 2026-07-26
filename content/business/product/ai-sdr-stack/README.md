# The $50/Month AI SDR, Complete Build
Welcome. This package gives you a working AI sales assistant that finds your leads,
writes personalized cold emails, sends them, reads the replies, and flags the
interested ones for you. It runs on about $45 to $50 a month of tools, and you own
all of it.

No coding is needed. If you can follow a recipe, you can set this up.

## What is in this package
1. `workflows/1-outreach-sender.json`  (the robot that writes and sends your emails)
2. `workflows/2-reply-classifier.json` (the robot that reads replies and tells you who is interested)
3. `prompts.md`   (the exact instructions the AI uses, copy-paste ready)
4. `troubleshooting.md` (plain-English fixes for everything that commonly goes wrong)
5. The video walkthrough (15 minutes, watch it first)

## What you need before starting (the $50 stack)
| What | Where to get it | Cost |
|---|---|---|
| n8n (the engine) | a $5/month server from Hetzner, or n8n cloud trial | ~$5 |
| An AI account | Anthropic or OpenAI API key | ~$20 based on use |
| Sending mailboxes | Instantly.ai starter, or your own warmed inbox | ~$15 |
| A lead list | Apollo free tier, or any CSV/Google Sheet of leads | $0-10 |

## Task 1: Get n8n running
- Easiest path: sign up at n8n.io (cloud) and start a workspace. Done in 5 minutes.
- Cheaper path: rent the $5 Hetzner server and install n8n with their one-line installer.
  The video shows both. If a step looks scary, use the cloud path.

## Task 2: Import the two workflows
- In n8n, click "Add workflow", then the three dots menu, then "Import from file".
- Pick `1-outreach-sender.json`. Repeat for `2-reply-classifier.json`.
- You will see some nodes marked with a warning triangle. That is normal: they are
  waiting for your accounts to be connected (next task).

## Task 3: Connect your accounts (credentials)
Each workflow needs three connections. n8n asks for them when you click a node:
- Google Sheets: sign in with Google when prompted. This is where your lead list lives.
- Your AI key: paste the Anthropic or OpenAI key into the "AI: draft email" node.
- Your mailbox: for sending, enter the SMTP details from Instantly or your inbox
  provider. For reading replies, enter the IMAP details of the same inbox.
  (SMTP means "the sending door", IMAP means "the reading door". Your inbox provider
  lists both on their help page, usually under "app setup".)

## Task 4: Point it at your lead list
- Make a Google Sheet with these columns: fullName, email, company, website, status.
- Put your leads in it, leave status empty.
- Open the "Read leads" node and choose your sheet. That is the only change needed.

## Task 5: Test with yourself first
- Put YOUR OWN email as the only lead in the sheet.
- Press "Execute workflow" once. Within a minute you should get a personalized
  email written to you, and the sheet should say status = sent.
- Reply to that email with "sounds interesting, tell me more". Run the second
  workflow. You should get a notification flagging yourself as INTERESTED.
- If both happened: your AI SDR is alive. If not: open troubleshooting.md.

## Task 6: Turn it on for real
- Add real leads to the sheet (10 to 20 per day to start, not hundreds).
- Switch both workflows from "Inactive" to "Active" (toggle at the top).
- The sender runs each weekday morning. The reader checks your inbox every 15 minutes.
- Interested replies land in your notification email with the full conversation.
  You take it from there: reply personally and send your booking link.

## The one rule
Start slow. 10 to 20 emails a day for the first two weeks. Sending hundreds
from a fresh mailbox gets you spam-foldered, and no tool can undo that quickly.
