---
name: card-news
description: Generate visually polished, information-optimized card news images from any topic or content. Designs in HTML, converts to PNG, and generates custom illustrations via Nano Banana API. Use this skill whenever the user asks for card news, infographics, SNS content, summary cards, Instagram cards, slide design, visual explainers, or any visual content creation request -- even if they don't explicitly say "card news".
---

# Card News Generator

Generate a series of 5-10 card news images from user-provided topics/content. Each card is designed as an individual HTML file, enriched with AI-generated illustrations, and converted to a final PNG image.

## Tech Stack

- **Design**: HTML (single file per card, inline CSS/SVG) + Paperlogy font (9 weights)
- **Illustrations**: Nano Banana API (gemini-3.1-flash-image-preview)
- **Background removal**: rembg (use when needed)
- **PNG conversion**: Playwright
- **Card size**: 1080x1350px (4:5 ratio, Instagram portrait)

Scripts directory: `scripts/` relative to this skill file
Font directory: `assets/fonts/` relative to this skill file

**IMPORTANT: Always activate the virtual environment before running any script:**
```bash
source <skill_dir>/scripts/.venv/bin/activate
```

---

## Scripts Reference (use as black-box tools -- do NOT read source code)

### generate_image.py -- Nano Banana Image Generation

**Single image (text-to-image):**
```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "A 3D clay style friendly robot icon with glowing cyan eyes, soft rounded edges, matte texture. White background. No text." \
  --aspect-ratio "1:1" \
  --output ./images/card1_illust.png
```

**Single image (edit existing image):**
```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "Change the background color to dark navy blue, keep everything else identical" \
  --input ./images/card1_v1.png \
  --output ./images/card1_edited.png
```

**Single image (with style reference):**
```bash
python <skill_dir>/scripts/generate_image.py \
  --prompt "A 3D clay style icon of a book with sparkles, same visual style as reference" \
  --refs ./images/card1_final.png \
  --aspect-ratio "1:1" \
  --output ./images/card2_illust.png
```

**Batch mode (parallel generation -- preferred for multiple images):**
```bash
# First, write a batch JSON file:
cat > batch.json << 'EOF'
[
  {"prompt": "...", "output": "./images/v1.png", "aspect_ratio": "1:1"},
  {"prompt": "...", "output": "./images/v2.png", "aspect_ratio": "1:1"},
  {"prompt": "...", "refs": ["./images/ref.png"], "output": "./images/v3.png", "aspect_ratio": "16:9"}
]
EOF

# Then run:
python <skill_dir>/scripts/generate_image.py --batch batch.json
```

**Parameters:**
- `--prompt` (required for single mode): English, narrative description
- `--output` (required for single mode): Output PNG file path
- `--aspect-ratio` (optional, default "1:1"): Supported values: 1:1, 1:4, 1:8, 2:3, 3:2, 3:4, 4:1, 4:3, 4:5, 5:4, 8:1, 9:16, 16:9, 21:9
- `--input` (optional): Input image for editing mode
- `--refs` (optional): One or more reference images for style consistency
- `--batch` (optional): Path to JSON file for parallel batch generation

### html_to_png.py -- HTML to PNG Conversion

**Convert all HTML files in a directory:**
```bash
python <skill_dir>/scripts/html_to_png.py ./outputs/
```

**Convert a single HTML file:**
```bash
python <skill_dir>/scripts/html_to_png.py ./outputs/card_01.html
```

**Convert with custom output path:**
```bash
python <skill_dir>/scripts/html_to_png.py ./outputs/card_01.html --output ./final/card_01.png
```

Output: PNG at 1080x1350px viewport, 2x device scale (actual 2160x2700px retina resolution).

### rembg -- Background Removal

**Single file:**
```bash
rembg i input.png output.png
```

**Batch (entire directory):**
```bash
rembg p ./images_raw/ ./images_nobg/
```

---

## Workflow

**Actively communicate with the user via AskUserQuestion at each phase.**

### Phase 1: Content Analysis

1. Extract **3 core messages** from the user's topic/content
2. Simplify jargon to middle-school comprehension level
3. Plan the card series structure (number of cards, role of each):
   - Card 1: Cover (topic + impactful visual -- full-bleed, bold, attention-grabbing)
   - Cards 2 to N-1: Body cards (core content -- vary layouts: LR split, TB, Z-pattern, grid)
   - Card N: Ending (quote or vision statement -- never "thank you". Must be as visually dense as other cards, NOT a sparse page with text only. Include illustration + summary grid or key takeaways)
