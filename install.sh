#!/bin/bash
# CCPlugins Installer for Mac/Linux

set -e
COMMANDS_DIR="$HOME/.claude/commands"
MANIFEST="$HOME/.claude/.ccplugins_manifest.json"
VERSION="2.6.0"
mkdir -p "$COMMANDS_DIR"

# Prefer local files when run from a clone (consistent bytes with install.py);
# otherwise download from GitHub. This avoids the divergence where install.sh
# pulled floating main while install.py copied the local checkout.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || echo "")"
LOCAL_COMMANDS="$SCRIPT_DIR/commands"
REPO_URL="https://raw.githubusercontent.com/brennercruvinel/CCPlugins/main/commands"

COMMANDS=(
    "batch-fix.md"
    "cleanproject.md"
    "contributing.md"
    "fix-imports.md"
    "format.md"
    "implement.md"
    "predict-issues.md"
    "refactor.md"
    "resume.md"
    "review.md"
    "scaffold.md"
    "security-scan.md"
    "test.md"
    "todos.md"
    "undo.md"
    "validate.md"
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

echo "Installing commands..."
for cmd in "${COMMANDS[@]}"; do
    if [ -f "$LOCAL_COMMANDS/$cmd" ]; then
        cp "$LOCAL_COMMANDS/$cmd" "$COMMANDS_DIR/$cmd"
    else
        # --fail so a 404 returns non-zero instead of writing an HTML error page
        curl -fsSL "$REPO_URL/$cmd" -o "$COMMANDS_DIR/$cmd"
    fi
done

# Write an install manifest so uninstall removes exactly what we installed.
{
    echo "{"
    echo "  \"version\": \"$VERSION\","
    echo "  \"commands\": ["
    last=$((${#COMMANDS[@]} - 1))
    for i in "${!COMMANDS[@]}"; do
        sep=","
        [ "$i" -eq "$last" ] && sep=""
        echo "    \"${COMMANDS[$i]}\"$sep"
    done
    echo "  ]"
    echo "}"
} > "$MANIFEST"

echo "CCPlugins installed to $COMMANDS_DIR"
echo "Type / in Claude Code to see available commands"
