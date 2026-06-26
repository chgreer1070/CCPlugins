#!/bin/bash
# CCPlugins Installer for Mac/Linux

set -e
COMMANDS_DIR="$HOME/.claude/commands"
mkdir -p "$COMMANDS_DIR"


# Download commands from GitHub
REPO_URL="https://raw.githubusercontent.com/brennercruvinel/CCPlugins/main/commands"
COMMANDS=(
    "cleanproject.md"
    "contributing.md"
    "docs.md"
    "fix-imports.md"
    "format.md"
    "implement.md"
    "make-it-pretty.md"
    "predict-issues.md"
    "refactor.md"
    "remove-comments.md"
    "review.md"
    "scaffold.md"
    "security-scan.md"
    "test.md"
    "todos.md"
    "undo.md"
)

# Check for existing commands
EXISTING=0
for cmd in "${COMMANDS[@]}"; do
    if [ -f "$COMMANDS_DIR/$cmd" ]; then
        EXISTING=$((EXISTING + 1))
    fi
done

if [ $EXISTING -gt 0 ]; then
    echo "[WARNING] Found $EXISTING existing commands"
    read -p "Overwrite existing commands? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "[CANCELLED] Installation cancelled."
        echo "Tip: Use uninstall script first to remove old commands."
        exit 0
    fi
fi

echo "Downloading commands..."
for cmd in "${COMMANDS[@]}"; do
    # --fail so a 404 returns non-zero instead of writing an HTML error page to the command file
    curl -fsSL "$REPO_URL/$cmd" -o "$COMMANDS_DIR/$cmd"
done
echo "CCPlugins installed to $COMMANDS_DIR"
echo "Type / in Claude Code to see available commands"