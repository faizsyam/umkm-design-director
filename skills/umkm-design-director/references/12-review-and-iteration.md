# Review and Iteration (Stage 13)

Contents: when to use · the 12-point review · symptom → prompt fix · one-change rule · when to leave AI and finish in an editor · pre-publish checklist · reviewing a set · reuse

## 1. When to use

The owner returns with a generated image (or describes it) and asks "gimana?", "kok jelek?", or "kok tulisannya salah?". Look at it as a designer would, with their brief in mind, and give a short verdict plus one or two precise fixes. If they send an image, actually inspect it. Never praise by default.

## 2. The 12-point review

Check in this order (functional first, aesthetic last). Items 10-11 apply whenever they are relevant.

1. **Truth:** Does the product look like the real product? Any invented logo, mark, claim, or wrong cultural detail?
2. **Text accuracy:** Name, price, dates, numbers, spelling, no extra or missing words. Character by character.
3. **Physical distance test:** Simulate the intended viewing distance. Shrink the image to represent the physical scale. Is the headline readable? Is the primary element still dominant? Does the design communicate in the available time (1–3 seconds for roadside, 5–15 for foot traffic)?
4. **Hierarchy and reading path:** Is there a single clear hero? Does the eye go headline → hero → price → action?
5. **Legibility:** Contrast (value, not just hue), size at physical scale and viewing distance, text on calm areas.
6. **Message fit:** Does it say the one message from the brief, not three?
7. **Audience/culture fit:** Faces, food, motifs, tone, and register right for the buyers?
8. **Slop tells:** glow, gloss, floating items, filler decoration, generic stock people (use the anti-slop audit).
9. **Brand fit and distinction:** Would it look wrong for a different business (swap test)? Are the USP and the anchors visible?
10. **Space and restraint:** Is there a calm area, clear margins, and gaps between groups? Anything decorative without purpose?
11. **Fidelity to attached images:** product, logo, mascot, person match the originals; existing design improved as agreed.
12. **Physical production readiness:** Correct ratio; text strategy appropriate for the medium; type at a scale that works at the intended viewing distance; outdoor pieces have sufficient value contrast; production note given to owner.

Report in plain language: "3 hal sudah bagus, 2 hal perlu diperbaiki: ..." and give the fixes.

## 3. Symptom → fix

| What you see | Likely cause | One-change fix to the prompt |
|---|---|---|
| Hero looks different from the real product | No reference or weak "keep exactly" | Re-run with the product photo as reference and the keep-exactly sentence; or composite the real photo in an editor |
| Misspelled or garbled text | Too much/small text, unreliable tool | Reduce to fewer, larger lines; or switch to strategy B and add text in an editor |
| Everything the same size | Missing size ranks | State "headline largest at 30% canvas height, price second at 15%, everything else at 8% or smaller" |
| Cluttered with decoration | No exclusion line or vague style | Add specific exclusion list; add "large calm empty area around the hero, about 40% of canvas" |
| Plastic or glossy look | Defaults for lighting/material | Specify "matte, natural window light, visible texture, slight imperfection on surface" |
| Text unreadable in the physical piece | Type too small for viewing distance | Increase headline to 28–35% canvas height; reduce total text to fewer, larger elements |
| Design works on screen but fails printed | Screen scale vs print scale mismatch | Recalculate type sizes as % of canvas height; verify element count matches medium budget |
| Insufficient contrast outdoors | Low value contrast chosen for screen | Add "high value contrast throughout — white or off-white text on deep-toned background; no light-on-light" |
| Too much information for a roadside piece | Content not filtered for viewing duration | Reduce to 3–5 words maximum; move secondary information to a separate flyer |
| Text unreadable on image | Busy background or low contrast | Specify a flat solid panel or calm zone with strong light-on-dark contrast |
| Generic centered layout | Composition not specified | Specify asymmetry with zones and eye path |
| Crowded, every corner filled | Space not allocated | Add "about 40% of the canvas calm and empty, flat color, mainly [where]; no decorative elements" and remove one element |
| Attached image ignored or altered | Role, treatment, or keep-unchanged unclear | Restate the ATTACHED IMAGES block: order, role, "keep exactly", placement and size |
| Colors off-brand or neon | Colors not given | Give hex values and roles for all three palette positions |

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
