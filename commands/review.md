---
description: Multi-agent code review (security, performance, quality, architecture) of your changes
argument-hint: "[path or leave blank for current diff]"
allowed-tools: Read, Grep, Glob, Bash, Task
---

# Code Review

I'll review your code for real problems across four dimensions.

**Scope:** `$ARGUMENTS` if provided, otherwise the current `git diff` and the files it touches. This is a **read-only** analysis — I won't stage, modify, or commit anything, so no checkpoint is needed.

I'll delegate to four specialized sub-agents in parallel, each with isolated context and read-only tools:

- **security-reviewer** — credential exposure, injection, weak validation, insecure config, dependency risk
- **performance-reviewer** — algorithmic blowups, redundant I/O, N+1 queries, blocking hot paths, memory growth
- **quality-reviewer** — complexity, duplication, dead code, error handling, missing test coverage
- **architecture-reviewer** — layer separation, dependency direction, coupling, fix-at-the-right-depth

I invoke these via the Task tool (the `security-reviewer`, `performance-reviewer`, `quality-reviewer`, and `architecture-reviewer` agents ship with this plugin). For a small diff I may run only the relevant ones.

Once they report back, I'll:
1. Merge and de-duplicate findings across the four dimensions.
2. Rank by severity and effort, each with `file:line`, concrete impact, and a specific fix.
3. Drop anything that's pure style with no observable effect.

When there are multiple real issues, I'll track them with TodoWrite so nothing is lost.

After the review I'll ask whether you want to:
- Create GitHub issues for the critical findings, or
- Keep them as a local todo list, or
- Just take the summary report.

This focuses on problems that actually impact reliability and maintainability — not a dissertation.
