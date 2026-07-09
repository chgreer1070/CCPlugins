#!/usr/bin/env python3
# CCPlugins Uninstaller

"""
CCPlugins Uninstaller
Removes command files from ~/.claude/commands/
"""

import json
import os
import shutil
from pathlib import Path


def load_commands_from_manifest(manifest_path):
    if not manifest_path.exists():
        return None

    try:
        recorded = json.loads(manifest_path.read_text()).get("commands", [])
    except Exception as e:
        print(f"[WARN] Could not read install manifest: {e}")
        return []

    if not isinstance(recorded, list):
        print("[WARN] Install manifest has invalid commands list.")
        return []

    return sorted(cmd for cmd in recorded if isinstance(cmd, str))


def main():
    # Command files to remove (including old ones for compatibility)
    commands = [
        "batch-fix.md",
        "cleanproject.md",
        "cleanup-types.md",  # Old command (removed)
        "commit.md",
        "context-cache.md",  # Old command (removed)
        "contributing.md",
        "create-todos.md",
        "docs.md",
        "explain-like-senior.md",
        "find-todos.md",
        "fix-imports.md",
        "fix-todos.md",
        "format.md",
        "implement.md",
        "make-it-pretty.md",
        "predict-issues.md",
        "remove-comments.md",
        "review.md",
        "scaffold.md",
        "security-scan.md",
        "session-end.md",
        "session-start.md",
        "resume.md",
        "test.md",
        "todos.md",
        "todos-to-issues.md",
        "undo.md",
        "understand.md",
        "refactor.md",
        "validate.md"
    ]

    commands_dir = Path.home() / ".claude" / "commands"
    manifest_path = Path.home() / ".claude" / ".ccplugins_manifest.json"

    recorded_commands = load_commands_from_manifest(manifest_path)
    if recorded_commands is not None:
        commands = recorded_commands
    
    print("CCPlugins Uninstaller")
    print("=" * 40)
    
    if not commands_dir.exists():
        print("[INFO] Commands directory not found. Nothing to uninstall.")
        return
    
    # Count installed commands
    installed = 0
    for cmd in commands:
        if (commands_dir / cmd).exists():
            installed += 1
    
    if installed == 0:
        print("[INFO] No CCPlugins commands found.")
        return
    
    print(f"[FOUND] {installed} CCPlugins commands installed")
    response = input("\nRemove all CCPlugins commands? (y/N): ")
    
    if response.lower() != 'y':
        print("[CANCELLED] Uninstall cancelled.")
        return
    
    # Remove commands
    removed = 0
    for cmd in commands:
        cmd_path = commands_dir / cmd
        if cmd_path.exists():
            try:
                os.remove(cmd_path)
                print(f"  - Removed {cmd}")
                removed += 1
            except Exception as e:
                print(f"  ! Failed to remove {cmd}: {e}")
    
    # Clean up cache and backups if requested
    cache_dir = Path.home() / ".claude" / ".ccplugins_cache"
    backup_dir = Path.home() / ".claude" / ".ccplugins_backups"
    
    if cache_dir.exists() or backup_dir.exists():
        response = input("\nAlso remove cache and backups? (y/N): ")
        if response.lower() == 'y':
            if cache_dir.exists():
                shutil.rmtree(cache_dir)
                print("  - Removed cache directory")
            if backup_dir.exists():
                shutil.rmtree(backup_dir)
                print("  - Removed backups directory")
    
    # Remove the install manifest itself
    if manifest_path.exists():
        try:
            os.remove(manifest_path)
        except Exception:
            pass

    print(f"\n[SUCCESS] Uninstalled {removed} commands")
    print("Thanks for trying CCPlugins!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[CANCELLED] Uninstall cancelled.")
    except Exception as e:
        print(f"\n[ERROR] Uninstall failed: {e}")