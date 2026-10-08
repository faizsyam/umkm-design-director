# Prompt Assembly (Stage 9)

Contents: what a prompt must do · the template · block rules · text strategy · phrasing rules · length and tool notes · contradiction check · example A (feed post with images) · example B (spanduk background, no images) · example C (feed post with no images, identity treatment) · assembling a set

## 1. What a prompt must do

A prompt is a **complete, final design brief** for a model that cannot ask questions. It produces the finished design with zero manual post-editing of essential elements. It carries the **format**, the **concept**, the **attached images and what to do with each** (or nothing if there are none), the **hero**, the **layout, space, and reading path**, the **exact text with ranks**, the **Visual System**, the **truth constraints**, and a **short exclusion line**. Nothing else.

Every sentence must change the picture. A sentence that explains the reasoning, describes the design process, or re-states a viewing context without translating it into a design decision does not belong in the prompt.

**Viewing context → design decisions:** Never paste viewing-context or use-case statements directly into the prompt. Instead, translate them:
- "Viewed from 10 m on a motorbike" → "headline in heavy condensed type at 28% of canvas height, maximum 5 words, high value-contrast on flat single-color background."
- "Must read in 3 seconds" → "three text elements only, headline at the largest scale, no more than 8 words total, calm empty area isolating the hero."
- "Seen on a phone while scrolling" → "single dominant element at 55% of canvas height, headline in two short lines above it, strong silhouette contrast."

**Every prompt is fully standalone.** It works if pasted alone into a fresh chat: no "same as before", no reference to another prompt, no dependence on a generated result. When there are several outputs, each prompt repeats the shared Visual System verbatim (see `09-output-sets.md`).

## 2. The template

Two layers: **output blocks** (differ per output) and the **VISUAL SYSTEM block** (identical in every prompt of a set). Fill each block with decisions, not adjectives; omit a block only if it truly does not apply.

```
FORMAT: [material], [aspect ratio and pixels], for [platform].

CONCEPT: "[campaign idea, same words in every prompt of a set]". [Two feelings]. For [audience]. This output's job: [hook / inform / act].

[ATTACHED IMAGES block — include ONLY if images are being attached. Omit this block entirely when there are none:]
ATTACHED IMAGES (attach in this order):
Image 1 = [what it is, as visible]. Role: [...]. Treatment: [...]. Placement: [...]. Size: [...]. Keep unchanged: [...]. May change: [...].
Image 2 = ...
Priority if conflicts: [...].

HERO VISUAL: [specific subject, or "Image 1"], [angle/distance], [surface/setting], [light source and quality], [texture and material detail], [one or two ownable details].

COMPOSITION: [zones with positions and percentages]. [Alignment spine]. SPACE: about [N]% of the canvas stays calm and empty ([flat color], no texture or detail), mainly [where]; nothing floats in it; no decorative elements. Margins about [6-8]%. Eye path: [A -> B -> C -> D].

TEXT (render exactly as written, in [language], no additional words):
1. [role] "[exact text]" - [size rank], [type character], [case], [color], [position]
2. ...
[Clean empty zone for text added later, if strategy B or C. Reserved empty square for official marks, if needed.]

VISUAL SYSTEM (identical in every prompt of this set):
Palette: [dominant ~60% name+hex]; [support ~30%]; [accent ~10%, used only for ___]. Type: [headline character]; [support character]; [case/weight]. Style and material: [photo/illustration], [texture, finish, light quality]. Image treatment: [how real images are cleaned, cropped, grounded]. Device: [one recurring graphic device, or none]. Space level: [calm / moderate / dense-but-grouped].

KEEP / AVOID: Keep [truth constraints]. Avoid [4-6 specific failure modes for this brief].
```

## 3. Block rules

**FORMAT.** State the ratio explicitly. Do not include a viewing-context sentence here — translate it into design decisions in HERO VISUAL, COMPOSITION, and TEXT instead.

