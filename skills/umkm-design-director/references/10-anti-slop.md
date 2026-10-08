# Anti-Slop: Root Causes, Specificity, and Intentional Design

Contents: what slop actually is · the eleven root causes · the visual tells (with their real causes) · fixes: from tell to decision · the positive-specification principle · realistic product imagery for physical print · missing brand assets · the 14-point slop audit · human traces that work in print

---

## 1. What slop actually is

"AI slop" in design is output that was generated with insufficient direction, and therefore filled with model defaults — the statistical average of what the model has seen most often in designs that fit the vague category it was given.

Slop is not caused by laziness. It is caused by unspecified decisions. Every design decision you did not make was made for you by the model's training data: a sea of generic commercial graphics that trend toward glowing gradients, plastic surfaces, everything centered, every corner filled, symmetrical compositions, generic copy, and visually similar "professional" appearances that belong to no one in particular.

The cure is not "make it look less like AI." That is a negative instruction that primes the model toward the next statistical default.

The cure is: **make every decision on purpose, from the real facts, real differences, and real materials of this specific business.**

Three habits prevent most slop:
1. **Understand what makes this business different** and design from that, not from the category.
2. **Subtract.** Space, silence, and fewer elements keep attention on what matters.
3. **Use the owner's real material** — real photos, real product, real place — instead of inventing it.

---

## 2. The eleven root causes

Understanding the cause is the only way to fix it. Vague instructions ("avoid AI slop") treat the symptom. Identifying the root cause and specifying the alternative eliminates the slop.

1. **Unspecified decisions** → the model chooses defaults for every unspecified parameter
2. **Adjective stacking** ("modern luxury vibrant elegant premium") → contradictory, averaged, generic results
3. **No concept** → no idea to organize the image around, so decoration substitutes for meaning
4. **No constraints on hierarchy, space, palette** → everything equally loud, nothing dominant
5. **Generic content** → generic copy and generic imagery produce generic results regardless of style
6. **Space left to the model** → it fills every empty area with decoration, props, and extra text
7. **Text left to chance** → garbled, invented, or misspelled words
8. **Accepting the first output** without audit or iteration
9. **Negative-only phrasing** ("don't look like AI") → primes the thing you want to avoid; replaces one default with the next
10. **No visual direction established** → model defaults to the statistical average of all styles it has seen
11. **Missing brand assets treated as blanks** → model invents generic placeholders (fake logos, stock faces, generic symbols)

---

## 3. The visual tells — with their root causes

Knowing *why* a tell exists is more useful than just recognizing it.

### Visual and rendering

| Tell | Root cause | Fix |
|---|---|---|
| Neon purple/blue/teal gradients | Default "modern" aesthetic when no color system specified | Commit to a palette with named roles and hex values derived from the product and brand |
| Glowing edges, lens flares, bokeh orbs, sparkles | "Premium" default when no concept or mood specified | Specify flat or naturally lit surfaces; name the specific failure modes to avoid |
| Plastic-glossy surfaces on food and objects | Studio-advertising default when no surface described | Name the surface material, light source, direction, and quality; ask for visible texture and slight imperfection |
| Generic smiling stock people | "Friendly" default when no person description or real photo provided | Use real owner/staff photos; or describe a specific person with age, clothing, setting, and genuine expression; or remove people |
| Western-looking faces for Indonesian audience | Model default when no demographic specified | Ask for "Indonesian appearance," or use real photos |
| Warped hands, merged fingers, impossible physics | Generative model weakness on hands and physical detail | Avoid close-up hands unless necessary; when needed, describe the action and position specifically |

### Composition

| Tell | Root cause | Fix |
|---|---|---|
| Cramped, every corner filled | No space allocation — model fills voids | Allocate specific percentage of calm space in the prompt with a flat-color instruction |
| Everything centered and symmetrical | Composition default when no spatial structure specified | Specify asymmetric zones: "product occupies left 55%, headline right-aligned in upper third" |
| Equal sizing — no clear hierarchy | No size ranks specified | Rank every element by size: "headline at 30% canvas height, price at 15%, name at 8%" |
| Text floating in rounded translucent boxes | Default "text-on-image" solution when no text zone planned | Plan a calm flat zone for text; specify text on a solid panel with high contrast |
| Decorative filler (scattered beans, flowers, icons) | Empty space treated as needing content | Specify "no decorative elements" and remove them in the subtraction pass |
| Cream/beige + sage/terracotta auto-aesthetic | Current "tasteful" default palette | Derive palette from actual brand and product; specify with hex values |

