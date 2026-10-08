# Prompt Skeleton (one per output)

Copy for each output. Fill every block with decisions, not adjectives. The VISUAL SYSTEM block is written once and pasted word for word into every prompt of the set. Each prompt must work alone: no "same as", no mention of other prompts, image numbers local to this prompt.

Target length 200-450 words (up to about 550 with three or more images). Instructions in English; on-image text in the owner's language.

Every sentence must change what the image model produces. No meta-commentary, no process notes, no viewing-context statements that have not been translated into design decisions.

```
FORMAT: [physical material and production purpose — e.g. "Printed roadside spanduk, 3×1 m, vinyl tarpaulin"], [aspect ratio and pixels — e.g. "3:1 (3000×1000 px)"].

CONCEPT: "[campaign idea, same words in every prompt — derived from Distinction Brief]". [Feeling 1] and [feeling 2]. For [specific audience]. This output's job: [hook / inform / act].

[INCLUDE this block ONLY when images are being attached:]
ATTACHED IMAGES (attach in this order):
Image 1 = [what it is, as visible]. Role: [hero / logo / mascot / person / base design / style reference]. Treatment: [keep exactly / cut out and place / clean up / enhance and upscale / illustrate / extend canvas / style-only / revise]. Placement: [zone, anchor, margin]. Size: [about N% of canvas height or width]. Keep unchanged: [...]. May change: [...].
Image 2 = ...
Priority if conflicts: [...].

[OMIT the ATTACHED IMAGES block entirely when there are no images. Write this single line instead:]
No images are attached; create everything from this description.

HERO VISUAL: [specific subject or "Image 1"], [angle and distance], [surface material and named imperfections], [light source, direction, and quality], [texture and physical detail], [one or two ownable specifics].

COMPOSITION: [zones with positions and percentages]. [Alignment spine — symmetrical or asymmetrical, chosen on purpose]. SPACE: about [N]% of the canvas stays calm and empty ([flat color or quiet surface], no texture or detail), mainly [where]; nothing floats in it; no decorative elements. Margins about [6-8]%. Eye path: [A -> B -> C -> D].

[If no logo — add IDENTITY block:]
IDENTITY: Business name "[name]" rendered as [specific type character — e.g. heavy condensed slab-serif caps], [color], [treatment — e.g. inside a full-width panel, stamped-ink look with slight texture], at [position and size]. Below it: "[tagline or subline]" in [smaller type character], [color].

TEXT (render exactly as written, in [language], no additional words):
1. [role] "[exact text]" - [size rank], [type character], [case], [color], [position]
2. ...
[Clean empty zone for text added later (strategy B/C only). Reserved empty square for official marks.]

VISUAL SYSTEM (identical in every prompt of this set):
Palette: [dominant ~60% name+hex]; [support ~30%]; [accent ~10%, used only for ___]. Type: [headline character]; [support character]; [case/weight]. Style and material: [photo/illustration], [named surface texture, finish, light quality]. Image treatment: [how real images are cleaned, cropped, grounded — or if none: how the scene is described]. Device: [one recurring graphic device, or none]. Space level: [calm / moderate / dense-but-grouped].

KEEP / AVOID: Keep [truth constraints]. Avoid [4-6 specific failure modes for this brief — e.g. floating ingredients, glow effects, gradient backgrounds, decorative sparkles, extra invented text, glossy plastic surfaces, stock smiling people].
```

---

## Lampiran (give under each prompt)

```
Prompt N ([name, ratio]):
- Lampirkan [n] gambar, urutannya harus sama:
  1. [file/description] — [role]
  2. ...
- Atau: Tidak ada lampiran.
```

---

## Checklist before sending

**Prompt-level:**
- [ ] Fully standalone — works pasted alone into a fresh chat
- [ ] No "same as", "previous", or cross-prompt references
- [ ] Image numbers local to this prompt only
- [ ] One hero and one action
- [ ] Calm-space line present with percentage and location
- [ ] Exact text quoted, correct, same facts as other prompts
- [ ] ATTACHED IMAGES block present only if images are being attached — omitted entirely otherwise
- [ ] No meta-commentary or process explanations
- [ ] Viewing context translated into design decisions, not pasted as-is
- [ ] No official marks, QR codes, or logos assigned to the model
- [ ] If strategy A chosen: all essential elements (text, branding, pricing, CTA) are fully specified
- [ ] If no logo: IDENTITY block present with named type character, color, and device

**Set-level:**
- [ ] Visual System block word-for-word identical in all prompts
- [ ] Concept line identical in all prompts
- [ ] Same facts (name, price, deadline) across all prompts
- [ ] No prompt depends on another

**Physical print specific:**
- [ ] Headline type size specified as % of canvas height (not in points — model works in proportions)
- [ ] Element count within the budget for the viewing duration (roadside = max 3–4 elements; hand-held = up to 5–6)
- [ ] High value contrast specified for outdoor pieces
- [ ] No text element smaller than the legibility threshold for the intended viewing distance
- [ ] Text strategy B confirmed for: spanduk, menu, phone numbers, addresses, legal marks, menus
- [ ] Production note added to plan (AI output to be upscaled; text/logo added in Canva or printer software)
