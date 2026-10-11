# Prompt Assembly (Stage 8)

Contents: the creative-direction-first rule · what a prompt must do · the prompt structure · block rules · text strategy · phrasing rules · semantic density · length · contradiction check · example A (poster with images) · example B (spanduk background, no images) · example C (table card, no reference images, identity treatment) · assembling a set

## 0. The creative-direction-first rule

**Never write a prompt directly from a concept or design strategy.**

Before the first word of a prompt is written, the Creative Direction Summary must exist (see `13-design-thinking.md` Section 9 / Stage 7). The summary is the complete crystallization of all design thinking — what is being made, who it is for, what must appear, what the design should feel and communicate, and what makes it specific to this business.

The prompt is a translation of that direction into a brief the image model can execute. If the creative direction is vague, the prompt will be vague. If the creative direction is strong and distinctive, the prompt will be strong and distinctive.

**The test:** before writing a prompt, ask: "Does a Creative Direction Summary exist for this design — a clear statement of what it must communicate, who it is for, what should appear, and what visual character it should have?" If not, produce it first.

**What strong creative direction catches that a direct prompt misses:**
- Generic style adjectives with no organizing concept
- Content listed without priority — no sense of what dominates
- Business-specific identity missing — could belong to any business in the category
- Physical context not reflected in the design character
- Audience's visual language not considered

---

## 1. What a prompt must do

A prompt is a **complete creative brief** for a model that cannot ask questions. It must give the model a clear, specific, and distinctive understanding of:

- **What** is being created and what it is meant to accomplish
- **Who** it belongs to and who it is communicating with
- **What** must visibly appear (content, product, text, brand identity)
- **What** the overall creative direction, visual character, and emotional tone should be
- **What** makes this design belong specifically to this business

The prompt must not:
- Prescribe pixel positions, exact canvas percentages, or coordinate-level layout instructions
- Enumerate every minor visual component
- Contain design rationale, reasoning, or process explanation
- Include post-processing instructions or "add text later" notes outside the text strategy declaration
- Leave intentional empty areas for the owner to fill in — unless text strategy B or C was explicitly chosen

**Every sentence must change what the model generates.** A sentence that explains the reasoning, describes the design process, or states a viewing context without translating it into a design character requirement does not belong in the prompt.

**Viewing context → design character:** Never paste viewing-context statements directly into the prompt. Instead, translate them into what kind of design they require:
- "Viewed from 10 m on a motorbike" → "A design that communicates one bold idea — readable at a glance from a distance, with maximum contrast and nothing competing for attention"
- "Must read in 3 seconds" → "Spare and immediate — one dominant message, one supporting element, generous space around the essential content"
- "Held in hand for 30 seconds" → "A design with layered information that rewards a closer read — clear hierarchy from the most important to the supporting details"

**Every prompt is fully standalone.** It works if pasted alone into a fresh chat: no "same as before", no reference to another prompt, no dependence on a generated result.

---

## 2. The prompt structure

The prompt is organized to give the model its most important orientation first — what is being made and why — then what must appear, then how it should feel and what makes it distinctive. This order ensures the model has the design's purpose and character before it starts solving the composition.

