# Anti-Slop: Why AI Graphics Look Generic and How to Avoid It

Contents: what slop is · root causes · the tells (visual, composition, type, copy, content) · fixes · the positive-specification principle · the 13-point slop audit · human traces that work

## 1. What slop is

"AI slop" in design is low-effort, generic visual output published with little direction or editing. It is recognizable because image models, when you specify little, fall back to the most statistically common solution for the request: the average of everything they have seen. The result looks "finished" but belongs to nobody, says nothing specific, and breaks trust the moment viewers sense it was not made with care.

Owners are mocked for slop, but the cause is rarely laziness: they gave the model a vague request ("buatkan poster promo ayam geprek") and the model filled the gaps with defaults. This skill's job is to fill those gaps with *their* facts and *good decisions*.

## 2. Root causes

1. **Unspecified decisions** → the model chooses defaults.
2. **Adjective stacking** ("modern luxury vibrant elegant premium") → contradictory, averaged results.
3. **No concept** → no idea to organize the image around, so decoration substitutes for meaning.
4. **No constraints** (hierarchy, text, space, palette) → everything equally loud.
5. **Generic content** (generic copy, generic imagery) → generic result regardless of style.
6. **Space left to the model** (it fills every empty area with decoration and extra text).
7. **Text left to chance** → garbled or invented words.
8. **Accepting the first output** without audit or iteration.
9. **Negative phrasing** ("don't look like AI") primes the thing you want to avoid and replaces one default with the next. Describe what you *want* instead.

## 3. The tells

### Visual and rendering
- Neon purple/blue/teal gradients; glowing edges; lens flares; bokeh orbs; sparkles.
- Teal-and-orange "cinematic" grading on everything.
- Glossy, plasticky, over-smooth surfaces; "3D render" look on foods and objects.
- Skin with no pores, perfect symmetric faces, generic smiling stock people; Western-looking faces for an Indonesian audience.
- Warped hands, merged fingers, odd cutlery, impossible physics (floating food, ingredients exploding mid-air).
- Everything lit like a studio ad; no natural light, no imperfection.

### Composition
- **Cramped and over-filled:** every corner occupied, no calm area, the hero crowded by props, badges, and effects (horror vacui).
- Everything centered and symmetrical by default.
- Every element about the same size; no clear hero.
- Text floating in rounded translucent boxes; stacked badges and ribbons.
- Border frames, drop shadows, glows on every element.
- Decorative filler (random leaves, stars, confetti, coffee beans scattered) unrelated to the product.
- Cream/beige + sage/terracotta used as automatic "tasteful".

### Type
- Garbled, doubled, or invented words; misspelled prices.
- Three or more type styles; script used for important information.
- Text too small for the medium; low-contrast text over busy imagery.
- Gradient or chrome-effect lettering.

### Copy
- Generic filler: "Nikmati kelezatan terbaik", "Kualitas terbaik, harga terjangkau", "Solusi terbaik untuk Anda".
- Every line is a superlative; nothing concrete (no number, place, ingredient, time, proof).
- Too many sentences for the medium.

### Content and truth
- A product image that does not match the real product.
- Invented logos, certificates, awards, or testimonials.
- Wrong cultural details (wrong food presentation, wrong motif, wrong clothing).

## 4. Fixes: from tell to decision

| Tell | Decision that replaces it |
|---|---|
| Neon gradient / glow | A committed palette with roles drawn from product + brand; flat or softly lit natural background |
| Plastic gloss | Natural light, visible texture, slight imperfection; "photographed on a real counter with window light" |
| Floating ingredients | Product grounded on a real surface; nothing floats |
| Centered, equal | Asymmetric composition with one dominant element and a stated reading path |
| Rounded glass boxes | Plain text on a calm area, or one solid panel with strong contrast |
| Decorative filler | Delete; if needed use one specific product-related prop |
| Cramped, no breathing room | Allocate space in the prompt ("about 40% calm and empty, flat color, mainly right"); cut elements with the subtraction pass |
| Stock people | Real photo of owner/staff/customer with consent, or a specific person description (age, clothing, setting, genuine expression), or no people |
| Generic gloss on food | The owner's actual dish photo kept as reference; the rest built around it |
| Many fonts | Two type characters with defined roles |
| Garbled text | Few, short, quoted text lines; critical details added later in Canva |
| Generic copy | Concrete copy (number, time, ingredient, place, proof) in the owner's voice |
| Invented logo/marks | Reserved placeholder; real logo and official marks added after |
| Wrong cultural detail | Specific, region-correct details named in the prompt |

## 5. The positive-specification principle

Do not fight defaults with prohibitions alone. For every default you want to avoid, **name the alternative**:
- Instead of "no gradient": "flat deep-brown background with subtle paper grain".
- Instead of "not cluttered": "large empty area around the product; only four text elements".
- Instead of "not generic": name the concrete anchors (the real bottle, the specific street-sign lettering).
- Instead of "realistic": describe the light, surface, camera angle, and imperfections.

Then add a **short, specific exclusion line** (max 5-6 items) for the failure modes that matter in this brief ("no floating ingredients, no glow effects, no extra text, no decorative sparkles, no stock-style smiling people").

Also avoid "quality" buzzwords that push models toward the generic polished look: "ultra-detailed", "8k", "masterpiece", "stunning", "award-winning", "hyper-realistic", "trending on...".

## 6. The 13-point slop audit

Use on the plan, the prompt, and the generated image:

1. Is there **one** clear hero and a visible reading order?
2. Does it pass the **squint test** and the **3-second test**?
3. Is there **a concept** (an idea) beyond a style?
4. Are there at least **two ownable anchors** from this business?
5. Is every element **earning its place** (inclusion test)?
6. Are colors **committed with roles**, not defaults?
7. Are there **two type characters** at most, readable at phone width?
8. Is the **text correct**, short, and concrete (not generic copy)?
9. Does the **product look like the real product** (honest imagery)?
10. Are **people, food, and motifs culturally correct** for the audience?
11. Is there **room to breathe** (calm space allocated, margins, gaps between groups) or deliberate density that is strictly grouped, with nothing decorative left after the subtraction pass?
12. Would this design **look wrong for a different business**? (The swap test: if it fits anyone, it fits no one.)
13. Does it express the business's **USP and perceived character**, not just its category?

Fewer than 11 passes → revise before delivering.

## 7. Human traces that work (use only if they fit the brand)

- Real photos from the owner's phone, lightly cleaned, as the hero.
- Hand-painted or sign-lettering style from the owner's own neighborhood.
- Tactile materials: kraft paper, banana leaf, enamel plate, woven rattan, stamped labels.
- Slight asymmetry and deliberate, readable imperfection.
- A voice: copy that sounds like the owner talking to a regular customer.
- A recurring graphic device that becomes the brand's signature.
- Restraint: fewer, bigger, calmer.
