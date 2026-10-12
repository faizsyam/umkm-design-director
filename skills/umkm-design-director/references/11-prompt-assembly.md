# 11 — Prompt Assembly: Professional Art Direction in Standalone Image Prompts

Contents: the art-direction-first rule · what a prompt must do · the canonical prompt structure · block rules & visual language standards · final artwork rule · phrasing & optical translation rules · semantic density & high-information language · realistic food & product imagery · length & tool notes · contradiction check · Example A (poster with images) · Example B (roadside spanduk, no images) · Example C (table card, identity treatment) · assembling a set

---

## 0. The Art-Direction-First Rule

**Never write a prompt directly from business attributes or literary mood descriptions.**

Before composing a single prompt line, the **Creative Direction Summary** (Stage 7) and its **Visual Thesis** must exist. The summary is not a poetic narrative about feelings; it is an expert art director's brief defining:
- The visual tradition and historical lineage
- The image-making technique and graphic medium
- The formal form language, line character, and edge definitions
- The typographic anatomy and lettering voice
- The material substrate, ink finish, and surface physics
- The business-specific anchors that make the design un-swappable

An image model cannot render abstract psychological sentiments like *"domestic satisfaction," "quiet confidence,"* or *"honest pride."* When fed literary mood prose, it defaults to generic commercial CGI, airbrushed plastic textures, and floating decorative clutter.

**The Test:** Before writing a prompt, ask: *"Does this brief specify the exact artistic tradition, rendering technique, form language, material substrate, and typographic anatomy needed for the image model to build a cohesive, distinctive graphic?"* If not, define the Visual Thesis first.

---

## 1. What a Prompt Must Do

A prompt is a **complete, standalone art-direction brief** for a master image-maker that cannot ask clarifying questions. It must communicate:

1. **What is being created:** Physical print medium, format, aspect ratio, and viewing objective.
2. **Who it belongs to and addresses:** The specific business and audience posture.
3. **What must visibly appear:** Essential content only, with all on-image copy quoted verbatim for direct in-image rendering.
4. **The Visual World & Art Direction:** The overarching artistic lineage, image-making medium, formal shape/edge language, palette relationships, and spatial atmosphere.
5. **The Proprietary Design Character:** The business's authentic truth, craft, and physical reality translated into un-swappable visual forms.
6. **Element-Specific Treatments:** The exact rendering, lighting, texture, and edge behavior of typography, hero subjects, and graphic devices.

### What the Prompt Must NOT Do:
- Micromanage layout with pixel coordinates, bounding box percentages, or rigid layout coordinates.
- List dozens of trivial background props or decorative filler.
- Include design rationale, reasoning steps, or meta-commentary ("we chose this because...").
- Paste raw viewing-context sentences without translating them into optical design requirements.
- Leave empty placeholder zones for external post-editing (unless explicitly requested by the owner).

**The Rule of Creative Freedom:** Specify the visual language, the rendering craft, and the non-negotiable content with maximum precision. Then allow the image model the creative freedom to discover the most effective composition.

---

## 2. The Canonical Prompt Structure

Every prompt follows this canonical order to give the image model its core orientation first, followed by content, art direction, element treatments, and constraints:

