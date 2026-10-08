# Prompt Assembly (Stage 11)

Contents: the blueprint-first rule · what a prompt must do · spatial explicitness · the template · block rules · text strategy · phrasing rules · length and tool notes · contradiction check · example A (feed post with images) · example B (spanduk background, no images) · example C (feed post with no images, identity treatment) · assembling a set

## 0. The blueprint-first rule

**Never write a prompt directly from a concept or design strategy.**

Before the first word of a prompt is written, the Visual Blueprint must exist (see `13-design-thinking.md` Section 9.9). The blueprint is the complete spatial specification of the artwork — layout zones, proportions, hierarchy, exact text, logo treatment, hero visual, graphic elements, color roles, and whitespace allocation.

The prompt is a translation of the blueprint into instructions an image model can execute. If the blueprint is incomplete, the prompt will be incomplete. If the blueprint is skipped, the design thinking done in Stages 1–9 cannot reach the image model.

**The test:** before sending a prompt, ask: "Does a Visual Blueprint exist for this design?" If not, produce it first.

**What the blueprint catches that a direct prompt misses:**
- Layout described as adjectives instead of zones ("balanced and dynamic" vs. "hero right 55%, message column left 45%")
- Hierarchy stated as intent instead of specification ("price should stand out" vs. "price at 14% canvas height in accent orange, second-largest element")
- Whitespace forgotten until the image arrives overloaded with decoration
- Graphic elements added by the model because their prohibition was never stated
- Logo treatment undefined, leading to an invented or distorted mark
- Viewing-context statements pasted in unchanged instead of translated into design decisions

---

## 1. What a prompt must do

A prompt is a **complete, final design brief** for a model that cannot ask questions. It produces the finished design with zero manual post-editing of essential elements. It carries the **format**, the **concept**, the **attached images and what to do with each** (or nothing if there are none), the **hero**, the **layout, space, and reading path**, the **exact text with ranks**, the **Visual System**, the **truth constraints**, and a **short exclusion line**. Nothing else.

Every sentence must change the picture. A sentence that explains the reasoning, describes the design process, or re-states a viewing context without translating it into a design decision does not belong in the prompt.

**Viewing context → design decisions:** Never paste viewing-context or use-case statements directly into the prompt. Instead, translate them:
- "Viewed from 10 m on a motorbike" → "headline in heavy condensed type at 28% of canvas height, maximum 5 words, high value-contrast on flat single-color background."
- "Must read in 3 seconds" → "three text elements only, headline at the largest scale, no more than 8 words total, calm empty area isolating the hero."
- "Seen on a phone while scrolling" → "single dominant element at 55% of canvas height, headline in two short lines above it, strong silhouette contrast."

**Every prompt is fully standalone.** It works if pasted alone into a fresh chat: no "same as before", no reference to another prompt, no dependence on a generated result. When there are several outputs, each prompt repeats the shared Visual System verbatim (see `09-output-sets.md`).

## 2. The template

The blocks follow the order a designer thinks in: spatial structure first, then hero, then text, then brand, then color, then style system. This order helps the image model build the composition correctly before filling it.

Two layers: **output blocks** (differ per output) and the **VISUAL SYSTEM block** (identical in every prompt of a set). Fill each block with decisions, not adjectives; omit a block only if it truly does not apply.

