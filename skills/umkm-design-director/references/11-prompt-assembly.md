# Prompt Assembly (Stage 9)

Contents: what a prompt must do · the template · block rules · text strategy · phrasing rules · length and tool notes · contradiction check · example A (feed post with images) · example B (spanduk background) · assembling a set

## 1. What a prompt must do

A prompt is a compressed design brief for a model that cannot ask questions. It carries the **format**, the **idea**, the **attached images and what to do with each**, the **hero**, the **layout, space, and reading path**, the **exact text with ranks**, the **Visual System**, the **truth constraints**, and a **short exclusion line**. Nothing else. Every sentence must change the picture.

**Every prompt is fully standalone.** It works if pasted alone into a fresh chat: no "same as before", no reference to another prompt, no dependence on a generated result. When there are several outputs, each prompt repeats the shared Visual System verbatim (see `09-output-sets.md`).

## 2. The template

Two layers: **output blocks** (differ per output) and the **VISUAL SYSTEM block** (identical in every prompt of a set). Fill each block with decisions, not adjectives; omit a block only if it truly does not apply.

```
FORMAT: [material], [aspect ratio and pixels], for [platform]. Viewed [how/where/how long].

CONCEPT: "[campaign idea, same words in every prompt of a set]". [Two feelings]. For [audience]. This output's job: [hook / inform / act].

ATTACHED IMAGES (attach in this order):
Image 1 = [what it is, as visible]. Role: [...]. Treatment: [...]. Placement: [...]. Size: [...]. Keep unchanged: [...]. May change: [...].
Image 2 = ...
Priority if conflicts: [...].
(If none: "No images are attached; create everything from this description.")

HERO VISUAL: [specific subject, or "Image 1"], [angle/distance], [surface/setting], [light], [one or two ownable details].

COMPOSITION: [zones with positions and percentages]. [Alignment spine]. SPACE: about [N]% of the canvas stays calm and empty ([flat color], no texture or detail), mainly [where]; nothing floats in it; no decorative elements. Margins about [6-8]%. Eye path: [A -> B -> C -> D].

TEXT (render exactly as written, in [language], no additional words):
1. [role] "[exact text]" - [size rank], [type character], [case], [color], [position]
2. ...
[Clean empty zone for text added later, if strategy B or C. Reserved empty square for official marks, if needed.]

VISUAL SYSTEM (identical in every prompt of this set):
Palette: [dominant ~60% name+hex]; [support ~30%]; [accent ~10%, used only for ___]. Type: [headline character]; [support character]; [case/weight]. Style and material: [photo/illustration], [texture, finish, light]. Image treatment: [how real images are cleaned, cropped, grounded]. Device: [one recurring graphic device, or none]. Space level: [calm / moderate / dense-but-grouped].

KEEP / AVOID: Keep [truth constraints]. Avoid [4-6 specific failure modes for this brief].
```

## 3. Block rules

**FORMAT.** State the ratio explicitly. Include the viewing context because it changes density ("viewed on a phone in a fast scroll"). For stories: "keep all text inside the central 70% of the height".

**CONCEPT.** The campaign idea, in the same words in every prompt of the set, plus the output's job. It comes from the Distinction Brief (USP and proof, desired perception).

**ATTACHED IMAGES.** The most error-prone block; follow `03-reference-images.md` section 10 exactly: fixed order, one primary treatment per image, placement as zone and margin, size as percent of canvas, keep-unchanged and may-change, and an explicit statement of any requested modification (enhance, upscale, cut out, illustrate, extend, restyle, revise). Numbering is local to this prompt. Use "Image 1" the same way in HERO, COMPOSITION, and TEXT blocks.

**HERO VISUAL.** Name the real thing. Not "a delicious dish" but "a bowl of bakso with a tennis-ball-sized tendon meatball in clear broth on a worn wooden cart counter, side window light, a little real steam". If a photo is attached, say to keep it.

**COMPOSITION and SPACE.** Zones with proportions ("headline in the top 25%, product 50% of height left of center, price lower third, CTA strip bottom 10%"). Choose symmetrical or asymmetrical on purpose. Give the **space instruction** with a percentage and where it sits; this is the single most effective line against cramped, decorated output. End with the eye path.