4. Write titles as **conclusions, not topics** (Tesla Rule)
   - Bad: "The Effects of Temperature and Humidity"
   - Good: "Maintaining 25C and 60% Humidity Is Essential for Livestock Growth"

-> **AskUserQuestion**: Present the card structure plan and ask the user to confirm or modify

### Phase 2: Design Planning

1. **Color palette** (3-color limit)
   - primary (extracted from brand/topic) + accent + neutral
   - 80% neutral tones + 20% accent color principle
   - Lock as CSS variables: `--primary`, `--accent`, `--neutral`, `--text`, `--bg`

2. **Overall tone/mood** direction

3. **Layout patterns** -- match to content's semantic structure:
   - Timeline/causation -> Left-Right (LR) layout
   - Narrative/conclusion-reason -> Top-Bottom (TB) layout
   - Title-image-description -> Z-pattern layout

4. **Illustration placement and aspect ratio** for each card:
   - Full card background -> 4:5
   - Top/bottom banner -> 16:9 or 3:2
   - Side placement -> 2:3 or 3:4
   - Icon/symbol -> 1:1

-> **AskUserQuestion**: Present color palette and design tone options (e.g., "dark + cyan" vs "bright + pastel" vs "minimal monotone")

### Phase 3: Illustration Generation (Nano Banana)

Refer to `references/image-prompt-guide.md` for prompt writing. All prompts must be in English, narrative form.

#### Step 3-1: Establish Style (First Card)

1. Write **2-3 style variation** prompts and generate in **batch mode (parallel)**:
   ```bash
   source scripts/.venv/bin/activate
   python scripts/generate_image.py --batch batch.json
   ```
   Example `batch.json`:
   ```json
   [
     {"prompt": "A 3D clay style icon of ...", "output": "card1_v1.png", "aspect_ratio": "1:1"},
     {"prompt": "A flat design icon of ...", "output": "card1_v2.png", "aspect_ratio": "1:1"},
     {"prompt": "An isometric scene of ...", "output": "card1_v3.png", "aspect_ratio": "1:1"}
   ]
   ```
   For a single image:
   ```bash
   python scripts/generate_image.py --prompt "..." --aspect-ratio "1:1" --output card1_v1.png
   ```
2. **Read generated images** to visually compare them
3. -> **AskUserQuestion**: Ask the user to pick their preferred style
4. If the selected image is 80%+ satisfactory, use **image editing mode** for fine-tuning:
   ```bash
   python scripts/generate_image.py --prompt "Change the background to navy blue" --input card1_v1.png --output card1_final.png
   ```
5. The finalized image becomes the **style reference** for the entire series

#### Step 3-2: Remaining Card Illustrations (Character & Style Consistency is CRITICAL)

**The #1 visual quality issue is inconsistent illustration style across cards.** All cards in a series MUST feel like they belong together. This means:
- The **same character/mascot** should appear across multiple cards (not a different character on every card)
- The **same rendering style** (same 3D clay texture, same color temperature, same level of detail)
- The **same color palette** in illustrations matching the card's CSS color scheme

To achieve this, ALWAYS provide the first card's finalized illustration as `--refs` for every subsequent image generation. Include explicit instructions in the prompt:
- "Same character as in the reference image"
- "Identical 3D clay rendering style, same color temperature and texture"
- "Same visual universe as the reference"

Generate remaining illustrations in **batch mode (parallel)**:
```bash
python scripts/generate_image.py --batch remaining_cards.json
```
Example `remaining_cards.json`:
```json
[
  {"prompt": "..., same visual style as reference", "refs": ["card1_final.png"], "output": "card2_illust.png", "aspect_ratio": "1:1"},
  {"prompt": "..., same visual style as reference", "refs": ["card1_final.png"], "output": "card3_illust.png", "aspect_ratio": "1:1"},
  {"prompt": "..., same visual style as reference", "refs": ["card1_final.png"], "output": "card4_illust.png", "aspect_ratio": "16:9"}
]
```
Single image with reference:
```bash
python scripts/generate_image.py \
  --prompt "A 3D clay style icon of a growing plant, same visual style as reference" \
  --refs card1_final.png \
  --aspect-ratio "1:1" \
  --output card2_illust.png
```

