#!/usr/bin/env python3
"""Static validation for the CCPlugins plugin — run in CI and locally.

Checks:
  1. All JSON manifests parse.
  2. Every command / agent / skill has valid YAML frontmatter with the
     fields that surface make it usable.
  3. install.sh's hardcoded COMMANDS array matches the actual commands/ dir.

Exits non-zero (with a list of problems) on any failure.
Requires PyYAML.
"""
import glob
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
problems = []


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---\n"):
        return None, "missing YAML frontmatter (must start with '---')"
    end = text.find("\n---", 4)
    if end == -1:
        return None, "unterminated frontmatter (no closing '---')"
    try:
        return yaml.safe_load(text[4:end]) or {}, None
    except yaml.YAMLError as e:
        return None, f"invalid YAML: {e}"


def require(meta, path, keys):
    for k in keys:
        if not (isinstance(meta, dict) and meta.get(k)):
            problems.append(f"{path}: frontmatter missing required '{k}'")


# 1. JSON manifests
for rel in [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", "hooks/hooks.json"]:
    p = os.path.join(ROOT, rel)
    try:
        json.load(open(p, encoding="utf-8"))
    except Exception as e:
        problems.append(f"{rel}: invalid JSON: {e}")

# 2. Frontmatter
for p in sorted(glob.glob(os.path.join(ROOT, "commands", "*.md"))):
    meta, err = frontmatter(p)
    if err:
        problems.append(f"commands/{os.path.basename(p)}: {err}")
    else:
        require(meta, f"commands/{os.path.basename(p)}", ["description"])

for p in sorted(glob.glob(os.path.join(ROOT, "agents", "*.md"))):
    meta, err = frontmatter(p)
    if err:
        problems.append(f"agents/{os.path.basename(p)}: {err}")
    else:
        require(meta, f"agents/{os.path.basename(p)}", ["name", "description"])

for p in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))):
    meta, err = frontmatter(p)
    if err:
        problems.append(f"skills/.../{os.path.basename(p)}: {err}")
    else:
        require(meta, f"{os.path.relpath(p, ROOT)}", ["description"])

# 3. install.sh COMMANDS array == commands/ dir
sh = open(os.path.join(ROOT, "install.sh"), encoding="utf-8").read()
m = re.search(r"COMMANDS=\((.*?)\)", sh, re.S)
listed = set(re.findall(r'"([a-zA-Z0-9_-]+\.md)"', m.group(1))) if m else set()
actual = {os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "commands", "*.md"))}
if listed != actual:
    missing = actual - listed
    extra = listed - actual
    if missing:
        problems.append(f"install.sh COMMANDS missing: {sorted(missing)}")
    if extra:
        problems.append(f"install.sh COMMANDS lists non-existent: {sorted(extra)}")

if problems:
    print("VALIDATION FAILED:")
    for p in problems:
        print(f"  - {p}")
    sys.exit(1)
print(f"Validation passed: {len(actual)} commands, manifests + frontmatter OK.")
