#!/usr/bin/env python3
"""Bundle the skill into ONE markdown file for general AI chat interfaces without skill support
(ChatGPT, Claude, Gemini: upload it at the start of a chat, or store it as project/GPT/Gem knowledge).

Usage: python scripts/bundle.py [output_path]
"""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
skill_dir = root / "skills" / "umkm-design-director"
out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "siap-pakai" / "umkm-design-director-lengkap.md"
out.parent.mkdir(parents=True, exist_ok=True)

def strip_frontmatter(t: str) -> str:
    return re.sub(r"^---\n.*?\n---\n", "", t, count=1, flags=re.S)

parts = [
    "# UMKM Design Director (all-in-one)\n",
    "INSTRUCTIONS FOR THE AI: Follow the workflow below with the user. As soon as you have read this file, greet the user and begin at Stage 0 in their language (Indonesian by default). "
    "Reference sections later in this file replace the `references/` and `assets/` files mentioned in the workflow.\n",
    strip_frontmatter((skill_dir / "SKILL.md").read_text(encoding="utf-8")),
]
for sub in ("references", "assets"):
    for f in sorted((skill_dir / sub).glob("*.md")):
        parts.append(f"\n\n---\n\n<!-- FILE: {sub}/{f.name} -->\n\n" + f.read_text(encoding="utf-8"))

out.write_text("\n".join(parts), encoding="utf-8")
print(f"Wrote {out} ({out.stat().st_size // 1024} KB)")
