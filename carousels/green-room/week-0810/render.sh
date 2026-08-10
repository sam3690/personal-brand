#!/usr/bin/env bash
# Renders week-of-2026-08-10 media. Run from anywhere.
#   ./render.sh
# Outputs into ./out/ : three 1080x1350 PNGs + one 8-page PDF (the LinkedIn document post).
# Needs google-chrome and an internet connection (Google Fonts).
set -euo pipefail

cd "$(dirname "$0")"
mkdir -p out
CHROME=$(command -v google-chrome || command -v chromium || command -v chromium-browser)
# ponytail: virtual-time-budget is the whole webfont-race fix. No font downloads, no local server.
FLAGS="--headless --disable-gpu --no-sandbox --hide-scrollbars --virtual-time-budget=8000"

shot() {
  "$CHROME" $FLAGS --window-size=1080,1350 --screenshot="out/$2" "file://$PWD/$1" 2>/dev/null
  echo "  out/$2"
}

echo "PNG cards:"
shot post-1-story-card.html   1-story-card.png
shot post-2-studio-stats.html 2-studio-stats.png
shot post-4-before-after.html 4-before-after.png

echo "Carousel PDF (upload as a LinkedIn document post):"
"$CHROME" $FLAGS --print-to-pdf="out/3-carousel.pdf" --print-to-pdf-no-header \
  --no-pdf-header-footer "file://$PWD/post-3-carousel.html" 2>/dev/null
echo "  out/3-carousel.pdf"

echo
echo "Done. Two assets are still stand-ins until you export them from the design project:"
echo "  carousels/green-room/bg-main.png        (BG-MAIN flow-field, CSS approximation in use)"
echo "  carousels/green-room/headshot-round.png (author badge shows 'UA' initials until it lands)"
echo "Drop both in and re-run. No code changes needed."