```
FORMAT: [physical medium, e.g. "Printed roadside banner, 3×1 m, vinyl tarpaulin"], [aspect ratio and px, e.g. "3:1 (3000×1000 px)"].
PHYSICAL CONTEXT: [one line — viewing distance and duration translated into design decisions, e.g. "Headline at 30% canvas height, max 5 words, extreme value contrast; no supporting text readable at 8 m."]

OBJECTIVE: [one sentence — what this specific output must accomplish for the viewer in their available time, e.g. "Attract passing traffic on foot to stop and read the phone number."]

CONCEPT: "[campaign idea — same words in every prompt of a set]". [Two feelings]. For [audience].

COMPOSITION: [overall structure]. [Named zones with positions and proportions, e.g. "Hero occupies right 55%, message column left 45%. Brand zone upper-left 15% of canvas height."]. [Alignment spine: symmetric / asymmetric]. Margins about [6-8]%. Eye path: [A → B → C → D].

WHITESPACE: About [N]% of the canvas stays calm and empty ([flat color hex], no texture or detail), mainly [where]. Nothing floats in it. No decorative elements enter this zone.

HERO VISUAL: [specific subject — not "a dish" but the physically specific thing]. [Angle and distance]. [Surface and setting]. [Light source, direction, quality]. [Texture and material detail]. [One or two ownable physical details]. [If photo attached: "Image 1 — keep exactly as provided."]

TEXT (render exactly as written, in [language], no additional words):
1. [role] "[exact text]" — [size rank, e.g. "largest, 28% canvas height"], [type character], [case], [color #hex], [position]
2. [role] "[exact text]" — [size rank], [type character], [case], [color #hex], [position]
3. ...
[If strategy B or C: "Leave a clean, flat, empty [position] area, about [size], for text to be added later. Do not render any text, letters, numbers, or symbols in this zone."]
[If official marks needed: "Reserved empty [shape] for official mark, [position], [size]."]

LOGO / IDENTITY:
[If logo attached: "Image [N] is the business logo. Place unaltered at [position], about [size] canvas width. Keep unchanged: everything. Do not redraw or reinterpret."]
[If identity treatment: "Business name '[exact name]' rendered as [type character], [color #hex], [case], at [position], inside [graphic device description]."]
[If no logo and no identity needed: omit this block.]

COLOR SYSTEM:
Dominant field: [name #hex] ~60% — [emotional role, e.g. "deep warm background that signals trust and craft"].
Primary content: [name #hex] ~30% — used for all body text and secondary elements.
Accent: [name #hex] ~10% — used ONLY for [one specific element, e.g. "price and CTA strip"]; nowhere else.
[Structural: [name #hex] — [specific use, e.g. "bottom band and divider rule"]; omit if none.]

GRAPHIC ELEMENTS:
[Element name]: [communication purpose] — [position] — [size].
[If none: "No graphic elements beyond hero, text, and logo. Do not add decorative shapes, icons, or fills."]

[ATTACHED IMAGES — include ONLY if images are being attached. Omit this block entirely when there are none:]
ATTACHED IMAGES (attach in this order):
Image 1 = [what it is, as visible]. Role: [...]. Treatment: [...]. Placement: [...]. Size: [...]. Keep unchanged: [...]. May change: [...].
Image 2 = ...
Priority if conflicts: [...].

VISUAL SYSTEM (identical in every prompt of this set):
Type: [headline character — weight, personality, case]; [support character — weight, case]. Style and material: [photo/illustration], [texture, finish, light quality]. Image treatment: [how real photos are handled — grounding, cleaning, cropping]. Device: [one recurring graphic element, or none]. Space level: [calm / moderate / dense-but-grouped].

EXCLUSIONS: Keep [truth constraints — e.g. "product shape and proportions exactly as in Image 1"]. Avoid [4-8 specific failure modes for this brief — concrete, not generic, e.g. "floating chilli slices, plastic-glossy broth, extra invented text, glow effects, gradient backgrounds, decorative sparkles, generic smiling stock people"].
```

**Why this order:**
- FORMAT + PHYSICAL CONTEXT → the model knows the constraints before anything else
- OBJECTIVE → purpose is clear before composition decisions
- CONCEPT → organizing idea before spatial structure
- COMPOSITION + WHITESPACE → spatial skeleton established before elements are placed into it
- HERO → dominant element placed into the already-defined spatial structure
- TEXT → text placed with known zones and hierarchy
- LOGO / IDENTITY → brand placed with known zones
- COLOR SYSTEM → palette applied after spatial and element decisions are known
- GRAPHIC ELEMENTS → supporting elements added after dominant ones are placed
- ATTACHED IMAGES → asset declarations after role and placement are defined
- VISUAL SYSTEM → shared brand-consistency block, after all output-specific decisions
- EXCLUSIONS → prohibitions stated last, as a closing fence


## 3. Block rules

**FORMAT.** State the physical medium and production context explicitly: "Printed roadside banner, 3×1 m, vinyl tarpaulin." State the aspect ratio for generation: "3:1 (3000×1000 px)." Do not include a viewing-context statement here — that belongs in PHYSICAL CONTEXT.

**PHYSICAL CONTEXT.** One line only. Translate the viewing conditions directly into design constraints. Never paste a viewing-context statement unchanged. Examples:
- "Headline at 30% canvas height, max 5 words, white on deep background; no text element under 12% canvas height." (roadside 8 m)
- "Three information zones, headline at 18% canvas height, supporting text readable at 360 px wide, clear group separation." (hand-held flyer)
- "Single dominant element at 55% canvas height, two text lines only, high value contrast for outdoor sun." (sidewalk spanduk)

**OBJECTIVE.** One sentence — what this specific output must accomplish. Not the campaign concept (that is CONCEPT), but the specific communication task: "Attract passing motorbike traffic to stop and read the phone number." "Convince a standing customer to order the hero product." "Introduce the business name and one differentiator to pedestrians." This line tells the model what success looks like before it processes anything else.

**CONCEPT.** The campaign idea in the same words in every prompt of the set, plus the two feelings. It comes from the Distinction Brief (USP, desired perception). This is a design concept — an organizing idea — not an aesthetic direction.

