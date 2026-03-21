# Card News Design Principles

Principles for designing professional card news at 1080x1350px. Each principle explains *why* it works -- use them both as design guides during creation and as diagnostic criteria when reviewing generated PNGs.

---

## 1. Typography -- Hierarchy Through Weight and Spacing

### Weight Creates Drama, Not Labels

Beginners apply `font-weight: bold` uniformly and wonder why everything looks flat. Professional typography uses the full 100-900 spectrum, but the key insight is that **contrast between weights matters more than the weights themselves**. A pairing of 400 (regular body) against 800 (extra-bold title) creates instant visual hierarchy because the eye registers the difference in density. A pairing of 400 against 500 is nearly invisible -- the brain perceives them as the same level of importance.

Use a maximum of 3 weight levels per card. More than 3 creates ambiguity about what's important. Paperlogy's 9 weights (100-900) give fine control: reserve 100-200 for decorative watermarks and source attributions where the text should be felt but not consciously read.

### Letter-spacing: Mass vs Breath

Tightening letter-spacing on titles (-0.03 to -0.05em) packs the characters into a single visual chunk -- the word gains a sense of mass and authority, like a headline stamped into the page. This is why large type in magazines and posters always looks "chunkier" than body text: the letters are physically closer together.

Body text needs the opposite treatment: default or slightly positive spacing, because reading flow depends on each character having breathing room. Captions and labels benefit from *widened* tracking (+0.05em) paired with uppercase -- this makes tiny text feel deliberate rather than accidentally small.

### Emphasis by Reduction, Not Addition

