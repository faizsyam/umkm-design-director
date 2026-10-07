#!/usr/bin/env python3
"""Validate the skill structure: frontmatter, naming, size limits, and reference links.

Usage: python scripts/validate.py [skill_dir]
"""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
skill_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "skills" / "umkm-design-director"
errors, warnings = [], []

skill_md = skill_dir / "SKILL.md"
if not skill_md.exists():
    sys.exit(f"ERROR: {skill_md} not found")

text = skill_md.read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    sys.exit("ERROR: SKILL.md has no YAML frontmatter")
fm = m.group(1)

try:
    import yaml
    meta = yaml.safe_load(fm)
except ImportError:
    meta = None
    warnings.append("pyyaml not installed: frontmatter parsed loosely (pip install pyyaml)")
except Exception as exc:
    sys.exit(f"ERROR: frontmatter is not valid YAML: {exc}")

if meta is None:
    name_v = (re.search(r"^name:\s*(.+)$", fm, re.M) or [None, None])[1]
    desc_v = ""
else:
    name_v = meta.get("name")
    desc_v = meta.get("description") or ""

if not name_v:
    errors.append("missing name")
else:
    n = str(name_v).strip()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", n) or len(n) > 64:
        errors.append(f"invalid name: {n}")
    if n != skill_dir.name:
        errors.append(f"name '{n}' must match folder '{skill_dir.name}'")
if meta is not None:
    if not desc_v:
        errors.append("missing description")
    elif len(desc_v) > 1024:
        errors.append(f"description has {len(desc_v)} characters (limit 1024)")

lines = text.count("\n") + 1
if lines > 500:
    errors.append(f"SKILL.md has {lines} lines (limit 500)")

for ref in sorted(set(re.findall(r"`((?:references|assets)/[^`\s]+)`", text))):
    if not (skill_dir / ref).exists():
        errors.append(f"broken reference: {ref}")

# every numbered reference file mentioned anywhere in the skill must exist
existing = {f.name for f in (skill_dir / "references").glob("*.md")}
for f in list(skill_dir.rglob("*.md")):
    for name in set(re.findall(r"(?<!examples/)\b(\d{2}-[a-z-]+\.md)\b", f.read_text(encoding="utf-8"))):
        if name not in existing:
            errors.append(f"{f.relative_to(skill_dir)} mentions missing file {name}")

# compact instruction-box version must fit common 8,000-character limits
ringkas = root / "siap-pakai" / "umkm-design-director-ringkas.md"
if ringkas.exists():
    n = len(ringkas.read_text(encoding="utf-8"))
    print(f"ringkas: {n} characters")
    if n >= 8000:
        errors.append(f"ringkas has {n} characters (limit 8000)")

# worked examples: prompts in a set must be standalone and share an identical Visual System
for ex in sorted((root / "examples").glob("*.md")):
    doc = ex.read_text(encoding="utf-8")
    blocks = re.findall(r"```\n(FORMAT.*?)\n```", doc, flags=re.S)
    systems = [re.search(r"VISUAL SYSTEM \(identical.*?\n.*?(?=\n\n|$)", b, flags=re.S) for b in blocks]
    systems = [s.group(0) for s in systems if s]
    if len(systems) > 1 and len(set(systems)) != 1:
        errors.append(f"{ex.name}: Visual System differs between prompts")
    for b in blocks:
        low = b.lower()
        for bad in ("same as", "previous prompt", "prompt 1", "as before", "from the first"):
            if bad in low:
                errors.append(f"{ex.name}: prompt refers to another prompt ('{bad}')")

for f in (skill_dir / "references").glob("*.md"):
    n_lines = f.read_text(encoding="utf-8").count("\n")
    if n_lines > 300 and "Contents:" not in f.read_text(encoding="utf-8")[:600]:
        warnings.append(f"{f.name}: >300 lines without a contents line")

print(f"SKILL.md: {lines} lines")
for w in warnings:
    print("WARN:", w)
for e in errors:
    print("ERROR:", e)
if errors:
    sys.exit(1)
print("OK: skill is valid")
