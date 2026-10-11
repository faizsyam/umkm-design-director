# Prompt Skeleton (one per output)

Copy for each output. Fill every block with decisions, not adjectives. The VISUAL SYSTEM block is written once and pasted word for word into every prompt of the set. Each prompt must work alone: no "same as", no mention of other prompts, image numbers local to this prompt.

Target length 200-450 words (up to about 550 with three or more images). Instructions in English; on-image text in the owner's language.

Every sentence must change what the image model produces. No meta-commentary, no process notes, no viewing-context statements that have not been translated into design decisions.

```
FORMAT: [physical medium, e.g. "Printed roadside banner, 3×1 m, vinyl tarpaulin"], [aspect ratio and px, e.g. "3:1 (3000×1000 px)"].

OBJECTIVE: [one sentence — what this specific output must accomplish for the viewer].

CONCEPT: "[campaign idea, same words in every prompt of a set — derived from Distinction Brief]". [Feeling 1] and [feeling 2]. For [specific audience].

CONTENT:
- [Primary message / headline — exact text quoted verbatim]
- [Key supporting text — exact text quoted verbatim]
- [Product or service]
- [Brand identity — logo or identity treatment]
- [Any important visual elements or motifs]
- [All copy and graphic elements rendered directly into final artwork — no blank reserved text zones]

CREATIVE DIRECTION: [The visual concept, personality, mood, aesthetic world, emotional character, and overall feeling the design should project. Derived from the business and informed by 14-visual-language.md and 15-creative-direction-framework.md — not generic style language. 3-6 sentences.]

DESIGN CHARACTER: [What makes this design specifically belong to this business — the ownable visual idea, USP expressed visually, specificity anchors, and what would distinguish it from a competitor using the same format. 2-4 sentences.]

HERO VISUAL: [What the dominant visual element is. Physically specific — not "a dish" but the real thing with its real character. If a photo is attached, say to use it exactly. If generated, describe what it should look like: subject, lighting quality, surface, material feel, angle, texture, what makes it honest and specific rather than generic.]

[If no logo — add LOGO / IDENTITY block:]
LOGO / IDENTITY: Business name "[name]" rendered in [specific type character — weight, personality, feel, case], [color], [device / treatment — e.g. inside a full-width panel, stamp mark, etc.].

VISUAL SYSTEM (identical in every prompt of this set):
Type: [headline character — weight, personality, case]; [support character]. Style and material: [photo/illustration, texture, finish, light quality]. Image treatment: [how real photos are handled]. Device: [one recurring graphic element, or none]. Space level: [calm / moderate / dense-but-grouped].

[ATTACHED IMAGES — include ONLY if images are being attached. Omit this block entirely when there are none:]
ATTACHED IMAGES (attach in this order):
Image 1 = [what it is]. Role: [hero / brand mark / style reference]. Treatment: [keep exactly / clean up / integrate]. Keep unchanged: [...]. May change: [...].
Image 2 = ...
Priority if conflicts: [...].

EXCLUSIONS: Keep [truth constraints]. Avoid [4-8 specific failure modes for this brief — concrete, not generic].
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
- [ ] Creative Direction Summary existed before writing this prompt
- [ ] Fully standalone — works pasted alone into a fresh chat
- [ ] No "same as", "previous", or cross-prompt references
- [ ] FORMAT block present with physical medium and aspect ratio
- [ ] OBJECTIVE block present with specific viewer communication task
- [ ] CONCEPT block present and identical across set
- [ ] CONTENT block lists what must appear, with exact quoted text
- [ ] CREATIVE DIRECTION block describes visual world, mood, personality — business-derived, not generic adjectives
- [ ] DESIGN CHARACTER block specifies what makes this design belong specifically to this business (swap test passed)
- [ ] HERO VISUAL described with physical specificity (subject, lighting, surface, texture, honesty)
- [ ] If no logo: LOGO / IDENTITY block present with named type character, color, and device
- [ ] VISUAL SYSTEM block word-for-word identical in all prompts of the set
- [ ] ATTACHED IMAGES block present only if images are being attached — omitted entirely otherwise
- [ ] EXCLUSIONS block has 4-8 specific prohibitions for this brief
- [ ] No meta-commentary, process explanations, or layout coordinate micromanagement
- [ ] Viewing context translated into design character, not pasted as-is
- [ ] No fake regulatory certificates or functional QR codes invented; graphic badges kept clean
- [ ] Final artwork confirmed: all text quoted verbatim for complete in-image rendering without reserved text zones (unless user specifically requested a blank template)

**Set-level:**
- [ ] Visual System block word-for-word identical in all prompts
- [ ] Concept line identical in all prompts
- [ ] Same facts (name, price, deadline) across all prompts
- [ ] No prompt depends on another

**Physical print specific:**
- [ ] Physical medium and viewing conditions reflected in design character (scale, contrast, simplicity level)
- [ ] High value contrast specified for outdoor pieces
- [ ] Final artwork verified: complete in-image typography and layout; no post-edits required
- [ ] Typographic scale verified for physical viewing distance
