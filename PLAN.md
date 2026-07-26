# n8n Content Workflow — Architecture Plan

> **Purpose:** Take structured content input → generate image + post → analyze → publish → log
> **Platforms:** X (Twitter) + LinkedIn
> **Constraint:** n8n official nodes only (no premium nodes). No high-cost APIs.

---

## Panorama

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          WORKFLOW: Content-to-Post Pipeline                      │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                   │
│  INPUT ──► 1. PARSE ──► 2. KEYWORDS ──► 3. IMAGE ──► 4. CONTENT                  │
│  (text)      (Code)      (AI Chat)       (HTTP Req)    (AI Chat)                  │
│                                │                                                │
│                                ▼                                                │
│                         5. QUALITY CHECK ──fail──► Human Review (Webhook)        │
│                                │ pass                                            │
│                                ▼                                                │
│                     ┌────────────────────┐                                      │
│                     │  6. POST to X      │  (Twitter node — official)            │
│                     │  7. POST to Li     │  (HTTP Req — LinkedIn API v2, free)   │
│                     │  8. LOG to Sheets  │  (Google Sheets node — official)       │
│                     └────────────────────┘                                      │
│                                                                                   │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Node Design

### Step 0: Input Format

Trigger: **Webhook node** (receives POST) or **Manual node** (for testing).

Expected payload:

```json
{
  "topic": "Build 500 AI workflows and this is what businesses actually want",
  "visual_hook": "Split screen showing a flashy AI demo on one side and a simple calendar booking on the other",
  "verbal_hook": "Most people do not realize businesses do not want fancy AI agents...",
  "key_points": [
    "After 500 client workflows the top demand is appointment booking...",
    "The second most requested is lead response automation...",
    "The pricing is better for boring workflows..."
  ],
  "cta": "type BORING",
  "platform": "x"  // or "linkedin" or "both"
}
```

---

### Step 1: Parse Input

| Field | Node | Detail |
|-------|------|--------|
| **1.1 Validate** | **Code** (JS) | Check all required fields present. Return 400 if missing. |
| **1.2 Extract** | **Code** (JS) | Normalise fields, build a clean `content` object, set `status: "parsed"`. |

```javascript
// Code node - Parse & Validate
const input = $json;
const required = ['topic', 'visual_hook', 'verbal_hook', 'key_points', 'cta'];
const missing = required.filter(k => !input[k]);
if (missing.length) throw new Error(`Missing fields: ${missing.join(', ')}`);

return [{
  json: {
    ...input,
    parsed_at: new Date().toISOString(),
    status: 'parsed'
  }
}];
```

ⓘ *n8n node:* `Code`
⚡ *Cost:* Free

---

### Step 2: Hashtag & Keyword Research

| Field | Node | Detail |
|-------|------|--------|
| **2.1 AI researcher** | **OpenAI Chat** | Prompt the model to: (a) extract 3–5 lead-magnet keywords from the topic, (b) suggest 8–10 platform-specific hashtags (X + LinkedIn), (c) rank keywords by search intent (cold/warm/hot). |

**Node config:**
- **Model:** `gpt-4o-mini` (~$0.15/1M input tokens — optimise with short prompt)
- **Messages:** System prompt defining the keyword-research role + user message with the topic + key points

**System prompt:**
```
You are a social-media keyword researcher. Given a content topic and key points,
return ONLY valid JSON (no markdown):
{
  "keywords": [
    {"word": "AI workflow", "intent": "warm", "reason": "topic core"},
    {"word": "appointment automation", "intent": "hot", "reason": "buying signal"},
    {"word": "lead response", "intent": "warm", "reason": "pain point"}
  ],
  "hashtags": {
    "x": ["#AIWorkflows", "#BoringAutomation", "#n8n", ...],
    "linkedin": ["#AIAutomation", "#SalesTech", "#WorkflowAutomation", ...]
  },
  "primary_hashtag": "#BoringAutomation"
}
```
3 keywords max. 8 hashtags per platform. 1 primary hashtag.

ⓘ *n8n node:* `OpenAI` (model: `gpt-4o-mini`)
⚡ *Cost:* ~$0.001 per run

---

### Step 3: Image Generation

| Field | Node | Detail |
|-------|------|--------|
| **3.1 Generate prompt** | **OpenAI Chat** | Convert `visual_hook` into a detailed image-generation prompt (optimised for the chosen engine). |
| **3.2 Image API** | **HTTP Request** | POST to image API. |

**Image engine options (ranked by cost):**

| Engine | Node | Cost/Image | Notes |
|--------|------|------------|-------|
| **Hugging Face** (Stable Diffusion 3.5) | **HTTP Request** | **Free** (rate-limited) | Best for zero budget. Use `stabilityai/stable-diffusion-3.5-large-turbo`. HF token from free account. |
| **OpenAI DALL-E 3** | **OpenAI** node (or HTTP) | ~$0.04/image | Reliable, brand-accurate, but costs. |
| **Replicate** (SDXL) | **HTTP Request** | ~$0.002/image | Very cheap, needs Replicate API key. |

