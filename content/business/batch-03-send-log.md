# Batch 03 send log

(batch-03-emails.md was drafted 2026-07-20 intending a 7/21 send, but no send occurred then — confirmed via Gmail search on 2026-07-23 that none of the 10 addresses had ever received a message. Sent for real in this run instead.)

- [2026-07-23 20:00 PKT] TOUCH1 SENT hellofellows@useallfive.com (Levi Brooks, Use All Five) messageId: 19f8f7eb8e4f3a98
- [2026-07-23 20:00 PKT] TOUCH1 SENT gaylekalvert@creocollective.io (Gayle Kalvert, Creo Collective) messageId: 19f8f7eb7a8de552
- [2026-07-23 20:00 PKT] TOUCH1 SENT dave.anderson@andersonp.com (Dave Anderson, Anderson & Partners) messageId: 19f8f7eb793a1156
- [2026-07-23 20:00 PKT] TOUCH1 SENT jeffrey@boostmediagroup.com (Jeffrey Pulvino, Boost Media Group) messageId: 19f8f7eb71c91cb7
- [2026-07-23 20:00 PKT] TOUCH1 SENT fernandez@bluepureloyalty.com (Augusto Fernandez, Blue Pure Loyalty) messageId: 19f8f7ebf6ba7aaa
- [2026-07-23 20:00 PKT] TOUCH1 SENT john@avexdesigns.com (John Surdakowski, Avex E-commerce) messageId: 19f8f7ec14388cb9
- [2026-07-23 20:00 PKT] TOUCH1 SENT casey@uppercasebrands.com (Casey Brown, Uppercase Brands) messageId: 19f8f7ebea7312f0
- [2026-07-23 20:00 PKT] TOUCH1 SENT arya@kobedigital.com (Arya Bina, Kobe Digital) messageId: 19f8f7ec209ae1e4
- [2026-07-23 20:00 PKT] TOUCH1 SENT brooke@coastalcollectivemarketing.com (Brooke Apffel, Coastal Collective Marketing) messageId: 19f8f7ec9ff82c48
- [2026-07-23 20:00 PKT] TOUCH1 SENT cheryl@weare325.com (Cheryl Marchese, 325) messageId: 19f8f7eca386d1a9

MX records verified for all 10 domains before sending (all resolved: Google Workspace, Zoho, PrivateEmail, or Microsoft 365 MX records present). Touch 2 due 2026-07-26, Touch 3 due 2026-07-30.

## Bounces (found 2026-07-23, same run)
- BOUNCED gaylekalvert@creocollective.io (550 5.1.1 address not found). DEAD ADDRESS, added to dead-addresses.md, remove from all future sequences.
- BOUNCED jeffrey@boostmediagroup.com (550 5.1.1 address not found). DEAD ADDRESS, added to dead-addresses.md, remove from all future sequences.
- Delivered: 8/10 (at the time). Remaining live for touch 2/3: Levi Brooks, Dave Anderson, Augusto Fernandez, John Surdakowski, Casey Brown, Arya Bina, Brooke Apffel, Cheryl Marchese.

## Correction (found 2026-07-27, before sending touch 2)
Re-checked all 8 "delivered" threads for replies before sending touch 2 and found 2 more bounces that were missed the first time:
- BOUNCED dave.anderson@andersonp.com: initial 450 delayed-retry on 07-24/07-25, permanent 550 "address not found" surfaced 2026-07-26. DEAD ADDRESS, added to dead-addresses.md.
- BOUNCED fernandez@bluepureloyalty.com: "address not found" bounce arrived 2026-07-23 (same day as send) but was missed in the original log. DEAD ADDRESS, added to dead-addresses.md.
Actual delivered from batch-03 touch 1: 6/10 (Levi Brooks, John Surdakowski, Casey Brown, Arya Bina, Brooke Apffel, Cheryl Marchese).

## Touch 2 (day 3, due 2026-07-26, sent 2026-07-27 catching up 1 day late)
Sent as in-thread replies (GMAIL_REPLY_TO_THREAD) to the 6 confirmed-live addresses. Skipped Dave Anderson and Augusto Fernandez (both dead, see correction above). Checked all 8 threads for genuine replies first — none found, only the 2 bounce notifications above.