```
FORMAT: [physical medium, e.g. "Printed roadside banner, 3×1 m, vinyl tarpaulin"], [aspect ratio and px].

OBJECTIVE: [one sentence — what this specific output must accomplish for the viewer].

CONCEPT: "[campaign idea — same words in every prompt of a set]". [Two feelings]. For [audience].

CONTENT:
- [Primary message/headline — exact text]
- [Key supporting text — exact text]
- [Product or service]
- [Brand identity — logo or name treatment]
- [Any important visual elements or motifs]
[If text strategy B or C: "Text zone reserved: [description of the clean area]. Owner adds [what] there."]
[If official marks needed: "Reserved space for [mark type]."]

CREATIVE DIRECTION: [The visual concept, personality, mood, aesthetic world, emotional character, and overall feeling the design should project. Derived from the business — not generic style language. This is where the design's distinctive identity lives. 3-6 sentences.]

DESIGN CHARACTER: [What makes this design specifically belong to this business — the ownable visual idea, USP expressed visually, specificity anchors, and what would distinguish it from a competitor using the same format. 2-4 sentences.]

HERO VISUAL: [What the dominant visual element is. Physically specific — not "a dish" but the real thing with its real character. If a photo is attached, say to use it exactly. If generated, describe what it should look like: subject, lighting quality, surface, material feel, angle, what makes it honest and specific rather than generic.]

VISUAL SYSTEM (identical in every prompt of this set):
Type: [headline character — weight, personality, case]; [support character]. Style and material: [photo/illustration, texture, finish, light quality]. Image treatment: [how real photos are handled]. Device: [one recurring graphic element, or none]. Space level: [calm / moderate / dense-but-grouped].

[ATTACHED IMAGES — include ONLY if images are being attached. Omit this block entirely when there are none:]
ATTACHED IMAGES (attach in this order):
Image 1 = [what it is]. Role: [...]. Treatment: [...]. Keep unchanged: [...]. May change: [...].
Image 2 = ...

EXCLUSIONS: Keep [truth constraints]. Avoid [4-8 specific failure modes for this brief — concrete, not generic].
```

**Why this order:**
- FORMAT → the model knows the physical medium and aspect ratio first
- OBJECTIVE → purpose is established before any creative decision
- CONCEPT → the organizing idea before content and style
- CONTENT → what must appear in the image, in priority order
- CREATIVE DIRECTION → the visual world and character the design inhabits
- DESIGN CHARACTER → the business-specific identity that makes the design distinctive
- HERO VISUAL → the dominant element with physical specificity
- VISUAL SYSTEM → shared consistency block, identical across all prompts in a set
- ATTACHED IMAGES → asset declarations with use instructions
- EXCLUSIONS → specific prohibitions against the most likely failure modes

---

## 3. Block rules

**FORMAT.** State the physical medium and production context explicitly: "Printed roadside banner, 3×1 m, vinyl tarpaulin." State the aspect ratio for generation: "3:1 (3000×1000 px)."

**OBJECTIVE.** One sentence — what this specific output must accomplish. Not the campaign concept (that is CONCEPT), but the specific communication task: "Attract passing motorbike traffic and communicate the daily-use offer in under two seconds." "Convince a standing customer to order the hero product." "Introduce the business name and one differentiator to pedestrians."

**CONCEPT.** The campaign idea in the same words in every prompt of the set, plus the two feelings and the audience. It comes from the Distinction Brief (USP, desired perception). This is a design concept — an organizing idea — not an aesthetic direction.

**CONTENT.** List what must visibly appear in the image, in order of importance. Primary message first, then supporting content, then brand identity, then any important visual motifs. Quote exact text. Do not enumerate minor decorative details here — only content the design must communicate. If text strategy B or C applies, state what zone is reserved and what the owner will add there.

**CREATIVE DIRECTION.** This is the heart of the prompt. Describe the visual concept, personality, mood, emotional character, aesthetic world, and overall feeling. Be specific and business-derived — not generic. Express the design's visual logic: why this character fits this business and this audience. Include:
- The overall visual impression and emotional register
- The color world and what it communicates (not just hex values — what the colors *mean* in context)
- The typographic personality and what it signals
- The spatial feeling (spacious, energetic, restrained, warm, bold, quiet)
- What the design should feel like to the viewer encountering it in real physical space

Avoid: "eye-catching," "professional," "beautiful," "stunning," "modern and clean" alone. These words add nothing. Replace with specific sensory and emotional language derived from the business.

**DESIGN CHARACTER.** State what makes this design belong to this specific business. Name the ownable elements — the USP expressed visually, the specificity anchors, the visual idea that could only come from this business's real identity. This is the swap-test answer: why a competitor's name could not be dropped in without the design looking wrong.

