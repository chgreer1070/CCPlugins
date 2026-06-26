---
description: Find, create, resolve, or file TODOs — one command, four modes
argument-hint: "<find | create | fix | to-issues> [path or focus]"
allowed-tools: Read, Grep, Glob, Edit, Bash, Task
---

# TODOs

I'll work with the TODO/FIXME/HACK markers in your codebase. The first argument selects the mode; the rest scopes it.

**Routing `$ARGUMENTS`:**
- `find` — locate and prioritize existing task markers (default if no mode given)
- `create` — write new, contextual TODO comments based on findings
- `fix` — resolve existing TODOs, with resumable progress
- `to-issues` — convert TODOs into GitHub issues

Resolution/scan state, when persisted, lives in `.claude/state/todos/` (gitignored) — never the repo root.

---

## `find`

I'll Grep for `TODO|FIXME|HACK|XXX|NOTE` (case-insensitive) across source files, scoped to `$ARGUMENTS` if a path was given. For each marker I'll show `file:line`, the full comment, and enough surrounding code to understand it. I'll group results with TodoWrite by priority:
- **Critical** — `FIXME`, `HACK`, `XXX`
- **Important** — `TODO`
- **Informational** — `NOTE`

I'll also flag markers that point at missing implementations, stubbed functions, or incomplete error handling. Then I'll offer to `fix` them or convert them `to-issues`.

## `create`

I'll write actionable TODO comments anchored to real issues — typically findings from a prior `/ccplugins:review`, `/ccplugins:security-scan`, or `/ccplugins:test` run **that actually happened in this session** (if none did, I'll say so and scan instead of inventing context). Before writing, I'll check your conventions: existing TODO style (`[Security]` vs `(SECURITY)`), comment syntax (`//`, `#`, `/* */`), ticket-reference patterns, and linter line limits. Each TODO is placed where the work belongs (near the vulnerable code, the bottleneck, the failing path) and references its source. I won't flood files with comments or write vague, non-actionable notes.

## `fix`

I'll resolve TODOs systematically with session continuity.

**State:** `.claude/state/todos/plan.md` (the TODO list + resolution status) and `.claude/state/todos/state.json` (progress). On start I check for an existing session under `.claude/state/todos/` and resume from the last TODO; otherwise I scan, categorize, and create a plan. Sub-modes: `resume`, `status`, `new`.

I'll categorize (quick-fix / feature / refactor / security / performance), then resolve in priority order (security → bugs → simple improvements → features → performance), matching your existing error-handling, validation, and naming patterns. One optional git checkpoint up front (I won't auto-commit your whole tree mid-run); after each fix I verify functionality and update the plan. I never delete a TODO without implementing it. After critical fixes I'll suggest `/ccplugins:test`.

## `to-issues`

I'll convert TODOs into well-formed GitHub issues matching your project's conventions.

I'll read what shapes a good issue here: `README`, `CONTRIBUTING`, `.github/ISSUE_TEMPLATE/*`, existing labels and milestones. For forks, I'll inspect upstream guidelines **without mutating local refs**:
```bash
git remote get-url upstream >/dev/null 2>&1 && git fetch upstream 2>/dev/null || true
```
I won't gate issue creation on build/test/lint passing — failing tests are often *why* a TODO exists, and filing the issue shouldn't be blocked by them. I'll classify each TODO (bug / enhancement / documentation / performance / security / tech-debt / chore), group related ones, write a clear title + body with a link to the exact `file:line`, and apply only labels that already exist in the repo (I'll verify, not invent). I prefer the GitHub MCP tools where available, falling back to `gh`. I'll show a summary of everything created and respect rate limits.

---

I won't add AI attribution, "Generated with Claude" text, or emojis to any comment, commit, or issue.