#### Step 3-3: Background Removal (Critical)

Read each generated image to determine if background removal is needed. **Using a white-background image on a dark card looks "pasted on" -- in most cases, background removal is required.**

Decision criteria:
- Dark card background + bright image background -> **always remove with rembg**
- Light card background + light image background -> removal unnecessary
- Image used as full card background -> removal unnecessary
- Image must float over text/content -> **always remove with rembg**

```bash
source scripts/.venv/bin/activate
# Single file
rembg i input.png output.png

# Batch: process entire directory at once
rembg p ./images_raw/ ./images/
```

After background removal, integrate images naturally with CSS:
- **White Glow** (dark backgrounds): `filter: drop-shadow(0 0 30px rgba(255,255,255,0.2))`
- **Soft Shadow** (light backgrounds): `filter: drop-shadow(0 8px 20px rgba(0,0,0,0.3))`
- **Background blending**: `radial-gradient` beneath the image for subtle glow

### Phase 4: HTML Generation + Preview

Refer to `references/css-patterns.md` for base templates and patterns.

1. Generate **1 HTML file per card** (1080x1350px)
2. Illustrations saved as **separate image files**, referenced via path in HTML (`<img src="./images/card1_illust.png">`)
3. Decorative elements via inline SVG + CSS

**CRITICAL: Sizing & Density Guidelines (cards must feel "full", not sparse)**

The 1080x1350px canvas must be used efficiently. Overly small elements and excessive whitespace make cards look amateurish. Follow these concrete sizing rules:

| Element | Minimum Size | Notes |
|---------|-------------|-------|
| Main title | 64-80px font-size | Can go up to 96px for single-word impact |
| Subtitle | 28-36px | |
| Body text | 22-28px | |
| Caption/meta | 14-18px | |
| Card padding | 48-60px | Never exceed 70px. Less padding = more content space |
| Illustration | 500-700px wide | Should occupy 45-65% of card width |
| Element gap | 20-32px | Never exceed 40px between adjacent elements |

Key principles:
- **Fill the canvas**: Elements should collectively occupy 75-85% of the card area
- **No dead space**: If empty space exists, fill it with decorative elements, watermark text, or expand existing elements
- **Bold typography**: Titles should feel imposing. When in doubt, go bigger
- **Illustrations should be prominent**: They are the visual anchor, not a small thumbnail
- **Edge-to-edge when appropriate**: Some elements (images, gradient bars, dividers) can span the full width without padding
- **Overlap for dynamism**: Allow illustrations to overlap text areas or break grid boundaries (z-index layering)

**Design Quality Checklist (verify for every card):**
- [ ] **Canvas density**: Elements fill 75-85% of card area (no sparse, empty feeling)
- [ ] **Title is bold enough**: Main title is 64px+ and feels imposing
- [ ] **Illustration is prominent**: 500px+ wide, visually dominant
- [ ] **Padding is tight**: Card padding is 48-60px, not more
- [ ] Image background integrates naturally (no white residue after rembg)
- [ ] Gradient mask or glassmorphism ensures text readability
- [ ] Gray dimming applied to all non-essential text
- [ ] Corner anchors placed (page number, logo, decorative marks)
- [ ] Key phrases highlighted with `<span>` (different weight/color)
- [ ] White glow or drop-shadow applied to illustrations

4. **Generate ALL cards** as HTML first (applying the sizing guidelines above)

5. **Visual Review Loop (critical for quality -- do NOT skip this):**
   a. Convert all HTML to PNG:
      ```bash
      python <skill_dir>/scripts/html_to_png.py ./outputs/
      ```
   b. **Read every PNG** to visually evaluate the actual rendered result
   c. Check across all cards for these specific issues:
      - **Density**: Do elements fill 75-85% of canvas? Any card that feels sparse or has large empty areas MUST be fixed
      - **Sizing**: Are titles 64px+? Are illustrations 500px+ wide? Is padding under 60px?
      - **Consistency**: Are font sizes, padding, and spacing uniform across ALL cards?
      - **Illustration style**: Do all illustrations look like they belong to the same series? Same character, same rendering style?
      - **Ending card**: Is it as visually rich as body cards? (Ending cards often end up too sparse)
      - **Text readability**: Can all text be read clearly against its background?
   d. If ANY issues are found:
      - Identify the specific CSS values causing the problem
      - **Apply fixes across ALL HTML files at once** (not one card at a time)
      - Re-convert to PNG
      - Read again to verify the fix worked
   e. Repeat until all cards pass visual inspection