**TEXT.** One line per element with role, rank, character, color, and position. Quote exact text; instruct "render exactly as written". Three to six elements. Unrelated instructions never go inside quotation marks.

**VISUAL SYSTEM.** Compact (about 60-80 words). Palette with roles and hex, type character, style and material, image treatment, device, space level, voice. For a single-output job it is still written, so the prompt stays self-contained and the owner can reuse it.

**KEEP / AVOID.** "Keep" = truth constraints. "Avoid" = a short list of concrete failure modes: "floating ingredients, glow effects, gradient backgrounds, decorative sparkles, extra or invented text, stock-style smiling people, crowded corners".

## 4. Text strategy

| Strategy | When | Prompt approach |
|---|---|---|
| **A: in-image text** | Tool renders text well; short headline, offer, price, CTA; screen only | Quote each line; "render exactly as written, no additional words" |
| **B: clean text zones** | Print, spanduk, menus, long info, phone numbers, legal marks, text-heavy redesigns | "Leave a clean, calm, empty [position] area, about [size], for text added later. Do not render any text, letters, numbers, or logos." |
| **C: hybrid** | Default for screen posts with contact info | Headline and price in-image; "leave a clean strip at the bottom 12% for contact details added later; no other text" |

Rules for A and C: quote exactly, keep lines short and large, specify the language, say what not to add ("no taglines, no extra words, no watermarks"), and tell the owner to proofread after generation.

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

## 6. Length and tool notes

- Aim for **200-450 words per prompt**, up to about 550 when three or more images are attached; shorter for simple briefs. The Visual System (60-90 words) and the image block are most of the length and are intentional. If you pass these limits you are probably describing decoration or repeating yourself: cut.
- Tools differ in text accuracy, image-input support, number of images accepted, and respect for aspect ratio. Ask which tool; when unsure choose C for screen and B for print; if the tool ignores ratio, set it in the interface or crop and keep content inside the safe area.
- Let the owner change **one thing at a time** when iterating (`12-review-and-iteration.md`).

## 7. Contradiction check

- Any sentence asking for both "minimal" and "rich detail"?
- More than one "largest" element? More than one accent color?
- Text count above the density budget?
- Style (illustration) in conflict with the hero (real photo)?
- Anything the model cannot do reliably (small text, QR, logos, official marks)?
- An exclusion that forbids something the composition requires?
- Any reference to another prompt, or any image numbering that does not match the attachment list?

## 8. Example A: feed post with attached images (strategy C)

Brief: "Kopi Mbak Rini", Bekasi, 1-litre milk coffee; buyers: anak kos and office workers 20-35; action: order via WhatsApp; message: "satu botol cukup seharian"; offer Rp 55.000/botol, beli 2 Rp 100.000, until Sunday; owner has a bottle photo and a logo; feel: warm, modern; no pastels.