**COMPOSITION.** Zones with proportions and explicit positions. Name every major zone and give its approximate % of canvas height or width. Choose symmetric or asymmetric on purpose. State the alignment spine. End with the eye path: "Eye path: brand zone → headline → hero → price → CTA strip." Do not use adjectives ("balanced," "dynamic") — use positions and proportions.

**WHITESPACE.** Separate from COMPOSITION so the model processes it as an explicit allocation, not an afterthought. State the location, approximate %, flat color hex, and what is prohibited from entering the zone. "About 45% of the canvas stays calm and empty (flat deep coffee-brown #3B2418, no texture), mainly the left half. Nothing decorative floats in this area. No props, no patterns, no extra text."

**HERO VISUAL.** Name the real thing with physical specificity. Not "a delicious dish" but "a 20 cm earthenware bowl of mie ayam with golden broth, visible slices of chicken on top, chopped spring onion lying flat in the broth, on a worn rattan placemat, soft morning window light from the left, slight steam curl above the bowl." Push toward credible photography: real surfaces, natural light, believable proportions, visible texture, slight physical imperfection. If a photo is attached, say to use it exactly.

**TEXT.** One line per element: role, exact quoted text, size rank as % canvas height, type character, case, color hex, position. Quote text exactly; add "render exactly as written, no additional words." Three to six elements maximum. If strategy B or C, describe the clean zone for later text — do not describe text that will not be in the image.

**LOGO / IDENTITY.** Dedicate a block to brand treatment — do not bury it in COMPOSITION. If a logo file is attached: name the image number, state placement, size, clear space, and prohibitions against redrawing. If an identity treatment was developed: specify type character, color, graphic device, and placement exactly as they will appear. Omit the block only if there is genuinely no logo or identity element in the design.

**COLOR SYSTEM.** Three or four roles with hex values and stated purposes. The accent rule is absolute: accent color appears on exactly one element type. If it appears on two, it stops functioning as an attention signal. State the emotional role of the dominant field — it is a design decision, not a label ("deep warm background that signals trust and craft" not just "#3B2418").

**GRAPHIC ELEMENTS.** One line per element with its communication purpose, position, and size. If no graphic elements beyond hero, text, and logo: state it explicitly — "No graphic elements beyond hero, text, and logo. Do not add decorative shapes, icons, or fills." This prohibition prevents the model from filling empty space with default decoration.

**ATTACHED IMAGES.** Include only when image files are literally being attached to the AI prompt. Omit entirely when there are none — no placeholder, no "no images" note (that goes in HERO VISUAL if needed). Follow `03-reference-images.md` section 10: fixed order, one primary treatment per image, placement as zone and %, keep-unchanged and may-change, explicit modification instruction.

**VISUAL SYSTEM.** Compact shared identity block (~40-60 words). Contains: type characters (headline + support), style and material (photo/illustration, texture, finish, light quality), image treatment (how real photos are handled), graphic device (one element or none), space level. Does NOT contain palette hex values — those are in COLOR SYSTEM. Identical word-for-word in every prompt of a set. For a single-output job, still write it so the prompt stays self-contained and reusable.

**EXCLUSIONS.** "Keep" = truth constraints (what must not be invented or altered). "Avoid" = specific failure modes for this brief — concrete, not generic. "Floating ingredients, glow effects, gradient backgrounds, decorative sparkles, extra invented text, stock-style smiling people, crowded corners" beats "avoid AI slop." Write 4-8 exclusions. More than 8 usually means the composition is not specified tightly enough.


## 4. Text strategy

| Strategy | When | Prompt approach |
|---|---|---|
| **A: in-image text** | Tool renders text well; short headline, offer, price, CTA; screen only; **default for simple screen promos** | Quote each line; "render exactly as written, no additional words" |
| **B: clean text zones** | Print, spanduk, menus, long info, phone numbers, addresses, legal marks, text-heavy redesigns | "Leave a clean, calm, empty [position] area, about [size], for text added later. Do not render any text, letters, numbers, or logos." |
| **C: hybrid** | Screen posts with contact info that the owner wants to add themselves | Headline and price in-image; "leave a clean strip at the bottom 12% for contact details added later; no other text" |

Rules for A and C: quote exactly, keep lines short and large, specify the language, say what not to add ("no taglines, no extra words, no watermarks"), and tell the owner to proofread after generation.

**Do not choose B or C to avoid the effort of specifying text.** If the content is short and the tool renders text reasonably, use A and produce the finished design.

## 5. Spatial explicitness

Image models need to understand **where things go**, not merely that they exist. A prompt that lists elements without placing them produces a composition the model invents — which is generic by default.

**Use explicit spatial language for every major element:**

