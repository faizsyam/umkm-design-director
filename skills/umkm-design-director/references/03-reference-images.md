# Reference Images and Existing Materials (Stage 2, then used in Stages 7, 8, 9, 10)

Contents: why references matter · material types and their jobs · asking for the right materials per business · receiving and verifying · analyzing each image · treatments · how materials change the design decisions · multiple images · enhance-existing-design mode · visual-direction examples · writing references into the prompt · tool limits and fallbacks · handoff checklist · consent and ownership

## 1. Why references matter

A real photo, logo, mascot, or old design is the strongest anti-slop asset an owner has: it is true, it is theirs, and no model can invent it. Once a reference exists, the job changes from *inventing* to *adapting, composing, or enhancing*. The wrong move is to ignore the material and let the model improvise; the second wrong move is to paste it in without thinking about what it needs (cleaning, cropping, restyling, a place in the hierarchy).

Treat every reference like a design element: it needs a **role**, a **treatment**, a **place**, a **size**, and a rule for **what must not change**.

## 2. Material types and their jobs

| Material | Typical role | Default treatment | Watch out for |
|---|---|---|---|
| **Product photo** (dish, bottle, garment, item) | Hero | Keep exactly; clean background if needed | Low resolution, flash glare, busy background, color cast, label unreadable |
| **Logo** | Brand mark, small and consistent | Place unaltered at a stated position and size | Models distort or redraw logos; transparent vs white background; tiny details |
| **Mascot / character** | Brand personality, hero or accent | Keep design exactly; may change pose only if requested | Drift in proportions and colors across generations |
| **Person** (owner, staff, customer, model) | Trust, human warmth, hero | Keep face and features exactly; choose gaze and placement deliberately | Consent, children, likeness drift, mismatch with audience |
| **Existing design** (old poster, banner, menu, feed post) | Base to improve | Diagnose, then refine, restructure, or rebuild (section 8) | Models alter text and drift layout when "editing" |
| **Visual-direction examples** (designs they like) | Style guidance | Borrow named principles only | Copying layout, text, logos, or another brand's identity |
| **Storefront / cart / interior / packaging photo** | Setting, anchor, palette source | Use as background or as palette and material reference | Cluttered backgrounds, signage with other brands |
| **Handwritten or printed menu / price list photo** | Content source | Extract and retype the text, then rebuild | Handwriting misread: confirm every item and price |
| **Fabric, pattern, texture, packaging swatch** | Palette, pattern, material | Palette-only or pattern-only reference | Sacred or region-specific motifs used out of context |
| **Official marks / certificates** (halal, PIRT, BPOM, NIB) | Compliance | Never generated; added afterward | Models invent lookalikes |

## 3. Asking for the right materials

Ask in Stage 2, after the Distinction Brief (Stage 1), so the request is specific to what makes the business different. Use a tappable multi-select question if the interface supports it, otherwise lettered options. Always allow "tidak ada".

Example (id): "Ada gambar yang bisa jadi acuan supaya hasilnya benar-benar mirip usaha Kakak? Boleh pilih lebih dari satu: A. Logo, B. Foto produk, C. Maskot atau foto orang (pemilik/pelanggan), D. Desain lama yang mau diperbaiki, E. Contoh desain yang Kakak suka, F. Foto warung/toko/gerobak, G. Belum ada."

Give the reason in one phrase: "Foto asli bikin pembeli percaya, dan hasilnya nggak mirip desain AI pasaran."

Then make the request **specific to the business**:

