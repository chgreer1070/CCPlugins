#!/usr/bin/env python3
# CCPlugins Installer for Windows

"""
CCPlugins Installer
Copies command files to ~/.claude/commands/
"""

import json
import os
import shutil
import sys
from pathlib import Path
from datetime import datetime


def read_version(script_dir):
    """Read the plugin version from .claude-plugin/plugin.json; fallback constant."""
    plugin_json = script_dir / ".claude-plugin" / "plugin.json"
    try:
        return json.loads(plugin_json.read_text()).get("version", "unknown")
    except Exception:
        return "unknown"


def main():
    # Determine paths
    script_dir = Path(__file__).parent.absolute()
    commands_source = script_dir / "commands"
    claude_dir = Path.home() / ".claude"
    commands_dest = claude_dir / "commands"
    
    print("CCPlugins Installer")
    print("=" * 40)
    
    # Check source directory exists
    if not commands_source.exists():
        print(f"[ERROR] Commands directory not found at {commands_source}")
        sys.exit(1)
    
    # Create destination directory
    commands_dest.mkdir(parents=True, exist_ok=True)
    print(f"[OK] Target directory: {commands_dest}")
    
    # Copy command files
    command_files = list(commands_source.glob("*.md"))
    if not command_files:
        print(f"[ERROR] No .md files found in {commands_source}")
        sys.exit(1)
    
    # Check for existing commands
    existing_commands = []
    for file in command_files:
        dest_file = commands_dest / file.name
        if dest_file.exists():
            existing_commands.append(file.name)
    
    if existing_commands:
        print(f"\n[WARNING] Found {len(existing_commands)} existing commands:")
        for cmd in existing_commands:
            print(f"  ! {cmd}")
        
        response = input("\nOverwrite existing commands? (y/N): ")
        if response.lower() != 'y':
            print("[CANCELLED] Installation cancelled.")
            print("Tip: Use uninstall script first to remove old commands.")
            sys.exit(0)
    
    print(f"\n[INSTALL] Installing {len(command_files)} commands:")
    installed = []
    for file in command_files:
        dest_file = commands_dest / file.name
        shutil.copy2(file, dest_file)
        installed.append(file.name)
        print(f"  + {file.name}")

    # Write an install manifest so uninstall removes exactly what we installed,
    # rather than guessing from a hardcoded list (which can delete a user's own
    # same-named command or orphan renamed ones).
    manifest = {
        "version": read_version(script_dir),
        "installed_at": datetime.now().isoformat(timespec="seconds"),
        "commands": sorted(installed),
    }
    manifest_path = claude_dir / ".ccplugins_manifest.json"
    try:
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
        print(f"\n[OK] Wrote manifest: {manifest_path}")
    except Exception as e:
        print(f"\n[WARN] Could not write manifest: {e}")

    print("\n[SUCCESS] Installation complete!")
    print("\nUsage:")
    print("  1. Open Claude Code CLI")
    print("  2. Type / to see available commands")
    print("  3. Use /cleanproject, /refactor, /todos, etc.")
    print("\nTip: These commands will save you 6-8 hours per week!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[ERROR] Installation failed: {e}")
        sys.exit(1)