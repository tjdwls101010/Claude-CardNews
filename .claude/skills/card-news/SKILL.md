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

## Design Principles (Paperology-based tacit knowledge)

These principles are what distinguish professional card news from amateur output. They represent non-obvious design decisions learned from Paperology design philosophy and refined through iterative testing.

### Emphasis by Reduction, Not Addition
Dim non-essential text to gray (#888) instead of coloring keywords. This "gray dimming" technique is counter-intuitive but produces far more sophisticated results than colored highlights. Avoid red for general emphasis -- it signals danger. However, red can be used deliberately for urgency or confrontational messaging where that danger signal is the intended effect.

### Titles Are Conclusions, Not Topics (Tesla Rule)
Bad: "Temperature and Humidity Effects" / Good: "25C and 60% Humidity Are Essential for Growth"
Exception: Explanatory content can use question-format titles ("[What does this law do?]") and event content can lead with the event name + date. Match the title format to the content's purpose: persuade→conclusion, explain→question, announce→event.

### Density Is Quality
The #1 recurring quality issue is excessive whitespace. Professional card news typically fills 85-95% of the canvas -- though memorial, respectful, or contemplative content can use intentional whitespace as an emotional device. Sizing guidelines learned through 4 iterations at 1080x1350:
- Padding: 36-48px (never >50). Gaps: 12-24px (never >28)
- Titles: 72-96px. Illustrations/photos: 600-900px wide
- Background photos must fill the entire frame edge-to-edge
- **Squint test**: Read the PNG and squint. Large uniform-color areas with no content are dead zones

### Background Is Stage, Not Star
When text density is high, suppress the background (darken, blur, overlay). Always use gradient masks behind text over photos. Use glassmorphism panels for structured content over complex backgrounds.

### Character Consistency Across Series
The biggest visual quality issue in AI-illustrated series is inconsistent character/style across cards. Always provide the first card's finalized illustration as `--refs` for every subsequent generation, with explicit prompts: "same character, identical rendering style, same color temperature."

### Visual Review Loop (Never Skip)
Generate HTML -> convert to PNG -> Read every PNG -> check density, sizing consistency, illustration style, ending card fullness -> fix across ALL HTMLs at once -> reconvert -> re-read. This self-review catches issues before showing to the user.

### 3-Color Discipline
Lock 3 colors as CSS variables (primary + accent + neutral). 80% neutral tones, 20% accent. Extract dominant color from brand/topic.

### Bookending and Cinematic Endings
Open and close the series with matching visual tone. End with a vision statement or quote -- never "감사합니다" or "Thank you."

### Corner Anchors
Place small elements at all 4 corners (page number, brand name, date, decorative mark "+") for visual stability and framing.

### Font Weight as Hierarchy
Paperlogy 9 weights (100-900) in `assets/fonts/`. Use max 3 weights per card with strong contrast (400+800 good, 400+500 bad). Titles get letter-spacing -0.03 to -0.05em for chunky impact. Use weight 100 at 5% opacity for background watermark text.

### Tool Role Division
- **Pillow** (process_photo.py): mechanical, precise operations (crop, resize, composite, grayscale)
- **Nano Banana** (generate_image.py --input): creative AI edits (color grading, style transfer, mood change)
- **CSS filters**: render-time effects (grayscale, brightness, hue-rotate, blur, sepia)
- **rembg**: background removal for cutouts

### Edit, Don't Regenerate
If a Nano Banana image is 80% satisfactory, use edit mode (`--input`) to refine rather than regenerating from scratch.

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
