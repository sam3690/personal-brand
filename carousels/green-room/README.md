# Green Room — brand design kit (v1.2)

Synced from the Claude Design project **"Brand system design for social media carousels"**:
https://claude.ai/design/p/5790bcce-f02c-4647-a1dd-9837aee8c75f

Full token/spec writeup: [`../../content/knowledge-base/brand-design-system.md`](../../content/knowledge-base/brand-design-system.md).
Second-brain note: [`../../content/brain/Brand Design System.md`](../../content/brain/Brand%20Design%20System.md).

## What's in this folder
- `brand-system.dc.html` — the full interactive design-system reference (colors, type, every component, sample slides). Open in a browser to eyeball tokens.
- `carousel-multichannel-outbound.dc.html` — the finished 9-slide carousel for the "Single-channel outreach is losing you the deal" LinkedIn post (`content/drafts/week-of-2026-07-20/2-multichannel-carousel.md`, Wed 2026-07-22 slot). Keyboard-navigable deck (←/→, number keys).
- `carousel-multichannel-outbound-print.dc.html` — same deck, print-optimized (`@media print` rules, no on-screen nav chrome). This is the one to feed to `google-chrome --headless --print-to-pdf` (same pipeline already used for `../carousel.html`, permission already granted in `../.claude/settings.local.json`).
- `support.js`, `deck-stage.js` — the runtime these decks need (self-loads React/ReactDOM/Babel from unpkg at render time, so an internet connection is required — same assumption `../carousel.html` already makes for Tailwind/Google Fonts CDN).
- `grain.png` — the texture overlay asset. Synced complete.

## ⚠️ Two assets still missing (manual step)
`get_file` on the design MCP caps at 256 KiB, and these two exceed it — they came back truncated/corrupted, so they are **not** included here:
- `bg-main.png` — the one background used behind every slide/banner/CTA (deep emerald flow-field, grain baked in). Referenced everywhere as `background-image:url('bg-main.png')`.
- `headshot-round.png` — the round author-badge headshot on every carousel slide.

**To finish the sync:** open the project link above → click each asset → download → save into this folder (`carousels/green-room/`) using those exact filenames. Once both are present, every `.dc.html` in this folder renders correctly with no other changes.

Until then, the decks will show broken-image placeholders where the background/headshot should be — text, layout, colors, and fonts are otherwise fully correct.

## Rendering to PNG/PDF
```
google-chrome --headless --disable-gpu --print-to-pdf=carousel.pdf \
  --print-to-pdf-no-header \
  "carousel-multichannel-outbound-print.dc.html"
```
Or open `carousel-multichannel-outbound.dc.html` directly in a browser and use its keyboard nav / screenshot each slide at 1080×1350.

## Status vs. the older kit
`../carousel.html` and `../linkedin-banner.html` (Tailwind, emerald/gold/Playfair Display) are the **previous** kit — still functional, not deleted, but **Green Room is now the standard** going forward per brand-design-system.md.