| Business | Ask for first | Then ask for |
|---|---|---|
| Warung, catering, kopi, jajanan | Photo of the real dish or drink in its real vessel or packaging | Storefront or cart, owner at work, menu list |
| Bakery, oleh-oleh, frozen food | Photo of the product and the packaged version | Gift box, label, cross-section photo |
| Fashion, hijab, thrift | Photos of the actual garments (flat-lay or worn), fabric close-up | Model or owner photo, size chart, shop corner |
| Beauty, salon, barber | Photos of real results (with consent), shop interior | Products used, tools, before/after only if genuinely theirs |
| Laundry, cleaning, repair | Shop front, uniform or tools, folded-clothes or finished-work photo | Pickup motorbike, price list |
| Kost, properti, rental | Real room or building photos | Floor plan, nearest landmark photo |
| Handmade, craft, local products | The object and the maker's hands, workshop | Material close-ups, packaging |
| Education, community, events | Photos of past classes or events (with consent), instructor photo | Venue photo, previous poster |
| Any business with a design already | The existing design | What they like and dislike about it |

**If they have none of these:** ask for the single most valuable one and offer help. For a product photo, give the owner the 5-tip card:
1. Shoot by a window in daylight; no flash; no filters.
2. Plain, uncluttered background (a wall, a table, a clean cloth).
3. Fill the frame; shoot from the angle customers would see.
4. Hold the phone steady, clean the lens, tap to focus.
5. Take 3-5 shots, including one where there is empty space around the product.

If photos are truly not possible, continue without them but use a stylized, clearly illustrated direction rather than a photoreal fabrication of the product (honest-imagery rule), and say so in the plan.

## 4. Receiving and verifying

- **Check that each image is actually visible in the conversation.** A message that says "ini fotonya" does not mean a file arrived. If you cannot see it, ask to send again.
- **Number images in upload order** ("Gambar 1, Gambar 2...") and confirm the numbering and roles with the owner in one line: "Gambar 1 saya pakai sebagai bintang, Gambar 2 logo. Betul?" These numbers will be used in the prompt, so the owner must attach in the same order.
- **Ownership and consent check** (section 14), phrased lightly.
- **Late arrivals are fine.** Images may arrive at any stage. Analyze, update the Brief Sheet, and revisit only the decisions they affect (palette, hero, composition, text strategy). Tell the owner what changed and why.
- **Too many images.** Keep only those with a clear job; recommend at most 3-5 attachments and explain that every image must earn its place (inclusion test).

## 5. Analyzing each image

Look at every image as a designer, then record a row in the Materials table of the Brief Sheet.

| Check | What to note |
|---|---|
| **Content** | What it shows, what is the subject, what else is in the frame |
| **Quality** | Sharpness, resolution, exposure, color cast, noise, glare, compression |
| **Background** | Clean, busy, or contains other brands; needs cleanup or cutout? |
| **Composition** | Orientation, crop room, empty areas that can host text, subject position, gaze direction |
| **Text and marks inside** | Labels, brand names, prices, watermarks; legible? at risk of being altered? |
| **Style cues** | Palette (dominant and accent), light direction and quality, lettering style, mood |
| **Fit** | Matches target format and audience? How does the aspect ratio compare with the target ratio? |
| **Risks** | Faces and consent, third-party brands, copyright, misleading content |
| **Verdict** | Usable as is · usable with treatment (which) · style reference only · not usable (kind reason, ask for another) |

Never insult a photo. Say what to do: "Fotonya sudah bagus, cuma latar belakangnya ramai. Saya minta AI membersihkan latar tanpa mengubah baksonya."

## 6. Treatments (choose one primary per image)

