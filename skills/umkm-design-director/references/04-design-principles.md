# Design Principles: How People See, Think, and Decide

Contents: how viewers actually look · space and functional minimalism · hierarchy · Gestalt grouping · contrast, alignment, balance, rhythm, scale · cognitive load and information density · psychology of trust, desire, urgency, value · decoration vs communication · making it feel human and specific · from principle to prompt

These are tendencies from perception and behavioral research and long design practice, not laws. Use them as defaults, and let the real audience override them.

## 1. How viewers actually look

- **People sample, they do not read.** A promo seen while scrolling gets roughly a glance. The design must work as a *silhouette* first (shapes and masses), then as a headline, then as detail.
- **The eye is pulled by difference:** high contrast, large size, saturated or isolated color, faces and eyes, a sharp edge against calm space. The first fixation lands on the most different element. Make sure that element is your intended hero.
- **Faces and gaze steer attention.** Viewers tend to look where a depicted person looks or points. Aim gaze and gestures *toward* the offer or product, not off the canvas.
- **Reading path is learned.** In left-to-right scripts (Indonesian), the scan tends to start top-left and move down and right. Sparse promo layouts follow a Z-shape (top-left → top-right → diagonal → bottom-right); list-like layouts (menus, price lists) follow an F-shape (headings and left edges get scanned, middles get skipped). Place the CTA where the path ends, usually bottom-right or bottom-center.
- **Mobile screens are small and thumb-framed.** Center and upper-middle are most seen; platform UI covers edges (see formats file). Text that is comfortable on a laptop can be unreadable at phone width.
- **Squint test.** Blur your eyes: you should still see (1) one dominant shape, (2) one headline block, (3) a clear end point. If you see a gray mush or five equal blobs, the hierarchy fails.
- **Three-second test.** A stranger glancing for 3 seconds should answer: What is it? Who is it for? What do I do? Design so the answer survives that glance.

## 2. Space is a design element: whitespace and functional minimalism

**What space does.** Empty space isolates the hero (hierarchy), separates groups (proximity), carries the eye along the reading path, rests the viewer (lower cognitive load), improves legibility, and signals confidence and clarity. A design with no room to breathe looks anxious and cheap, however good each element is.

**Why AI graphics are cramped.** Image models tend to equate "more detail" with "better": they fill every empty area with decoration, props, effects, and extra text. Unless you assign space on purpose, the model will spend it. So in every prompt space is *allocated*, not left over.

**Functional minimalism, not a style.** "Less is more" here means fewer *competing* things, never fewer *needed* things. The test for every element is: if I remove it, does the message, trust, desire, or action get weaker? If not, it goes. Price, offer, contact, deadline, and mandatory legal marks always stay, and they get the space that makes them easy to find. Minimalism is justified by communication and outcome; if a minimalist look hides information or makes a mass-market buyer feel the shop is empty or expensive, it is wrong for this business.

**Calm space is flat space.** A usable empty area is low-detail and low-contrast (flat color, soft gradient of light, quiet wall), so text can sit in it and the hero can stand out against it. Texture, glow, and particles in the empty zone are noise.

**Space budget (starting points, adjust to audience).**

| Context | Calm space | Notes |
|---|---|---|
| Premium, gifts, craft | ~50-60% | Few words, one great image, quiet type |
| Feed or story promo | ~35-45% | One hero, one offer, one action |
| Marketplace banner | ~40-50% | Thumbnail clarity |
| Spanduk / roadside | ~40-60% around the words | Distance needs air |
| Flyer | ~30-40% | Zones with clear gaps |
| Menu, price list, mass-market "ramai" | ~20-30% | Dense is allowed; grouping and gaps between groups must be strict |

**Margins and gaps.** Keep an outer margin of about 6-8% of the shorter side. Make the gap *between* groups clearly larger (about double) than the gap *within* a group. Give the hero clear room around it; crowding the hero is the most common cause of a weak focal point.

**Element budget.** For a feed or story promo, aim for no more than five visible elements besides the background: hero, headline, offer or price, name or logo, action. Decorative elements: zero by default; one only if it is a specificity anchor (a lettering style, a stamp, a real prop).