| Vague | Explicit |
|---|---|
| "Include the logo" | "Logo upper-left corner, about 12% of canvas width, with clear space on all sides" |
| "Show the price prominently" | "Price in the lower-left third, at 14% canvas height, directly below the bottle base" |
| "Product in the center" | "Product centered, occupying about 55% of canvas height, base resting on the counter surface at 60% from the top" |
| "Leave some space" | "About 40% of the canvas stays calm and empty (flat deep brown, #3B2418), mainly the right half; nothing floats in it" |
| "Headline at the top" | "Headline stacked left-aligned in the top 28% of canvas, two lines, directly beneath the logo" |
| "CTA at the bottom" | "CTA strip spanning the full canvas width, bottom 10%, off-white text on dark background" |

**Required spatial terms for every major zone:**
- upper-left / upper-right / upper-center
- lower-left / lower-right / lower-center
- centered / off-center
- left third / right third / center third
- foreground / background
- directly beneath / directly above / directly beside
- aligned with / extending into / overlapping
- occupying approximately [N]% of canvas height or width
- isolated within [calm zone description]
- spanning full width

**Every element in the COMPOSITION block must have a spatial address.** An element without a stated position will be placed by the model's default logic — which is the statistical average of all designs it has seen. That average is generic.

**State spatial relationships, not just positions.** "Price directly beneath the headline, with about 8% canvas height gap" is more useful than "price in the middle area" because it describes the relationship, not just a zone.

## 6. Phrasing rules

1. **Decisions, not adjectives.** "Deep coffee-brown (#3B2418) background" beats "rich warm luxurious tones".
2. **One idea per sentence.**
3. **No stacked contradictions** ("minimal yet rich", "luxurious but cheap-looking").
4. **No quality buzzwords** ("ultra-detailed", "8k", "masterpiece", "stunning", "hyper-realistic").
5. **Positive first, negatives last, and few.**
6. **Concrete nouns and measures:** positions and sizes as percentages, colors as hex.
7. **Name the single most important thing early** (the hero and its dominance).
8. **Allocate space explicitly**; do not rely on the model to leave room.
9. **Instructions in English, on-image text in the owner's language and spelling.**
10. **Do not name model versions** or other products as style ("like Midjourney").
11. **No meta-commentary.** Do not explain why a decision was made, describe the design process, or write sentences that are useful only to a human reader. Every sentence must change what the model generates.
12. **No viewing-context sentences.** "Viewed from the sidewalk at 3–8 m" tells the model nothing useful. Translate into: type scale, element count, contrast level, space allocation.

## 7. Realistic food and product imagery

When the prompt must generate food or product imagery without a reference photo, describe it to push toward credible commercial photography:

- **Light:** name the source and direction ("soft morning light from a north-facing window, diffused through white curtain, shadows falling left"). Never "professional studio lighting" or "beautifully lit".
- **Surface:** real, named material ("worn dark-teak wood counter with visible grain and a water ring stain"; "pale stone table with matte finish"). Never "beautiful background".
- **Angle:** specific camera angle and distance ("looking slightly down at 25°, close enough that the bowl fills 55% of the frame"). Never "appetizing angle".
- **Texture and detail:** visible food texture that is physically plausible ("glossy broth surface with a thin orange oil film, meatball with visible sear marks, chopped green onion lying flat in the broth"). Never "perfectly plated", "gorgeous garnish".
- **Proportions:** realistic, not exaggerated ("a standard 18 cm bowl, meatball at about 4 cm diameter"). Never "enormous", "overflowing".
- **Imperfection is realism:** a condensation drop on a bottle, a small chip on a plate, a slightly uneven sprinkle. These details signal a real photo.
- **Avoid explicitly:** "excessive gloss, exaggerated portion size, ingredients floating mid-air or erupting from the dish, plastic-looking surfaces, extreme depth-of-field blur, generic stock-food aesthetics."

## 8. Length, tool notes, and AI tool selection

**Length:** Aim for 250–500 words per prompt. The new template is longer than the old one because PHYSICAL CONTEXT, OBJECTIVE, WHITESPACE, COLOR SYSTEM, and GRAPHIC ELEMENTS are now explicit blocks. This length is intentional — each block removes a decision the model would otherwise make by default. If you pass 550 words, you are probably describing decoration or repeating yourself: cut.

**AI tool selection** (ask in Stage 0: "Kakak biasanya pakai AI apa?"):

| Tool | Image attachments | Text accuracy | Aspect ratio | Best for |
|---|---|---|---|---|
| ChatGPT / DALL-E 3 | Yes, multiple | Good | Set in interface | Strategy A with attached photos and logo |
| Midjourney (v6+) | Limited (one image, Vary Reference) | Poor | `--ar` flag | Strategy B backgrounds; no in-image text |
| Adobe Firefly | Yes | Good | Set in interface | Print-safe outputs; CMYK-aware colors |
| Ideogram (v2+) | Yes | Excellent | Set in interface | Strategy A when text accuracy is critical |
| Canva AI (Magic Media) | Yes | Good | Auto from template | Strategy C hybrid; integrates with Canva editor |
| Leonardo AI | Yes | Moderate | Set in interface | Hero imagery; strategy B |