**Recommended: Hugging Face** (free tier, 30k inference calls/mo on certain models).

**HTTP Request config for HF:**
- **Method:** POST
- **URL:** `https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large-turbo`
- **Headers:** `Authorization: Bearer {{ $env.HF_API_KEY }}`
- **Body:**
```json
{
  "inputs": "Split screen: left side shows a flashy AI robot dashboard with stock 'AI AGENT' label and dollar signs; right side shows a simple clean calendar booking interface with checkmarks. Split down the middle, high contrast.",
  "parameters": { "negative_prompt": "blurry, low quality, text artifacts", "num_inference_steps": 20 }
}
```

ⓘ *n8n node:* `HTTP Request` (or `OpenAI` if using DALL-E)
⚡ *Cost:* **$0** (HF free tier) or ~$0.04 (DALL-E)

---

### Step 4: Content Creation

| Field | Node | Detail |
|-------|------|--------|
| **4.1 Decide format** | **Code** (JS) | Based on `platform` field: `x` → short post, `linkedin` → article/post, `both` → decide by topic length. |
| **4.2 Generate post** | **OpenAI Chat** | Create platform-native content from the topic + hooks + keywords + brand voice. |

**System prompt:**
```
You are a content writer for Usama Ayoub, a personal brand in AI automation.
Brand voice: direct, specific, no fluff. No "game-changer", no "revolutionary".
Each sentence carries a claim or a proof point.

Write a {platform} post using these components:

TOPIC: {topic}
VERBAL HOOK: {verbal_hook}
KEY POINTS: {key_points}
CTA: {cta}
KEYWORDS: {keywords}

Rules:
- {platform_rule}
- Use the verbal hook as the opening line
- Weave in 1-2 key points naturally
- End with the CTA
- Max {max_chars} characters

Return ONLY the post text, no explanations.
```

**Platform rules:**
- **X:** Max 280 chars (or 4000 with X Premium). Open with strongest claim. One post, no thread unless content demands it.
- **LinkedIn:** Expand for niche audience. 800-1200 chars. End with question embedded in CTA, not a lazy engagement bait.

**Carousel decision:**
For topics with 3+ distinct data points or a teachable framework, the Code node can flag `format: "carousel"`. Carousel generation requires a separate sub-workflow (each slide = one OpenAI call for copy + one image call for slide background).

ⓘ *n8n node:* `OpenAI` (model: `gpt-4o-mini`)
⚡ *Cost:* ~$0.002 per post

---

### Step 5: Quality Analysis

| Field | Node | Detail |
|-------|------|--------|
| **5.1 Score content** | **OpenAI Chat** | Score 0-100 on: (a) hook strength, (b) specificity, (c) CTA clarity, (d) platform fit. |
| **5.2 Gate** | **IF** | Score >= 70 → pass (proceed to publish). Score < 70 → fail (pause for human review). |

**System prompt for scoring:**
```
You are a content quality analyst. Score this post 0-100 on four criteria:

1. Hook strength (0-25): Does the first sentence make you want to read more?
2. Specificity (0-25): Does it use numbers, data, or concrete claims instead of generalities?
3. CTA clarity (0-25): Is the call-to-action clear and actionable?
4. Platform fit (0-25): Does it match {platform} norms without being generic?

Return ONLY valid JSON: {"score": 78, "breakdown": {"hook": 20, "specificity": 22, "cta": 18, "platform": 18}, "verdict": "pass", "reason": "Strong hook with specific data point"}
```

**IF node logic:**
```
Condition: {{ $json.score }} >= 70
  true  → Continue to publish branch
  false → Webhook (pause, notify for human review)
```

ⓘ *n8n node:* `OpenAI` → `IF`
⚡ *Cost:* ~$0.001 per score

---

### Step 6: Post to X

| Field | Node | Detail |
|-------|------|--------|
| **6.1 X post** | **Twitter** (n8n official) | Send the generated text + image to X. |

**Node config:**
- **Credential:** Twitter/X OAuth 2.0 (set up in n8n credentials)
- **Resource:** Tweet
- **Text:** `{{ $json.post_text }}`
- **Media:** `{{ $json.image_url }}` (attached as media)

ⓘ *n8n node:* `Twitter` (official, works on all n8n plans)
⚡ *Cost:* Free (node usage) + Twitter API free tier (1500 tweets/month)

---

### Step 7: Post to LinkedIn

**Decision:** n8n's native LinkedIn node requires **premium plan**. The free alternative is **HTTP Request** → LinkedIn API v2.