### Typography

| Tell | Root cause | Fix |
|---|---|---|
| Garbled, doubled, or invented words | Too much text, too small, or unreliable tool | Fewer, larger, quoted text lines; critical details added in editor (text strategy B) |
| Three or more font styles | Default when no type system specified | Two type characters maximum, each with a defined role |
| Low-contrast text over busy imagery | Background not planned as a text surface | Specify a flat panel or calm zone for all text in the composition |
| Chrome, gradient, or glow effects on text | "Premium" text treatment default | Specify plain high-contrast text; name the failure to exclude |

### Copy

| Tell | Root cause | Fix |
|---|---|---|
| "Nikmati kelezatan terbaik" | Default advertising copy when no specific message provided | Quote the exact text; derive copy from the actual USP and proof ("Kuah sapi, dimasak 8 jam") |
| Every line a superlative | No specific message hierarchy provided | One primary message; everything else tertiary or removed |
| Wrong information or invented details | Model fills unspecified content | Quote every text element exactly; instruct "render exactly as written, no additional words" |

---

## 4. Fixes: from tell to decision

| Tell | Decision that replaces it |
|---|---|
| Neon gradient | Deep flat background color derived from product palette; named with hex |
| Plastic gloss on food | "Natural window light from [direction], matte surface, visible texture, slight imperfection" |
| Floating ingredients | "Product grounded on a real named surface; contact shadow beneath; nothing floats" |
| Centered, everything equal | Asymmetric zone map with named positions and size percentages for each element |
| Rounded glass text boxes | Plain text in calm flat area, or text on solid panel with strong contrast |
| Decorative filler | Deleted in the subtraction pass; replaced with one specific product-related prop if needed |
| No breathing room | "About 40% of canvas calm and empty (flat [color], no texture), mainly [where]; nothing floats" |
| Generic stock people | Real photo with consent, or specific age/clothing/setting/expression description, or no people |
| Generic food gloss | Real photo of real dish; if no photo, physically described with surface, light direction, texture, realistic proportions |
| Many fonts | Two type characters with explicitly defined roles |
| Garbled text | Short, quoted lines; critical details added later in editor |
| Generic copy | Concrete copy from USP and proof: specific number, ingredient, time, place, or process |
| Invented logo / marks | Reserved placeholder; owner adds real logo and official marks after generation |
| Wrong cultural details | Named, specific, region-correct details from the owner's own context |
| No visual direction | Concept sentence from Stage 7; applied as the logic of every design decision |

---

## 5. The positive-specification principle

Do not fight defaults with prohibitions alone. For every default you want to avoid, **name the alternative you want instead:**

- Instead of "no gradient": "flat deep-brown background (#2B1A0E) with subtle matte paper grain texture"
- Instead of "not cluttered": "large empty area (about 45% of canvas) around the product; maximum five text elements"
- Instead of "not generic": name the concrete anchors (the real bottle, the specific sign-painter lettering, the worn wooden counter)
- Instead of "realistic food": describe the light source, direction, surface material, camera angle, and specific imperfection

Then add a **short, specific exclusion list** (maximum 5–6 items) for the failure modes most likely for this specific brief:
"Avoid: floating ingredients, glow effects on food, extra text, decorative sparkles, stock-style smiling people, gradient backgrounds."

Also exclude "quality" buzzwords that push models toward the generic polished look: "ultra-detailed," "8k," "masterpiece," "stunning," "award-winning," "hyper-realistic," "trending on..."

---

## 6. Realistic product imagery for physical print

When no reference photo exists, the prompt must work harder to prevent the model from defaulting to glossy CGI aesthetics. For food businesses especially, generic-looking images erode trust with local buyers faster than almost anything.

**Light:**
Name the source, direction, and quality. "Morning light from a north-facing window, diffused through white curtain, soft shadows falling to the right." Never: "beautiful lighting," "professional lighting," "well-lit," "studio quality."

