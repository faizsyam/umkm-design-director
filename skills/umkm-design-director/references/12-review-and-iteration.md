# Review and Iteration (Stage 10)

Contents: when to use · the 12-point review · symptom → prompt fix · one-change rule · when to leave AI and finish in an editor · pre-publish checklist · reviewing a set · reuse

## 1. When to use

The owner returns with a generated image (or describes it) and asks "gimana?", "kok jelek?", or "kok tulisannya salah?". Look at it as a designer would, with their brief in mind, and give a short verdict plus one or two precise fixes. If they send an image, actually inspect it. Never praise by default.

## 2. The 12-point review

Check in this order (functional first, aesthetic last). Items 10-11 apply whenever they are relevant.

1. **Truth:** Does the product look like the real product? Any invented logo, mark, claim, or wrong cultural detail?
2. **Text accuracy:** Name, price, dates, numbers, spelling, no extra or missing words. Character by character.
3. **Three-second test:** What is it, who is it for, what do I do?
4. **Hierarchy and reading path:** Is there a single clear hero? Does the eye go headline → hero → price → action?
5. **Legibility:** Contrast, size at phone width, text on calm areas.
6. **Message fit:** Does it say the one message from the brief, not three?
7. **Audience/culture fit:** Faces, food, motifs, tone, and register right for the buyers?
8. **Slop tells:** glow, gloss, floating items, filler decoration, generic stock people (use the anti-slop audit).
9. **Brand fit and distinction:** Would it look wrong for a different business (swap test)? Are the USP and the anchors visible?
10. **Space and restraint:** Is there a calm area, clear margins, and gaps between groups? Anything decorative that does not carry meaning? Would the message survive removing one more element?
11. **Fidelity to attached images:** product, logo, mascot, person match the originals; nothing altered or invented; existing design improved as agreed.
12. **Medium fit:** Correct ratio, safe zones, density; print-ready or at least upscalable?

Report in plain language: "3 hal sudah bagus, 2 hal perlu diperbaiki: ..." and give the fixes.

## 3. Symptom → fix

| What you see | Likely cause | One-change fix to the prompt |
|---|---|---|
| Hero looks different from the real product | No reference or weak "keep exactly" | Re-run with the product photo as reference and the keep-exactly sentence; or composite the real photo in an editor |
| Misspelled or garbled text | Too much/small text, unreliable tool | Reduce to fewer, larger lines; or switch to strategy B/C and add text in an editor |
| Everything the same size | Missing size ranks | State "headline largest, price second, everything else at 1/4 the headline size" |
| Cluttered with decoration | No exclusion line or vague style | Add a specific exclusion list; add "large calm empty area around the hero" |
| Plastic or glossy look | Defaults for lighting/material | Specify "matte, natural window light, visible texture, slight imperfection" |
| Text unreadable on image | Busy background or low contrast | Specify a flat panel or calm zone with strong light-on-dark contrast |
| Generic centered layout | Composition not specified | Specify asymmetry with zones and eye path |
| Crowded, every corner filled | Space not allocated | Add "about 40% of the canvas calm and empty, flat color, mainly [where]; no decorative elements" and remove one element |
| Attached image ignored or altered | Role, treatment, or keep-unchanged unclear | Restate the ATTACHED IMAGES block: order, role, "keep exactly", placement and size; or composite in an editor |
| Colors off-brand or neon | Colors not given | Give hex values and roles |
| Wrong people (faces, clothing) | No description | Describe specific age, clothing, setting; or remove people / use real photo |
| Wrong ratio/cropping | Ratio ignored | Set ratio in the tool interface; restate in the prompt; check safe zones |
| Feels cold or off-mood | Light/color/temperature unspecified | Specify the warm or cool light, surface material, and two feelings |
| Elements floating or unrealistic | Missing grounding | "Everything rests on the counter; nothing floats" |
| Style wanders between variations | No consistent system | Reuse skeleton; reference the earlier image as style reference |

## 4. One-change rule

Change **one major thing per iteration** (e.g. only the text zone, or only the light, or only the composition). Changing everything at once makes it impossible to learn what worked and often reintroduces earlier problems. When the tool supports in-conversation editing, phrase the fix as an edit: "Keep everything the same, but make the headline larger and move the price below the bottle."

Stop after 3-5 rounds on the same problem. If it persists, change tactics (switch text strategy, composite in an editor, simplify the brief).

## 5. When to leave the AI and finish in an editor

Use Canva or a similar editor when:
- Text must be exact and large (spanduk, menu, phone numbers, addresses).
- The product must be the real product (composite the real photo).
- Logo, halal/PIRT/BPOM marks, QR codes are needed.
- Several posts need identical layout and type.
- Print requires proper bleed and resolution.

A good workflow: AI makes the **background and mood**; the owner adds **exact text, logo, and official marks** on top.

## 6. Pre-publish checklist (give to the owner)

- [ ] Nama usaha, harga, tanggal, nomor WA/alamat sudah benar (cek huruf demi huruf)
- [ ] Produk di gambar sama dengan produk asli
- [ ] Logo halal/PIRT/BPOM resmi (jika perlu) sudah ditempel dengan benar
- [ ] Tidak ada klaim yang tidak bisa dibuktikan ("terlaris", "nomor 1", testimoni)
- [ ] Tulisan terbaca di layar HP kecil dan di bawah sinar matahari
- [ ] Foto orang: sudah izin
- [ ] Format sesuai platform (story tidak terpotong, feed tidak terpotong)
- [ ] Caption berisi detail tambahan (alamat lengkap, syarat, jam buka)

## 7. Reviewing a set of outputs

When several outputs were made from one set of prompts, review each one, then put them side by side:

- **Family check:** same palette roles, type character, material and light, graphic device, and space feeling? Layouts may differ because the ratios differ.
- **Message check:** same facts everywhere (name, offer, price, deadline), each output with one job.
- **Fix at the right level:** if the family drifts, tighten the Visual System block and regenerate; if one output is wrong, change only that prompt. Because prompts are standalone, an edited prompt never needs the others.
- **Optional consistency booster:** if one result is clearly right, the owner may attach it as an extra *style-only* image in a regenerated prompt (state it in that prompt's ATTACHED IMAGES block). This is a repair step, never a requirement of the original set.

## 8. Reuse

After a good result, help the owner save:
- the **final prompt** (as their template),
- the **style note** (palette with roles, type character, layout skeleton, device, photographic style),
- the **text list** with changeable parts marked.

Next time they only change content (offer, date, product), keeping the same system so their posts look like one recognizable brand.