#### Option 7.1: HTTP Request to LinkedIn API (Recommended for free tier)

| Field | Node | Detail |
|-------|------|--------|
| **7.1a Auth** | **HTTP Request** | Use OAuth 2.0 Client Credentials flow to get a token. |
| **7.1b Post** | **HTTP Request** | POST to LinkedIn API v2 to create a share. |

**Setup:**
1. Create a LinkedIn app at https://developer.linkedin.com/
2. Get `Client ID` and `Client Secret` → store in n8n credentials as `LINKEDIN_CLIENT_ID`, `LINKEDIN_CLIENT_SECRET`
3. Use `https://api.linkedin.com/v2/ugcPosts`

**n8n flow for auth:**
```
HTTP Request (POST to https://www.linkedin.com/oauth/v2/accessToken)
  → Code node (extract access_token, store expiry)
  → HTTP Request (POST ugcPosts with the image + text)
```

**Post body:**
```json
{
  "author": "urn:li:person:{person_id}",
  "lifecycleState": "PUBLISHED",
  "specificContent": {
    "com.linkedin.ugc.ShareContent": {
      "shareCommentary": {
        "text": "{{ $json.post_text }}"
      },
      "shareMediaCategory": "IMAGE",
      "media": [{
        "status": "READY",
        "description": { "text": "{{ $json.topic }}" },
        "media": "{{ $json.linkedin_image_urn }}"
      }]
    }
  },
  "visibility": {
    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
  }
}
```

**Image upload requires 2 extra steps:**
- POST `/assets` to register the image
- POST `/images` with the binary data
- Then reference the returned URN in the ugcPosts call

#### Option 7.2 (If LinkedIn API is too complex to auth):

**Webhook to a serverless function** (Cloudflare Worker, Vercel Edge) that handles the LinkedIn post. This moves the complexity out of n8n.

#### Option 7.3 (Fallback if no LinkedIn API access):

**Log to Google Sheet only** for LinkedIn content. Post manually.

ⓘ *n8n node:* `HTTP Request` (no premium node needed)
⚡ *Cost:* **$0** (LinkedIn API is free for personal posting)

---

### Step 8: Log to Google Sheets

| Field | Node | Detail |
|-------|------|--------|
| **8.1 Log** | **Google Sheets** (official) | Append a row to the content tracker. |

**Sheet schema:**

| Column | Value |
|--------|-------|
| A: Title | `{{ $json.topic }}` |
| B: Posted | Auto-timestamp |
| C: Platform | `X` / `LinkedIn` / `Both` |
| D: Post URL | Returned from Twitter/LinkedIn API |
| E: Keywords | `{{ $json.keywords.join(', ') }}` |
| F: Hashtags | `{{ $json.hashtags.primary }}` |
| G: Status | `published` / `failed` |
| H: Score | `{{ $json.score }}` |
| I: Image URL | Link to stored image |
| J: Notes | Any failure reason |

**Node config:**
- **Operation:** Append
- **Sheet ID:** (from your Google Drive — made by creating a Google Sheet)
- **Columns / Mapping:** Map the 10 fields above
- **Credential:** Google OAuth 2.0 (n8n official)

ⓘ *n8n node:* `Google Sheets` (official, works on all plans)
⚡ *Cost:* Free (Google API free tier)

---

## Complete n8n Workflow JSON Structure

```
{
  "name": "Content-to-Post Pipeline",
  "nodes": [
    { "name": "Webhook / Manual Trigger", "type": "n8n-nodes-base.webhook" },
    { "name": "Parse Input",              "type": "n8n-nodes-base.code" },
    { "name": "Research Keywords",        "type": "n8n-nodes-base.openAi" },
    { "name": "Generate Image",           "type": "n8n-nodes-base.httpRequest" },
    { "name": "Create Post",             "type": "n8n-nodes-base.openAi" },
    { "name": "Quality Score",           "type": "n8n-nodes-base.openAi" },
    { "name": "Quality Gate",            "type": "n8n-nodes-base.if" },
    { "name": "Post to X",               "type": "n8n-nodes-base.twitter" },
    { "name": "Post to LinkedIn",        "type": "n8n-nodes-base.httpRequest" },
    { "name": "Log to Google Sheets",    "type": "n8n-nodes-base.googleSheets" },
    { "name": "Human Review (pause)",    "type": "n8n-nodes-base.webhook" }
  ]
}
```

---

## Environment Variables Required