**Rules by tool:**
- If the tool does not support image attachments → use Strategy B or C; describe the product entirely in HERO VISUAL without relying on a photo reference.
- If the tool has poor text accuracy → use Strategy B for all print pieces; Strategy C for social content.
- If unsure which tool → default to Strategy B for anything that will be printed (the owner adds text in Canva), Strategy A for social-only content with short headlines.
- Ask the tool's image-per-prompt limit before planning an attached-images set.

**One-change iteration:** let the owner change one major thing per round (`12-review-and-iteration.md`). Changing everything at once makes diagnosis impossible.

## 9. Contradiction check

- Visual Blueprint completed before this prompt was written?
- Any sentence asking for both "minimal" and "rich detail"?
- More than one "largest" element? More than one accent color?
- Text count above the density budget?
- Style (illustration) in conflict with the hero (real photo)?
- Anything the model cannot do reliably (small text, QR, logos, official marks)?
- An exclusion that forbids something the composition requires?
- Any reference to another prompt, or any image numbering that does not match the attachment list?
- Any viewing-context statement that was not converted into a design decision?
- Any meta-commentary sentence that does not change the picture?
- Is the ATTACHED IMAGES block present when there are no images?
- Does the prompt leave any essential element (text, pricing, CTA, branding) unspecified when strategy A was chosen?

## 10. Example A: feed post with attached images (strategy A)

Brief: "Kopi Mbak Rini", Bekasi, 1-litre milk coffee; buyers: anak kos and office workers 20-35; action: order via WhatsApp; message: "satu botol cukup seharian"; offer Rp 55.000/botol, beli 2 Rp 100.000, until Sunday; bottle photo and logo available; direction: warm, confident, merakyat.

**Blueprint summary (produced before writing the prompt):**
- Concept: "One confident bottle against generous space — the smallness of the product vs. the scale of the daily promise." Concept trace: generous empty space → daily confidence; warm coffee-brown field → honest warmth matching merakyat positioning.
- Zones: bottle hero left-center 55% canvas height; headline top-left 28%; price block lower-left; CTA strip bottom 10%; calm zone right half ~40%.
- Information levels: L1 headline "SATU BOTOL, CUKUP SEHARIAN"; L2 price "Rp 55.000"; L3 bundle offer + deadline; L4 removed (tagline, social proof).
- Logo: attached file, top-left, 10% canvas width, unaltered.
- Hero: real bottle photo, kept exactly, low angle, warm window light from left.
- Accent: chili-orange — price only.
- Prohibitions: floating coffee beans, liquid splashes, glow, gradients, stock people.

