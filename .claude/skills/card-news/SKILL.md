---
name: card-news
description: Generate visually polished, information-optimized card news images from any topic or content. Designs in HTML, converts to PNG, and generates custom illustrations via Nano Banana API. Use this skill whenever the user asks for card news, infographics, SNS content, summary cards, Instagram cards, slide design, visual explainers, or any visual content creation request -- even if they don't explicitly say "card news".
---

# Card News Generator

Generate 5-10 card news images (1080x1350px, 4:5) as HTML, convert to PNG. Two visual asset paths: AI-generated illustrations (Nano Banana) or user-provided photos (Pillow/rembg).

**Activate venv before any script:** `source <skill_dir>/scripts/.venv/bin/activate`

## Scripts (black-box tools -- do NOT read source code)

**generate_image.py** -- Nano Banana API (text-to-image, edit, multi-reference, batch)
```
--prompt "..." --output out.png [--aspect-ratio "1:1"] [--input edit.png] [--refs ref1.png ref2.png]
--batch batch.json  # [{"prompt":"...","output":"...","aspect_ratio":"1:1","refs":["ref.png"]}]
```

**html_to_png.py** -- Playwright HTML-to-PNG (2x retina)
```
html_to_png.py ./outputs/                    # directory
html_to_png.py card.html --output card.png   # single file
```

**process_photo.py** -- Pillow (crop, resize, grayscale, adjust, composite, batch)
```
--crop 4:5 --input photo.jpg --output cropped.png
--resize 1080x1350 --input photo.jpg --output resized.png
--grayscale --input photo.jpg --output bw.png
--brightness 0.7 --contrast 1.3 --input photo.jpg --output adj.png
--composite layout.json --output collage.png  # {"canvas":{...},"layers":[{...}]}
--batch batch.json  # [{"action":"crop","input":"...","output":"...","ratio":"4:5"}]
```

**rembg** -- background removal: `rembg i in.png out.png` / `rembg p dir_in/ dir_out/`

---

## Workflow

Communicate with the user via **AskUserQuestion** at each phase transition.

### Phase 1: Content Analysis
- Extract 3 core messages, simplify jargon to middle-school level
- Plan card series: Cover (card 1) / Body cards / Ending (last card)
- -> **AskUserQuestion**: confirm card structure

### Phase 2: Design Planning
- **If user provided reference design images:** Read each image to analyze its visual language -- color palette, background treatment (dark/light/textured), layout structure, typography weight and spacing, overall emotional tone. Extract these as the style direction for the current project. The reference images tell you *what style to aim for*; the design principles tell you *why it works*.
- 3-color palette (primary + accent + neutral), lock as CSS variables
- Match visual tone to content emotion -- not all content is dark and dramatic. Serious politics can be dark navy; informational content can be light and clean; memorial content can be soft and muted; youth/casual content can be bright and playful
- Match layout pattern to content semantics (timeline->LR, narrative->TB, comparison->Z)
- Choose illustration aspect ratios per card based on placement
- -> **AskUserQuestion**: present palette/tone options

### Phase 3: Visual Assets

**Path A -- User photos:** Read photos -> crop/resize with process_photo.py -> decide treatment per photo (rembg for cutouts, Nano Banana edit mode for color/mood, CSS filters for render-time effects) -> integrate into HTML

**Path B -- AI illustrations:** Generate 2-3 style variations in batch -> AskUserQuestion to pick style -> fine-tune with edit mode -> use first card's image as `--refs` for ALL subsequent cards to maintain character/style consistency -> rembg for background removal on dark cards

### Phase 4: HTML Generation + Visual Review Loop
1. Generate all HTML cards (images as separate files, NOT base64)
2. Convert all to PNG with html_to_png.py
3. **Read every PNG** to visually evaluate
4. If density/sizing/consistency issues found: fix CSS across ALL HTMLs at once, reconvert, re-read
5. Repeat until all cards pass inspection
6. -> **AskUserQuestion**: show finals, collect feedback

---

## Design Principles