| Variable | Source | Purpose |
|----------|--------|---------|
| `OPENAI_API_KEY` | OpenAI account | Keyword research + content gen + scoring |
| `HF_API_KEY` | Hugging Face (free) | Image generation (Stable Diffusion via free tier) |
| `TWITTER_ACCESS_TOKEN` | Twitter Dev Portal | X posting |
| `TWITTER_ACCESS_SECRET` | Twitter Dev Portal | X posting |
| `LINKEDIN_CLIENT_ID` | LinkedIn Developer App | LinkedIn posting |
| `LINKEDIN_CLIENT_SECRET` | LinkedIn Developer App | LinkedIn posting |
| `LINKEDIN_PERSON_URN` | Your LinkedIn profile ID | LinkedIn posting (author field) |
| `GOOGLE_SHEETS_ID` | Your Sheet URL | Logging |
| `GOOGLE_SERVICE_ACCOUNT` | Google Cloud Console | Google Sheets access |

**Alternative to LinkedIn API:** If the OAuth setup is too heavy, use a **Webhook node** that fires to a small Cloudflare Worker or a `make.com` scenario (free tier — 1000 ops/mo) just for the LinkedIn post, then returns to n8n for logging.

---

## Content Format Detector (Carousel vs Post)

Add a **Code node** before Step 4 that decides output format:

```javascript
const points = $json.key_points || [];
const topic = $json.topic || '';

// Carousel triggers: 3+ distinct data-heavy points OR framework content
const carouselTriggers = [
  points.length >= 3 && topic.toLowerCase().includes('step'),
  points.length >= 3 && topic.toLowerCase().includes('framework'),
  points.length >= 3 && topic.toLowerCase().includes('process'),
  points.length >= 4,
];

if (carouselTriggers.some(Boolean) && $json.platform === 'linkedin') {
  return [{ json: { ...$json, format: 'carousel', slides: points.length } }];
}

return [{ json: { ...$json, format: 'post' } }];
```

**Carousel sub-workflow** (separate flow triggered by `format: "carousel"`):

```
For each slide:
  → OpenAI: generate slide headline + body (keep within visual boundaries)
  → HTTP Request: generate slide background image
  → Collect into array

After all slides:
  → Compose LinkedIn carousel post (text + "swipe through" indicator)
  → Post + log
```

---

## Cost Estimate per Run

| Step | Cost | Notes |
|------|------|-------|
| Parse | $0 | Code node, no API |
| Keywords | ~$0.001 | gpt-4o-mini, ~200 tokens |
| Image | $0 | Hugging Face free tier |
| Content | ~$0.002 | gpt-4o-mini, ~500 tokens |
| Quality | ~$0.001 | gpt-4o-mini, ~300 tokens |
| X post | $0 | Twitter API free tier |
| LinkedIn | $0 | LinkedIn API free |
| Sheets | $0 | Google API free tier |
| **Total** | **~$0.004** | **Less than half a cent per run** |

---

## Edge Cases & Error Handling

| Scenario | Handling |
|----------|----------|
| **Image API rate-limited** (HF) | `IF` node → check HTTP status 429 → retry after 5s delay (`Wait` node) → fallback to DALL-E if second retry also fails |
| **Twitter API down** | Log status as `x_failed` to Sheets, still post to LinkedIn |
| **LinkedIn auth expired** | `IF` → check 401 → trigger re-auth webhook → log as `linkedin_auth_failed` |
| **Content score < 70** | Pause via `Webhook` node → send Slack/email notification → wait for human approval callback |
| **Input missing fields** | `Code` node → throw descriptive error → response to caller with field list |
| **Carousel too many slides** | Cap at 5 slides max in the Code node → truncate key points to top 5 |

---

## Implementation Order

```
Phase 1 (core):
  1. Trigger + Parse + Keywords + Content Gen + Quality
  2. Google Sheets log
  3. X post (simplest official node)

Phase 2 (image):
  4. Hugging Face image generation
  5. Attach image to X post

Phase 3 (LinkedIn):
  6. LinkedIn API setup + HTTP Request node
  7. Image upload for LinkedIn

Phase 4 (carousel):
  8. Format detector Code node
  9. Carousel sub-workflow

Phase 5 (polish):
  10. Error handling + retries
  11. Human review webhook
  12. Scheduling (cron trigger for batch)
```

---

## Decisions Summary

| Decision | Choice | Why |
|----------|--------|-----|
| Image API | **Hugging Face** (free) | $0 cost, quality sufficient for social media. Fallback to DALL-E if rate limited. |
| LinkedIn | **HTTP Request → API v2** | n8n LinkedIn node requires premium. HTTP Request + OAuth is free with a 5-min setup. |
| LLM model | **gpt-4o-mini** | $0.15/M input tokens — ~10x cheaper than gpt-4o for negligible quality loss on short prompts. |
| Carousels | **Detect + sub-workflow** | Don't always generate carousels. Only for 3+ data-heavy points on LinkedIn. Keeps costs down. |
| Quality gate | **AI score ≥ 70** | Catches weak hooks and generic filler before publishing. Adjustable threshold. |
| Post timing | **Immediate (trigger-based)** | You control when to feed content. Add cron scheduling later if needed. |