**Subtraction pass (always, before the plan is final).** List every element planned. For each: remove it, merge it with another, move it to the caption, or shrink it. Prefer removing to shrinking. When in doubt, take it out.

**Audience adjustment.** Some audiences read abundance as value (traditional markets, price-sensitive buyers): allow more density, but keep the structure and the gaps between groups. Others read space as quality (premium, modern, urban professionals): allow more. Decide from the audience, never from taste.

**In the prompt:** state it as an instruction: "Keep about 40% of the canvas calm and empty (flat [color], no texture or detail), mainly [where]. Nothing floats in it. No decorative elements."

## 3. Visual hierarchy: what deserves emphasis

Decide *before* styling. Rank elements:

1. **Primary (1 only):** the thing that delivers the message (the product, the offer, or the headline), never all three equal.
2. **Secondary (max 2):** what makes primary credible or complete (price, proof, name).
3. **Action (1):** the CTA, visually distinct but quieter than primary.
4. **Tertiary:** details, legal, address, fine print: small, calm, grouped.

Ways to create rank, strongest first: **scale, contrast (value), isolation (space around), position, color saturation, weight, and shape**. Using three of these on the primary and one on the rest produces clear order. If an element needs five effects to be noticed, it is probably not the right primary.

How to choose the primary:
- Promo with a strong offer → the offer (price or discount) is primary; product is secondary.
- New or unfamiliar product → the product image is primary; name secondary.
- Trust-sensitive service (laundry, repair, catering) → the promise/proof is primary; contact is the action.
- Brand awareness → the name and one signature visual, minimal text.

## 4. How the brain groups information (Gestalt)

- **Proximity:** things close together are read as related. Put price next to the item it prices; separate unrelated groups with space, not boxes.
- **Similarity:** same color/size/style = same role. Keep all prices one style, all labels one style.
- **Figure-ground:** the subject must separate clearly from background (value contrast, edge, depth). Busy backgrounds behind text destroy this.
- **Continuity:** the eye follows lines, edges, and alignments. Use them to lead from headline to product to CTA.
- **Closure and common region:** a simple shape or panel groups content, but over-boxing every item adds noise. Use a panel only when it improves legibility or grouping.
- **Enclosure for emphasis:** one highlighted badge works; five badges nullify each other.

## 5. Contrast, alignment, balance, rhythm, scale

- **Contrast comes in types:** size, value (light/dark), color temperature, weight, shape, texture, and emptiness. Value contrast does most of the legibility work; hue contrast alone fails for many viewers and in bright sun.
- **Alignment** makes a layout look intentional. Pick one alignment spine (left edge is easiest to read in Indonesian) and hang elements from it. Mixed alignments are a top amateur signal and a top AI signal.
- **Repetition and consistency** (same style for same role) build coherence and brand memory more than any single effect.
- **Balance:** symmetrical = stable, formal, trustworthy, calm (good for services, religious or ceremonial). Asymmetrical = dynamic, modern, energetic, can feel more designed (good for food promos, youth, retail). Choose on purpose; "centered because default" is a slop tell.
- **Rhythm:** a clear beat of big / medium / small and of space / content gives movement. Equal spacing and equal sizes feel static.
- **Scale and proportion:** dramatic scale difference (a huge product, tiny text beside it) creates drama and hierarchy; timid scale difference feels indecisive. Aim for roughly 3:1 or more between primary and secondary text sizes.
- **Space** has its own section (section 2): treat it as an element you budget, not leftovers.

## 6. Cognitive load and information density

- Working memory holds only a few chunks at once (about four). A promo with more than ~4 distinct pieces of information at the same weight overloads.
- **Hick's law:** more choices → slower decisions. One CTA beats three. One channel to order beats five.
- **Chunk and label:** group related facts (menu categories, package tiers), then give the group a clear heading.
- **Density by medium** (see formats file): passing traffic = a few words; scroll = a headline and one offer; menu/catalog = dense but strongly grouped; printed flyer held in hand = more allowed.
- **Remove, then move, then shrink:** first delete the unnecessary; then relocate to caption/second slide; then reduce size. Never solve density by shrinking everything.
- **Distinguish essential vs optional:** essential = name, offer, price, how to act, mandatory legal marks. Optional = slogans, extra benefits, social icons (usually only the one channel they want used), decorative taglines.

