# Table & Co. — Brand & Project Context

Everything about the business, brand, and how the site behaves, beyond the code.
Source: Brand Book Vol. 01 (2026) plus decisions made with Audra while building the site.
Companion file: `CLAUDE.md` (hard rules, deployment, working style). If the two disagree, ask Audra.

## 1. The business
- **Table & Co.** — vintage tableware rental house in **Cypress & Katy, Texas** (NW Houston).
- Rents verified, inspected vintage china, crystal and silverware (the brand book also says porcelain) for weddings, showers, dinner parties, garden gatherings, birthdays, holidays.
- Service: delivered, hand-packed, styled, collected, and washed by us. "The host's only job is to host."
- Owner/contact on this project: Audra Rosales. Instagram is linked in the footer.
- Signature line: **"The art of the gathered table."**
- Brand essence: heirloom-grade tablescapes, made effortless.
- Mission: make the beauty of a thoughtfully set table accessible for every celebration across NW Houston, without the cost, storage, or risk of owning it.
- Vision: the trusted name for the table in greater Houston, the first call for a host, planner or couple.

## 2. Positioning
For design-minded hosts and planners in Cypress & Katy who want a characterful table without owning one. Unlike big-box party rental or unpredictable flea-market sourcing, every piece is quality-checked and curated to work together.
Differentiators:
1. Verified, not flea-market (no chips, no cracks)
2. Curated to coordinate (collections layer together)
3. Full white-glove service (deliver, pack, collect, wash)
4. Local & personal (we know the venues and neighborhoods)

## 3. Audience
- **Primary, the Host:** women ~28–55 in Cypress, Katy, NW Houston; dinner parties, bridal/baby showers, milestone birthdays, holidays. Design-aware, active on Instagram and Pinterest.
- **Secondary, the Planner:** wedding/event planners needing consistency, range, depth.
- **Tertiary, the Couple:** millennial/Gen-Z couples drawn to vintage character over banquet uniformity.
- Do NOT invent personas, testimonials, or customer stories on the site (an earlier incident; see CLAUDE.md).

## 4. Voice
Refined, warm, considered, confident, characterful. Speaks like a well-travelled host with excellent taste. Plain and concrete; states the actual service.
- Do: speak plainly like an invitation; lead with beauty, service, ease; use "verified", "curated", "by the setting"; let white space breathe.
- Don't: shout, hard-sell, use exclamation marks; use "luxury", "elegant", "stunning" as filler; crowd or over-explain; use emoji or slang.
- Audra rejected vague mood copy ("Authenticated china, crystal, and porcelain — delivered, styled, and washed"). Hero copy must say what we do. Open question: shorter hero line proposed ("Verified vintage china, crystal & silverware for your event — delivered, styled, and picked up after. You host. We handle the rest."); not yet approved, live site still has the longer "We rent real vintage china…" line.
- All CTAs read **"Request a quote."**

## 5. Logo
Wordmark "TABLE & CO" in Bodoni Moda, all caps, wide-tracked; the ampersand is always italic Willow Blue (Bone on dark grounds). Single colour, no shadows/outlines/gradients, never stretched or recoloured. Variations: horizontal (primary), stacked, T&C monogram, ampersand mark (favicon). Clear space = cap height. Min size 22px on screen; below that use monogram/ampersand.

## 6. Colour
| Name | Hex | Role |
|---|---|---|
| Ink | `#1b1a18` | Primary text, dark grounds, and the ONLY CTA/interactive colour |
| Porcelain Bone | `#f1ece4` | Primary background (`--paper`) |
| Willow Blue | `#45627a` | Signature accent, decoration ONLY (ampersands, italic heading accent, eyebrows). Never on anything clickable |
| Ash Grey | `#9e978b` | Secondary/muted text |
| Warm White | `#f8f5ef` | Cards, raised surfaces, photo letterbox fill (`--card`) |
| Deep Willow | `#38505f` | Hover/depth (`--blue-deep`) |
Balance: Bone ~60, Ink ~24, Ash ~10, Blue ~6. On dark sections, buttons invert to paper/ink.