Three-layer system: **Foundation** (structural logic) → **Techniques** (execution) → **Signature Style** (Paperology defaults). For deep explanations and examples, consult `references/design-principles.md`.

### Foundation: CRAP (apply in this order)
1. **Proximity** -- Related elements close, unrelated elements far. Gap ratio ~3:1 (intra-group 8-16px, inter-group 32-48px). Squint test: 2-4 visual clusters per card.
2. **Alignment** -- Every element on an invisible shared edge. One alignment axis per card (flush-left default for body cards). No trapped white space between misaligned elements.
3. **Repetition** -- Lock all design tokens in `:root` CSS variables (colors, spacing, typography). Same treatment patterns across the entire series. Repetition is what makes 8-10 cards feel like one brand.
4. **Contrast** -- If not the same, make VERY different. Weight gap minimum 200 units (400+800 good, 400+500 = conflict). Size ratio minimum 2:1. Stack 2-3 contrast dimensions per hierarchy level (size + weight + form). Don't be timid.

### Key Techniques
- **Emphasis by reduction**: Dim non-essential text to gray (#888) instead of coloring keywords. Accent 1-2 keywords only.
- **Titles as conclusions (Tesla Rule)**: Bad: "EV Market Status" / Good: "EV Sales Surge 42% YoY." Exception: question-format for explanatory, event name for announcements.
- **Color selection**: Choose colors by wheel relationship (complementary→energy, analogous→calm, split complement→sophistication). Shift to tints/shades (HSL L=25-40% or 65-85%) to escape cliché. Warm accents need less area (10-15%), cool need more (20-25%).
- **Typography contrast**: 5 dimensions available with Paperlogy -- Size, Weight, Form (caps/lowercase), Typographic color (density), Direction. Each hierarchy level differs in 2-3 dimensions simultaneously. Reverse type (white on dark) needs heavier weight / larger size.
- **Background as stage**: Suppress when text density is high. Gradient masks follow text position. Glassmorphism for complex backgrounds.
- **Density**: 85-95% canvas utilization. Enemy is trapped white space (accidental gaps), not white space itself. Padding 36-48px, titles 72-96px, body 24-28px, illustrations 600-900px. Background photos full-bleed.
- **Bookending**: Match cover and ending card visual tone. End with vision statement, never "감사합니다."

### Signature Style (Paperology defaults -- evaluate per content tone)
- **Corner Anchors**: Apply for informational/business. Evaluate for casual. Likely omit for emotional/minimal.
- **Background Typography**: Weight 900, 150-200px, opacity 3-5% for low-density cards. Omit when text density is already high.
- **Decorative Shapes**: Opacity 0.08-0.15, only when serving a structural role. Don't fill space just because it's empty.

### Operational
- **Character Consistency**: First card's finalized illustration as `--refs` for all subsequent generations.
- **Visual Review Loop (Never Skip)**: Generate HTML → PNG → Read every PNG → check against Foundation diagnostics → fix ALL HTMLs at once → reconvert → re-read.
- **Tool Roles**: Pillow = mechanical precision. Nano Banana = creative AI edits. CSS filters = render-time effects. rembg = background removal.
- **Edit, Don't Regenerate**: If a Nano Banana image is 80% satisfactory, use `--input` to refine.

---

## HTML Rules (only non-obvious ones)

- Images as separate files referenced by path -- never base64 (bloats HTML to megabytes)
- `@font-face` with absolute paths to `assets/fonts/`
- `word-break: keep-all` for Korean text
- Fixed viewport: `width:1080px; height:1350px; overflow:hidden; position:relative`
- After rembg, apply white glow on dark backgrounds: `filter: drop-shadow(0 0 30px rgba(255,255,255,0.2))`

---

## References

Consult these only when you need deeper technique details:
- `references/design-principles.md` -- Paperology design philosophy and advanced techniques
- `references/image-prompt-guide.md` -- Nano Banana prompt patterns for card news illustrations
- `references/css-patterns.md` -- CSS code patterns for common card news layouts and effects
- `references/photo-processing-guide.md` -- Photo processing decision criteria and patterns