**Surface:**
Name the actual material. "Worn dark-teak counter with visible grain and faint water stain." "Pale cement tabletop with matte finish and fine aggregate." "Terracotta floor tile with visible grout lines." Never: "beautiful background," "elegant surface."

**Camera angle and distance:**
Specify both. "Looking slightly downward at about 20°, close enough that the bowl fills 55% of the frame." Never: "appetizing angle," "flattering view."

**Food and product texture:**
Physical specificity. "Meatball with visible sear marks, glossy bone-broth surface with thin orange oil film and faint steam wisp, sliced green onion lying flat in the liquid." Never: "perfectly plated," "gorgeous garnish."

**Proportions:**
Physically plausible. "A standard 18 cm bowl, meatball approximately 4 cm diameter." Never "enormous," "overflowing," "generously portioned."

**Imperfection as credibility signal:**
Include one or two specific small imperfections: a condensation drop on a bottle, a slightly uneven sprinkle of topping, a chipped edge on a plate, a sauce smear on the bowl rim. These signal real, not rendered.

**Explicit exclusions for product imagery:**
"Avoid: excessive gloss on food surfaces, ingredients floating or erupting from the dish, exaggerated portion size, studio-style background or lighting, plastic-looking surfaces, fake depth-of-field blur that erases context."

---

## 7. Missing brand assets: build an identity, not a label

When the owner has no logo, no brand colors, and no visual identity:

**Do not:** place the business name in a generic font at the top of the design and call it done. That looks like a template with a name typed in — which is what it is.

**Do:** develop a visual identity treatment that is specific to this business and this design direction. Read `references/07-business-archetypes.md` for the default identity treatment by archetype.

Three components:
- **Named type character:** a specific description of weight, feel, and case (e.g., "heavy condensed slab-serif capitals with slight stamp-ink texture"). This becomes the business name treatment.
- **Graphic device:** a full-width panel, a stamp shape, a rule, a motif from the product or place. Described precisely in the prompt.
- **Color mark:** the specific combination and placement that signals the brand before any text is read.

The result should look like a deliberate brand decision — not a placeholder. State it in the plan: *"Belum ada logo. Saya rancang tampilan nama dengan [treatment] supaya terasa seperti merek, bukan template."*

---

## 8. The 14-point slop audit

Apply to the design plan, the prompt, and the generated image:

1. **One clear hero.** Is there a single dominant element at every viewing distance?
2. **Squint test.** Blur your eyes: one dominant shape, one headline block, one end point?
3. **A concept, not just a style.** Is there an organizing idea, not just a collection of attributes?
4. **Two ownable anchors.** Are there at least two visual elements specific to this business?
5. **Every element earns its place.** Does each element pass the inclusion test?
6. **Colors committed with roles.** Are all colors specified with hex values and roles?
7. **Two type characters maximum.** Both readable at the intended viewing distance?
8. **Text correct, short, and concrete.** No generic copy. No garbled or invented words.
9. **Product looks like the real product.** Honest imagery, not aspirational fabrication.
10. **People, food, and motifs culturally correct.** Right for the specific audience.
11. **Space allocated.** Calm area present; margins clear; inter-group gaps larger than intra-group gaps.
12. **Swap test passed.** Would this design look wrong for a different business?
13. **USP and character expressed.** Does the design communicate what makes this business different?
14. **Visual direction explicit.** Does the design have a named concept and direction from Stage 7 — not from model defaults?

Fewer than 12 passes → revise before delivering.

---

## 9. Human traces that work in physical print

Use only if they fit the brand and concept:

- **Real product photos from the owner's phone**, lightly cleaned and composited as the hero — the strongest anti-slop asset
- **Hand-painted or sign-lettering style** from the owner's neighborhood and category tradition
- **Tactile local materials:** kraft paper, banana leaf, terracotta tile, enamel plates, woven rattan, stamped texture, worn wood
- **Slight asymmetry and deliberate imperfection** — reads as human, not templated
- **A voice:** copy that sounds like the owner talking to a regular customer; concrete and specific
- **A recurring graphic device** that becomes the business's visual signature across printed pieces
- **Restraint:** fewer elements, larger scale, calmer field — the opposite of trying to fill space