**CONCEPT.** The campaign idea, in the same words in every prompt of the set, plus the output's job. It comes from the Distinction Brief (USP and proof, desired perception). This is a *design concept*, not a process note.

**ATTACHED IMAGES — critical rules:**
- **Omit this block entirely** when no images are attached. Do not write the header, do not write anything in its place — just move on to HERO VISUAL.
- Include the block only when the owner is literally attaching image files to the AI prompt.
- Follow `03-reference-images.md` section 10 exactly: fixed order, one primary treatment per image, placement as zone and margin, size as percent of canvas, keep-unchanged and may-change, and an explicit statement of any requested modification (enhance, upscale, cut out, illustrate, extend, restyle, revise). Numbering is local to this prompt.
- Use "Image 1" the same way in HERO, COMPOSITION, and TEXT blocks.

**HERO VISUAL.** Name the real thing with physical specificity. Not "a delicious dish" but "a bowl of bakso with a golf-ball-sized beef meatball in a clear bone broth on a worn wooden cart counter, late-afternoon window light from the left, a thin curl of steam above the broth, visible grain in the bowl glaze." If a photo is attached, say to keep it. Push toward credible commercial photography: real surfaces, natural light, believable proportions, visible texture, slight physical imperfection. Explicitly avoid studio-ad aesthetics.

**COMPOSITION and SPACE.** Zones with proportions ("headline in the top 25%, product 50% of height left of center, price lower third, CTA strip bottom 10%"). Choose symmetrical or asymmetrical on purpose. Give the **space instruction** with a percentage and where it sits; this is the single most effective line against cramped, decorated output. End with the eye path.

**TEXT.** One line per element with role, rank, character, color, and position. Quote exact text; instruct "render exactly as written". Three to six elements. Unrelated instructions never go inside quotation marks. If strategy B or C, describe the clean zone for later text.

**VISUAL SYSTEM.** Compact (about 60-80 words). Palette with roles and hex, type character, style and material, image treatment, device, space level, voice. For a single-output job it is still written, so the prompt stays self-contained and the owner can reuse it.

**KEEP / AVOID.** "Keep" = truth constraints. "Avoid" = a short list of concrete failure modes: "floating ingredients, glow effects, gradient backgrounds, decorative sparkles, extra or invented text, stock-style smiling people, crowded corners."

## 4. Text strategy

| Strategy | When | Prompt approach |
|---|---|---|
| **A: in-image text** | Tool renders text well; short headline, offer, price, CTA; screen only; **default for simple screen promos** | Quote each line; "render exactly as written, no additional words" |
| **B: clean text zones** | Print, spanduk, menus, long info, phone numbers, addresses, legal marks, text-heavy redesigns | "Leave a clean, calm, empty [position] area, about [size], for text added later. Do not render any text, letters, numbers, or logos." |
| **C: hybrid** | Screen posts with contact info that the owner wants to add themselves | Headline and price in-image; "leave a clean strip at the bottom 12% for contact details added later; no other text" |

Rules for A and C: quote exactly, keep lines short and large, specify the language, say what not to add ("no taglines, no extra words, no watermarks"), and tell the owner to proofread after generation.

**Do not choose B or C to avoid the effort of specifying text.** If the content is short and the tool renders text reasonably, use A and produce the finished design.

## 5. Phrasing rules

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

## 6. Realistic food and product imagery

When the prompt must generate food or product imagery without a reference photo, describe it to push toward credible commercial photography:

- **Light:** name the source and direction ("soft morning light from a north-facing window, diffused through white curtain, shadows falling left"). Never "professional studio lighting" or "beautifully lit".
- **Surface:** real, named material ("worn dark-teak wood counter with visible grain and a water ring stain"; "pale stone table with matte finish"). Never "beautiful background".
- **Angle:** specific camera angle and distance ("looking slightly down at 25°, close enough that the bowl fills 55% of the frame"). Never "appetizing angle".
- **Texture and detail:** visible food texture that is physically plausible ("glossy broth surface with a thin orange oil film, meatball with visible sear marks, chopped green onion lying flat in the broth"). Never "perfectly plated", "gorgeous garnish".
- **Proportions:** realistic, not exaggerated ("a standard 18 cm bowl, meatball at about 4 cm diameter"). Never "enormous", "overflowing".
- **Imperfection is realism:** a condensation drop on a bottle, a small chip on a plate, a slightly uneven sprinkle. These details signal a real photo.
- **Avoid explicitly:** "excessive gloss, exaggerated portion size, ingredients floating mid-air or erupting from the dish, plastic-looking surfaces, extreme depth-of-field blur, generic stock-food aesthetics."

