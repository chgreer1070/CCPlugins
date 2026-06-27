---
description: Remove development artifacts and debug files with a non-destructive safety checkpoint
argument-hint: "[path to clean]"
allowed-tools: Read, Grep, Glob, Bash, Edit
---

# Clean Project

I'll help clean up development artifacts while preserving your working code.

I'll start with a non-destructive safety checkpoint. This snapshots your current state (tracked **and** untracked files) into a git stash and immediately restores it, so you get a restore point **without** committing anything to your branch history or bundling unrelated/secret files into a commit:
```bash
# Snapshot working tree into a stash, then restore it so cleanup can proceed.
# Does NOT alter your commit history or current branch.
if git stash push --include-untracked --message "cleanproject checkpoint" >/dev/null 2>&1; then
    git stash apply --index >/dev/null 2>&1 || git stash apply >/dev/null 2>&1
    echo "Checkpoint saved. Restore anytime with: git stash list / git stash apply"
else
    echo "Nothing to checkpoint (clean working tree)"
fi
```

I'll identify cleanup targets using native tools:
- **Glob tool** to find temporary and debug files
- **Grep tool** to detect debug statements in code
- **Read tool** to verify file contents before removal

Critical directories are automatically protected:
- .claude directory (commands and configurations)
- .git directory (version control)
- node_modules, vendor (dependency directories)
- Essential configuration files

When I find multiple items to clean, I'll create a todo list to process them systematically.

I'll show you what will be removed and why before taking action:
- Debug/log files and temporary artifacts
- Failed implementation attempts
- Development-only files
- Debug statements in code

After cleanup, I'll verify project integrity and report what was cleaned.

If any issues occur, I can restore from the stash checkpoint created at the start (`git stash list`, then `git stash apply`).

This keeps only clean, working code while maintaining complete safety.