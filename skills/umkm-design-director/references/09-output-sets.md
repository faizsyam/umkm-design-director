# Output Sets: Several Physical Materials, One Design System (Stages 4, 8, 10)

Contents: why ask about outputs · deciding the set · Output Spec · the shared Visual System · what varies per output · standalone-prompt rule · attachments per prompt · splitting the message · delivery format · limits

Physical print materials for a single business are often needed as a set: a storefront spanduk, a flyer, a price board, and a menu. Design them as **one visual family** — one shared Visual System applied to each physical format with its own appropriate composition, text budget, and viewing context.

## 1. Deciding the set (Stage 4)

Ask after the objective and message are known: "Materi cetak apa saja yang Kakak butuhkan? Satu saja, atau beberapa?" If they do not know, propose a set with the reason and let them trim:

| Goal | Suggested physical set | Why |
|---|---|---|
| Promo / discount | Spanduk depan toko + flyer yang dibagikan | Spanduk attracts passing traffic; flyer delivers the detail for interested buyers |
| New product launch | Spanduk + poster + price board | Awareness from street + information inside + price visible |
| Grand opening | Spanduk besar + poster + flyer | Street hook + event information + hand-held detail |
| Menu / price list | Menu board + price board of best-sellers | Full list in place + highlight for quick decisions |
| Brand awareness | Spanduk + X-banner + label/stiker | Consistent presence at multiple touchpoints |
| Packaging and selling | Label kemasan + stiker promo + flyer | Product identity + promotion + information |

Rules: one output per **physical format and placement** (never stretch one design across different formats). Recommend **at most 4 outputs per session**; more in a second batch using the same Visual System.


## 2. Output Spec (one row per output)

Record in the Brief Sheet:

| Field | Meaning |
|---|---|
| **ID and name** | Prompt 1: Feed Instagram |
| **Job** | hook / inform / act / reinforce |
| **Placement and ratio** | e.g. Instagram feed, 4:5 |
| **Message variant** | The same core message, angled for this placement |
| **Text elements** | Exact text for this output (may differ in length) |
| **Hero and images to attach** | Which user images this prompt uses and how |
| **Text strategy** | A, B, or C for this output |

## 3. The shared Visual System

Decide **once** (Stage 8), then write it identically into every prompt. Keep it to the items that make a family recognizable:

- **Palette with roles** (dominant, support, accent, hex values) and where the accent is used
- **Type character** for headline and support, case, weight
- **Style and material** (photo or illustration, texture, finish, light)
- **Graphic device** (one recurring element: a stripe, label shape, stamp, border, lettering style), or none
- **Space level** (how calm, how many elements, margin) and the **alignment spine** logic
- **Photo or image treatment** (how real images are cleaned, cropped, grounded)
- **Voice** of the copy (register, sentence length): used when writing the text in Stage 6, not repeated in the image prompts

## 4. What varies per output

**Fixed across all outputs (Visual System — must be identical):**
- Palette hex values and assigned roles
- Type character (headline weight/personality, support character)
- Graphic device (if any) and its color
- Image treatment (surface material, light quality, photo style)
- Brand/identity treatment (logo placement rules, or identity treatment spec)

**Adapts per output (driven by format + viewing context — must change):**
- Space level (roadside spanduk: 40-60% calm; flyer: 20-35%)
- Element count (spanduk: 3-5 elements; flyer: 6-15 elements)
- Composition structure (recomposed for each ratio — never stretched)
- Text budget and content length
- Hierarchy emphasis for the job (feed: offer + hero; story: deadline + action; spanduk: one message only)
- Crop and scale of the hero image

**The test:** place any two outputs side by side. Same colors, same type character, same material feel, same graphic device, same space personality — yes. Same layout or element count — not required, and not expected.

**Warning:** if space level, element count, and composition all change but the palette or type character also drift, the family breaks. The Visual System block in each prompt must be copied verbatim — not paraphrased — to prevent drift.

## 5. Standalone-prompt rule

Every prompt must work if pasted alone into a fresh chat. Therefore:

- **Repeat the full Visual System block verbatim** in each prompt (same words, same hex values).
- **Never** write "same as the previous image", "like prompt 1", "continue the series", "as before", or refer to another prompt's attachments or numbering.
- Image numbering is **local to each prompt** ("Image 1" in Prompt 2 may be a different file than "Image 1" in Prompt 1).
- Describe the campaign concept in each prompt's CONCEPT line (the shared idea in the same words, plus this output's angle).
- Each prompt carries its own FORMAT, COMPOSITION, TEXT, ATTACHED IMAGES, and exclusions.

Because of this, the owner can run the prompts in any order, in separate chats, or on different days.

## 6. Attachments per prompt

For each prompt, list exactly the images to attach, in the order the prompt names them. The same file may appear in several prompts with a different role or crop. Use the handoff format from `03-reference-images.md` section 12:

```
Prompt 2 (Story 9:16): lampirkan 2 gambar, urutannya harus sama:
1. Foto-bakso.jpg - bintang
2. Logo.png - pojok kiri atas
```

If a prompt needs no images, write "Prompt 3: tidak ada lampiran". Do not make a prompt depend on an **output** of another prompt (for example "attach the generated feed post"); the set must not require the first result to exist.

## 7. Splitting the message across outputs

- Same core message, same offer, same price format everywhere. Do not contradict (dates, prices).
- Give each output a **single job** and tune density: story = fewer words and the action; feed = hero and offer; banner = promise only; menu = grouped information.
- Do not repeat every detail in every output: caption, story sticker links, or the shop sign can carry the rest.
- Keep exact text identical across outputs where it is the same fact (name, price, deadline).

## 8. Delivery format (Stage 9)

1. **Rencana desain bersama** (once): message, direction, Visual System in plain language, assumptions.
2. **Daftar output:** one line per output (name, ratio, job, attachments).
3. **Prompt 1, Prompt 2, ...** each in its own code block, headed by name and ratio, and each followed by its **Lampiran** list.
4. **Cara pakai** once: for each prompt, copy it and attach its images in the listed order, send; proofread text; check the set side by side.
5. Offer a review when results are ready (`12-review-and-iteration.md`, set check).

## 9. Limits

- More than 4 outputs: propose batches; the Visual System block is reused unchanged, so later batches match.
- Different languages per output: treat as separate outputs with their own text.
- Print and screen in one set: keep the Visual System; use text strategy B for print.
- If the owner's tool limits how many images a prompt can use, assign the highest-priority images to each prompt, not all images to all prompts.