**HERO VISUAL.** Name the real thing with physical specificity. Not "a delicious dish" but "a 20 cm earthenware bowl of mie ayam with golden broth, visible slices of chicken on top, chopped spring onion lying flat in the broth, on a worn rattan placemat, soft morning window light from the left, slight steam curl above the bowl." Push toward honest, credible imagery: real surfaces, natural light, believable proportions, visible texture, slight physical imperfection. If a photo is attached, say to use it exactly.

**VISUAL SYSTEM.** Compact shared identity block (~40-60 words). Contains: type characters (headline + support), style and material (photo/illustration, texture, finish, light quality), image treatment (how real photos are handled), graphic device (one element or none), space level. Identical word-for-word in every prompt of a set.

**ATTACHED IMAGES.** Include only when image files are literally being attached to the AI prompt. Omit entirely when there are none — no placeholder, no "no images" note. For each attached image: what it is, its role, its treatment, what to keep unchanged, what may change, and any conflict priority.

**EXCLUSIONS.** "Keep" = truth constraints (what must not be invented or altered). "Avoid" = specific failure modes for this brief — concrete, not generic. "Floating ingredients, glow effects, gradient backgrounds, decorative sparkles, extra invented text, stock-style smiling people, crowded corners" beats "avoid AI slop." Write 4-8 exclusions. More than 8 usually means the creative direction is not strong enough.

---

## 4. Text strategy

| Strategy | When | Prompt approach |
|---|---|---|
| **A: in-image text** | Tool renders text well; short headline, offer, price, CTA; **default for simple promos** | Quote each line in CONTENT; "render exactly as written, no additional words" |
| **B: clean text zones** | Print, spanduk, menus, long info, phone numbers, addresses, legal marks, text-heavy redesigns | State in CONTENT: "Text zone reserved: [description]. Owner adds [what] there." |
| **C: hybrid** | Posts with contact info the owner wants to add themselves | Headline and price in CONTENT; state the reserved strip |

Rules for A and C: quote text exactly, keep lines short and large, specify the language, say what not to add ("no taglines, no extra words, no watermarks"), and tell the owner to proofread after generation.

**Do not choose B or C to avoid the effort of specifying content.** If the content is short and the tool renders text reasonably, use A and produce the finished design.

---

## 5. Phrasing rules

1. **Meaning over mechanics.** Describe what the design should communicate and feel like — not where to place each pixel.
2. **Specific over generic.** "Deep coffee-brown warmth that signals honest neighborhood craft" beats "dark brown background."
3. **Business-derived over style-adjective.** Every direction should trace back to the real business, real audience, or real product.
4. **One idea per sentence.**
5. **No stacked contradictions** ("minimal yet rich", "luxurious but cheap-looking").
6. **No quality buzzwords** ("ultra-detailed", "8k", "masterpiece", "stunning", "hyper-realistic").
7. **Positive first, negatives last, and few.**
8. **Name the single most important content element early** (the hero and what it communicates).
9. **Instructions in English, on-image text in the owner's language and spelling.**
10. **Do not name model versions** or other products as style ("like Midjourney").
11. **No meta-commentary.** Do not explain why a decision was made or describe the design process.
12. **No viewing-context sentences.** "Viewed from the sidewalk at 3–8 m" tells the model nothing useful. Translate into design character: what kind of visual presence, what level of simplicity, what reading speed.

---

## 6. Semantic density

Every sentence in the prompt should carry useful meaning about:

**subject + business + audience + message + content + visual character + emotional direction + distinctive identity.**

Remove:
- Repetition of the same idea in different words
- Generic adjectives that could apply to any design ("eye-catching," "professional," "modern")
- Explanations of reasoning ("because the viewer is passing quickly, we need...")
- Redundant constraints (stating the same prohibition twice)
- Observations about what the design "should" do that are already implied by the creative direction

Every sentence should add something the model would not know from the rest of the prompt.

---

## 7. Realistic food and product imagery

When the prompt must generate food or product imagery without a reference photo, describe it to push toward honest, credible commercial photography:

