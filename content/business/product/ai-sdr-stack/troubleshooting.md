# Troubleshooting, in plain English
Find your symptom, apply the fix. No coding needed for any of these.

## "429 Too Many Requests" error on the AI node
This is the #1 issue people hit, and it just means the AI provider said
"slow down, you are asking too fast."
Fix (2 minutes): open the AI node, go to Settings, turn ON "Retry on Fail",
set Max Tries to 4, and Wait Between Tries to 2000. The workflow will now
wait and retry automatically instead of stopping. Both included workflows
already ship with this turned on; check it if you rebuilt the node.

## Emails are not sending
- Open the sending node and press "Test step". Read the message it gives you.
- "Authentication failed" means the mailbox login details are wrong. Re-copy
  the SMTP settings from your provider's help page. Watch for extra spaces.
- "Connection refused" usually means the port number is wrong. Try 587 first,
  then 465.

## Emails send but land in spam
- You are probably sending too many, too fast, from a mailbox that is too new.
  Drop to 10 a day for two weeks.
- Make sure your mailbox provider has SPF and DKIM set up (their help page
  walks you through it, it is a copy-paste job into your domain settings).
- Remove links from your first email. Links are the fastest way into spam.

## The reply reader flags everything as INTERESTED
- Open the "AI: classify reply" node and check the prompt was pasted fully,
  including the last line ("Output only the single word").
- Auto-replies ("I am out of office") sometimes look interested to the AI.
  The workflow already skips common auto-replies; if one slips through,
  just ignore it. It costs you nothing.

## The workflow ran but the Google Sheet did not update
- Open the sheet-update node and confirm it points at the same sheet and tab
  as the read node. The most common cause is two similarly named tabs.
- Check the column names in your sheet exactly match: fullName, email,
  company, website, status. Capital letters matter.

## "My workflow was working and just stopped"
- Check your AI account has credit remaining. This is the cause 8 times out of 10.
- Check the mailbox password did not expire or get rotated.
- Open "Executions" in n8n (left sidebar) and click the red run. The node
  that failed is highlighted, and its error message says what to fix.

## Still stuck?
Email me the screenshot of the red node and its error message. Buyers get
direct email support: [YOUR EMAIL]
