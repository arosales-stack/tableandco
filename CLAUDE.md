# Table & Co. — Project Notes for Claude

This repo is a single static website for **Table & Co.**, a vintage tableware
rental business in Cypress & Katy, Texas. Read this whole file before making
changes — it captures hard-won rules from earlier sessions, not just facts.

> Full brand, typography, colour, and collections reference: see `BRAND.md`.

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
   - The **one exception**: the hero background is a multi-photo slideshow (currently 9) that
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

10. **Desktop collections-row nav = round ink side arrows only**
    (`.collections-side`, left/right of the photos). The "← Previous / Next →"
    text nav under the cards was removed at Audra's request — don't re-add it.
    On desktop (≥901px) cards share rows via CSS subgrid (photo / title / text /
    meta / details) so "Learn more" and the piece count align across cards.
    Checkpoints strip is one line at ≥1200px; hero is `min-height: 100vh`.
    Instagram handle: **@table.andcompany**.

11. **Mobile has no "carousel of carousels."** At ≤900px the collections
    row (`.collections-grid`) switches from horizontal-scroll to normal
    wrap and each `.collection-card` goes full-width, stacking vertically.
    Each card keeps its own small internal photo carousel, but that's one
    layer, not nested inside a second horizontal-scroll layer.

Collection short descriptions (`.collection-desc`) are capped at 300 characters (Audra).

Each collection's details panel has 4 fact rows in this order: Time period, Place settings (or Pieces), Best for, Style. Field limits (so text never breaks the layout): desc 300, tag 20, Time period 25, Place settings/Pieces 20, Best for 80, Style 50, extra paragraph 200. `.collection-details.expanded` max-height is 900px to fit worst-case text.

## Typography minimums (Audra: never make text tiny)

Body copy >= 1rem, secondary text >= ~0.875rem, uppercase labels >= ~0.76rem,
form inputs 1rem (prevents iOS zoom). The collections intro has no right-hand
label — "No AI here" was removed at Audra's request; do not re-add it.

## MANDATORY editing protocol (added after the Oct 11 broken-carousel incident)

A blind string slice left `<span class="` unclosed in the Cherub Bleu dots, which
swallowed the nav and merged two cards on the live site. These rules are not optional:

1. **Read before you edit.** At the start of any session that will change
   `index.html`, read the ENTIRE file once (stripped copy, base64 removed — see
   below) before the first edit. Re-read the affected card/section's markup again
   right before editing it. No editing from memory or from a summary.
2. **Never edit by character position.** No `s[:k][:-n]`, no slicing by offsets,
   no regex that deletes "the last N chars". Replace whole, exact, asserted
   blocks (e.g. an entire `.carousel-dots` div) anchored on unique surrounding
   markup, and assert `count == 1` before replacing.
3. **Run `python3 scripts/check_site.py` before every commit.** It parses the
   HTML (tag balance), checks every card has matching img/dot counts, 2 arrows,
   one carousel and no nesting, 6 cards, no horizontal overflow at 320/390/1440,
   and no JS errors. It must print `OK`. If it prints `FAIL`, do not commit.
4. **Look at the result.** Screenshot (390px) every card you touched AND the card
   below it. Counts passing is not proof the page looks right.
5. **Check which branch you are on** (`git branch --show-current`) before
   committing, and make changes on `main` unless told otherwise.
6. **Verify the push landed:** after pushing, run `git ls-remote origin` and
   confirm `main` (and `dev`) show the new commit SHA, then check the Cloudflare
   check-run for that SHA. Never report "live" before that.
7. Never touch the site unless Audra explicitly asks (unchanged rule).

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
2. `<!-- HERO -->` — full-bleed 9-photo auto-slideshow (full screen height on mobile), headline, CTAs
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
| 1 | Amberidge Collection | 6 real photos (green-rimmed floral china). Copy is placeholder again — Audra's red-transferware text belongs to The Rose Garden (swapped Oct 12). |
| 2 | The Harvest Fête (brown transferware) | 5 real photos (brown transferware). Copy (16 place settings, stoneware/autumn) predates the photos; no text from Audra yet. |
| 3 | Versailles Garland Collection | 4 real photos. Copy from Audra's text (Haviland & Co. Limoges, early 1900s, 65 pieces). Shown as "65 pieces", not place settings. |
| 4 | Cherub Bleu Collection | 6 real photos. Copy from Audra's text (vintage blue & white, made in England; date unconfirmed so not shown). Place-settings count unconfirmed (earlier "10" was invented, removed). |
| 5 | Garden Party Collection | 6 real photos. Copy/occasions from Audra's text ("mix & match", story still to be defined). Place-settings count unconfirmed. |
| 6 | The Rose Garden Collection | 4 real photos (pink-bordered rose china). Copy from Audra's text for the red Woods Ware transferware (Staffordshire). Place-settings count unconfirmed. |

Names follow Audra's OneDrive folders (Amberidge, Rose Garden, Cherub Bleu, Versailles Garland, Garden Party). Never touch the site without an explicit instruction from Audra.

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
  via `https://github.com/apps/claude/installations/select_target`). Current
  workflow: edit `index.html` directly, commit, `git push origin main`. This is
  a current-stage convention, not a rule (see Working style below).
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
