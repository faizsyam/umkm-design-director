# Contributing

Thank you for helping UMKM owners design better. Useful contributions:

- **Real sessions:** anonymized conversations where the skill asked a confusing question, missed a key variable, or produced a prompt that gave slop. Add as `examples/NN-name.md`.
- **Archetypes:** new business types in `references/07-business-archetypes.md` (trust drivers, hero, composition, palette/type, anchors, slop traps). Local, specific knowledge is the most valuable.
- **Cultural notes:** corrections or regional additions in `references/05-color-and-culture.md`. State the region and, where possible, how you know.
- **Evals:** new cases in `evals/evals.json` (realistic user messages, observable assertions).
- **Tool notes:** what actually works (text rendering, reference images, aspect ratios) in specific image tools. Date your observations; tools change.

## Ground rules

1. Keep `SKILL.md` under 500 lines; move detail into `references/` and link it with a "read when" hint.
2. Explain *why* in instructions instead of piling up MUSTs.
3. Every question the skill asks must change a design decision.
4. No instructions that make the model fabricate official marks, certifications, testimonials, or misrepresent a product.
5. Do not add living artists' names or competitor brands as style instructions.
6. Prompts in a set must be standalone and share an identical Visual System block; no cross-prompt references.
7. Keep `siap-pakai/umkm-design-director-ringkas.md` under 8,000 characters and rebuild the full bundle (`python scripts/bundle.py`) after changing the skill.
8. Run `python scripts/validate.py` before opening a pull request.

## Folder conventions

`skills/<skill-name>/SKILL.md` (folder name equals the `name` field), optional `references/`, `assets/`, `scripts/`. File references stay one level deep from `SKILL.md`.