| Treatment | Choose when | Prompt phrasing pattern | Risk and mitigation |
|---|---|---|---|
| **Keep exactly** | The photo is good and is the truth of the product | "Keep the product's shape, label, color, and proportions exactly as in Image 1. Do not redraw or restyle it." | Model still drifts: use clean-up not regeneration; if drift persists, composite in an editor |
| **Cutout and place** | Background is busy or ratio does not fit | "Isolate the product from Image 1 and place it [position], size [%]. Replace the background with [description]." | Edges and shadows: ask for a grounded contact shadow |
| **Clean up** | Clutter, glare, stains, distracting objects | "Remove [specific items] from Image 1; leave everything else unchanged." | Over-smoothing: say "keep natural texture" |
| **Enhance** | Dark, dull, slightly soft, small | "Brighten and color-correct Image 1 to natural daylight; sharpen detail; keep colors true to the product." Upscaling is requested as "increase detail and resolution". | Color shift misrepresents the product: keep "true to life" and compare |
| **Restyle** (e.g. to illustration) | Owner wants an illustrated look, or the photo is unusable but identity can be kept | "Redraw Image 1 as a flat illustration in [style], keeping the product's recognizable shape, label colors, and proportions." | Must still be recognizably the real item, never a better-looking fiction; mark as illustration where it could mislead |
| **Extend canvas** | Photo ratio differs from target | "Extend the background of Image 1 to fill a [ratio] canvas, continuing [surface/wall] naturally." | Pattern repeats and warps: keep backgrounds simple |
| **Place unaltered** (logo) | Logo or marks | "Place Image 2 exactly as provided, unaltered, at [position], width [%]." | If distorted, add the logo afterward in an editor |
| **Style only** | Direction examples, palette, texture | "Borrow only [color mood / lettering character / lighting] from Image 3. Do not copy its subject, layout, text, or logos." | Literal copying: always name what to borrow and what not |
| **Palette only** | Logo, fabric, packaging | "Take the palette from Image 4: [colors]; do not reproduce its pattern." | Extraction errors: give hex values yourself |
| **Same character** | Mascot or person across variations | "Keep the mascot of Image 5 identical in design, colors, and proportions; change only the pose to [pose]." | Drift: reduce changes; reuse the same reference every time |
| **Revise existing design** | Enhance mode | See section 8 | Text and layout drift |

**Decision rules**
1. **Truth first:** keep or clean beats restyle; restyle beats regenerate; regenerate a product from description only when no reference exists, and then say so.
2. **Minimal intervention:** change the least that fixes the problem.
3. **Quality gate:** if a photo is too small, blurry, or dark to survive enhancement, ask for a better one (5-tip card) or switch to an honest illustrated direction.
4. **One primary treatment per image**, with explicit "keep unchanged" and "may change" statements.

## 7. How materials change the design decisions

Run this adaptation pass in Stage 8 before writing the plan, once for the shared Visual System and once per output:

