---
description: Pre-commit gate — run build, tests, lint, and type checks in one pass
argument-hint: "[scope: staged | all | path]"
allowed-tools: Read, Grep, Glob, Bash
---

# Validate

I'll run your project's quality gates in one pass and give you a single go/no-go before you commit. This is the real pre-commit gate (the old `/commit` only described it).

**Scope (`$ARGUMENTS`):** `staged` (default — only what's staged), `all` (whole project), or a path.

## What I check

I detect what your project actually has and run only those — I won't invent commands that don't exist:

1. **Build** — if a build script/target exists (`package.json` scripts, `Makefile`, `pyproject`/`setup`, etc.).
2. **Tests** — the project's test runner, scoped to the changed files where the runner supports it.
3. **Lint** — the configured linter (eslint, ruff, golangci-lint, rubocop, …).
4. **Types** — the type checker if the stack has one (tsc, mypy, etc.).

I find these by reading manifests and config files (`@package.json`, `@pyproject.toml`, `@Makefile`, CI workflows) rather than guessing.

## How I report

I run each gate, capture output, and summarize:

```
VALIDATE
├── build   ✓
├── tests   ✗  3 failing (auth/login_test.ts)
├── lint    ✓
└── types   ✓
→ NO-GO: fix failing tests before committing
```

For failures I show the exact output and the `file:line` where it broke. If everything passes, I say **GO** and stop — I don't commit for you (native commit handles that). If something's missing (no linter configured, say), I note it as skipped rather than failing.

I make no code changes during validation — this is read-and-run only.