## 7. Length and tool notes

- Aim for **200-450 words per prompt**, up to about 550 when three or more images are attached; shorter for simple briefs. The Visual System (60-90 words) and the image block are most of the length and are intentional. If you pass these limits you are probably describing decoration or repeating yourself: cut.
- Tools differ in text accuracy, image-input support, number of images accepted, and respect for aspect ratio. Ask which tool; when unsure choose C for screen and B for print; if the tool ignores ratio, set it in the interface or crop and keep content inside the safe area.
- Let the owner change **one thing at a time** when iterating (`12-review-and-iteration.md`).

## 8. Contradiction check

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

## 9. Example A: feed post with attached images (strategy A)

Brief: "Kopi Mbak Rini", Bekasi, 1-litre milk coffee; buyers: anak kos and office workers 20-35; action: order via WhatsApp; message: "satu botol cukup seharian"; offer Rp 55.000/botol, beli 2 Rp 100.000, until Sunday; bottle photo and logo available; direction: warm, confident, merakyat.

```
FORMAT: Instagram feed promo post, vertical 4:5 (1080×1350 px).

CONCEPT: "Satu botol, cukup seharian." Confident and unpretentious. For students and office workers who want honest daily coffee. This output's job: hook and offer.

ATTACHED IMAGES (attach in this order):
Image 1 = owner's real photo of a 1-litre milk-coffee bottle with a kraft paper label. Role: hero. Treatment: keep exactly; replace background with flat deep coffee-brown. Placement: left of center, bottle base resting on a plain wooden counter. Size: about 55% of canvas height. Keep unchanged: bottle shape, kraft label design, cap color, liquid color. May change: background, light direction softened to match the scene.
Image 2 = business logo, dark brown on transparent background. Role: brand mark. Treatment: place unaltered. Placement: top-left corner, about 10% of canvas width, with clear space on all sides. Keep unchanged: everything.
Priority if conflicts: Image 1 wins on product appearance; Image 2 must never be redrawn or recolored.

HERO VISUAL: Image 1. Bottle standing upright, slightly low angle looking up at 10°, on a worn dark-teak counter with visible grain. Window light from the left, soft and warm, casting a faint shadow rightward. No reflections on the label.

COMPOSITION: Asymmetric. Headline stacked left-aligned under the logo in the top 28%. Price block in the lower-left third, below the bottle base. WhatsApp call-to-action strip across the bottom 10%. SPACE: about 40% of canvas stays calm and empty (flat deep coffee-brown, #3B2418, no texture), mainly the right half; nothing floats there; no decorative elements. Margins 6%. Eye path: headline → bottle → price block → WhatsApp strip.

TEXT (render exactly as written, in Indonesian, no additional words):
1. Headline "SATU BOTOL, CUKUP SEHARIAN" — largest, two lines, heavy condensed caps, off-white (#F6EFE6), top-left under logo.
2. Price "Rp 55.000" — second largest, chili-orange (#E4572E); beside it in smaller off-white "beli 2 jadi Rp 100.000".
3. Deadline "s.d. Minggu ini" — small, off-white, immediately below the price.
4. CTA strip "Pesan lewat WhatsApp" — clean bottom strip, off-white text on deep brown, same width as canvas.
No other text, taglines, decorative words, or watermarks.

VISUAL SYSTEM (identical in every prompt of this set):
Palette: deep coffee-brown (#3B2418) dominant ~60%; warm off-white (#F6EFE6) ~30%; chili-orange (#E4572E) ~10%, used only for prices. Type: heavy condensed sign-painter capitals for headline and price; clean humanist sans for support text; no scripts. Style and material: photographic product on flat painted dark-brown surface, matte finish, natural window light with slight warm cast. Image treatment: real product photos kept exactly, placed on surface with a soft grounded contact shadow, no glow. Device: none. Space level: calm.

KEEP / AVOID: Keep bottle shape, label, and logo exactly as photographed. Avoid floating coffee beans or liquid splashes, glow effects, gradient backgrounds, decorative sparkles, rounded glass panels behind text, extra invented text, stock smiling people.
```