Beginners reach for red or bright colors to emphasize keywords, but red triggers a danger/warning response in the viewer's brain -- it's the color of error messages, stop signs, and alerts. Professional designers take the opposite approach: leave the key text at full brightness and dim everything else to gray (#888). This "reverse highlighting" works because the eye is naturally drawn to the brightest element in a field of muted tones. The emphasis emerges from contrast with its surroundings, not from the color applied to it.

Within a single sentence, wrap only 1-2 keywords in the accent color + heavier weight. The rest of the sentence gets dimmed. This creates a scannable rhythm where the eye can extract the core message without reading every word.

**Review diagnostic:** If a card feels "loud" or chaotic, check whether emphasis was added (colored keywords) rather than subtracted (dimmed surroundings). Switch to gray dimming.

---

## 2. Color -- Restraint Creates Sophistication

### The 3-Color Discipline

Every additional color in a composition competes for the viewer's attention and dilutes the impact of the accent. Lock exactly 3 chromatic roles as CSS variables: primary (from the brand/topic), accent (a lighter variation), and neutral (the background tone). All other color in the card should be achromatic -- black, white, and grays.

The 80/20 ratio is the mechanism that makes accents work: approximately 80% of the card's surface area should be achromatic tones, with chromatic color occupying only the remaining 20%. Think of a single red flower in a field of green -- the flower commands attention *because* it's rare. If the entire field were red, nothing would stand out.

### Variable Locking Across Series

Define the palette once in `:root` and never hard-code color values in individual elements. This isn't just good engineering -- it's a design principle. When all cards in a series reference the same variables, the series develops a brand-like visual cohesion. The moment one card uses a hard-coded `#FF5733` that doesn't match the palette, the series feels inconsistent, as if different designers worked on different cards.

**Review diagnostic:** If a card feels visually "off" compared to others in the series, check for hard-coded colors that bypass the CSS variables.

---

## 3. Layout -- Guiding the Eye

### Big-Medium-Small: The Entry Point Problem

When every element on a card is roughly the same size, the viewer's eye has no entry point -- the brain scans aimlessly and fatigues. The Big-Medium-Small principle (60-30-10% of visual weight) solves this by creating a hierarchy of attention: the Big element (main visual or title) anchors the eye first, Medium elements (body text, subheadings) deliver the message, and Small elements (page number, source, date) provide context without competing.

A card composed entirely of Medium elements feels like a wall of text. Every card needs at least one Big element to serve as an anchor.

### Content Semantics Drive Layout Choice

The layout pattern should match the logical structure of the content, not be chosen arbitrarily:
- **Timeline or cause-and-effect** → Left-Right (LR) split, because the brain reads causation as left-to-right progression
- **Conclusion followed by reasoning** → Top-Bottom (TB), because the headline-then-explanation pattern reads naturally downward
- **Title + image + description** → Z-pattern, tracing the natural Z-shaped scan path across the card

Mismatches create cognitive friction: placing a timeline vertically forces the viewer to read against their spatial intuition.

### Corner Anchors: Invisible Framing

Placing small elements at all four corners (page number, brand name, date, decorative mark like "+") creates invisible boundary lines that frame the composition. The card feels architecturally solid even without a visible border -- the eye perceives the corners as structural supports. Without them, content floats in undefined space.

### Four-Quadrant Balance

Divide the card into four quadrants mentally. If one quadrant is significantly emptier than the others, the composition feels lopsided -- designers describe this as "visual weight" imbalance. Fill light quadrants with subtle decorative elements (geometric shapes, dots, lines) at opacity 0.08-0.15, just enough to be sensed without being consciously noticed.

**Review diagnostic:** If a card feels "unbalanced" or "empty on one side," check the four-quadrant weight distribution.

---

## 4. Background -- Stage, Not Star

### Role Reduction

Beginners fill backgrounds with flashy, detailed images and then struggle to make text readable. Professional designers treat the background as a stage set: its job is to establish mood and context, not to be the focal point. When text density increases, the background's role must be *actively suppressed* -- darkened, blurred, or overlaid -- so the text can do its job.

This is the principle Paperology calls "role reduction": the moment an image starts competing with the text for the viewer's attention, cover it with a gradient, dim it, or blur it. The background should be felt, not studied.

### Gradient Masks Follow Text Position

When placing text over a photo, the gradient direction must follow the text position: text at the bottom gets a bottom-to-top gradient (dark at bottom, transparent at top), text on the left gets a left-to-right gradient. The gradient transitions the photo smoothly into a readable surface. Use 6-7 opacity stops for a natural, cinematic feel rather than a harsh 2-stop cutoff.

### Suppression Scales with Text Density

The amount of background suppression should be proportional to how much text sits on top:
- **Title only:** Light treatment -- brightness 0.7 is enough
- **Title + 2-3 lines of body:** Moderate -- brightness 0.4 plus a slight blur
- **5+ lines of dense text:** Aggressive -- brightness 0.2, strong blur, or a glassmorphism panel

Glassmorphism (frosted glass effect) is particularly effective when the background context matters -- maps, cityscapes, complex scenes -- because the viewer's brain can sense the environment through the blur without being distracted by details.

**Review diagnostic:** If text is hard to read over a background image, the background isn't being suppressed enough for the text density level.

---

## 5. Depth & Shadow -- Subtlety Reads as Quality

### Soft Shadows Only

Sharp, dark shadows (alpha 0.5+, minimal blur) are the hallmark of amateur digital design -- they look like a Photoshop default from the 2000s. Professional shadows are soft, wide, and nearly transparent (alpha 0.1-0.15 for boxes, wide blur radius). They mimic how light naturally diffuses in the real world: you rarely see a hard-edged shadow in a well-lit room. The result feels physical and grounded rather than digitally "pasted on."

### White Glow on Dark Backgrounds

When a background-removed (rembg) cutout is placed on a dark card, it looks disconnected -- floating in a void without any relationship to the surface. A subtle white glow (`drop-shadow` with rgba(255,255,255,0.2) and 30px spread) creates an implied light source behind the subject, integrating it into the composition. This is the digital equivalent of backlighting in photography.

Use `filter: drop-shadow()` for transparent PNGs (it follows the image silhouette) rather than `box-shadow` (which creates a rectangular shadow around the entire image box).

### Z-index Layering for Cinematic Depth

The layering order background(z:0) → gradient overlay(z:1) → text(z:3) → cutout subject(z:4) creates a sense of depth on a flat card. When text sits *behind* a person cutout, the viewer perceives the person as physically present in front of the information -- the same depth illusion used in movie poster design.

**Review diagnostic:** If a cutout image looks "pasted on" or "floating," add a white glow on dark backgrounds or check the z-index layering order.

---

## 6. Content Structure -- Feed the Conclusion

### The Tesla Rule

Amateurs write titles like "Temperature and Humidity Effects" -- topic labels that force the viewer to read the body text to understand the point. Professionals write conclusions: "25C and 60% Humidity Are Essential for Growth." The title alone delivers the message. Elon Musk doesn't title a slide "Job Creation Data" -- he writes "Tesla Created 125,000 Jobs in 10 Years."

| Amateur (topic) | Professional (conclusion) |
|---|---|
| EV Market Status | EV Sales Surge 42% Year-over-Year |
| Consumer Preferences | 7 in 10 Gen Z Choose Eco-Friendly |
| Revenue Trends | Q3 Revenue Hits All-Time High at 20B |

**Review diagnostic:** Read only the titles across all cards. If you can't understand the story without reading body text, the titles are topic-style and need rewriting.

### Jargon Simplification

Difficult vocabulary signals insecurity, not expertise. Spotify's investor presentations use language a middle-schooler could follow -- and they're presenting to Wall Street. Simplify jargon at the text preprocessing stage: "ROI maximization" becomes "getting more value for the investment."

### Question-Answer Pagination

When you have a surprising statistic, don't waste it on a single card. Split it: Card A asks "How much did it grow in 3 years?" (dark, minimal, tension-building), Card B reveals "6x Growth" (bold, high-impact, giant number). The brain craves resolution once a question is posed -- the two-card structure creates a micro-narrative.

### Bookending and Cinematic Endings

Reusing the cover card's visual tone (image, color, mood) on the ending card creates narrative closure -- the series feels like a complete story, not an interrupted list. The ending should carry a vision statement or a resonant quote, never "감사합니다" or "Thank you." Generic closings leave zero emotional residue; a well-chosen closing sentence lingers in the viewer's mind.

### Dimming for Sequential Explanation

When a series of cards explains items from a shared list (e.g., 5 strategies explained one per card), keep all 5 items visible on each card but dim the inactive ones to opacity 0.3. Only the currently-explained item stays at full brightness. This preserves context (the viewer always knows where they are in the list) while forcing attention to the active item.

---

## 7. Density & Sizing -- Calibrated Through 4 Iterations

The single most recurring quality issue across all testing rounds was **excessive whitespace**. Professional card news fills 85-95% of the canvas with meaningful content. Empty space doesn't signal elegance in this format -- it signals that the designer ran out of ideas.

These specific values were calibrated through 4 rounds of generate-review-fix cycles at 1080x1350px:

- **Padding:** 36-48px from card edges. Above 50px, the content feels adrift in the middle of the card
- **Gaps between elements:** 12-24px. Above 28px, the elements feel disconnected from each other
- **Title font size:** 72-96px. Below 64px, titles lack authority on a 1080-wide canvas
- **Body text:** 24-28px. Below 22px, text feels like fine print
- **Illustrations/photos:** 600-900px wide. Below 500px, visuals feel like thumbnails
- **Background photos:** Must fill the entire frame edge-to-edge. Any visible gap between the photo edge and the card boundary looks like a rendering error

Ending cards deserve special attention: the most common amateur mistake is a sparse ending with just a quote floating in empty space. Endings must be as visually dense and carefully composed as body cards.

**The squint test:** After generating a PNG, squint at it. Large uniform-color areas with no content are dead zones that need to be filled -- enlarge elements, reduce padding, add illustrations, or place a background watermark.

---

## 8. Watermark & Decoration -- Filling Silence

### Background Typography

When a card has low text density (covers, dividers, endings), large empty areas can feel barren. Place a thematically relevant English keyword (e.g., "REFORM", "GROWTH", "DESIGN") in weight 900 at an extremely large size (150-200px+) and reduce opacity to 3-5%. On dark backgrounds: rgba(255,255,255,0.03-0.05). On light backgrounds: rgba(0,0,0,0.03).

The result is a subtle texture that the viewer senses without consciously reading -- the space feels *occupied* rather than empty. The watermark should sit behind all content (z-index: 0) with `pointer-events: none` and `user-select: none` to prevent interaction.

### Decorative Shapes

When the four-quadrant balance check reveals an empty area, place subtle geometric elements (circles, lines, dot grids, "+" marks) at opacity 0.08-0.15. They serve as visual ballast -- restoring equilibrium without adding information. Any opacity above 0.15 risks the decorative element competing with actual content.

**Review diagnostic:** If a card feels "empty" despite having content, try adding a background watermark or corner decorations. If a card feels "busy," check whether decorative elements exceed 0.15 opacity.
