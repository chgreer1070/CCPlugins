---
description: Find and continue an in-flight CCPlugins session (refactor, implement, scaffold, …)
argument-hint: "[command name to resume, or blank to list all]"
allowed-tools: Read, Grep, Glob, Bash
---

# Resume

I'll find any in-progress CCPlugins work and offer to pick it back up — so you don't have to remember which command you left mid-flight.

## How it works

I scan `.claude/state/` for session folders left by the stateful commands (`refactor/`, `implement/`, `scaffold/`, `fix-imports/`, `security-scan/`, `todos/`). For each one I find, I read its `state.json` and `plan.md` and show you where it stands:

```
IN-FLIGHT SESSIONS (.claude/state/)
├── refactor/    12/18 steps done — last: extract PaymentService
├── implement/   plan ready, 0 applied — "import stripe checkout flow"
└── todos/       8/23 resolved — next: src/api/auth.js:42
```

If you passed a command name in `$ARGUMENTS` (e.g. `/resume refactor`), I go straight to that session. Otherwise I list everything and ask which to continue.

## Continuing

Once you pick one, I hand back to the owning command's resume path — reading its plan, showing completion stats, and continuing from the last checkpoint with all prior decisions intact. If a session looks stale or finished, I'll say so and offer to clear it rather than resuming into nothing.

I only read state here; I don't modify code until you've chosen a session to continue.