- **Light:** name the source and direction ("soft morning light from a north-facing window, diffused through white curtain, shadows falling left"). Never "professional studio lighting" or "beautifully lit."
- **Surface:** real, named material ("worn dark-teak wood counter with visible grain and a water ring stain"). Never "beautiful background."
- **Angle:** specific camera angle ("looking slightly down at 25°, close enough that the bowl fills most of the frame"). Never "appetizing angle."
- **Texture:** visible and physically plausible ("glossy broth surface with a thin orange oil film, visible sear marks on the meatball, chopped green onion lying flat"). Never "perfectly plated."
- **Proportions:** realistic, not exaggerated ("a standard 18 cm bowl"). Never "enormous," "overflowing."
- **Imperfection is realism:** a condensation drop, a small chip, a slightly uneven sprinkle. These signal a real photo.
- **Avoid explicitly:** "excessive gloss, exaggerated portion size, ingredients floating mid-air or erupting from the dish, plastic-looking surfaces, extreme depth-of-field blur, generic stock-food aesthetics."

---

## 8. Length and tool notes

**Length:** Aim for 200–400 words per prompt. The CREATIVE DIRECTION and DESIGN CHARACTER blocks replace the former explicit zone-specification blocks — they are denser in meaning and shorter in word count. If you pass 450 words, check whether you are repeating yourself or over-specifying: cut.

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
- If the tool does not support image attachments → use Strategy B or C; describe the product entirely in HERO VISUAL.
- If the tool has poor text accuracy → use Strategy B for all print pieces.
- If unsure → default to Strategy B for large-format print and menus, Strategy A for short-text posters/flyers.

**One-change iteration:** let the owner change one major thing per round (`12-review-and-iteration.md`).

---

## 9. Contradiction check

- Creative Direction Summary completed before this prompt was written?
- Does the CREATIVE DIRECTION reflect the emotional brief from Stage 4 — the causal chain from desired perception to visual element?
- Any sentence asking for both "minimal" and "rich detail"?
- Does the CONTENT block list what actually needs to appear, or just what seemed comprehensive?
- Does the CREATIVE DIRECTION trace back to the actual business, or is it generic style language?
- Does the DESIGN CHARACTER pass the swap test — would the design look wrong for a different business?
- Style (illustration) in conflict with the hero (real photo)?
- Anything the model cannot do reliably (small text, QR, logos, official marks)?
- An exclusion that forbids something the creative direction requires?
- Any reference to another prompt, or any image numbering that does not match the attachment list?
- Any meta-commentary sentence that does not change the picture?
- Is the ATTACHED IMAGES block present when there are no images?
- Does the prompt leave any essential content unspecified when strategy A was chosen?

---

## 10. Example A: counter poster with attached images (strategy A)

Brief: "Kopi Mbak Rini", Bekasi, 1-litre milk coffee; buyers: anak kos and office workers 20-35; action: order via WhatsApp; message: "satu botol cukup seharian"; offer Rp 55.000/botol, beli 2 Rp 100.000, until Sunday; bottle photo and logo available; direction: warm, confident, merakyat.

**Creative Direction Summary (produced before writing the prompt):**
Concept: "One confident bottle against generous space — the smallness of the product vs. the scale of the daily promise." The design should feel like an honest neighborhood product that quietly delivers on a big promise — warm, direct, nothing to hide. Deep coffee-brown warmth as the field, the real bottle as the single hero, the offer as the second thing the eye lands on. The character is sign-painter confidence, not polished commercial. Specificity: the real kraft-paper bottle label, the daily-use positioning, the merakyat warmth.