## 7. Typography
- **Bodoni Moda**: display, headlines, logo (italic for ampersand/emphasis). Brand book: fixed optical size (opsz 16), weights 400/500/600.
- **Archivo**: body, UI, labels, buttons, forms (300–600). Eyebrows/labels in caps with wide tracking.
- Both loaded via Google Fonts `<link>`.
- **Size minimums (Audra: never tiny; based on 16px body / 44px touch-target research):**
  - Body copy ≥ 1rem (16px); hero paragraph 1.1–1.15rem
  - Secondary text ≥ ~0.875rem
  - Uppercase labels/eyebrows ≥ ~0.76–0.8rem, tracking trimmed so they don't overflow
  - Form inputs 1rem (prevents iOS zoom)
  - Collection name 1.6rem; collection description 1rem; why-section headings 1.4rem; pull quote 1.9rem
  - Nav: logo 1.05rem (0.95rem ≤480px), CTA 0.8rem (0.76rem ≤900px, 0.7rem ≤480px). Must stay on ONE line at 320/375/390/430px; verify with screenshots.

## 8. Art direction
Editorial and calm. Natural daylight, generous negative space, muted bone–ink–blue palette; one setting or close detail per frame. Avoid fluorescent/flash, heavy filters, clutter, busy backgrounds behind the logo. Product photos are portrait and are never cropped (`object-fit: contain` in a 3:4 box, Warm White letterbox). Collections intro states "No AI here" (Audra's wording; real photography only).

## 9. Site structure (top to bottom)
1. Fixed nav: logo, links (desktop only), "Request a quote".
2. Hero: full-bleed 3-photo slideshow, auto-advances every 3s, no controls (the single allowed ambient motion), dark gradient for legibility, eyebrow, headline, copy, two CTAs.
3. Checkpoints: dark strip with 4 trust claims (every piece inspected, delivered/styled/collected, we wash every glass & plate, rooted in Cypress & Katy). Left-aligned, NOT centered; generous top/bottom padding (3.25rem desktop, 2.5rem mobile); stacked in a column on mobile.
4. Collections: eyebrow, headline "Every piece has a story. *Yours is next.*", the line "No AI here", then cards.
5. Why Table & Co. (stays after Collections).
6. Inquiry form.
7. Footer.
No "How It Works" section (deleted on request; don't rebuild).

## 10. Collections behaviour
Six collections, shown as e-commerce-style cards (not one big carousel; parallel choices compare better).
- **Card:** own small photo carousel (arrows + dots merged into a single bottom bar, no floating circles), name, short description, tag, "Learn more".
- **Desktop:** cards in a horizontal scroll row (~300px wide), with centered "← Previous / Next →" text controls underneath.
- **Mobile (≤900px):** no carousel of carousels. The row becomes a normal vertical stack, each card full-width, one after another. Each card keeps only its own internal photo carousel.
- **Learn more:** expands inline under the card (never a modal/popup/new screen): Best for, Style, Place settings, extra description, "Request a quote" button. Fact rows: label left (nowrap), value right-aligned and may wrap.

| # | Name | Status |
|---|---|---|
| 1 | Amberidge Collection | Real photos (6; order: medium, closer, further, closer, further, detail). Place-settings count unknown, shows "—"; ask Audra |
| 2 | The Harvest Fête (renamed from The Harvest Table) | 7 real photos; 16 place settings, stoneware, autumn |
| 3 | The Gilded Edge | Placeholder photos; 8 place settings, gold-rimmed, crystal, weddings |
| 4 | The Willow Set | Placeholder photos; 10 place settings, blue-and-white transferware (name/copy invented by Claude as a Willow Blue tie-in, flagged to Audra) |
| 5 | Collection Five | Full placeholder, awaiting real details |
| 6 | Collection Six | Full placeholder, awaiting real details |
Never invent counts, names, or testimonials; leave `—` or ask.

## 11. Hosting & workflow
Single self-contained `index.html` (inline CSS/JS, base64 images). GitHub `arosales-stack/tableandco`, branch `main` → Cloudflare Pages (connected via dashboard; no build, output `/`). No GitHub Actions deploy. Currently push straight to `main`; Audra will move to a `dev` branch once the real domain is connected (a current convention, not a rule). Details in `CLAUDE.md`.

## 12. Open items
- Approve/reject the shorter hero copy.
- Amberidge place-settings count.
- Real names, photos, details for Collections 5 and 6 (and real photos for 2–4).
