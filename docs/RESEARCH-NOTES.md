# Research Notes

Short record of what informed the repository structure and the design of the skill. Use it to judge what to revisit when tools or conventions change.

## Repository and skill conventions (observed in public skill repos)

- A skill is a folder with `SKILL.md` (YAML frontmatter with at least `name` and `description`, then Markdown instructions) plus optional `scripts/`, `references/`, `assets/`. The format is an open standard (agentskills.io) used by Claude and a growing set of other coding/agent tools.
- **Progressive disclosure:** agents load only name + description at startup, the full `SKILL.md` when a task matches, and bundled files only when referenced. Hence: keep `SKILL.md` under about 500 lines, push detail into `references/`, say when to read each, keep references one level deep, and give long reference files a contents line.
- The **description is the trigger.** It must say what the skill does *and* when to use it, in the words real users use; undertriggering is the common failure, so descriptions are written to be a little pushy and to include the user's own phrasing (here, Indonesian).
- Larger collections (Anthropic's `anthropics/skills`, the `obra/superpowers` family, community aggregators) separate: one folder per skill, a `template` skill, a README with install instructions, a marketplace/plugin manifest where distribution matters, and scripts for deterministic work. This repo keeps one skill but follows the same layout so more skills can be added under `skills/`.
- Cross-agent portability: some tools read `skills/`, `.claude/skills/`, or `.github/skills/`; others use `AGENTS.md` for always-on project rules. Skills are for "how to do this task on demand"; `AGENTS.md` is for "how this project works".
- Primary distribution is **general AI chat** (ChatGPT, Claude, Gemini), because the actual users (UMKM owners) are unlikely to use developer tools. That is why `siap-pakai/` ships a full single-file bundle (upload to a chat), a compact version under 8,000 characters (instruction boxes of custom GPTs, Gems, Projects), and a `.skill` file for Claude; developer installs are secondary in the README.

## Anti-slop findings

- Slop is largely **unspecified defaults**: models fall back to the statistically common solution. Generic output follows from missing constraints, not only from model weakness.
- Practitioner guidance converges on: commit to a specific concept and aesthetic before generating; replace adjectives with concrete constraints; supply real reference material; name the defaults you want to avoid *and* the alternative; subtract against a checklist of known tells; iterate from the output, not from vibes.
- Known visual tells are listed in `references/10-anti-slop.md`. Note that telling a model "avoid X" tends to push it to the next most common default, so the skill specifies positive alternatives.

## Image-prompt findings

- Strong prompts for text-bearing graphics specify exact text, language, hierarchy, placement, and font *character*; keep text short; and separate what must be rendered from what must stay untouched (product photos, logos).
- Text rendering has improved across recent image models, yet small text, long text, numbers, and non-English words remain error-prone. The skill therefore treats text as a strategy decision (A in-image, B clean zones, C hybrid) and tells owners to proofread.
- Tool capabilities change quickly; the skill avoids hard-coding model names and asks which tool the owner uses.

## Strategy and system findings

- **Differentiation** is established before any visual choice: USP with proof, customers' reasons, competitor visual territory, desired perception and a "never be", positioning, and personality dials translated into concrete design parameters; validated with a swap test (would a rival's name fit?). Standard brand-strategy practice (positioning statements, laddering, perceptual contrast with competitors) adapted to non-designer owners.
- **Whitespace and functional minimalism** are treated as allocated resources (space budgets, element budgets, a subtraction pass) because image models tend to fill every empty area. Minimalism is justified by communication; required information always stays.
- **Output sets** follow design-system practice: one shared visual system (palette roles, type character, material, device, space level), re-composed per ratio rather than stretched. Because users run prompts in separate chats, each prompt repeats the system verbatim and never references another prompt or its result.
- **Reference images** are handled as design elements: each gets a role, one primary treatment, placement, size, and keep/change rules; numbering is local to each prompt; the handoff lists attachments per prompt.

## Open questions for future versions

- Validate question flow with real UMKM owners; measure where they drop off.
- Add regional archetype packs (e.g. Jawa, Sumatra, Bali, Sulawesi) with local lettering and motif guidance written by people from those places.
- Add a carousel/series mode that outputs a consistent multi-prompt set.
- Add an image-review mode that grades an uploaded result against the 10-point review.
