#!/usr/bin/env python3
"""CCPlugins PreToolUse hook: block git commits that carry AI attribution.

Reads the PreToolUse payload from stdin. If the Bash command is creating a
git commit whose text contains AI/assistant attribution (Co-Authored-By:
Claude, "Generated with Claude Code", a claude.ai/code link, etc.), it exits
with code 2 to block the call and tells Claude to remove the attribution.

This centralizes the anti-attribution rule that used to be copy-pasted into
every git-related command body. It only blocks — it never modifies files or
commits anything.
"""
import json
import re
import sys


ATTRIBUTION_PATTERNS = [
    r"co-authored-by:\s*claude",
    r"co-authored-by:[^\n]*anthropic",
    r"generated with\s*\[?\s*claude",
    r"\U0001f916\s*generated with",   # 🤖 generated with
    r"claude\.ai/code",
    r"written by claude",
    r"authored by claude",
]


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        # Can't parse the payload — fail open, never block on our own error.
        sys.exit(0)

    if data.get("tool_name") != "Bash":
        sys.exit(0)

    command = (data.get("tool_input") or {}).get("command", "")
    if not command:
        sys.exit(0)

    # Only inspect commands that actually create a git commit.
    if not re.search(r"\bgit\b[^\n]*\bcommit\b", command):
        sys.exit(0)

    lowered = command.lower()
    for pattern in ATTRIBUTION_PATTERNS:
        if re.search(pattern, lowered):
            sys.stderr.write(
                "Blocked by CCPlugins: this git commit contains AI/assistant "
                "attribution.\nCCPlugins keeps commits free of AI signatures. "
                "Remove the attribution (e.g. a 'Co-Authored-By: Claude' trailer, "
                "a 'Generated with Claude Code' line, or a claude.ai/code link) "
                "and commit again.\n"
            )
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
