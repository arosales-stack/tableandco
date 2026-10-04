# Table & Co. — Project Notes for Claude

This repo is a single static website for **Table & Co.**, a vintage tableware
rental business in Cypress & Katy, Texas. Read this whole file before making
changes — it captures hard-won rules from earlier sessions, not just facts.

## What the business actually does

Table & Co. rents verified, inspected vintage china, crystal, and silverware
for events (weddings, showers, dinner parties, garden gatherings). The
differentiator versus big-box party rental or flea-market sourcing: every
piece is quality-checked and curated to actually coordinate together, not
sold/rented piecemeal.

Signature line: **"The art of the gathered table."**

Brand voice rules (from the brand book):
- Never lean on "luxury," "elegant," "stunning" as filler adjectives.
- Never crowd the page or over-explain. Say the thing plainly.
- Copy should state the actual value/service in concrete terms — not vague
  mood language. ("We rent real vintage china... for weddings, showers, and
  dinner parties" beats "Authenticated china, crystal, and porcelain —
  delivered, styled, and washed," which was rejected as too vague.)

## Hard rules established in this project (do not silently revert these)

1. **Color roles are fixed and non-negotiable:**
   - `--ink` (`#1b1a18`) is the **only** CTA/interactive color. Every button,
     link-as-button, and clickable control uses ink.
   - `--blue` (`#45627a`, "Willow Blue") is **decoration only** — ampersands,
     the italic accent in headings, the eyebrow color. It must **never**
     appear on anything clickable.
   - If you add a new button/CTA, it must be ink-filled (or ink-outlined on
     a dark section, inverted to paper/ink), never blue.

2. **No ambient/automatic motion, with exactly one explicit exception:**
   - No autoplay carousels, no scroll-reveal-on-load animations, no marquee
     tickers, no load-triggered fades anywhere on the site.
   - The **one exception**: the hero background is a 5-photo slideshow that
     auto-advances every 3 seconds with no user controls (no arrows/dots).
     This was an explicit, deliberate request — don't "fix" it by removing
     the motion, and don't add more auto-motion elsewhere by precedent.
   - User-triggered feedback (hover states, click-triggered carousel slides,
     click-to-expand panels) is fine and expected.

3. **Never fabricate specifics.** This project had a serious incident
   earlier where fake customer personas and fake testimonials were added as
   if real — treat that as a hard boundary, not a style note. If a fact
   (place-settings count, a testimonial, an occasion list) isn't confirmed,
   leave it as an explicit placeholder (e.g. `— place settings`) or ask.
   Never invent a plausible-sounding number or quote.

4. **Collections = cards, not one big carousel.** We prototyped a
   single-image-carousel treatment for the Collections section in a
   separate test file and the grid/card approach won (cards are parallel,
   comparable choices — better fit than sequential content). Each card has
   its own small internal photo carousel.

5. **"Learn more" expands inline — it is never a modal/popup/separate
   screen.** Earlier versions used a quick-view modal overlay; it was
   explicitly removed because the user wants details ("Best for," "Style,"
   "Place settings," extra description, CTA) to unfold in place under the
   card (`.collection-details` / `.collection-details-inner`, toggled by
   `toggleCollectionDetails(this)`), mobile-first. Don't reintroduce a
   modal for this.

6. **Fact rows must stay readable when the value wraps.** In
   `.collection-modal-fact` rows, the label (`span:first-child`) is
   `white-space: nowrap` and pinned left; the value (`span:last-child`) is
   `text-align: right` and allowed to wrap — so a long "Best for" value
   still ends flush right instead of drifting left and looking ragged.

7. **Real product/detail photos are never cropped.** `.carousel-track img`
   and `.collection-modal-image img` use `object-fit: contain` (not
   `cover`), inside a portrait `aspect-ratio` box, with a `var(--card)`
   background for any letterboxing — because the real photography is
   portrait-oriented and cropping it (especially top/bottom) cuts off the
   table setting. The **hero background** is the one place that still uses
   `object-fit: cover`, because it's a full-bleed landscape treatment with
   a heavy dark gradient over it — that's intentional, don't "fix" it to
   match the card photos.

8. **All CTAs read "Request a quote."** Not "Reserve your table" — that
   was the original copy and was explicitly changed everywhere, including
   nav, hero, and the inquiry section.

9. **Mobile nav must fit on one line at every breakpoint.** The logo and
   "Request a quote" button in `<nav>` have dedicated sizing at both
   `@media (max-width: 900px)` and `@media (max-width: 480px)` — they were
   first shrunk too aggressively (hard to read) and then fixed by sizing
   up while re-verifying with real headless-browser screenshots at 320 /
   375 / 390 / 430px that they still never wrap to a second line. If you
   touch nav sizing, **re-verify with a screenshot at those widths** rather
   than eyeballing the CSS — guessing got this wrong twice already.

10. **Desktop collections-row nav ("← Previous / Next →") is
    center-aligned**, not right-aligned — `.collections-nav` uses
    `justify-content: center`.

11. **Mobile has no "carousel of carousels."** At ≤900px the collections
    row (`.collections-grid`) switches from horizontal-scroll to normal
    wrap and each `.collection-card` goes full-width, stacking vertically.
    Each card keeps its own small internal photo carousel, but that's one
    layer, not nested inside a second horizontal-scroll layer.

## Verifying changes — don't just eyeball CSS

Chromium + Playwright are preinstalled in the Claude session
(`/opt/pw-browsers/chromium`, both Python and Node bindings work). For any
layout/responsive change — nav sizing, card alignment, modal/expand
behavior — **render the actual file with Playwright at real phone widths
(320/375/390/430px) and screenshot it** before pushing. This project has
had multiple rounds of "fixed" CSS that wasn't actually verified and turned
out wrong. A quick pattern:

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 390, "height": 844})
    page.goto("file:///home/claude/tableandco/index.html")
    page.screenshot(path="/tmp/check.png")
