# Typography, Text, and Readability

Contents: why type decides trust · describing type to an image model · type character by feeling · limits and hierarchy · prices and numbers · Indonesian-specific notes · text on photos · text risk and proofreading

## 1. Why type decides trust

Text is where most small-business designs fail first: too much of it, too many styles, too small, low contrast, or misspelled. Legibility is credibility. A viewer forgives a plain layout; they do not forgive a price they cannot read or a word that is spelled wrong.

Typography has three jobs: **be read** (legibility and readability), **rank information** (hierarchy), and **carry personality** (voice). Always satisfy the first two before the third.

## 2. Describing type to an image model

Models respond better to a description of letter *character* than to a font name they may not reproduce. Describe: weight, width, contrast, shape, finish, case, spacing, and role.

Good: `heavy condensed sans-serif capitals with slightly rounded corners, tight but even spacing, hand-painted sign look`
Weak: `nice bold font`, `modern font`, `font like Montserrat` (names are optional, never the only instruction)

Template per text element: **text · role · size rank · weight/character · case · color · position · alignment**.

## 3. Type character by feeling

| Feeling | Type character | Suits | Avoid |
|---|---|---|---|
| Friendly, casual, youthful | Rounded or soft sans, medium-heavy, generous spacing | Drinks, snacks, kids, student audience | Hairline weights |
| Urgent, street-smart, bargain | Condensed bold grotesque or sign-painter capitals | Promos, markets, bengkel, price boards | Delicate scripts |
| Warm, traditional, homemade | Hand-lettered or brush-sign style for the headline only; sturdy slab or humanist sans for support | Warung, masakan rumahan, jajanan pasar | Too many ornamental flourishes |
| Premium, calm, refined | High-contrast serif or a light, wide sans; lots of space; small caps for labels | Gifts, hampers, craft, salon | Heavy drop shadows, glitter |
| Clean, competent, trustworthy | Neutral geometric or humanist sans, regular/semibold, ample spacing | Laundry, clinic, services, tech | Novelty display faces |
| Craft, authentic | Slab serif, typewriter, stamp-like, hand-drawn labels | Handmade goods, coffee, artisan food | Perfectly sterile spacing |
| Playful, handwritten | Script or marker for 1-2 words max | Accents, greetings | Using it for prices, addresses, or paragraphs |

Local lettering is a rich anchor: hand-painted warung boards, angkot and truck lettering, market price signs, enamel-sign styles, kopitiam-era shop signs. Naming one specific local lettering tradition makes a design look rooted rather than templated.

## 4. Limits and hierarchy

- **At most two type characters** (e.g. one display, one text) plus weight variations. Three or more reads as chaos and as AI.
- **Size ratio:** headline at least ~3x the size of supporting text; primary-to-secondary difference should be obvious at a glance.
- **Case:** ALL CAPS for short headlines (under ~4 words) only; sentence case for anything longer; never long sentences in capitals.
- **Alignment:** one spine, usually left-aligned. Centered short text is fine for formal or symmetrical designs; centered paragraphs are hard to read.
- **Line length and breaks:** break lines by meaning ("Beli 2 / hemat 10rb"), not just by width. Keep lines short.
- **Spacing:** tight but even for display; open for small text; avoid wide-tracked lowercase.
- **Contrast and placement:** text goes on calm areas or panels; never across busy detail.
- **Word budgets** (headline + support, excluding contact): spanduk/billboard 3-7 words; story/status 8-15 words; feed promo 15-40; marketplace banner 6-12; flyer 40-90 with grouping; menu: as needed, grouped in 3-6 categories.
- **Minimum sizes:** phone-viewed text should remain readable when the image is about 360 px wide (can you still read the smallest line?). If not, it is too small or too long.
- **Viewing distance rule of thumb:** roughly 2.5 cm of letter height per 3 m of reading distance for comfortable reading of signs; passing motorbikes and cars need considerably larger and fewer words.

## 5. Prices and numbers

- A price is often the second most important element. Give it its own size, weight, and the accent color.
- Use one consistent format everywhere: `Rp 55.000` or `55rb`; do not mix. Prefer large number, small unit.
- Show the comparison when it helps: old price struck through smaller, new price large, savings stated once ("hemat Rp 10.000").
- Limit price points on a promo to what viewers can compare in a glance (1-3). Menus use aligned right-hand price columns, not scattered prices.
- Phone/WhatsApp numbers: grouped in readable blocks (0812-3456-7890), large enough, high contrast, placed at the end of the reading path. Prefer adding them manually after generation (text strategy B/C).
- Dates: use unambiguous format ("s/d Minggu, 12 Okt" or "12-14 Oktober").

## 6. Indonesian-specific notes

- Indonesian words are often longer than English; plan widths. A 3-word English headline can become 4-5 Indonesian words.
- Use the audience's register: "Pesan sekarang" (neutral), "Yuk pesan!" (casual), "Segera hubungi kami" (formal). Match the owner's voice.
- Avoid generic ad filler ("Nikmati kelezatan terbaik", "Kualitas terbaik harga terjangkau"): specific beats generic every time. See the copy section of the anti-slop file.
- Regional language phrases add flavor but only if the owner uses them naturally.
- Watch for abbreviations that vary: "rb", "k", "ribu"; be consistent.
- Diacritics are rare in Indonesian, which helps rendering; but long compound words and "ng/ny" clusters still get misspelled, so proofread.

## 7. Text on photos and backgrounds

- Reserve a **text zone** in the composition: a calm area (sky, wall, tabletop, blurred background) of ~25-40% of the canvas, or a solid panel.
- If the background is busy, add a panel or tonal overlay and say so in the prompt.
- Keep a margin (about 5-8% of canvas) so text does not touch edges or platform UI.
- Do not wrap text around complex silhouettes.
- Never put text over faces or the product's key detail.

## 8. Text risk and proofreading

Image models can still misspell, merge letters, or invent extra words, especially with long text, small text, numbers, and non-English words.

Reduce risk:
1. Put exact text in quotes in the prompt and add: "render this text exactly as written, no additional words".
2. Limit the number of text elements (aim for 3-5).
3. Keep each line short; large sizes render more accurately.
4. Put phone numbers, addresses, URLs, QR codes, legal marks, and fine print outside the AI image (strategy B/C).
5. Always proofread character by character after generation: name, price, dates, number, spelling.
6. If one word is wrong, regenerate with a one-change prompt or fix it in Canva rather than accepting an error.