```
FORMAT: Printed counter promotional poster, A4 portrait (210×297 mm, 2480×3508 px at 300 dpi).

OBJECTIVE: Catch the eye of a customer standing at the counter and communicate the daily-use offer clearly enough that they buy or order.

CONCEPT: "Satu botol, cukup seharian." Confident and unpretentious. For students and office workers who want honest daily coffee.

CONTENT:
- Headline: "SATU BOTOL, CUKUP SEHARIAN"
- Price: "Rp 55.000" with bundle "beli 2 jadi Rp 100.000"
- Deadline: "s.d. Minggu ini"
- CTA: "Pesan lewat WhatsApp"
- Hero: 1-litre milk-coffee bottle (Image 1)
- Brand: business logo (Image 2), upper area
Render all text exactly as written, in Indonesian, no additional words.

CREATIVE DIRECTION: A warm, direct promotional composition built around one honest product and one generous promise. The dominant feeling is confident and merakyat — the design of a neighborhood product that does not need to shout because the daily value speaks for itself. Deep coffee-brown warmth fills the field; the bottle stands as the quiet hero; the headline carries the promise in bold sign-painter caps. Generous breathing room around the bottle signals confidence. The overall character is honest and direct — warm without being casual, simple without being empty.

DESIGN CHARACTER: The warmth of a kopitiam counter that has served the same neighborhood for years — the kraft-paper label, the sign-painter headline, and the deep-brown field all signal a real product with a real story behind it. The daily-use promise ("cukup seharian") is the organizing idea that makes this specific to Kopi Mbak Rini, not just a coffee promo.

HERO VISUAL: Image 1 — the 1-litre milk-coffee bottle with kraft paper label. Keep the product exactly as photographed: bottle shape, label design, cap color, liquid color unchanged. Place standing upright at a slightly low angle, on a worn dark-teak counter surface with visible wood grain. Window light from the left, soft and warm, casting a faint shadow. No reflections on the label. Replace background with flat deep coffee-brown (#3B2418).

VISUAL SYSTEM (identical in every prompt of this set):
Type: heavy condensed sign-painter caps for headline; clean humanist sans for support text; no scripts. Style and material: photographic product on flat painted dark-brown surface, matte finish, natural window light with slight warm cast. Image treatment: real product photos kept exactly, placed on surface with a soft grounded contact shadow, no glow. Device: none. Space level: calm.

ATTACHED IMAGES (attach in this order):
Image 1 = owner's real photo of a 1-litre milk-coffee bottle with a kraft paper label. Role: hero. Treatment: keep exactly; replace background with flat deep coffee-brown. Keep unchanged: bottle shape, kraft label design, cap color, liquid color. May change: background, light direction softened to match scene.
Image 2 = business logo. Role: brand mark. Treatment: place unaltered, upper area. Keep unchanged: everything.
Priority if conflicts: Image 1 wins on product appearance; Image 2 must never be redrawn or recolored.

EXCLUSIONS: Keep bottle shape, label, and logo exactly as photographed. Avoid floating coffee beans or liquid splashes, glow effects, gradient backgrounds, decorative sparkles, rounded glass panels behind text, extra invented text, stock smiling people, busy patterned backgrounds.
```

Lampiran: 1. Foto botol (hero). 2. Logo (pojok kiri atas). Cara: unggah keduanya dalam urutan ini, lalu tempel prompt di kolom yang sama dan kirim bersamaan.

---

## 11. Example B: spanduk background (strategy B, no images attached)

Brief: "Laundry Bersih Kilat", Depok; students and workers; message "selesai besok"; action: call or WhatsApp; spanduk 3 m × 1 m on roadside shop front; price Rp 6.000/kg; direction: clean, reliable, sky-blue.

**Creative Direction Summary (produced before writing the prompt):**
Concept: "Beres sebelum besok — the domestic relief of done." The design should communicate clean reliability in one strong visual read — a neat stack of fresh laundry on the right, a generous flat text zone on the left for the owner to add the message in bold type. The sky-blue field signals cleanliness and openness. The feeling is calm and dependable: a service that works without drama. Specificity: a real folded clothes stack (not soap or machines), a paper tag in a warm accent, the promise itself as the organizing visual idea.