```
FORMAT: Instagram feed promo post, vertical 4:5 (1080×1350 px).
PHYSICAL CONTEXT: Viewed on a phone screen while scrolling; headline and price must be readable at 360 px wide; max 4 text elements for visual calm.

OBJECTIVE: Hook a student or office worker mid-scroll and communicate the daily-use offer clearly enough that they tap to order.

CONCEPT: "Satu botol, cukup seharian." Confident and unpretentious. For students and office workers who want honest daily coffee.

COMPOSITION: Asymmetric. Bottle occupies left-center, base resting on a worn dark-teak counter at the 60% mark from top, bottle top reaching the 8% mark. Headline stacked left-aligned in the top 28%, directly beneath the logo. Price block lower-left third, immediately below the bottle base. CTA strip spanning the full canvas width at bottom 10%. Alignment spine: left edge. Margins 6%. Eye path: logo → headline → bottle → price block → CTA strip.

WHITESPACE: About 40% of the canvas stays calm and empty (flat deep coffee-brown #3B2418, no texture or detail), mainly the right half of the canvas. Nothing decorative floats in this area. No props, no beans, no patterns.

HERO VISUAL: Image 1 — the 1-litre milk-coffee bottle with kraft paper label. Keep product exactly as photographed: bottle shape, label design, cap color, liquid color unchanged. Place standing upright at a slightly low angle (looking up 10°), on the worn dark-teak counter with visible wood grain. Window light from the left, soft and warm, casting a faint shadow rightward. No reflections on the label. Replace background with flat deep coffee-brown (#3B2418).

TEXT (render exactly as written, in Indonesian, no additional words):
1. Headline "SATU BOTOL, CUKUP SEHARIAN" — largest, two lines, 18% canvas height per line, heavy condensed sign-painter caps, off-white (#F6EFE6), top-left under logo.
2. Price "Rp 55.000" — second largest (~14% canvas height), chili-orange (#E4572E), lower-left directly below bottle base; beside it in smaller off-white (~6% canvas height) "beli 2 jadi Rp 100.000".
3. Deadline "s.d. Minggu ini" — small (~5% canvas height), off-white (#F6EFE6), immediately below the price.
4. CTA strip "Pesan lewat WhatsApp" — clean bottom strip spanning full width, off-white text on deep brown (#3B2418).
No other text, taglines, decorative words, or watermarks.

LOGO / IDENTITY: Image 2 is the business logo. Place unaltered at the upper-left corner, about 10% of canvas width, with clear space on all sides. Keep unchanged: everything. Do not redraw or reinterpret.

COLOR SYSTEM:
Dominant field: deep coffee-brown (#3B2418) ~60% — honest warmth, the confidence behind the promise.
Primary content: warm off-white (#F6EFE6) ~30% — all text and secondary elements.
Accent: chili-orange (#E4572E) ~10% — used ONLY for price; nowhere else.

GRAPHIC ELEMENTS: No graphic elements beyond hero, text, and logo. Do not add decorative shapes, icons, or fills.

ATTACHED IMAGES (attach in this order):
Image 1 = owner's real photo of a 1-litre milk-coffee bottle with a kraft paper label. Role: hero. Treatment: keep exactly; replace background with flat deep coffee-brown. Placement: left-center, bottle base at 60% from top. Size: about 55% of canvas height. Keep unchanged: bottle shape, kraft label design, cap color, liquid color. May change: background, light direction softened to match scene.
Image 2 = business logo, dark brown on transparent background. Role: brand mark. Treatment: place unaltered. Placement: top-left corner, about 10% of canvas width, clear space on all sides. Keep unchanged: everything.
Priority if conflicts: Image 1 wins on product appearance; Image 2 must never be redrawn or recolored.

VISUAL SYSTEM (identical in every prompt of this set):
Type: heavy condensed sign-painter caps for headline; clean humanist sans for support text; no scripts. Style and material: photographic product on flat painted dark-brown surface, matte finish, natural window light with slight warm cast. Image treatment: real product photos kept exactly, placed on surface with a soft grounded contact shadow, no glow. Device: none. Space level: calm.

EXCLUSIONS: Keep bottle shape, label, and logo exactly as photographed. Avoid floating coffee beans or liquid splashes, glow effects, gradient backgrounds, decorative sparkles, rounded glass panels behind text, extra invented text, stock smiling people, busy patterned backgrounds.
```

Lampiran: 1. Foto botol (hero, kiri tengah). 2. Logo (pojok kiri atas). Cara: unggah keduanya dalam urutan ini, lalu tempel prompt di kolom yang sama dan kirim bersamaan.

## 11. Example B: spanduk background (strategy B, no images attached)

Brief: "Laundry Bersih Kilat", Depok; students and workers; message "selesai besok"; action: call or WhatsApp; spanduk 3 m × 1 m on roadside shop front; price Rp 6.000/kg; direction: clean, reliable, sky-blue.

**Blueprint summary (produced before writing the prompt):**
- Concept: "Beres sebelum besok — the domestic relief of done." Concept trace: sky-blue left zone → clean and spacious for fast reading; clothes stack right → physical proof of the promise; no text in image → strategy B for roadside accuracy.
- Zones: text zone left 65% (flat sky-blue, text added later); clothes stack right 35%; navy band bottom 8%.
- Format: 3:1 wide horizontal, viewed from 5-8 m on foot. Headline must be at least 25% canvas height when added.
- Information levels: L1 "SELESAI BESOK" (added later); L2 price per kg (added later); L3 phone (added later); no in-image text.
- Hero: folded laundry stack, real-photo feel, right third.
- Prohibitions: any text rendered in image, floating bubbles, washing machines, stock families.

