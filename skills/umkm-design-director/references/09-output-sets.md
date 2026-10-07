# Output Sets: Several Graphics, One System (Stages 4, 8, 9)

Contents: why ask about outputs · deciding the set · Output Spec · the shared Visual System · what varies per output · standalone-prompt rule · attachments per prompt · splitting the message · delivery format · limits

Owners rarely need one graphic. A promo usually lives as a feed post, a story, and a broadcast; an opening needs a post and a banner. Ask what they need, design them as **one family**, and give **one standalone prompt per output**.

## 1. Deciding the set (Stage 4)

Ask after the goal and message are known: "Untuk menyampaikan ini, Kakak butuh gambar apa saja? Satu saja, atau beberapa (misal feed + story)?" If they do not know, propose a set with the reason and let them trim:

| Goal | Suggested set | Why |
|---|---|---|
| Promo / discount | Feed post 4:5 + Story/Status 9:16 | Feed carries the offer for browsing; story pushes the deadline and action |
| New product launch | Feed post + Story + marketplace/product banner (if sold there) | Awareness + action where the purchase happens |
| Grand opening | Feed post + Story + spanduk background | Online hook + physical presence |
| Menu or price list | Menu board/print + feed highlight of best-sellers | Full list in print, one hero item online |
| Brand awareness / new look | Feed post + profile or cover image | Recognition across places |
| Regular posting (weekly) | A series of N posts with the same system, different content | Consistency builds recognition |

Rules: one output per **placement and ratio** (never stretch one image across ratios). Recommend **at most 4 outputs per session**; more can be done in a second batch using the same Visual System. Remove outputs without a clear job (inclusion test).

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

Format and ratio · composition (recomposed for the ratio and its safe zones, never stretched) · hierarchy emphasis for the job (feed: offer + hero; story: deadline + action) · text length and content · crop of the hero image · which images are attached.

Consistency check: put any two outputs side by side. Same colors, same type, same material, same graphic device, same space feeling: yes. Same layout: not required.

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