Lampiran: 1. Foto botol (hero, kiri tengah). 2. Logo (pojok kiri atas). Cara: unggah keduanya dalam urutan ini, lalu tempel prompt di kolom yang sama dan kirim bersamaan.

## 10. Example B: spanduk background (strategy B, no images attached)

Brief: "Laundry Bersih Kilat", Depok; students and workers; message "selesai besok"; action: call or WhatsApp; spanduk 3 m × 1 m on roadside shop front; price Rp 6.000/kg; direction: clean, reliable, sky-blue.

```
FORMAT: Wide horizontal banner background, 3:1 (3000×1000 px), for a printed roadside shop banner.

CONCEPT: "Selesai besok." Clean and reliable. For students and workers with no time to wait. This output's job: hook and act.

No images are attached; create everything from this description.

HERO VISUAL: Right third of the banner. A neat stack of three freshly folded garments — a white cotton shirt, a sky-blue towel, a cream linen shirt — resting on a plain white laminate table. One hand-tied paper tag in sunny yellow tucked under the top fold. Overhead natural daylight, slightly diffused, crisp shadow beneath the stack. Fabric creases and weave texture visible. No extra props.

COMPOSITION: Asymmetric. Right third holds the clothes stack, grounded on the table. The left two-thirds is a single flat sky-blue area (#BFE3F2) reserved entirely for text added later. A narrow navy band (#14284B) runs along the full bottom 8%. SPACE: left two-thirds completely empty, flat sky-blue, no texture or detail; nothing floats in it; render no text, letters, numbers, logos, or symbols anywhere in this zone. The clothes stack occupies about 60% of canvas height on the right. Margins 5%. Eye path: empty text area → clothes stack → navy band.

TEXT: Do not render any text, letters, numbers, or logos anywhere. Strategy B — all text to be added in an editor.

VISUAL SYSTEM (identical in every prompt of this set):
Palette: sky-blue (#BFE3F2) dominant ~65%; white and soft cream ~20%; navy (#14284B) ~10%; sunny yellow (#FFC83D) ~5%, used only for the paper tag. Type: bold neutral humanist sans, added later in editor. Style and material: real-photo feel, matte, clean flat background. Image treatment: objects grounded on a surface with crisp edges and a soft grounded shadow. Device: navy bottom band. Space level: calm.

KEEP / AVOID: Keep left two-thirds entirely flat and empty with no detail. Avoid any text or symbols, washing machines, floating bubbles, sparkles, decorative wave patterns, steam, stock families, soap-foam effects.
```

Lampiran: Tidak ada lampiran.

Cara pakai: Tambahkan teks di Canva atau di percetakan — nama usaha, "SELESAI BESOK", harga per kg, dan nomor telepon — dalam huruf navy tebal yang besar di area biru kiri.

## 11. Example C: feed post, no reference images, with identity treatment (strategy A)

Brief: "Sambal Mbah Sari", Yogyakarta, hand-ground sambal in jars, sold via WhatsApp; buyers: urban adults 25-45; message: "diulek pagi ini, dikirim hari ini"; action: order via WhatsApp; price Rp 25.000/jar; no logo, no photos; direction: handmade warmth, honest, artisanal, traditional Java.