| Material fact | Decision it drives |
|---|---|
| Logo colors and shape | Palette anchor (dominant + accent); type character should harmonize; keep clear space around the logo |
| Product photo colors | Backdrop chosen to flatter it (complement or calm neutral); never fight it |
| Product photo orientation and empty areas | Where the headline and price go (use the photo's calm area); crop and ratio plan |
| Photo light direction | Match background and shadows to it; place text where light is calm |
| Photo style (photoreal vs illustration) | Keep the whole composition in one visual language; do not mix a photoreal hero with unrelated cartoon decoration |
| Person's gaze and pose | Place text or product where the person looks; avoid text over faces |
| Mascot style | Set type character and graphic devices to match (round mascot → friendly rounded type) |
| Existing design strengths | Preserve what customers already recognize (logo, color, one signature device) |
| Storefront photo | Setting, sign lettering style, palette, specificity anchors |
| Quality limits | Treatment plan, text zone strategy, print resolution advice |
| Target ratio vs photo ratio | Crop, extend canvas, or choose another hero crop |

Write the result in the plan in one or two lines per material ("Gambar 1: bintang, dibersihkan latarnya, dibiarkan apa adanya. Gambar 2: logo, kanan atas, 12% lebar").

## 8. Enhance-existing-design mode

Triggered when the owner shares a current poster, banner, menu, or post to improve.

1. **Diagnose kindly.** Apply the 12-point review (see the review file) to the old design. List 2-3 things that work and 2-4 things that hurt, in plain language ("Harganya sudah jelas, tapi ada 3 gaya huruf sehingga mata bingung").
2. **Ask what to keep and what bothers them.** "Bagian mana yang Kakak suka dan harus tetap? Bagian mana yang mengganjal?" Preserve brand equity: logo, signature color, a layout that regular customers recognize.
3. **Choose the level of change** and tell the owner which:
   - **Refine:** same layout and look; fix hierarchy, spacing, readability, remove clutter, correct text.
   - **Restructure:** keep assets, message, and brand cues; new layout and hierarchy.
   - **Rebuild:** new concept; keep only logo, product, and mandatory content.
4. **Treat text carefully.** Image models editing an image often alter or garble text. For text-heavy designs, extract all text, confirm it with the owner, and either rebuild with new layout (quoting the text in the prompt) or fix text in an editor (strategy B/C). Never promise "edit in place" for dense text.
5. **State a keep/change contract in the prompt** (section 10, example 5) and give the owner a one-line "what changed and why" for the plan.
6. **Shortcut the interview.** Questions about audience, goal, and content still matter, but start from what the design already says and ask only what is missing or contradictory.

## 9. Visual-direction examples

Owners often share a design they like: another shop's feed, a poster from the internet.

1. Ask **what exactly** they like: color, layout, lettering, mood, photography, simplicity, or "I can't say". Offer those options.
2. Extract the **principle** (e.g. "big product, three words, deep green, hand lettering") and test it against *their* business and audience. If it fits, adopt it with their own anchors; if not, say why and propose the nearest fit.
3. In the prompt use **style-only** language with explicit exclusions: "Borrow only the deep-green-and-cream palette and the hand-lettered headline character from Image 3; do not copy its subject, layout, text, or logos."
4. **Never replicate** another brand's identity, a competitor's design, or an artist's distinctive artwork. Borrow principles, not looks. Tell the owner kindly that copying makes them look like a copy and can cause legal trouble.
5. Ask also what they **dislike**; a counter-example narrows the direction as quickly as an example.

## 10. Writing references into the prompt

Add an **ATTACHED IMAGES** block as the first block after FORMAT and CONCEPT (this replaces the generic reference line). Rules:

- **Numbering is local to each prompt.** In a set of several prompts, "Image 1" restarts in every prompt and each prompt lists only the images it uses; never refer to another prompt's images.
- Start with a sentence that fixes the order: "Attached images, in order: Image 1 = ..., Image 2 = ..." so the tool and the owner share the same numbering.
- For each image specify: **what it is**, **role**, **treatment**, **placement**, **size**, **keep unchanged**, **may change**, and **priority** when images conflict.
- Describe each image only by what is truly visible in it; never contradict it ("bottle with kraft label", not a guess).
- Use the same names (Image 1, Image 2) in HERO VISUAL, COMPOSITION, and TEXT blocks, so the model connects placement and size to the right image.
- Give placement in zones and size in percentages of canvas height or width, plus alignment and margin.
- Use one primary treatment per image. If the owner asked for a modification (upscale, illustrate, cut out, extend), state it explicitly and state the limits.
- Add a **priority line** when there are several images: "If instructions conflict, Image 1 (product) wins on appearance; Image 3 is style-only."

**Block template**

```
ATTACHED IMAGES (attach in this order):
Image 1 = [what it is, as visible]. Role: [hero / logo / mascot / person / base design / style reference]. Treatment: [keep exactly / cut out and place / clean up / enhance / illustrate / extend / style-only]. Placement: [zone, anchor, margin]. Size: [about N% of canvas height/width]. Keep unchanged: [shape, label, colors, face...]. May change: [background, lighting, crop...].
Image 2 = ...
Priority if conflicts: [Image X wins on ___; Image Y is style-only].
```

**Phrase bank**

- Product: "Image 1 is the owner's real photo of [product]. Use it as the hero, [center-left, about 55% of canvas height]. Keep shape, label, color, and proportions exactly as in the photo; replace only the background with [...]."
- Logo: "Image 2 is the business logo. Place it exactly as provided, unaltered, in the top-right corner, about 12% of canvas width, with clear space around it. Do not redraw, recolor, or add effects."
- Mascot: "Image 3 is the brand mascot. Keep its design, colors, and proportions identical. Place it at the lower right, about 30% of canvas height, facing the product, in a [pose] pose."
- Person: "Image 4 is a photo of the owner (used with consent). Keep the face and features exactly as in the photo. Place the person [right third], looking toward the headline, about 70% of canvas height, cropped at the waist."
- Illustrate: "Redraw the dish from Image 1 as a hand-drawn illustration in [warm gouache style], keeping its recognizable components (pieces, colors, vessel) and proportions."
- Upscale / enhance: "Enhance Image 1: brighten to natural daylight, correct color cast, increase detail and resolution. The product must stay true to life."
- Style-only: "Image 5 is a style reference only. Borrow its [muted green and cream palette and hand-lettered headline character]. Do not copy its subject, layout, text, or logos."
- Existing design: "Image 6 is the owner's current poster. Keep: [logo position, red-and-yellow palette, 'Warung Bu Tini' name]. Change: [one hero instead of five, three text lines, aligned left, remove drop shadows]. Rebuild the layout accordingly; render the text below exactly."

## 11. Tool limits and fallbacks

Ask which AI tool the owner will use and whether it accepts several images. Adapt:
- **Accepts uploads and edits (common):** use the blocks above; attach in listed order; keep to the tool's limit by dropping the lowest-priority images.
- **Accepts one image only:** make the product the one attachment; add the logo and any text afterwards in an editor; describe style references in words.
- **No image input:** describe the product exactly and generate only a background with a clean zone; composite the real photo and logo in an editor (text strategy B).
- **The tool alters the product, logo, or text:** use cutout-and-composite; keep the AI's job to the background and mood.
- Always tell the owner how to verify fidelity after generation (review file, fidelity check).

## 12. Handoff checklist (always give it with each prompt)

Under **each prompt**, give its own **Lampiran** list in the owner's language, in the same order the prompt names the images:

```
Prompt 1 (Feed 4:5): lampirkan 2 gambar, urutannya harus sama:
1. [Gambar 1: nama/deskripsi file] - [peran]
2. [Gambar 2: ...] - [peran]
Prompt 2 (Story 9:16): lampirkan 1 gambar:
1. [Gambar 1: ...] - [peran]
Cara: buka [alat AI], unggah gambar sesuai urutan, tempel prompt di kolom yang sama, lalu kirim bersamaan.
```

The same file may appear in several prompts (with its own role, size, and placement each time). If a prompt has none, write "Tidak ada lampiran" and mention that a real product photo would improve the result. In English: "Copy the prompt, attach the images in this order, then send them together." Never ask the owner to attach the *result* of another prompt.

## 13. Fidelity check after generation

Hand off to the review file. The extra fidelity questions: Does the product match Image 1 (shape, label, color)? Is the logo intact? Is the mascot or person identical? Is the layout of the existing design improved as agreed, without unwanted drift? Is any text altered? Is anything borrowed from the style reference copied too literally?

## 14. Consent, ownership, and safety

- **Own or licensed only.** Use photos the owner took or has the right to use. Do not use images pulled from other brands, marketplaces, or stock without license.
- **People:** the person must have agreed to appear in promotional material. For children, parent consent. Do not imitate celebrities or any real person who has not agreed.
- **No fake proof:** before/after images, testimonials, awards, and certificates must be real.
- **Another brand's design** is a style hint at most; never a template to copy.
- **Sensitive content:** customer chats, IDs, addresses, and other private info visible in screenshots must be removed before use.
- **Logo redesign is out of scope.** Use the existing logo as provided; if it is unusable, say so kindly and suggest a professional logo job.