```

For `index.html`, the file contains large embedded base64 images — **never
read/print the raw file with the generic file tools** (it will blow the
context budget). Strip base64 payloads first when you need to inspect
structure:

```python
import re
content = open('index.html', encoding='utf-8').read()
stripped = re.sub(r'(data:image/\w+;base64,)[A-Za-z0-9+/=]+', r'\1BASE64_OMITTED', content)
open('/tmp/stripped.html', 'w', encoding='utf-8').write(stripped)
```
Then read/grep the stripped copy, and make edits on the real file using
exact-string Python replacements anchored on surrounding markup (never on
the base64 itself).

## Site structure (`index.html`, single self-contained file)

No build step, no framework, no separate asset files — everything
(including every photo) is inline in one HTML file: inline `<style>`,
inline `<script>`, images as `data:` URIs. This is deliberate; don't split
it into multiple files or add a bundler unless explicitly asked.

Section order top to bottom:
1. `<nav>` — fixed, logo + nav links (desktop only) + "Request a quote" CTA
2. `<!-- HERO -->` — full-bleed 5-photo auto-slideshow, headline, CTAs
3. `<!-- CHECKPOINTS -->` — dark trust-signal strip (4 short claims)
4. `<!-- COLLECTIONS -->` — intro + horizontally-scrollable card row +
   inline-expand details per card (no modal)
5. `<!-- WHY -->` — "Why Table & Co." section (moved to *after* Collections
   per explicit request — don't move it back before Collections)
6. `<!-- INQUIRY -->` — contact form
7. `<footer>`

Note: there is **no "How It Works" section** — it was built, then fully
deleted (including its nav link and all its CSS) per explicit request.
Don't rebuild it.

### Collections (6 total, as of this writing)

| # | Name | Status |
|---|------|--------|
| 1 | Amberidge Collection | **Real photos** (6, ordered medium→closer→further→closer→further→detail per explicit request). Place-settings count still unconfirmed — ask Audra, don't guess. |
| 2 | The Harvest Table | Placeholder photos, has real copy (16 place settings, stoneware/autumn) |
| 3 | The Gilded Edge | Placeholder photos, has real copy (8 place settings, gold-rimmed/crystal/weddings) |
| 4 | The Willow Set | Placeholder photos, has real copy (10 place settings, blue-and-white transferware — name/copy invented by Claude as a tie-in to the Willow Blue brand color, flagged to Audra at the time) |
| 5 | Collection Five | Full placeholder — no real name/photos/details given yet |
| 6 | Collection Six | Full placeholder — no real name/photos/details given yet |

Each card = one `.collection-card` containing a `.carousel` (own photo
carousel, arrows+dots consolidated into one bottom `.carousel-nav` bar —
not two floating circles) + `.collection-body` (name, short desc, tag,
"Learn more" toggle, and the `.collection-details` inline-expand panel).

### Key CSS custom properties (`:root`)

```
--paper: #f1ece4       porcelain bone background
--card: #f8f5ef         raised warm white (cards, letterbox fill)
--ink: #1b1a18          ONLY CTA/interactive color, primary text
--blue: #45627a         Willow Blue — decoration ONLY, never clickable
--blue-deep: #38505f
--ash: #9e978b          secondary/muted text
--line / --line-soft    hairline borders
```

Typography: **Bodoni Moda** (serif, display/headings, italic for the
ampersand/emphasis) + **Archivo** (sans, body/UI/labels), both via Google
Fonts `<link>` tags.

## Deployment: GitHub → Cloudflare Pages

- Repo: `arosales-stack/tableandco`, default branch `main`.
- **Cloudflare Pages is connected directly to this GitHub repo** via
  Cloudflare's own dashboard "Connect to Git" integration — it watches
  `main` and redeploys automatically on every push. Build command: none.
  Output directory: `/` (root) — it's a static `index.html`, nothing to
  build.
- We *also* tried a GitHub Actions workflow
  (`cloudflare/pages-action`) as an alternative deploy path early on, but
  **removed it** once the direct Cloudflare↔GitHub dashboard connection was
  confirmed working, to avoid two competing deploy pipelines firing on the
  same push. **Don't re-add a GitHub Actions deploy workflow** unless the
  dashboard connection is first disconnected — check with Audra before
  adding any `.github/workflows/` deploy step.
- Claude's GitHub App has push access to this repo (was explicitly granted
  via `https://github.com/apps/claude/installations/select_target`). Normal
  workflow: edit `index.html` directly, commit, `git push origin main` — no
  feature branches, no PRs. Audra has consistently asked for direct-to-main
  pushes on this project, not a dev/review branch flow.
- There is no GitHub Pages fallback in use — Cloudflare Pages is the live
  deployment target.

## Working style on this project (current stage, not a fixed rule)

- Right now, **push straight to `main`**, no branches/PRs — this is just
  where the project is (pre-domain, Cloudflare Pages deploying straight
  from `main`), not a permanent policy.
- **This will change.** Once the site is connected to the real domain,
  Audra has said she'll move to a `dev` branch workflow — expect a future
  instruction to start branching changes and only pushing to `main` (or
  merging) when she says so. When that happens, update this file instead
  of relying on this note.
- When a request is ambiguous about *which* collection/section "the first
  one" or "that one" refers to, infer from context (position in the grid,
  what was just discussed) but say plainly what you assumed.
- Keep responses about *what changed*, not a recap of every step taken.