```
FORMAT: Printed roadside shop banner, 3×1 m vinyl tarpaulin. 3:1 aspect ratio (3000×1000 px).

OBJECTIVE: Provide a clean, flat visual background for the owner to complete with business name, "SELESAI BESOK", price per kg, and phone number in large bold type.

CONCEPT: "Selesai besok." Clean and reliable. For students and workers who need their laundry done without waiting.

CONTENT:
Text zone reserved: left two-thirds of the canvas, completely flat sky-blue (#BFE3F2), no detail or texture. Owner adds: business name, "SELESAI BESOK", price per kg, and phone number in large navy bold type.
Visual content: folded laundry stack, right third only.
No text, letters, numbers, symbols, or logos anywhere in the generated image.

CREATIVE DIRECTION: A clean, confident composition built around the promise of done. The feeling is orderly and calm — the domestic satisfaction of finding your laundry ready before you expected it. The sky-blue left field is the text canvas: flat, open, uncluttered, designed to carry the owner's message in maximum legibility. The folded clothes on the right are the proof — real fabric texture, a handwritten tag, no soap or machines. A narrow navy band at the base grounds the whole piece and adds structure without decoration.

DESIGN CHARACTER: The visual language of a trustworthy local service — clear, clean, and practical. The folded stack with a hand-tied tag signals care and craft; the open blue field signals confidence and clarity. This is not a laundry generic: the combination of the domestic warmth of the stack and the pure openness of the text zone creates a piece that works as a real neighborhood banner, not a template.

HERO VISUAL: Right third of the banner only. A neat stack of three freshly folded garments — a white cotton shirt on top, a sky-blue towel in the middle, a cream linen shirt at the base — resting directly on a plain white laminate surface. One hand-tied paper tag in sunny yellow (#FFC83D) tucked under the top fold. Overhead natural daylight, slightly diffused, crisp grounded shadow beneath. Fabric texture and weave visible on each garment. No extra props, no hangers, no soap, no machines.

VISUAL SYSTEM (identical in every prompt of this set):
Type: bold neutral humanist sans, to be added later in editor. Style and material: real-photo feel, matte surfaces, clean flat background. Image treatment: objects grounded on surface with crisp edges and a soft grounded shadow, no glow. Device: navy bottom band. Space level: calm.

EXCLUSIONS: Keep left two-thirds entirely flat sky-blue with zero detail. Avoid any text or symbols anywhere on the canvas, washing machines, floating soap bubbles, sparkles, decorative wave patterns, steam effects, stock families, foam splashes, any decoration in the text zone.
```

Lampiran: Tidak ada lampiran.

Cara pakai: Tambahkan teks di Canva atau di percetakan — nama usaha, "SELESAI BESOK", harga per kg, dan nomor telepon — dalam huruf navy tebal yang besar di area biru kiri.

---

## 12. Example C: table card / promotional flyer, no reference images, with identity treatment (strategy A)

Brief: "Sambal Mbah Sari", Yogyakarta, hand-ground sambal in jars, sold via WhatsApp; buyers: urban adults 25-45; message: "diulek pagi ini, dikirim hari ini"; action: order via WhatsApp; price Rp 25.000/jar; no logo, no photos; direction: handmade warmth, honest, artisanal, traditional Java.

**Creative Direction Summary (produced before writing the prompt):**
Concept: "A jar that arrived this morning — the texture of something made before dawn." The design is organized around one small honest jar of sambal and the freshness promise that makes it specific. The visual character is Javanese domestic authenticity: terracotta surfaces, morning side-light, the stone mortar softly present in the background. A full-width dark-brown panel carries the identity in slab-serif stamp caps — this is a brand name, not a label. Spacious and warm; the jar earns its space by being the real thing. Specificity: hand-ground texture visible through the glass, the cobek mortar, the kraft paper tie, the "since 1987" proof.

