# 06 — Typography, Lettering, and Readability for Physical Print

Contents: why type decides trust in physical print · physical print viewing distance & scale · anatomical & stylistic type classifications · describing letterforms to an image model · typographic contrast & hierarchy · prices, numbers, and currency formatting · Indonesian language typographic nuances · text on backgrounds & calm zones · proofreading & in-image rendering safeguards

---

## 1. Why Typography Decides Trust in Physical Print

Text is where small-business physical graphics fail first and most visibly: illegible at viewing distance, overcrowded, low contrast against bleached sunlight, or misspelled. 

Legibility is credibility. A viewer forgives a plain layout; they never forgive an unreadable price or a garbled headline.

Typography in physical print has three sequential obligations:
1. **Be read under actual physical conditions:** Distance, angle, lighting, and viewing duration (legibility).
2. **Organize information:** Make reading effortless through unmistakable scale and weight contrast (hierarchy).
3. **Embody the brand voice:** Carry authentic character and cultural resonance (voice & art direction).

Always satisfy legibility and hierarchy before indulging in personality.

---

## 2. Physical Print: Viewing Distance and Minimum Type Scale

The primary failure mode in print typography is designing for the computer screen rather than the physical environment. Letterforms must be sized for actual physical viewing distance:

**The Working Rule:** Approximately 2.5 cm of capital letter height per 3 meters of comfortable reading distance. For outdoor roadside signage viewed from moving motorbikes or cars, add 50–100% to compensate for speed, vibration, and peripheral distraction.

| Physical Viewing Distance | Typical Medium & Posture | Min Capital Height | Typographic Strategy & Word Budget |
|---|---|---|---|
| **0.3–0.5 m** | Handheld flyer, table menu, product label | 3–5 mm (8–14 pt body) | Full text possible; multi-tiered hierarchy; scannable sections; up to 60 words |
| **0.5–1.5 m** | Counter display, table card, window poster | 5–15 mm (24–48 pt headline) | Clear dominant headline; supporting price/proof point; 15–25 words max |
| **1.5–5 m** | Storefront poster, indoor X-banner | 15–50 mm (60–120 pt headline) | Bold headline dominance; secondary subhead; 8–15 words max |
| **5–10 m** | Storefront fascia, sidewalk banner | 50–100 mm | Massive headline; 1 visible price/action; 5–8 words max |
| **10–20 m** | Roadside spanduk (passing motorbikes) | 100–200 mm+ | 3–5 words maximum; massive condensed display capitals; extreme value contrast |
| **20+ m** | Highway billboard, overhead gantry | 250 mm+ | 1–3 words only; single iconic silhouette |

*Tropical Sunlight Factor:* Direct tropical sun bleaches value contrast. For outdoor banners, increase minimum letter height by 30% and ensure extreme dark-on-light or light-on-dark value separation.

---

## 3. Anatomical & Stylistic Type Classifications

Image models reproduce typography with vastly greater precision when directed using established anatomical and stylistic terminology rather than font brand names:

