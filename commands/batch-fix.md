---
description: Apply one fix consistently across many files, with a preview before writing
argument-hint: "<description of the change, or a path scope>"
allowed-tools: Read, Grep, Glob, Edit, Bash
---

# Batch Fix

I'll apply a single, well-defined change consistently across every place it occurs — the thing a per-file hook can't do because it can't see the whole set at once.

**What to fix (`$ARGUMENTS`):** describe the change (e.g. "replace the deprecated `logger.warn` calls with `logger.warning`") and optionally a path scope.

## How I work

1. **Find every occurrence.** I Grep the codebase for the pattern and read enough context around each hit to tell true matches from look-alikes. I report the full list — no silent sampling or top-N truncation.
2. **Deduplicate & group.** I group the sites by the shape of the change so identical edits are applied identically, and I flag the ones that need a judgment call separately from the mechanical ones.
3. **Preview before writing.** I show you the grouped plan — N mechanical edits across M files, plus any that need review — and wait for your go-ahead. Nothing is written until you confirm.
4. **Apply consistently.** I make the edits, keeping each group uniform, and skip anything ambiguous (surfacing it for you to decide rather than guessing).
5. **Verify.** After applying, I re-grep to confirm zero stragglers and suggest `/validate` to confirm nothing broke.

If the change turns out to be more than a mechanical sweep (it needs real per-site reasoning or a structural change), I'll tell you and recommend `/refactor` instead — batch-fix is for consistent, repeatable edits, not redesign.
