---
name: docs
description: Keep project documentation (README, CHANGELOG, API docs, guides) in sync with the code. Use when the user asks to update or review documentation, after implementing a feature or refactor that changes documented behavior, or to audit documentation coverage and freshness.
---

# Documentation Manager

Keep documentation accurate by looking at what actually changed and updating every affected doc — not just one file.

## Approach

1. **Understand the change.** Read the conversation / recent diff to see the real scope (features, API changes, bug fixes, refactors, security/perf changes).
2. **Read the existing docs fully** before editing: `README`, `CHANGELOG`, `docs/**`, `CONTRIBUTING`, guides. Match their style, structure, and tone — never overwrite custom content.
3. **Update everything affected**, in place: README features, CHANGELOG entries (grouped by type, semver-aware), API/endpoint docs, configuration options, migration guides for breaking changes.
4. **Preserve** custom sections (e.g. content between `<!-- CUSTOM:START -->` / `<!-- CUSTOM:END -->`), fix broken internal links, and create a new doc only when one is genuinely missing (e.g. no README).

## Modes

- **Overview** — when asked what docs exist or their state: list every markdown doc with a freshness/coverage read and flag gaps.
- **Update** — the default after code changes: map code reality vs docs and update what drifted. For current architecture, invoke the `architecture-explorer` agent first.
- **Session** — after a long working session: summarize all changes, group by feature/fix/enhancement, and update the appropriate docs.

## Rules

- Read before writing; update in place; never duplicate a section.
- Preserve custom content and the project's existing style.
- No AI attribution, "Generated with Claude" text, or emojis in docs.
- Don't create documentation that isn't needed.

When done, report what changed and ask whether to update everything, focus on specific files, or generate a migration guide.