| Classification | Anatomical Characteristics | Voice & Cultural Associations | Best Suited For |
|---|---|---|---|
| **Heavy Condensed Grotesque** | Flat-cut terminals, tight tracking, uniform stroke weight, tall x-height, compact width | Industrial, urgent, authoritative, bold commercial punch | Roadside spanduk headlines, street-food offers, high-impact retail banners |
| **Humanist Sans-Serif** | Open apertures, subtle stroke modulation, organic humanist proportions, comfortable counters | Approachable, clear, warm, trustworthy, democratic | Supporting copy, addresses, service business branding, menus |
| **Geometric Sans-Serif** | Circular bowls, sharp 90° and 45° apexes, strict mathematical construction, monoline | Modern, architectural, objective, clean, progressive | Contemporary retail, youth-facing brands, tech services, modern laundry |
| **Egyptian Slab-Serif** | Heavy square block serifs, sturdy unbracketed slabs, minimal stroke contrast | Sturdy, time-tested, dependable, artisanal, mechanical | Handcrafted food labels, workshop signage, coffee roasters, price callouts |
| **Didone / High-Contrast Modern Serif** | Extreme contrast between thick verticals and hairline horizontals, unbracketed ball or hairline serifs | Luxurious, refined, formal, elegant, editorial | Upscale bakery, boutique wedding stationery, luxury hampers, cosmetic packaging |
| **Transitional / Old Style Serif** | Moderate stroke contrast, diagonal stress, bracketed serifs, organic warmth | Dignified, permanent, literate, trustworthy, authentic | Heritage institutions, formal menus, traditional Jamu branding |
| **Sign-Painter Casuals / Brush Enamel** | Flared brush terminals, gestural stroke stress, hand-painted enamel character | Energetic, local, welcoming, authentic human touch | Indonesian warung banners, pasar stall signage, street food heroes |
| **Chiseled Relief / Woodblock** | Angular gouge terminations, slight organic asymmetries, stamped ink texture | Raw, artisanal, small-batch, grounded, traditional | Stone-ground sambal, artisan coffee, traditional craft labels |
| **Display Serif Revival** | High-contrast strokes, dramatic thick-thin transitions, large x-height, ornamental ball terminals | Elevated, sophisticated, editorial, contemporary premium |
| **Decorative / Novelty Display** | Unique structural features: inline, stencil, 3D, shadowed, textured, or themed shapes | Event-specific, seasonal, playful emphasis, one-use headlines |
| **Script & Calligraphic** | Continuous flowing strokes, pen-derived forms, varying from formal copperplate to casual brush | Personal warmth, invitation quality, artisanal character, feminine elegance |
| **Hand-lettering & Brush** | Irregular stroke weight, visible brush or pen texture, organic imperfections, unique to each execution | Authentic, handmade, personal, street art, artisanal craft |
| **Vernacular Sign-Painter Extended** | Bold outlines, drop shadows, dimensional shading, high-contrast fills, optimized for distance | Street-level energy, festive, approachable, Indonesian commercial tradition |
| **Stencil & Industrial** | Broken letterforms suggesting spray-paint or cut-out origin, utilitarian geometry | Raw, industrial, military, workshop, masculine utility |
| **Retrofuturistic / Space Age** | Extended horizontal proportions, rounded geometric forms, 1960s-70s space-era optimism | Tech-forward nostalgia, creative studios, experimental food concepts |

---

## 4. Describing Letterforms to an Image Model

To direct typography in an image prompt, describe **eight anatomical and material attributes**:
$$\text{Text Element} = \text{Verbatim String} + \text{Role} + \text{Classification} + \text{Weight} + \text{Terminal/Anatomy} + \text{Case} + \text{Color/Finish} + \text{Surface/Substrate Interaction}$$

### Weak vs. Masterclass Art-Directed Phrasing

- **Weak:** *"Bold modern yellow font for the headline"*
- **Masterclass:** *"Headline 'SEGEDE BOLA TENIS' rendered in massive heavy condensed sign-painter capitals with flat-cut terminals, tight optical tracking, painted in warm cadmium yellow enamel (#FFD700) with subtle hand-painted brush fringe on a flat cobalt ground"*

- **Weak:** *"Nice vintage font for the logo"*
- **Masterclass:** *"Business name 'SAMBAL MBAH SARI' in heavy Egyptian slab-serif capitals with a stamped woodblock ink texture, warm bone off-white (#FAF0E6), set inside a dark-umber panel"*

- **Weak:** *"Clean font for the contact number"*
- **Masterclass:** *"Contact 'WA 0812-3456-7890' set in high-contrast neutral neo-grotesque bold numerals, clean open counters, rendered crisply in deep navy (#0F2444) on a luminous white base strip"*

### Typography personality axes

When developing typographic direction, consider these independent personality dimensions:
- **Formal ↔ Casual:** Court invitation vs handwritten note
- **Loud ↔ Quiet:** Massive condensed display vs delicate hairline caption
- **Geometric ↔ Organic:** Futura vs hand-lettered brush
- **Historical ↔ Contemporary:** Caslon vs Neue Haas Grotesk
- **Singular ↔ Systematic:** One expressive display face vs a disciplined type system
- **Culture-specific ↔ Culture-neutral:** Vernacular sign-painter vs neutral grotesque