```
FORMAT: Printed roadside shop banner, 3×1 m vinyl tarpaulin. 3:1 aspect ratio (3000×1000 px).
PHYSICAL CONTEXT: Viewed from 5-8 m by pedestrians and slow traffic; headline (added later) must occupy at least 25% of canvas height; left two-thirds must be completely flat and empty for text legibility; maximum 2 visual elements in the right third.

OBJECTIVE: Provide a clean, flat visual background that the printer or owner will complete with business name, "SELESAI BESOK", price per kg, and phone number in large bold type.

CONCEPT: "Selesai besok." Clean and reliable. For students and workers who need their laundry done without waiting.

COMPOSITION: Asymmetric. Left two-thirds is a single flat sky-blue field (#BFE3F2) reserved entirely for text to be added later — no detail, no texture, no symbols of any kind. Right third contains the clothes stack, grounded on a plain white laminate table surface. A narrow navy band (#14284B) runs the full width at the bottom 8%. Clothes stack occupies about 60% of canvas height on the right side. Margins 5%. Eye path: text zone (left) → clothes stack (right) → navy band.

WHITESPACE: Left two-thirds of canvas is the primary text zone and must be completely flat sky-blue (#BFE3F2) with zero texture, zero detail, zero decoration. Nothing enters this zone. This is not background — it is a reserved text surface.

HERO VISUAL: Right third of the banner only. A neat stack of three freshly folded garments — a white cotton shirt on top, a sky-blue towel in the middle, a cream linen shirt at the base — resting directly on a plain white laminate table surface. One hand-tied paper tag in sunny yellow (#FFC83D) tucked under the top fold. Overhead natural daylight, slightly diffused, with a crisp grounded shadow beneath the stack. Fabric creases and weave texture visible on each garment. No extra props, no hangers, no soap, no machines.

TEXT: Do not render any text, letters, numbers, symbols, or logos anywhere on the canvas. Strategy B — all text to be added in Canva or at the printer.

LOGO / IDENTITY: No logo in this image. Logo to be added by owner in Canva or at the printer.

COLOR SYSTEM:
Dominant field: sky-blue (#BFE3F2) ~65% — clean, open, readable.
Primary content: white and soft cream ~20% — garment colors.
Accent: navy (#14284B) ~10% — bottom band only.
Structural: sunny yellow (#FFC83D) ~5% — paper tag on garments only.

GRAPHIC ELEMENTS: Full-width navy band (#14284B) at bottom 8% of canvas — functions as a visual base and separates the image from the ground. No other graphic elements.

VISUAL SYSTEM (identical in every prompt of this set):
Type: bold neutral humanist sans, to be added later in editor. Style and material: real-photo feel, matte surfaces, clean flat background. Image treatment: objects grounded on surface with crisp edges and a soft grounded shadow, no glow. Device: navy bottom band. Space level: calm.

EXCLUSIONS: Keep left two-thirds entirely flat sky-blue with zero detail. Avoid any text or symbols anywhere on the canvas, washing machines, floating soap bubbles, sparkles, decorative wave patterns, steam effects, stock families, foam splashes, any decoration in the text zone.
```

Lampiran: Tidak ada lampiran.

Cara pakai: Tambahkan teks di Canva atau di percetakan — nama usaha, "SELESAI BESOK", harga per kg, dan nomor telepon — dalam huruf navy tebal yang besar di area biru kiri. Ukuran huruf judul minimal 25% tinggi canvas.

## 12. Example C: feed post, no reference images, with identity treatment (strategy A)

Brief: "Sambal Mbah Sari", Yogyakarta, hand-ground sambal in jars, sold via WhatsApp; buyers: urban adults 25-45; message: "diulek pagi ini, dikirim hari ini"; action: order via WhatsApp; price Rp 25.000/jar; no logo, no photos; direction: handmade warmth, honest, artisanal, traditional Java.

**Blueprint summary (produced before writing the prompt):**
- Concept: "A jar that arrived this morning — the texture of something made before dawn." Concept trace: terracotta surface → Javanese domestic authenticity; chunky sambal visible through glass → proof of handmade craft; slab-serif stamp identity → merek lokal bukan templat; generous space flanking jar → confident, nothing to hide.
- Zones: identity panel top 12% full-width; jar centered 50% canvas height in lower 55%; price block below jar; CTA strip bottom 10%; calm zones left and right of jar ~35% total.
- Information levels: L1 identity "SAMBAL MBAH SARI"; L2 price "Rp 25.000 / toples"; L3 headline "Diulek pagi ini, dikirim hari ini."; L4 CTA "Pesan via WhatsApp"; removed: social proof, tagline.
- Identity treatment: heavy slab-serif caps, off-white, dark-brown full-width panel, "Yogyakarta — diulek sejak 1987" in small caps beneath.
- Accent: golden yellow — price only.
- Prohibitions: glossy jar, neon-red sambal, floating chillies, heavy bokeh.