- [2026-07-27 18:33 PKT] TOUCH2 SENT hellofellows@useallfive.com (Levi Brooks, Use All Five) messageId: 19fa3c7db9e361aa hubspotEngagementId: 386438525689 hubspotContactId: 526401498836
- [2026-07-27 18:33 PKT] TOUCH2 SENT john@avexdesigns.com (John Surdakowski, Avex E-commerce) messageId: 19fa3c7dbc8a1a02 hubspotEngagementId: 386568969959 hubspotContactId: 526835854045
- [2026-07-27 18:33 PKT] TOUCH2 SENT casey@uppercasebrands.com (Casey Brown, Uppercase Brands) messageId: 19fa3c7e634bb0c3 hubspotEngagementId: 386568878805 hubspotContactId: 526707435236
- [2026-07-27 18:33 PKT] TOUCH2 SENT arya@kobedigital.com (Arya Bina, Kobe Digital) messageId: 19fa3c7e71586c42 hubspotEngagementId: 386491337402 hubspotContactId: 526848420567
- [2026-07-27 18:33 PKT] TOUCH2 SENT brooke@coastalcollectivemarketing.com (Brooke Apffel, Coastal Collective Marketing) messageId: 19fa3c7e863d07f7 hubspotEngagementId: 386537810650 hubspotContactId: 526691551940
- [2026-07-27 18:33 PKT] TOUCH2 SENT cheryl@weare325.com (Cheryl Marchese, 325) messageId: 19fa3c7e9e08fb02 hubspotEngagementId: 386534712031 hubspotContactId: 526399494858
- [2026-07-27 18:33 PKT] TOUCH2 SENT fernandez@bluepureloyalty.com (Augusto Fernandez, Blue Pure Loyalty) messageId: 19fa3c7ddcd351e8 hubspotEngagementId: 386568878808 (logged BOUNCED) — bounced again immediately, confirms dead, no further sends.

(Batch-03 contacts and this touch's engagements were logged to HubSpot for the first time in this run; touch 1 on 07-23 was never logged to CRM. Portal 246685260.)

Live for touch 3 (due 2026-07-30): Levi Brooks, John Surdakowski, Casey Brown, Arya Bina, Brooke Apffel, Cheryl Marchese (6 remaining).

## Touch 3 (day 7, due 2026-07-30, sent 2026-07-30 18:26 PKT, on time)
Sent as in-thread replies (GMAIL_REPLY_TO_THREAD). All 6 threads re-checked for bounces/replies before
sending (GMAIL_FETCH_MESSAGE_BY_THREAD_ID on each) — none found, clean SENT-only threads. Price line
corrected to match current-strategy.md SSOT ($500 founding / $1,500 anchor, not the stale $500/$750
generic-template line).

- [2026-07-30 18:26 PKT] TOUCH3 SENT hellofellows@useallfive.com (Levi Brooks, Use All Five) messageId: 19fb32ed0745bc7d hubspotEngagementId: 387295785665 hubspotContactId: 526401498836
- [2026-07-30 18:26 PKT] TOUCH3 SENT john@avexdesigns.com (John Surdakowski, Avex E-commerce) messageId: 19fb32ed16818818 hubspotEngagementId: 387291379421 hubspotContactId: 526835854045
- [2026-07-30 18:26 PKT] TOUCH3 SENT casey@uppercasebrands.com (Casey Brown, Uppercase Brands) messageId: 19fb32ed07fb9490 hubspotEngagementId: 387295851219 hubspotContactId: 526707435236
- [2026-07-30 18:26 PKT] TOUCH3 SENT arya@kobedigital.com (Arya Bina, Kobe Digital) messageId: 19fb32ed1487cf79 hubspotEngagementId: 387291055831 hubspotContactId: 526848420567
- [2026-07-30 18:26 PKT] TOUCH3 SENT brooke@coastalcollectivemarketing.com (Brooke Apffel, Coastal Collective Marketing) messageId: 19fb32ed671c6239 hubspotEngagementId: 387291896510 hubspotContactId: 526691551940
- [2026-07-30 18:26 PKT] TOUCH3 SENT cheryl@weare325.com (Cheryl Marchese, 325) messageId: 19fb32ed71443c2e hubspotEngagementId: 387295529710 hubspotContactId: 526399494858

6/6 sent, no immediate bounces. Batch-03 sequence is now COMPLETE (all 6 live prospects finished
touch 1/2/3). No further sends to this batch. Reply rate: 0/6 (0/10 original, 4 dead).