```
FORMAT: [Physical medium, e.g. "Printed roadside banner, 3×1 m, vinyl tarpaulin"], [aspect ratio and px, e.g. "3:1 (3000×1000 px)"].

OBJECTIVE: [One sentence — concrete communication task for the physical viewer].

CONCEPT: "[Campaign idea — identical across prompts in a set]". [Feeling 1] and [feeling 2]. For [specific audience].

CONTENT:
- [Primary message / headline — exact text quoted verbatim]
- [Key supporting text — exact text quoted verbatim]
- [Product or service]
- [Brand identity — logo or identity treatment]
- [Any important visual elements or motifs]
Render all copy and graphic elements directly into final integrated artwork. No blank reserved text zones.

CREATIVE DIRECTION: [The overarching art direction, visual tradition, rendering medium, formal shape and line language, material expression, and spatial atmosphere. High semantic density, professional design terminology. 3–5 sentences.]

DESIGN CHARACTER: [The proprietary visual thesis and business-specific anchors — how the business's USP, craft, materials, and physical reality are manifested in visual form. Swap-test passed. 2–3 sentences.]

HERO VISUAL: [The dominant visual element. Art-directed rendering method, stylization level, lighting physics, surface textures, edge quality, and physical grounding. If attached photo, specify exact preservation.]

[LOGO / IDENTITY — include if no logo file exists:]
LOGO / IDENTITY: Business name "[name]" rendered in [specific typographic anatomy: classification, optical weight, stroke stress, terminal cut, case], [color], [framing device or panel].

VISUAL SYSTEM (identical in every prompt of this set):
Type: [headline anatomy — weight, classification, terminal character, case]; [support character]. Style and material: [rendering medium, texture, finish, light physics]. Image treatment: [how photos/illustrations are grounded]. Device: [recurring graphic framing element, or none]. Space level: [calm / moderate / structured density].

[ATTACHED IMAGES — include ONLY if images are attached to this prompt; omit entirely otherwise:]
ATTACHED IMAGES (attach in this order):
Image 1 = [what it is]. Role: [hero / setting / brand mark]. Treatment: [keep exactly / clean up / integrate]. Keep unchanged: [...]. May change: [...].
Priority if conflicts: [...].

EXCLUSIONS: Keep [truth constraints]. Avoid [4–8 concrete failure modes for this specific brief].
```

---

## 3. Block Rules & Visual Language Standards