```
FORMAT: Instagram feed post, square 1:1 (1080×1080 px).
PHYSICAL CONTEXT: Viewed on a phone screen; image must read clearly at 360 px wide; headline and price readable as primary elements; max 5 text elements.

OBJECTIVE: Hook an urban adult mid-scroll and communicate the freshness and handmade authenticity of the product clearly enough that they message to order.

CONCEPT: "Diulek pagi ini, dikirim hari ini." Handmade and honest. For urban adults who want real food, not factory product.

COMPOSITION: Symmetric. Jar centered horizontally, occupying about 50% of canvas height, base resting on terracotta tile at the 65% mark from top. Identity panel spans the full canvas width at the top 12%. Price block centered below the jar. CTA strip at the bottom 10%. Alignment: centered. Margins 6%. Eye path: identity panel → jar → price → headline → CTA strip.

WHITESPACE: About 35% of the canvas stays calm — the terracotta surface areas flanking the jar (left and right of center) and the dark-brown field above the jar. Nothing decorative floats in these areas. The jar stands in open space; nothing crowds it on the sides.

HERO VISUAL: A small squat glass jar, about 8 cm tall and 7 cm diameter, filled with dark-red chunky sambal bawang. Lid sealed with a square of brown kraft paper tied with natural twine. The jar sits on a worn terracotta tile surface. A traditional batu cobek (stone mortar) partially visible and softly out of focus to the left. Morning side-light from a window, warm and slightly golden, short shadow falling to the right. Sambal texture visible through the glass — chunky, with visible whole chilli seeds and shallot slivers. No garnish, no extra props, no decorative chillies or garlic outside the jar.

TEXT (render exactly as written, in Indonesian, no additional words):
1. Business name "SAMBAL MBAH SARI" — largest, heavy slab-serif capitals, warm off-white (#FAF0E6), stamped-ink look with very slight texture, centered inside the dark-brown top panel.
2. Tagline "Yogyakarta — diulek sejak 1987" — small caps humanist sans, off-white (#FAF0E6), centered directly below the name in the same top panel.
3. Price "Rp 25.000 / toples" — second largest (~12% canvas height), warm golden yellow (#D4A017), centered below the jar.
4. Headline "Diulek pagi ini, dikirim hari ini." — medium (~7% canvas height), off-white (#FAF0E6), centered below the price.
5. CTA strip "Pesan via WhatsApp" — bottom strip spanning full canvas width, off-white text on dark brown (#2C1A0E).
No other text, taglines, decorative words, or watermarks.

LOGO / IDENTITY: No logo file available. Business name "SAMBAL MBAH SARI" rendered in heavy slab-serif capitals, warm off-white (#FAF0E6), with a stamped-ink texture, inside a full-width dark-brown rectangular panel (#2C1A0E) spanning the top 12% of canvas height. Below the name in the same panel: "Yogyakarta — diulek sejak 1987" in small caps humanist sans, off-white, smaller. This panel is the brand mark — it must appear exactly as described, not reinterpreted.

COLOR SYSTEM:
Dominant field: dark brown (#2C1A0E) ~55% — handmade depth, earthy authenticity.
Primary content: warm terracotta (#B5522A) ~25% — tile surface and background warmth.
Secondary content: warm off-white (#FAF0E6) ~15% — all text.
Accent: golden yellow (#D4A017) ~5% — used ONLY for price; nowhere else.

GRAPHIC ELEMENTS: Full-width dark-brown panel (#2C1A0E) at top 12% of canvas — serves as the brand identity carrier. No other graphic elements. Do not add decorative motifs, leaf patterns, or chilli illustrations.

VISUAL SYSTEM (identical in every prompt of this set):
Type: heavy slab-serif caps for business name and headline; small caps humanist sans for supporting text; no scripts. Style and material: photographic still life on real terracotta tile, warm morning window light, matte surfaces, slight visible texture on jar and tile. Image treatment: all objects grounded on surface with a natural contact shadow, no glow or studio effects. Device: full-width dark-brown panel as brand mark at top. Space level: calm.

EXCLUSIONS: Keep jar proportions realistic (squat, small) and sambal texture visibly chunky. Avoid glossy jar surfaces, neon-red sambal color, floating chillies or garlic outside the jar, heavy bokeh that erases the terracotta tile texture, invented certifications or award ribbons, extra decorative Javanese motifs not requested, generic "artisan" props (twine bundles, dried herbs scattered around).
```

Lampiran: Tidak ada lampiran.

## 13. Assembling a set

1. Write the **Visual System block once** and copy it word for word into every prompt.
2. Write the **CONCEPT** campaign line once; it is the same in every prompt.
3. For each output write its own: FORMAT + PHYSICAL CONTEXT, OBJECTIVE, COMPOSITION, WHITESPACE, HERO VISUAL, TEXT, LOGO/IDENTITY, COLOR SYSTEM, GRAPHIC ELEMENTS, (ATTACHED IMAGES if applicable), EXCLUSIONS.
4. Check: any "same as", "previous", "above", or cross-prompt image reference? Remove it.
5. Check: is there an ATTACHED IMAGES block in a prompt with no images? Remove it — do not replace with a note.
6. Run the self-check in `SKILL.md`, then give each prompt its **Lampiran** list (`03-reference-images.md` section 12). A full worked set is in `examples/01-warung-bakso-sesi-lengkap.md`.