```
FORMAT: Instagram feed promo post, vertical 4:5 (1080x1350 px). Viewed on a phone during a fast scroll; must read in 3 seconds.

CONCEPT: "Satu botol, cukup seharian." Confident and friendly, honest and a little playful. For students and office workers who want a good coffee that lasts the day. This output's job: hook and offer.

ATTACHED IMAGES (attach in this order):
Image 1 = the owner's real photo of a 1-litre milk-coffee bottle with a kraft label. Role: hero. Treatment: keep exactly, with the background replaced. Placement: left of center, standing on a plain wooden counter. Size: about 55% of canvas height. Keep unchanged: bottle shape, kraft label, cap, liquid color. May change: background, light direction to match the scene.
Image 2 = the business logo (dark brown on transparent). Role: brand mark. Treatment: place unaltered. Placement: top-left corner, about 10% of canvas width, with clear space. Keep unchanged: everything.
Priority if conflicts: Image 1 wins on product appearance; Image 2 must never be redrawn.

HERO VISUAL: Image 1, slightly low angle, on a wooden stall counter, soft window-light feel.

COMPOSITION: Asymmetric. Headline in the top 28%, left-aligned under the logo. Price block in the lower third under the bottle edge. Narrow call-to-action strip across the bottom 10%. SPACE: about 40% of the canvas stays calm and empty (flat deep brown), mainly the right side; nothing floats in it; no decorative elements. Margins about 6%. Eye path: headline -> bottle -> price -> WhatsApp line.

TEXT (render exactly as written, in Indonesian, no additional words):
1. Headline "SATU BOTOL, CUKUP SEHARIAN" - largest, two lines, off-white (#F6EFE6).
2. Price "Rp 55.000" - second largest, chili-orange (#E4572E); small beside it "beli 2 jadi Rp 100.000" in off-white.
3. Deadline "sampai Minggu" - small, off-white, near the price.
4. Call to action "Pesan lewat WhatsApp" - clean strip at the bottom, off-white on deep brown. Leave the phone number out; it will be added later.
No other text, taglines, or logos.

VISUAL SYSTEM (identical in every prompt of this set):
Palette: deep coffee brown (#3B2418) dominant ~60%; warm off-white (#F6EFE6) ~30%; chili-orange (#E4572E) ~10%, used only for prices. Type: heavy condensed sign-painter capitals for headline and price; clean humanist sans for support text. Style and material: photographic product on a flat painted brown wall with fine paper grain, matte, natural light. Image treatment: real product photos kept exactly, grounded on a surface with a soft contact shadow. Device: none. Space level: calm.

KEEP / AVOID: Keep the bottle exactly as photographed and the logo untouched. Avoid floating coffee beans or splashes, glow effects, gradient backgrounds, decorative sparkles, rounded glass boxes behind text, stock-style smiling people, crowded corners.
```

Lampiran: 1. Foto botol (hero). 2. Logo (pojok kiri atas). Cara: attach both in this order and paste the prompt.

## 9. Example B: spanduk background (strategy B, no images)

Brief: "Laundry Bersih Kilat", Depok; students and workers; message "selesai besok"; action: call or WhatsApp; spanduk 3 m x 1 m on a roadside shop front, seen from a motorbike; price Rp 6.000/kg.

```
FORMAT: Wide horizontal banner background, 3:1 (3000x1000 px), for a roadside shop banner viewed from 10-20 m by motorbike riders. Clear and bold.

CONCEPT: "Selesai besok." Clean, reliable, fast. For students and workers with no time. This output's job: hook and act.

ATTACHED IMAGES: No images are attached; create everything from this description.

HERO VISUAL: On the right third, a neat stack of fresh folded clothes in white and sky-blue with one hand-tied paper tag in sunny yellow, on a plain table. Soft daylight, crisp edges, matte, photographic look.

COMPOSITION: Asymmetric. SPACE: the left two-thirds, about 65% of the canvas, stays one completely empty, flat sky-blue area (#BFE3F2) reserved for text added later; render no text, letters, numbers, logos, or phone numbers anywhere. The clothes stack sits right of center at about 60% of the height, resting on a thin navy band (#14284B) along the bottom 12%. Margins about 5%. Eye path: empty text area -> clothes stack -> navy band.

VISUAL SYSTEM (identical in every prompt of this set):
Palette: sky blue (#BFE3F2) dominant ~65%; white and soft cream ~20%; navy (#14284B) ~10%; sunny yellow (#FFC83D) ~5%, used only for the paper tag. Type: bold neutral sans (added later). Style and material: real-photo feel on clean flat color, matte. Image treatment: objects grounded on a surface, crisp edges. Device: none. Space level: calm.

KEEP / AVOID: Keep the left two-thirds empty and flat. Avoid any text or symbols, washing machines, floating bubbles, sparkles, decorative patterns, stock families.
```

Then tell the owner to add three pieces of text in large navy letters in Canva or at the printer: the name, "SELESAI BESOK", and the price with phone number.

## 10. Assembling a set

1. Write the **Visual System block once** and copy it word for word into every prompt.
2. Write the **CONCEPT** campaign line once; add each output's job.
3. For each output write its own FORMAT, ATTACHED IMAGES (local numbering), HERO crop, COMPOSITION and SPACE, TEXT, KEEP/AVOID.
4. Check: any "same as", "previous", "above", or cross-prompt image reference? Remove it.
5. Run the self-check in `SKILL.md`, then give each prompt its **Lampiran** list (`03-reference-images.md` section 12). A full worked set is in `examples/01-warung-bakso-sesi-lengkap.md`.
