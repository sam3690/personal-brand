# Loom Script: "$50/mo AI SDR, Full Setup in 15 Minutes"
Style: screen recording, your face in the bubble, normal talking pace.
Do not read word for word. Each block has WHAT TO SHOW and WHAT TO SAY.
Total target: 14-16 minutes. Record in one take; small stumbles make it human.

## 0:00 - 1:00 | Intro (face full screen or big bubble)
SHOW: just you, or the README open.
SAY: "Hey, I'm Usama. In the next 15 minutes we're going to set up an AI sales
assistant that sends personalized cold emails from your lead list, reads the
replies, and pings you the moment someone is interested. It costs about 50
dollars a month to run and you own every piece of it. I've built more than
500 automation workflows for clients, and this is the same architecture I
charge for. Follow along task by task. Pause me whenever you need."

## 1:00 - 3:00 | Task 1: get n8n running
SHOW: n8n.io signup, click through to an empty workspace. Mention Hetzner
as the cheaper path but do NOT demo the whole server install; point to the
README for it.
SAY: "n8n is the engine that runs everything. Fastest path: n8n cloud, sign
up, you get a workspace like this in two minutes. Cheaper path if you want
the true 50 dollar setup: a 5 dollar Hetzner server, steps are in the README,
Task 1. Both end in exactly this screen, so from here on it makes no difference."

## 3:00 - 5:00 | Task 2: import the two workflows
SHOW: Add workflow, three-dots menu, Import from file, pick each JSON.
Zoom on the imported canvas.
SAY: "Two files in the workflows folder. This one writes and sends your
emails. This one reads the replies. Import both like this. See the warning
triangles on some nodes? Totally normal, they're just waiting for your
accounts, which is the next task."

## 5:00 - 8:30 | Task 3: connect your accounts
SHOW: click each credential node, connect Google Sheets via OAuth, paste an
AI key (blur yours!), fill SMTP and IMAP fields from a provider help page.
SAY: "Three connections. One: Google Sheets, just sign in when it asks,
that's where your lead list lives. Two: your AI key from Anthropic or OpenAI,
paste it here. Three: your mailbox, twice. SMTP is the sending door, IMAP is
the reading door. Every inbox provider lists both on their help page, I'll
show you where it is for Instantly. Copy carefully, the number one error in
troubleshooting is a pasted space at the end of a password."

## 8:30 - 10:00 | Task 4: the lead sheet
SHOW: create the Google Sheet live: columns fullName, email, company,
website, status. Add one row: YOUR OWN details. Point the Read leads node at it.
SAY: "Five columns, exactly these names, capitals matter. And notice the
first lead I'm adding is me. Never test on a stranger. Leave status empty,
the robot fills it."

## 10:00 - 12:30 | Task 5: the self test (the money moment)
SHOW: hit Execute workflow. Wait. Open your inbox on screen, show the
AI-written email arriving. Read a line of it out loud. Then reply "sounds
interesting", run workflow 2, show the HOT LEAD notification arriving.
SAY: "Execute, and watch. There it is: a personalized email, written to me,
about my company, in under a minute. Now I reply like an interested prospect...
run the second workflow... and there's the notification: hot lead, full reply
included. That loop you just watched is the whole product. Everything else
is volume."

## 12:30 - 14:00 | Task 6: going live + the one rule
SHOW: flip both workflows to Active. Show the schedule node (weekday
mornings). Open the prompts.md file, point at the [BRACKETS].
SAY: "Flip both to active and it runs itself: sender every weekday morning,
reader every 15 minutes. Before you load real leads, two things. First, open
prompts.md and fill every bracket so the AI writes as YOUR business, the
README shows exactly where. Second, the one rule: 10 to 20 emails a day for
the first two weeks. A fresh mailbox that blasts 200 emails goes to spam
and stays there. Slow is what makes this work."

## 14:00 - 15:00 | Outro
SHOW: troubleshooting.md scrolled slowly, then your face.
SAY: "When something breaks, and at some point something will, open
troubleshooting dot md first. It covers the 429 error, spam folders, sheets
not updating, all in plain English, symptom then fix. If you're still stuck,
email me a screenshot, the address is in the file, buyers get direct support.
That's it. You now run an AI SDR for about 50 dollars a month. Go slow,
stay boring, and let it book the calls. See you."

## Recording checklist (delete before publishing)
- Blur or regenerate your API key after recording.
- Use a clean browser profile: no client tabs, no bookmarks bar.
- Test mic for 10 seconds first.
- One take is fine. A restart costs more energy than a stumble.