- **FORMAT:** State the physical print medium and production substrate explicitly ("Printed roadside banner, 3×1 m, vinyl tarpaulin," "Printed counter poster, A4 portrait, 250 gsm matte art carton"). State the pixel dimensions and aspect ratio.
- **OBJECTIVE:** Single concrete communication task: *"Deliver instant offer recognition to passing motorbike traffic within two seconds,"* or *"Convince a seated diner to order the house specialty."*
- **CONCEPT:** The organizing campaign idea, identical in every prompt of a set.
- **CONTENT:** Ranked content elements with all text quoted verbatim. Instruct: *"Render all text exactly as written, in Indonesian, no additional words."*
- **CREATIVE DIRECTION:** The core **Art Direction & Visual Language** block. Must identify:
  1. Primary visual lineage (e.g., Plakatstil object-poster, Swiss International Style, Mid-Century offset lithography, Indonesian vernacular commercial sign).
  2. Image-making technique / medium (e.g., flat-plane gouache illustration, spot-color screenprint, medium-format editorial still life).
  3. Form language and edges (e.g., reductive geometric silhouettes, razor-sharp vector contours, hand-painted enamel brush fringe).
  4. Palette relationships and value contrast (e.g., saturated cobalt field #1E4B82 with high-contrast cadmium yellow lettering #FFD700).
  5. Spatial atmosphere (e.g., active negative space, asymmetric tension, uncluttered breathing room).
- **DESIGN CHARACTER:** The **Proprietary Visual Thesis & Business Anchors**. Explain how the business's real craft, tools, ingredients, or physical architecture are translated into visible graphic elements. This ensures the graphic passes the visual swap test.
- **HERO VISUAL:** Art-direct the hero subject's physical and optical rendering:
  - Subject with physical specificity (proportions, vessel, ingredient details).
  - Lighting physics: source, direction (e.g., 45° directional window raking light), quality (soft diffused vs. sharp directional), and authentic grounded contact shadow with penumbra falloff.
  - Surface texture: authentic micro-details (flour dusting, condensation drops, fabric weave, wood grain, slight natural imperfections).
  - Edge relationship: hard graphic contour, photographic depth falloff, or ink-bleed transition.
- **VISUAL SYSTEM:** The binding visual identity block (~40–60 words). Must be copied word-for-word into every prompt of a multi-output set.
- **ATTACHED IMAGES:** Include ONLY when image files are attached. Omit entirely when there are none. For each image, define Role, Treatment, Keep Unchanged, May Change, and Conflict Priority.
- **EXCLUSIONS:** Specific prohibitions against the most likely failure modes for this brief. Always include positive truth constraints ("Keep real dish proportions and authentic wood texture") followed by concrete negatives ("Avoid 3D glossy plastic food, floating ingredients, neon gradients, lens flares, decorative sparkles, invented badges").

---

## 4. Final Artwork Rule (Complete In-Image Generation)

Every generated prompt must produce **Final Integrated Artwork**: complete, finished, and ready to print with zero external post-editing:
- All typography (headlines, offers, prices, brand identity, contact numbers) must be fully rendered in the image by the generative model.
- Leaving blank placeholder zones or template boxes for manual editing in Canva or Photoshop is strictly forbidden UNLESS the user explicitly requests a blank template.
- Safeguard legibility by enforcing Stage 4 hierarchy: keep on-image copy concise, punchy, and quoted verbatim in capital letters where appropriate.

---

## 5. Phrasing & Optical Translation Rules

1. **Optical directives over literary storytelling:** Translate narrative sentiments into optical and material facts.
   - *Weak:* "Feels like a cozy family business where you feel welcomed."
   - *Professional:* "Indonesian vernacular commercial sign tradition: flat warm-ochre painted wooden surface, heavy hand-lettered sign-painter casual capitals in cream enamel, soft 45-degree directional window illumination."
2. **Translate viewing context into design character:**
   - *Weak:* "Viewed from a motorbike at 40 km/h."
   - *Professional:* "Plakatstil poster tradition: extreme value contrast, massive condensed grotesque capitals, singular bold hero silhouette against an unadorned solid color field, zero decorative clutter."
3. **High semantic density:** Every sentence must alter what the model generates. Eliminate redundant adjectives, meta-commentary, and process justifications.
4. **One language for instructions, owner's language for copy:** Prompt instructions in English for optimal model adherence; quoted on-image text in the owner's language and exact spelling.

---

## 6. Semantic Density & High-Information Language

Maximize **useful artistic specificity per word**:

$$\text{Density Score} = \frac{\text{Artistic Decisions (Lineage, Medium, Form, Typography, Substrate, Physics)}}{\text{Total Word Count}}$$

Remove:
- Empty filler ("stunning," "eye-catching," "masterpiece," "ultra-detailed," "beautiful").
- Redundant repetitions ("clean and uncluttered, with nothing messy, very neat").
- Unenforceable coordinates ("in the upper 34% of the canvas, 12 pixels from the left").
- Process storytelling ("because the customer has little time, we decided to...").

---

## 7. Realistic Food & Product Imagery

When generating food or product visuals without reference photos, specify realistic physical parameters:
- **Lighting Physics:** Name source, angle, and diffusion: *"Directional raking morning sunlight from the left at 45°, soft diffused window falloff, casting a grounded contact shadow with soft penumbra to the right."*
- **Material Substrate & Surface:** Real, named physical materials: *"Resting on a worn teak wood table surface with subtle longitudinal wood grain and satin finish,"* not *"nice rustic background."*
- **Tactile Micro-Details:** Visible ingredient reality: *"Visible flecks of chopped celery, golden fat droplets on the broth surface, authentic beef tendon grain, steam wisp curling naturally,"* not *"delicious steaming soup."*
- **Physical Imperfection:** Slight natural asymmetry, irregular cut vegetables, an authentic drizzle bead. Imperfection signals human reality; absolute symmetry signals AI synthetic plastic.

---

## 8. Length & Effectiveness

- **Length guidance:** 220–420 words per prompt for most outputs. This is guidance, not a target — shorter is better if every sentence changes the visual output. Do not pad prompts to reach a minimum length. A 180-word prompt with zero redundancy outperforms a 350-word prompt with filler.
- **The redundancy test:** Before delivering a prompt, check each sentence: "If I remove this sentence, will the generated image change?" If not, remove it.
- **Cross-block overlap:** Information should appear in exactly one block. If the material substrate is described in CREATIVE DIRECTION, do not repeat it in HERO VISUAL. If the type character is defined in VISUAL SYSTEM, do not re-describe it in CREATIVE DIRECTION.
- **OBJECTIVE and CONCEPT blocks:** These orient the image model but should contain only information that changes the visual output. Remove contextual narration, viewer behavior descriptions, and marketing language that has no visual consequence.
- **Midjourney v6+:** Add `--ar [ratio]` and consider `--style raw --s 100` flags to reduce AI beautification defaults.
- **Ideogram v2+ / DALL-E 3 / Imagen / Flux:** Set aspect ratio in the UI. For Flux, use dense descriptive prose. For DALL-E 3, explicitly instruct no CGI or digital rendering artifacts.

---

## 9. Contradiction Check

Before delivering a prompt, verify:
- [ ] Creative Direction Summary existed before writing the prompt.
- [ ] CREATIVE DIRECTION specifies visual lineage, image-making medium, form language, and material substrate.
- [ ] DESIGN CHARACTER specifies proprietary visual anchors and passes the visual swap test.
- [ ] HERO VISUAL directs rendering style, lighting physics, and edge quality.
- [ ] VISUAL SYSTEM is word-for-word identical across all prompts of the set.
- [ ] No literary mood sentences without optical translation.
- [ ] No coordinates or pixel micromanagement.
- [ ] No empty reserved text zones (Final Integrated Artwork confirmed).
- [ ] ATTACHED IMAGES block omitted when no images are attached.

---

## 10. Example A: Counter Poster with Attached Images (Final Integrated Artwork)

**Brief:** "Kopi Mbak Rini", Bekasi; 1-litre milk coffee; audience: college students and office workers 20–35; objective: counter poster driving WhatsApp orders; message: "SATU BOTOL, CUKUP SEHARIAN"; offer: Rp 55.000/botol, beli 2 Rp 100.000, until Sunday; attached assets: bottle photo (Image 1), logo (Image 2).

**Creative Direction Summary:**
- *What & Medium:* A4 portrait counter poster (210×297 mm) on 260 gsm matte art carton.
- *Objective:* Convert counter visitors into daily-bottle buyers within 5 seconds.
- *Visual Thesis:* **German Plakatstil object-poster structure combined with mid-century screenprinted coffee packaging aesthetic:** A singular monumental cold-brew bottle silhouette grounded on an unadorned, deep roasted-coffee field (#2A1810), framed by massive sign-painter condensed capitals (#F5E6D3), with active negative space signaling confidence and daily value.
- *Specificity Anchors:* Authentic kraft-paper bottle label, the daily volume promise ("cukup seharian"), worn teak counter contact.

```
FORMAT: Printed counter promotional poster, A4 portrait (210×297 mm, 2480×3508 px at 300 dpi), matte art carton finish.

OBJECTIVE: Catch the eye of a standing counter patron and communicate the daily-use value proposition clearly enough that they order immediately.

CONCEPT: "Satu botol, cukup seharian." Confident, unpretentious daily fuel. For students and office workers needing honest sustenance.

CONTENT:
- Headline: "SATU BOTOL, CUKUP SEHARIAN"
- Price: "Rp 55.000" with bundle callout "beli 2 jadi Rp 100.000"
- Condition: "s.d. Minggu ini"
- Action: "Pesan lewat WhatsApp"
- Hero: 1-litre milk-coffee bottle (Image 1)
- Brand mark: business logo (Image 2), upper placement
Render all copy exactly as written, in Indonesian, integrated directly into final artwork. No blank text zones.

CREATIVE DIRECTION: German Plakatstil object-poster lineage executed with a screenprinted commercial poster aesthetic. The composition is built around a singular dominant product silhouette commanding an unadorned, deep roasted coffee-brown field (#2A1810). Flat matte ink finish with subtle tooth; zero digital gradients, zero artificial glows. Heavy condensed sign-painter display capitals with flat-cut terminals in warm cream (#F5E6D3) anchor the headline with bold graphic mass. Generous unprinted negative space (approximately 45% of canvas) surrounds the bottle, creating powerful visual focus and communicating unhurried artisanal confidence.

DESIGN CHARACTER: The visual language of a proud neighborhood coffee roastery — anchored by the authentic kraft-paper bottle label, the sturdy sign-painter typography, and the deep coffee-field contrast. The scale relationship between the quiet upright bottle and the bold daily promise ("cukup seharian") belongs exclusively to Kopi Mbak Rini, distinguishing it from generic commercial cafe advertising.

HERO VISUAL: Image 1 — the 1-litre milk-coffee bottle with kraft paper label. Keep the product exactly as photographed: bottle silhouette, label graphics, cap color, and liquid tone unaltered. Ground upright on a worn dark-teak wooden counter surface with visible grain and satin finish. Directional raking morning window light from the left at 45°, casting a soft grounded contact shadow with penumbra falloff to the right. Seamless planar transition into the solid coffee-brown background field.

VISUAL SYSTEM (identical in every prompt of this set):
Type: heavy condensed sign-painter capitals with flat-cut terminals for headline; clean humanist sans for supporting text; no scripts. Style and material: photographic product on flat opaque dark-brown field, matte ink finish, natural directional window light. Image treatment: real product photos preserved exactly, grounded with soft contact shadows, no halo or glow. Device: solid warm-ochre accent bar under price. Space level: calm.

ATTACHED IMAGES (attach in this order):
Image 1 = owner's photo of a 1-litre milk-coffee bottle with kraft paper label. Role: hero. Treatment: keep product exactly; isolate onto solid coffee-brown background. Keep unchanged: bottle shape, label, cap, liquid color. May change: background, lighting balanced to directional window light.
Image 2 = business logo. Role: brand mark. Treatment: place unaltered in upper area. Keep unchanged: everything.
Priority if conflicts: Image 1 governs product appearance; Image 2 must never be recolored or redrawn.

EXCLUSIONS: Keep bottle silhouette, label graphics, and logo exactly as provided. Avoid floating coffee beans, liquid splash crowns, neon gradients, lens flares, decorative sparkles, glass-morphism panels behind text, stock smiling people, crowded decorative borders.
```

**Lampiran:** 1. Foto botol (hero). 2. Logo (area atas). Cara: Unggah kedua gambar dalam urutan ini, tempel prompt, kirim bersamaan.

---

## 11. Example B: Roadside Spanduk, No Reference Images (Final Integrated Artwork)

**Brief:** "Laundry Bersih Kilat", Depok; roadside shop front; audience: college students and busy workers passing on motorbikes; message: "SELESAI BESOK"; pricing: "Rp 6.000 / kg"; spanduk 3×1 m vinyl tarpaulin; no photos available; direction: clean, reliable, high-speed roadside legibility.

**Creative Direction Summary:**
- *What & Medium:* Roadside shop banner, 3×1 m vinyl tarpaulin, 3:1 aspect ratio (3000×1000 px).
- *Objective:* Register speed promise and pricing to moving motorbike riders in under 2 seconds.
- *Visual Thesis:* **Swiss International Style asymmetric grid meets commercial screenprint poster tradition:** Razor-sharp planar vector blocking, massive navy condensed grotesque typography (#0F2444) set against an unadorned luminous sky-blue field (#E6F3FA), anchored by a hyper-crisp still-life rendering of folded cotton laundry on the right, grounded by an ultramarine structural base band.
- *Specificity Anchors:* Tangible cotton fabric weave, hand-tied kraft paper tag in warm cadmium yellow (#FFC83D), decisive non-decorative clarity.

```
FORMAT: Printed roadside shop banner, 3×1 m vinyl tarpaulin, 3:1 aspect ratio (3000×1000 px), outdoor matte flex finish.

OBJECTIVE: Catch the attention of passing motorbike riders within 2 seconds, delivering instantaneous recognition of next-day turnaround and honest pricing.

CONCEPT: "Selesai besok." Crisp domestic reliability. For students and workers who need laundry solved without drama.

CONTENT:
- Business name: "LAUNDRY BERSIH KILAT" in sturdy humanist sans capitals
- Headline: "SELESAI BESOK" in massive condensed grotesque display capitals
- Price: "Rp 6.000 / kg" prominent and bold
- Contact: "WA 0812-3456-7890" in high-contrast numerals
- Visual content: crisp stack of folded garments on the right
Render all copy exactly as written, in Indonesian, integrated directly into the artwork with sharp edge boundaries. No blank text zones.

CREATIVE DIRECTION: Swiss International Style grid discipline combined with a flat-plane screenprinted commercial poster aesthetic. The composition is built on powerful asymmetric balance: the left two-thirds is a calm, luminous sky-blue field (#E6F3FA) carrying high-contrast navy display typography; the right third is anchored by a sharp, tactile still-life of neatly folded garments. Extreme value contrast engineered for tropical sunlight legibility. Razor-sharp contour edges, zero airbrushed gradients, zero digital glows. A solid deep ultramarine band (#0F2444) at the bottom edge provides architectural grounding for the contact details.

DESIGN CHARACTER: The visual authority of a disciplined, trustworthy neighborhood institution. By replacing generic laundry clichés with the tactile reality of perfectly ironed cotton weave and a hand-tied yellow paper ticket, the design conveys authentic domestic care and prompt delivery. Impossible to confuse with generic clip-art laundry templates.

HERO VISUAL: Right third of the canvas. A precise, rectilinear stack of three freshly ironed garments: a crisp white oxford cotton shirt on top with collar neatly pressed, a sky-blue woven towel in the center, and a cream linen shirt at the base. One rectangular paper laundry tag in warm cadmium yellow (#FFC83D) tucked neatly under the top collar fold. Diffused overhead daylight, casting a crisp, grounded contact shadow directly beneath. Tactile fabric weave clearly visible; sharp outline silhouette against the blue field.

VISUAL SYSTEM (identical in every prompt of this set):
Type: massive condensed grotesque display capitals for headline; neutral humanist sans for business name and price. Style and material: flat vector screenprint aesthetic combined with tactile realistic fabric still life, matte tarpaulin surface. Image treatment: objects grounded on surface with crisp contact shadows, no floating elements. Device: solid ultramarine base band. Space level: calm.

EXCLUSIONS: Keep fabric weave realistic, shirt collar crisp, and typography razor-sharp. Avoid cartoon washing machines, floating soap bubbles, foam splashes, water droplets, sparkles, steam swirls, neon cyan gradients, stock smiling families, curved script fonts.
```

**Lampiran:** Tidak ada lampiran. Cara: Salin prompt ke AI pembuat gambar, hasil langsung dicetak tanpa edit tambahan.

---

## 12. Example C: Table Card / Flyer, No Images, Identity Treatment (Final Integrated Artwork)

**Brief:** "Sambal Mbah Sari", Yogyakarta; artisanal hand-ground sambal bawang in glass jars; audience: food enthusiasts 25–45 seeking authentic culinary heritage; message: "DIULEK PAGI INI, DIKIRIM HARI INI"; price: Rp 25.000 / toples; provenance: "Yogyakarta — sejak 1987"; no logo, no photos; direction: authentic Javanese culinary craft, handmade warmth, honest stone-mortar process.

**Creative Direction Summary:**
- *What & Medium:* Table card / promotional flyer, A5 portrait (148×210 mm, 1748×2480 px at 300 dpi).
- *Objective:* Engage a seated diner or counter customer, establishing dawn-made freshness and generational authenticity.
- *Visual Thesis:* **Tactile woodcut/relief printmaking combined with Javanese domestic editorial still-life photography:** A squat glass jar filled with chunky stone-ground sambal resting on weathered terracotta tile under 45° warm morning raking light, anchored at the top by a woodcut-inspired dark umber identity panel (#2C1A0E) with stamped Egyptian slab-serif lettering (#FAF0E6).
- *Specificity Anchors:* Visible whole chili seeds and shallot shreds, traditional volcanic stone cobek softly out of focus, kraft-paper twine seal, "sejak 1987" provenance.

```
FORMAT: Printed table card / promotional flyer, A5 portrait (148×210 mm, 1748×2480 px at 300 dpi), 260 gsm uncoated textured cardstock.

OBJECTIVE: Engage a seated patron or counter visitor and communicate the raw handmade freshness of dawn-ground sambal so they order via WhatsApp.

CONCEPT: "Diulek pagi ini, dikirim hari ini." Authentic handmade culinary craft. For urban adults seeking real heritage food over factory condiment sauces.

CONTENT:
- Business name: "SAMBAL MBAH SARI" (in top identity panel)
- Provenance: "Yogyakarta — diulek sejak 1987"
- Headline: "DIULEK PAGI INI, DIKIRIM HARI INI"
- Price: "Rp 25.000 / toples"
- Action: "Pesan via WhatsApp"
- Hero: small glass jar of chunky dark-red sambal bawang
Render all text exactly as written, in Indonesian, integrated directly into the final artwork. No blank text zones.

CREATIVE DIRECTION: Javanese domestic culinary still-life tradition combined with tactile woodcut relief printmaking. The visual world evokes a quiet Yogyakarta home kitchen at dawn: warm, unhurried, and authentic. The upper canvas is anchored by a solid deep-umber header panel (#2C1A0E) functioning as an authoritative shop sign; the lower canvas opens into a warm still-life set on aged terracotta tile. Palette of rich burnt umber, raw terracotta, off-white bone, and vibrant deep-crimson sambal. Earthy, non-glossy matte surfaces with tactile paper tooth. Generous breathing room around the jar creates unforced dignity.

DESIGN CHARACTER: The undeniable authenticity of a generational home producer whose recipe has remained unchanged since 1987. Anchored by the chunky, hand-crushed texture visible through the jar glass, the kraft paper lid tied with coarse jute twine, the traditional volcanic stone cobek softly present in the background, and the stamped slab-serif typography. This design belongs uniquely to Sambal Mbah Sari and cannot be swapped into factory commercial food packaging.

HERO VISUAL: Center of the lower composition. A squat cylindrical glass jar (approx. 8 cm tall, 7 cm diameter) filled with coarse, hand-ground sambal bawang in rich crimson oil. Texture visibly chunky with split chili seeds, golden shallot shreds, and crushed bird's eye chilies. The metal lid is covered with a square of unbleached kraft paper bound with natural jute twine. The jar sits firmly on a weathered terracotta tile surface with natural clay texture. A traditional Javanese volcanic stone mortar (batu cobek) rests softly out of focus in the left background. Warm 45-degree morning raking window light from the left, casting a natural contact shadow to the right. No stray decorative vegetables or fake props.

LOGO / IDENTITY: No logo file. Business name "SAMBAL MBAH SARI" rendered in heavy Egyptian slab-serif capitals with a stamped woodblock ink texture, warm bone off-white (#FAF0E6), set inside a full-width dark-umber rectangular panel (#2C1A0E) across the top. Below the name in the same panel: "Yogyakarta — diulek sejak 1987" in small-caps humanist sans, bone white, smaller scale. This panel functions as the permanent brand mark.

VISUAL SYSTEM (identical in every prompt of this set):
Type: heavy stamped Egyptian slab-serif caps for brand mark; sturdy condensed humanist sans for headline; clean small-caps for support. Style and material: photographic editorial still life on real terracotta tile, warm morning window raking light, matte non-glare finish. Image treatment: all objects physically grounded with authentic contact shadows, no floating elements. Device: full-width dark-umber woodcut identity panel at top. Space level: calm.

EXCLUSIONS: Keep jar proportions squat and sambal texture visibly chunky. Avoid glossy plastic jar surfaces, neon-red translucent chili paste, floating garlic or chilies outside the jar, excessive depth blur that erases the clay tile, fake gold ribbons, invented certification logos, generic stock artisan props (loose dried herbs, scattered peppercorns).
```

**Lampiran:** Tidak ada lampiran. Cara: Salin prompt ke AI pembuat gambar, hasil siap langsung dicetak tanpa edit tambahan.

---

## 13. Assembling a Set

1. **Establish the Visual Thesis once:** Write the **VISUAL SYSTEM** block and copy it word-for-word into every prompt.
2. **Campaign Concept:** Keep the **CONCEPT** line identical across the entire set.
3. **Per-Output Customization:** Write output-specific FORMAT, OBJECTIVE, CONTENT, CREATIVE DIRECTION, DESIGN CHARACTER, HERO VISUAL, (LOGO/IDENTITY if applicable), and EXCLUSIONS.
4. **Self-Audit:** Verify that no prompt references another prompt ("same as prompt 1" is strictly prohibited). Each prompt must function in total isolation.
5. **Attach Local Lampiran:** Every prompt concludes with its own local attachment instructions.

---

*End of Reference 11 — Prompt Assembly.*