```
FORMAT: Printed table card / promotional flyer, A5 portrait (148×210 mm, 1748×2480 px at 300 dpi).

OBJECTIVE: Catch the attention of a patron seated at a table or cashier and communicate the freshness and handmade authenticity of the product clearly enough that they order.

CONCEPT: "Diulek pagi ini, dikirim hari ini." Handmade and honest. For urban adults who want real food, not factory product.

CONTENT:
- Business name: "SAMBAL MBAH SARI" (in identity panel, top)
- Provenance: "Yogyakarta — diulek sejak 1987"
- Price: "Rp 25.000 / toples"
- Freshness promise: "Diulek pagi ini, dikirim hari ini."
- CTA: "Pesan via WhatsApp"
- Hero: small glass jar of dark-red chunky sambal bawang
Render all text exactly as written, in Indonesian, no additional words.

CREATIVE DIRECTION: A still-life composition that feels like a photograph taken on a Yogyakarta kitchen counter at seven in the morning — before the day's orders have gone out. Warm morning side-light from a window catches the terracotta tile surface and the glass of the jar. The overall feeling is quiet, genuine, and slightly unhurried — this is food made by a real person with a real stone mortar, not produced at scale. The dark-brown identity panel at the top grounds the piece with the authority of a shopfront sign. The palette is earthy and warm: terracotta tile, dark brown, off-white text, a single touch of golden yellow on the price. Spacious around the jar — the empty space is part of the confidence.

DESIGN CHARACTER: The Javanese domestic authenticity of a home producer whose sambal has been made the same way since 1987 — the chunky texture visible through the glass, the kraft paper lid tie, the batu cobek partially visible in the background, the slab-serif stamp identity. These elements together could only belong to Sambal Mbah Sari: a neighborhood producer with a real process, a real origin, and a real promise.

HERO VISUAL: A small squat glass jar, about 8 cm tall and 7 cm diameter, filled with dark-red chunky sambal bawang. Lid sealed with a square of brown kraft paper tied with natural twine. The jar sits on a worn terracotta tile surface. A traditional batu cobek (stone mortar) partially visible and softly out of focus beside it. Morning side-light from a window, warm and slightly golden, short shadow falling to the right. Sambal texture visible through the glass — chunky, with visible whole chilli seeds and shallot slivers. No garnish, no extra props, no decorative chillies or garlic outside the jar.

LOGO / IDENTITY: No logo file. Business name "SAMBAL MBAH SARI" rendered in heavy slab-serif capitals, warm off-white (#FAF0E6), with a stamped-ink texture, inside a full-width dark-brown rectangular panel (#2C1A0E) at the top of the canvas. Below the name in the same panel: "Yogyakarta — diulek sejak 1987" in small caps humanist sans, off-white, smaller. This panel is the brand mark — render exactly as described, do not reinterpret.

VISUAL SYSTEM (identical in every prompt of this set):
Type: heavy slab-serif caps for business name; small caps humanist sans for supporting text; no scripts. Style and material: photographic still life on real terracotta tile, warm morning window light, matte surfaces, slight visible texture. Image treatment: all objects grounded on surface with a natural contact shadow, no glow or studio effects. Device: full-width dark-brown panel as brand mark at top. Space level: calm.

EXCLUSIONS: Keep jar proportions realistic (squat, small) and sambal texture visibly chunky. Avoid glossy jar surfaces, neon-red sambal color, floating chillies or garlic outside the jar, heavy bokeh that erases the terracotta tile texture, invented certifications or award ribbons, extra decorative Javanese motifs not requested, generic "artisan" props (twine bundles, dried herbs scattered around).
```

Lampiran: Tidak ada lampiran.

---

## 13. Assembling a set

1. Write the **Visual System block once** and copy it word for word into every prompt.
2. Write the **CONCEPT** campaign line once; it is the same in every prompt.
3. For each output write its own: FORMAT, OBJECTIVE, CONTENT, CREATIVE DIRECTION, DESIGN CHARACTER, HERO VISUAL, (LOGO/IDENTITY if needed), (ATTACHED IMAGES if applicable), EXCLUSIONS.
4. Check: any "same as", "previous", "above", or cross-prompt image reference? Remove it.
5. Check: is there an ATTACHED IMAGES block in a prompt with no images? Remove it.
6. Run the self-check in `SKILL.md`, then give each prompt its **Lampiran** list. A full worked set is in `examples/01-warung-bakso-sesi-lengkap.md`.