## 7. Psychology of trust, desire, urgency, perceived value

- **Processing fluency:** what is easy to read and clean feels more true and more trustworthy. Legibility *is* credibility. Typos and warped text do the opposite fast.
- **Aesthetic-usability effect:** tidy, coherent designs are judged to work better. A cheap product with a coherent design reads as cared-for.
- **Trust signals** that suit small businesses: a real photo of the real product, the owner's face or hands (with consent), a real location cue, a consistent look across posts, concrete proof ("sudah 300+ pelanggan" only if true), official marks (halal, PIRT) placed honestly, clear contact.
- **Desire:** appetite and desire are triggered by *specific* sensory cues (steam, texture, cut-open interiors, hands in action), correct portion and color, and the sense of "I can have this now". Generic gloss does not trigger desire; it triggers suspicion.
- **Perceived value:** large number plus small unit ("55rb"), strikethrough original price next to the new price (anchoring), bundles ("hemat 10rb"), and "mulai dari" help; but price clutter hurts. Premium positioning shows *less* (space, restraint, quiet type), not more.
- **Urgency and scarcity:** work only when real and specific ("sampai Minggu", "sisa 20 porsi"). Fake urgency erodes trust, and viewers have learned to ignore red burst stickers.
- **Social proof:** real reviews or numbers beat adjectives. Never invent testimonials.
- **Von Restorff (isolation) effect:** the one different item gets remembered. Reserve your accent color and your biggest scale for the one thing that matters.
- **Serial position:** the first and last items in a sequence are remembered best: lead with the hero, end with the action.
- **Emotional tone is made of concrete choices:** warm vs cool color, round vs angular shapes, loose vs tight spacing, handmade vs machined texture, close-up vs distance. Name the feeling, then name the choices that create it.

## 8. Decoration vs communication

(Works together with the subtraction pass in section 2.)

Every element is either **carrying meaning** (explains, proves, guides, or evokes the right feeling) or **decoration**. Decoration is not forbidden; unearned decoration is. Test each element:

1. If I removed it, would the viewer lose understanding, trust, desire, or direction?
2. Does it belong to *this* business (its product, place, story), or would it fit any business?
3. Does it compete with the hero for attention?

Answers: no / any business / yes → remove. Sparkles, floating particles, lens flares, random icons, gradient orbs, ornamental frames, stock props that do not match the product are the usual suspects.

## 9. Making it feel intentional, human, and specific

- **Commit to one clear idea** (a concept, not a theme): "satu botol cukup seharian", "mesin cuci kosong, baju bersih besok", "sambal ibu, diulek pagi ini".
- **Use ownable specifics** (specificity anchors): the real product and packaging, local landmark, signature ingredient, hand-painted sign lettering from the neighborhood, local dialect phrase (only if the owner uses it), the owner's hands.
- **Leave a human trace:** natural light and slight imperfection in photos; paper grain or print texture *only* if it fits; hand-lettered or sign-painter type; asymmetry; real materials (banana leaf, kraft paper, enamel plate, rattan).
- **Restraint reads as confidence:** fewer colors, fewer fonts, fewer effects, more decisive scale.
- **Consistency across posts** (same colors, type character, layout grid) is what turns a one-off into a recognizable brand; recommend it.

## 10. From principle to prompt

Your reasoning becomes concrete instructions:

| Decision | How it appears in the prompt |
|---|---|
| Hierarchy | Named elements with size ranks and positions ("headline largest, top-left, 30% of height") |
| Reading path | "Eye path: headline → product → price → WhatsApp line" |
| Contrast | Color roles with values and "light text on dark brown, strong contrast" |
| Balance | "Asymmetric: product left of center, headline right-aligned upper area" |
| Space | "About 40% of the canvas calm and empty, flat color, mainly on the right; nothing floats in it; no decorative elements" |
| Specificity | Concrete subject, props, place, lettering style, material |
| Density | Exact text lines only; "no extra words" |
| Emotion | Light, color temperature, texture, camera distance, expression |
