#!/usr/bin/env python3
"""CCPlugins PreToolUse hook: block git commits that carry AI attribution.

Reads the PreToolUse payload from stdin. If the Bash command creates a git
commit whose *message* contains AI/assistant attribution (a Co-Authored-By:
Claude trailer, "Generated with Claude Code", a claude.ai/code link, etc.),
it exits with code 2 to block the call and tells Claude to remove the
attribution.

Design notes:
- It scans the commit MESSAGE, not the whole command line, so a legitimate
  commit that merely mentions Claude/Anthropic in its subject is not blocked.
- It understands `-m/--message`, `-F/--file <path>` (reads the file), and
  heredoc bodies (`git commit -F - <<'EOF' ... EOF`).
- It only acts on an actual `git commit` invocation, not `git config
  commit.template` or `git log --grep commit`.
- It fails OPEN: any parsing/IO error results in exit 0 (never block a real
  commit because of a hook bug). The only non-zero exit is a confirmed match.
- `-C/--reuse-message`/`--amend -C` reuse a message the hook cannot see from
  the command alone; those are not inspected (documented limitation).

It only blocks — it never modifies files or commits anything.
"""
import json
import os
import re
import shlex
import sys


# Patterns are matched against the COMMIT MESSAGE only, case-insensitive,
# multiline. They are anchored to attribution-shaped text to avoid blocking a
# commit that merely mentions Claude/Anthropic in passing.
ATTRIBUTION_PATTERNS = [
    re.compile(r"^\s*co-authored-by:\s*.*\b(claude|anthropic|copilot|cursor|assistant)\b", re.I | re.M),
    re.compile(r"\bgenerated\s+(?:with|by)\b.*\bclaude\b", re.I),
    re.compile(r"\U0001f916\s*generated", re.I),            # 🤖 generated ...
    re.compile(r"https?://\S*claude\.ai/code", re.I),       # attribution link form
    re.compile(r"\b(?:written|authored)\s+by\s+claude\b", re.I),
]

# Long options that take the commit message (or a file containing it).
MESSAGE_OPTS = {"-m", "--message"}
FILE_OPTS = {"-F", "--file"}


def is_git_commit(tokens):
    """True if the token list is an actual `git commit` invocation."""
    try:
        i = next(idx for idx, t in enumerate(tokens) if t == "git" or t.endswith("/git"))
    except StopIteration:
        return False
    # Skip git's global options (e.g. -C <dir>, -c key=val, --git-dir=...).
    j = i + 1
    while j < len(tokens):
        tok = tokens[j]
        if tok in ("-C", "-c", "--git-dir", "--work-tree", "--namespace"):
            j += 2            # option + its value
            continue
        if tok.startswith("-"):
            j += 1            # --git-dir=... style or other global flag
            continue
        return tok == "commit"   # first non-flag token is the subcommand
    return False


def collect_message(tokens, raw_command):
    """Gather all candidate commit-message text from the command."""
    parts = []

    # 1) -m/--message values and -F/--file file contents.
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        key, _, inline = tok.partition("=")
        if key in MESSAGE_OPTS:
            if inline:
                parts.append(inline)
            elif i + 1 < len(tokens):
                parts.append(tokens[i + 1]); i += 1
        elif key in FILE_OPTS:
            path = inline if inline else (tokens[i + 1] if i + 1 < len(tokens) else "")
            if not inline and i + 1 < len(tokens):
                i += 1
            if path and path != "-":
                try:
                    with open(os.path.expanduser(path), "r", errors="ignore") as fh:
                        parts.append(fh.read())
                except Exception:
                    pass      # fail open — unreadable file isn't a block
        i += 1

    # 2) Heredoc bodies (git commit -F - <<'EOF' ... EOF / <<EOF ... EOF).
    for m in re.finditer(r"<<-?\s*['\"]?(\w+)['\"]?\n(.*?)\n[ \t]*\1\b", raw_command, re.S):
        parts.append(m.group(2))

    return "\n".join(parts)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    if data.get("tool_name") != "Bash":
        sys.exit(0)

    command = (data.get("tool_input") or {}).get("command", "")
    if not command or "commit" not in command:
        sys.exit(0)

    try:
        tokens = shlex.split(command)
    except Exception:
        sys.exit(0)           # unparseable shell — don't block

    if not is_git_commit(tokens):
        sys.exit(0)

    message = collect_message(tokens, command)
    if not message:
        sys.exit(0)           # nothing inspectable (e.g. -C, or interactive editor)

    for pattern in ATTRIBUTION_PATTERNS:
        if pattern.search(message):
            sys.stderr.write(
                "Blocked by CCPlugins: this git commit message contains "
                "AI/assistant attribution.\nCCPlugins keeps commits free of AI "
                "signatures. Remove the attribution (e.g. a 'Co-Authored-By: "
                "Claude' trailer, a 'Generated with Claude Code' line, or a "
                "claude.ai/code link) and commit again.\n"
            )
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
