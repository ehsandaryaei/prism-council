#!/usr/bin/env python3
"""Repository consistency checks for Prism Council.

Complements `agentskills validate` from skills-ref (frontmatter/spec checks) with checks the
spec tool does not cover: README install commands, local links, and size.
Standard library only. Exit code 1 on any failure.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "prism-council"
SKILL_MD = SKILL_DIR / "SKILL.md"
REPO = "ehsandaryaei/prism-council"
PRIMARY_INSTALL = (
    f"npx skills add {REPO} --skill prism-council "
    "--agent claude-code codex cursor gemini-cli github-copilot --global --yes"
)

errors = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


# 1. SKILL.md basics beyond the spec validator.
skill_text = SKILL_MD.read_text(encoding="utf-8")
fm = frontmatter(skill_text)
check(fm is not None, "SKILL.md: missing YAML frontmatter")
if fm:
    name = fm.get("name", "")
    desc = fm.get("description", "")
    check(name == SKILL_DIR.name, f"SKILL.md: name '{name}' != directory '{SKILL_DIR.name}'")
    check(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name or "") is not None, f"SKILL.md: invalid name '{name}'")
    check(0 < len(desc) <= 1024, f"SKILL.md: description length {len(desc)} not in 1..1024")
    check(REPO in skill_text, "SKILL.md: metadata.repository does not point at the public repo")
check(len(skill_text.splitlines()) < 500, "SKILL.md: over 500 lines")

# 2. The primary install command appears in both README languages.
readme = (ROOT / "README.md").read_text(encoding="utf-8")
fa_start = readme.find('<a id="fa"></a>')
check(fa_start > 0, "README.md: Persian section anchor <a id=\"fa\"></a> missing")
english, persian = readme[:fa_start], readme[fa_start:]
check(PRIMARY_INSTALL in english, "README.md: primary install command missing from English section")
check(PRIMARY_INSTALL in persian, "README.md: primary install command missing from Persian section")
en_cmds = sorted(set(re.findall(r"^npx skills .*$", english, re.M)))
fa_cmds = sorted(set(re.findall(r"^npx skills .*$", persian, re.M)))
check(en_cmds == fa_cmds, f"README.md: English/Persian npx commands differ:\n  en={en_cmds}\n  fa={fa_cmds}")
for cmd in en_cmds:
    if " add " in cmd or cmd.startswith("npx skills update") or cmd.startswith("npx skills remove"):
        check(REPO in cmd or "prism-council" in cmd, f"README.md: command does not name this skill: {cmd}")

# 3. Relative links in Markdown files resolve.
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"^(https?:|mailto:|#)", target):
            continue
        path = (md.parent / target.split("#")[0]).resolve()
        check(path.exists(), f"{md.relative_to(ROOT)}: broken link -> {target}")

if errors:
    print("FAIL")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("OK: all repository checks passed")
