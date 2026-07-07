#!/bin/bash
# SessionStart hook for Claude Code on the web.
# CCPlugins is a pure-stdlib Python project (no third-party dependencies),
# so there is nothing to install. This hook verifies the Python toolchain is
# present so the install/verify flow and any tests work out of the box.
set -euo pipefail

# Only run in the remote (Claude Code on the web) environment.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

echo "[session-start] Verifying Python toolchain for CCPlugins..."

if ! command -v python3 >/dev/null 2>&1; then
  echo "[session-start] ERROR: python3 not found on PATH." >&2
  exit 1
fi

python3 --version
echo "[session-start] No third-party dependencies to install (stdlib only)."
echo "[session-start] Environment ready."