6. -> **AskUserQuestion**: Show the final PNGs and collect feedback (adjustments, satisfaction)
7. Apply user feedback if any, re-convert, and finalize

### Phase 5: Final Conversion

```bash
source scripts/.venv/bin/activate
python scripts/html_to_png.py ./output/
```

-> **AskUserQuestion**: Final satisfaction check, individual card revision requests

---

## HTML Generation Rules

### Base Structure

- No external URL references (no CDN, no web fonts, no internet dependencies)
- Illustrations stored as **separate image files**, referenced via relative/absolute path (`<img src="./images/card1_illust.png">`)
  - Do NOT use base64 embedding -- it bloats file size unnecessarily
  - Playwright resolves local file paths correctly for PNG conversion
- Load Paperlogy TTF via `@font-face` with **absolute paths** to `assets/fonts/`
- Fixed viewport: `<div style="width:1080px; height:1350px; overflow:hidden; position:relative;">`
- `word-break: keep-all` for Korean text line-breaking
- CSS Grid/Flexbox-based layouts

### Paperlogy Font Usage Guide

Use **at most 3 weights per card**. Ensure strong contrast between weights (400+500 bad, 400+800 good).

| Role | Weight Name | font-weight | Usage |
|------|------------|-------------|-------|
| Main title | ExtraBold/Black | 800-900 | Card's core message, highest visual impact |
| Subtitle | Bold/SemiBold | 600-700 | Section dividers |
| Body text | Regular/Medium | 400-500 | Readable explanation text |
| Caption | Light/ExtraLight | 200-300 | Sources, page numbers |
| Decorative | Thin | 100 | Background watermark (opacity 5%) |

Additional rules:
- Titles: `letter-spacing: -0.03em to -0.05em` (chunky, impactful)
- Maintain the same weight combination across the entire series

---

## Core Design Principles (Paperology-Based)

These are the primary design standards. See `references/design-principles.md` for comprehensive details. The rules below are mandatory.

### Typography
- **Gray Dimming for emphasis**: Instead of coloring keywords, dim non-essential text to `color: #888`
- Never use red for emphasis (signals warning/danger)
- Within a single sentence, wrap only key phrases in `<span>` with different weight/color

### Color
- **3-color limit per card** (primary + accent + neutral)
- 80% neutral tones + 20% accent color
- Extract dominant color from brand/topic to build the palette
- Lock colors as CSS variables and apply consistently

### Background + Readability
- Text over images: **gradient mask required** (`linear-gradient` aligned to text direction)
- Complex backgrounds: **glassmorphism** (`backdrop-filter: blur(10px); background: rgba(255,255,255,0.15)`)
- Background is "the stage", not "the star" -- reduce background's role when text density is high

### Shadow / Depth
- Soft shadow: `box-shadow: 0 4px 15px rgba(0,0,0,0.4)` (40-50% opacity, wide blur)
- White Glow on dark backgrounds: `filter: drop-shadow(0 0 20px rgba(255,255,255,0.3))`
- Z-index layering: background(z:1) -> text(z:2) -> cutout image(z:3)

### Layout
- **Big-Medium-Small** size hierarchy (60-30-10%)
- Corner anchors: small elements at all four corners (page number, logo, decorative marks) for stability
- Fill empty space with decorative SVG or **background typography watermark** (opacity 5%, font-size 15rem)

### Content
- Titles = conclusions (never topics)
- Extract 3 core keywords and display them as visually separated chunks
- Bookending: open and close series with the same visual/message
- Cinematic Ending: end with a quote or vision statement, never generic "thank you"

### Icons / Assets
- Uniform style within a series (all flat OR all 3D clay -- never mix)
- Consistent stroke width, fill style, and corner radius

### Dimming Effect
- When highlighting a specific list item: active item `opacity: 1`, rest `opacity: 0.3`

---

## Detailed References

For deeper techniques and code examples, consult:

- `references/design-principles.md` -- Comprehensive Paperology design principles (most important reference)
- `references/css-patterns.md` -- Ready-to-use CSS code snippets
- `references/image-prompt-guide.md` -- Nano Banana image prompt writing guide