```
FORMAT: Instagram feed post, square 1:1 (1080×1080 px).

CONCEPT: "Diulek pagi ini, dikirim hari ini." Handmade and honest. For urban adults who want real food, not factory product. This output's job: hook and order.

No images are attached; create everything from this description.

HERO VISUAL: A small squat glass jar (about 8 cm tall, 7 cm diameter) filled with dark-red chunky sambal bawang, lid sealed with a square of brown kraft paper tied with natural twine. The jar sits on a worn terracotta tile surface, a traditional batu cobek (stone mortar) partially visible and softly out of focus to the left. Morning side-light from a window, warm and slightly golden, casting a short shadow to the right. The sambal texture visible through the glass — chunky, with visible whole chilli seeds and shallot slivers. No garnish, no extra props.

IDENTITY: Business name "SAMBAL MBAH SARI" rendered in heavy slab-serif capitals, warm off-white (#FAF0E6), stamped-ink look with very slight texture, centered at the top of the image inside a narrow dark-brown rectangular panel spanning the full width at 12% of canvas height. Below the name, in small caps humanist sans: "Yogyakarta — diulek sejak 1987".

COMPOSITION: Symmetric. The jar is centered, occupying about 50% of canvas height, resting on the terracotta surface in the lower 55% of the image. The identity panel sits at the top. Price block sits below the jar. CTA strip at the bottom 10%. SPACE: about 35% of canvas stays calm — the terracotta surface areas flanking the jar and the dark-brown background above; nothing decorative floats there. Margins 6%. Eye path: name panel → jar → price → WhatsApp strip.

TEXT (render exactly as written, in Indonesian, no additional words):
1. Business name "SAMBAL MBAH SARI" — largest, slab-serif capitals, off-white (#FAF0E6), centered in dark-brown top panel.
2. Tagline "Yogyakarta — diulek sejak 1987" — small caps, off-white, centered directly below the name in the same panel.
3. Price "Rp 25.000 / toples" — second largest, warm yellow (#D4A017), centered below the jar.
4. Headline "Diulek pagi ini, dikirim hari ini." — medium, off-white, centered below the price.
5. CTA strip "Pesan via WhatsApp" — bottom strip, off-white on dark brown (#2C1A0E).
No other text, taglines, decorative words, or watermarks.

VISUAL SYSTEM (identical in every prompt of this set):
Palette: dark brown (#2C1A0E) dominant ~55%; warm terracotta (#B5522A) ~25%; warm off-white (#FAF0E6) ~15%; golden yellow (#D4A017) ~5%, used only for price. Type: heavy slab-serif caps for business name and headline; small caps humanist sans for supporting text; no scripts. Style and material: photographic still life on real terracotta tile, warm morning window light, matte surfaces, slight visible texture on jar label and background tile. Image treatment: all objects grounded on a surface with a natural contact shadow, no glow or studio effects. Device: full-width dark-brown panel as brand mark at top. Space level: calm.

KEEP / AVOID: Keep the jar proportions realistic (squat, small) and the sambal texture visibly chunky. Avoid glossy jar surfaces, neon-red sambal color, floating chillies or garlic, bokeh-heavy backgrounds that erase the terracotta texture, extra decorative elements, invented certifications or ribbons.
```

Lampiran: Tidak ada lampiran.

## 12. Assembling a set

1. Write the **Visual System block once** and copy it word for word into every prompt.
2. Write the **CONCEPT** campaign line once; add each output's job.
3. For each output write its own FORMAT, (ATTACHED IMAGES or "No images" line), HERO crop, IDENTITY treatment if no logo, COMPOSITION and SPACE, TEXT, KEEP/AVOID.
4. Check: any "same as", "previous", "above", or cross-prompt image reference? Remove it.
5. Check: is there an ATTACHED IMAGES block in a prompt with no images? Remove it and add the "No images are attached" line.
6. Run the self-check in `SKILL.md`, then give each prompt its **Lampiran** list (`03-reference-images.md` section 12). A full worked set is in `examples/01-warung-bakso-sesi-lengkap.md`.
