#!/bin/bash
# CCPlugins Uninstaller for Mac/Linux

set -e

echo "CCPlugins Uninstaller"
echo "===================="

COMMANDS_DIR="$HOME/.claude/commands"
MANIFEST="$HOME/.claude/.ccplugins_manifest.json"

# List of CCPlugins commands (including old ones for compatibility)
COMMANDS=(
    "batch-fix.md"
    "cleanproject.md"
    "cleanup-types.md"     # Old command (removed)
    "commit.md"
    "context-cache.md"     # Old command (removed)
    "contributing.md"
    "create-todos.md"
    "docs.md"
    "explain-like-senior.md"
    "find-todos.md"
    "fix-imports.md"
    "fix-todos.md"
    "format.md"
    "implement.md"
    "make-it-pretty.md"
    "predict-issues.md"
    "remove-comments.md"
    "review.md"
    "scaffold.md"
    "security-scan.md"
    "session-end.md"
    "session-start.md"
    "resume.md"
    "test.md"
    "todos.md"
    "todos-to-issues.md"
    "undo.md"
    "understand.md"
    "refactor.md"
    "validate.md"
)

if [ -f "$MANIFEST" ]; then
    if ! command -v python3 >/dev/null 2>&1; then
        echo "[ERROR] Install manifest found, but python3 is required to read it safely."
        echo "        Run python3 uninstall.py or remove commands manually from $COMMANDS_DIR."
        exit 1
    fi

    manifest_commands=$(python3 - "$MANIFEST" <<'PY'
import json
import sys
from pathlib import Path

try:
    commands = json.loads(Path(sys.argv[1]).read_text()).get("commands", [])
except Exception as exc:
    print(f"[ERROR] Could not read install manifest: {exc}", file=sys.stderr)
    sys.exit(2)

if not isinstance(commands, list):
    print("[ERROR] Install manifest has invalid commands list.", file=sys.stderr)
    sys.exit(2)

for command in commands:
    if isinstance(command, str):
        print(command)
PY
)

    COMMANDS=()
    while IFS= read -r cmd; do
        [ -n "$cmd" ] && COMMANDS+=("$cmd")
    done <<< "$manifest_commands"
fi

# Count installed commands
INSTALLED=0
for cmd in "${COMMANDS[@]}"; do
    if [ -f "$COMMANDS_DIR/$cmd" ]; then
        INSTALLED=$((INSTALLED + 1))
    fi
done

if [ $INSTALLED -eq 0 ]; then
    echo "[INFO] No CCPlugins commands found."
    exit 0
fi

echo "[FOUND] $INSTALLED CCPlugins commands installed"
read -p "Remove all CCPlugins commands? (y/N): " -n 1 -r
echo

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "[CANCELLED] Uninstall cancelled."
    exit 0
fi

# Remove commands
REMOVED=0
for cmd in "${COMMANDS[@]}"; do
    if [ -f "$COMMANDS_DIR/$cmd" ]; then
        rm "$COMMANDS_DIR/$cmd"
        echo "  - Removed $cmd"
        REMOVED=$((REMOVED + 1))
    fi
done

# Remove the install manifest
rm -f "$HOME/.claude/.ccplugins_manifest.json"

# Clean up cache and backups
CACHE_DIR="$HOME/.claude/.ccplugins_cache"
BACKUP_DIR="$HOME/.claude/.ccplugins_backups"

if [ -d "$CACHE_DIR" ] || [ -d "$BACKUP_DIR" ]; then
    read -p "Also remove cache and backups? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        [ -d "$CACHE_DIR" ] && rm -rf "$CACHE_DIR" && echo "  - Removed cache directory"
        [ -d "$BACKUP_DIR" ] && rm -rf "$BACKUP_DIR" && echo "  - Removed backups directory"
    fi
fi

echo "[SUCCESS] Uninstalled $REMOVED commands"
echo "Thanks for trying CCPlugins!"