These axes are independent — a typeface can be formal AND loud (monumental serif), or casual AND quiet (relaxed humanist sans at small size). Combine axes deliberately.

---

## 5. Typographic Contrast, Scale & Hierarchy

1. **The Two-Voice Rule:** Use at most **two typographic personalities** per graphic piece (e.g., one expressive display headline + one neutral humanist sans for support). More than two personalities creates chaotic amateur clutter.
2. **Dramatic Scale Ratio:** In physical print, the headline must be at least **3x to 4x the optical size** of supporting copy. Timid scale steps (e.g. 1.5x) fail to create an immediate focal entry point.
3. **Case Discipline:**
   - **ALL CAPS:** Strictly for short headlines (under 5 words), price callouts, acronyms, and single-line brand headers.
   - **Sentence Case:** Mandatory for sentences longer than 5 words, addresses, descriptions, and disclaimers.
   - *Never set long paragraphs or multi-line copy in all caps — legibility collapses.*
4. **Alignment Spine:** Commit to a single alignment spine (typically left-aligned in Indonesian print). Centered typography is reserved exclusively for symmetrical ceremonial graphics or short 2-line badges.
5. **Calm Typographic Zone:** All rendered text must sit on a calm, low-information background (a solid color field, a flat architectural panel, or an untextured sky/counter area). Text placed across photographic edges or busy ingredient textures is instantly destroyed.

---

## 6. Prices, Numbers, and Currency Formatting

A price is frequently the Level 2 secondary hero in commercial UMKM design:
- **Format Consistency:** Always use standard Indonesian formatting: `Rp 55.000` or `Rp 6.000 / kg`. Never mix formats (e.g., `55k` and `Rp 55.000` on the same piece).
- **Scale Contrast:** Set the numerals significantly larger than the currency symbol (`Rp` small, `55.000` massive).
- **Accent Color Privilege:** Assign the singular accent color (e.g. golden yellow or signal orange) directly to the promotional price.
- **WhatsApp Phone Numbers:** Format with clear grouping for instant scanning: `WA 0812-3456-7890`.

---

## 7. Indonesian Language Typographic Nuances

- **Word Length & Line Breaks:** Indonesian compound words and affixes are often substantially longer than English (e.g. *"Membersihkan"* vs *"Clean"*; *"Memuaskan"* vs *"Great"*). Break lines strictly by grammatical meaning, never by arbitrary column width:
  - *Correct:*
    `Beli 2 Porsi`
    `GRATIS Es Teh`
  - *Incorrect:*
    `Beli 2 Porsi GRATIS`
    `Es Teh`
- **Register & Tone:** Mirror the owner's customer relationship:
  - Casual & friendly: *"Yuk pesan lewat WA!"*
  - Direct & commercial: *"Pesan sekarang via WhatsApp"*
  - Formal & polite: *"Silakan hubungi kami di..."*
- **Avoid Vague Category Superlatives:** Prohibit generic filler ("Nikmati kelezatan terbaik," "Kualitas bintang lima harga terjangkau"). Replace with concrete numbers, hours, or ingredients ("Dimasak 8 jam," "100% Daging Sapi").

---

## 8. In-Image Rendering Safeguards & Proofreading

Image models can misspell or duplicate letters if given excessive text:
1. **Verbatim Quoting:** Always place exact on-image text strings in quotation marks and add: *"Render all copy exactly as written, in Indonesian, with crisp edges and zero spelling errors."*
2. **Text Budget Cap:** Roadside spanduk: 3–6 words max. Counter poster: 10–20 words max.
3. **Character-by-Character Proofread:** Verify upon generation:
   - Business name spelling
   - Price numbers and currency symbol
   - Phone and WhatsApp digits
   - Date ranges
   - Official certification text (ensure no hallucinated fake permit numbers)

---

*End of Reference 06 — Typography, Lettering, and Readability.*
