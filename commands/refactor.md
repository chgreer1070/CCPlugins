---
description: Intelligent code restructuring with validation and resumable sessions
argument-hint: "[scope | pretty | comments | resume | status | new]"
allowed-tools: Read, Grep, Glob, Edit, Bash, Agent
---

# Intelligent Refactoring Engine

I'll help you restructure your code systematically - preserving functionality while improving structure, readability, and maintainability.

Arguments: `$ARGUMENTS` - files, directories, or refactoring scope

**KEY FEATURE: Built-in validation and refinement after EVERY change ensures nothing breaks and no code is left behind. The AI will automatically fix its own mistakes during the refactoring process.**

## Session Intelligence

I'll maintain refactoring continuity across sessions.

**Session files (gitignored, kept out of your source tree):**
- `.claude/state/refactor/plan.md` - Refactoring plan with progress tracking
- `.claude/state/refactor/state.json` - Current state and completed actions

**Auto-Detection:**
- If a session exists under `.claude/state/refactor/`: resume from the last checkpoint
- If not: create a new refactoring plan
- Commands: `resume`, `continue`, `status`, `new`

## Lightweight Polish Modes

For small, behavior-preserving cleanups you don't need the full plan/session machinery. Two quick modes (folded in from the former `/make-it-pretty` and `/remove-comments`):

**`/refactor pretty [path]`** — improve readability without changing behavior:
- Clearer variable/function/file names and consistent conventions
- Simplify complex expressions and deep nesting; group related logic
- Remove dead code and redundancy (DRY)
- Tighten loose/generic types and add missing annotations where the language supports it
- Functionality stays identical; existing tests must still pass

**`/refactor comments [path]`** — strip comments that add no value, keep the ones that do:
- Remove comments that merely restate the code or state the obvious (e.g. `// constructor` above a constructor)
- Preserve comments that explain WHY, document non-obvious behavior or business logic, or carry TODO/FIXME/HACK markers
- I'll show what I plan to remove and apply after you confirm

Both modes snapshot a checkpoint first (a stash, not a commit) and change no behavior. For anything structural, use the full refactor flow below.

## Phase 1: Initial Setup & Analysis

For complex refactors (large-scale architectural changes, dependency untangling, performance-critical paths, legacy modernization), I'll reason carefully about transformation order, risk mitigation, dependency update ordering, and how each step is validated before moving on.

**First, check for an existing session:** look for `.claude/state/refactor/state.json` and `.claude/state/refactor/plan.md`. If present, resume from there; otherwise start a new plan.

For complex, multi-step refactors I delegate the planning to the **refactor-planner** subagent (Agent tool), which inventories every call site and produces a safe, ordered sequence before any code changes.

I'll examine your codebase to identify improvement opportunities:

**Analysis Focus:**
- Code complexity hotspots using **Grep** patterns
- Duplication detection across files
- Architecture inconsistencies
- Test coverage for safe refactoring
- Performance bottlenecks

**Smart Scoping:**
- If specific files provided: Focused analysis
- If directory provided: Recursive analysis
- If no arguments: Strategic project-wide scan

## Phase 2: Refactoring Planning

Based on analysis, I'll create a structured plan:

**Refactoring Categories:**
- **Quick Wins**: Variable renames, method extractions
- **Structural**: Pattern applications, dependency improvements
- **Architectural**: Major reorganizations, module boundaries
- **Performance**: Algorithm optimizations, caching strategies

**Plan Structure:**
I'll create a detailed plan in `.claude/state/refactor/plan.md`:

```markdown
# Refactor Plan - [timestamp]

## Initial State Analysis
- **Current Architecture**: [description of existing patterns]
- **Problem Areas**: [specific issues found]
- **Dependencies**: [external/internal dependencies]
- **Test Coverage**: [current coverage %]

## Refactoring Tasks
[Prioritized list with risk levels]

## Validation Checklist
- [ ] All old patterns removed
- [ ] No broken imports
- [ ] All tests passing
- [ ] Build successful
- [ ] Type checking clean
- [ ] No orphaned code
- [ ] Documentation updated

## De-Para Mapping
| Before | After | Status |
|--------|-------|--------|
| OldService.method() | NewService.method() | Pending |
| /api/v1/* | /api/v2/* | Pending |
```

## Phase 3: Incremental Execution

I'll apply refactorings systematically:

**Execution Order:**
1. Create git checkpoint for safety
2. Apply low-risk improvements first
3. Validate after each change
4. Progress to higher-impact refactorings
5. Update plan with completion status

**Continuous Validation & Refinement:**
After EVERY refactoring change:
1. **Immediate Testing:**
   - Run unit tests for modified files
   - Execute integration tests if applicable
   - Verify no test regressions
   
2. **Deep Comparison:**
   - Compare function outputs before/after
   - Validate API contracts maintained
   - Check for missing edge cases
   - Verify error handling preserved
   
3. **Automated Fixes:**
   - Update broken imports automatically
   - Fix reference errors
   - Adjust type definitions
   - Resolve linting issues
   
4. **Quality Gates:**
   - STOP if tests fail - fix immediately
   - STOP if behavior changes - investigate
   - STOP if performance degrades - optimize
   - Only proceed when 100% validated

5. **Continuous Refinement:**
   - Re-scan for missed patterns
   - Update all related files
   - Clean up orphaned code
   - Document breaking changes

## Phase 4: Pattern Application

I'll apply consistent patterns throughout:

**Pattern Recognition:**
- Identify existing patterns in your code
- Detect anti-patterns to eliminate
- Apply design patterns where beneficial
- Maintain architectural consistency

**Code Improvements:**
- Extract duplicated code into utilities
- Simplify complex functions
- Improve naming for clarity
- Reduce coupling between modules

## Phase 5: Quality Metrics

I'll track refactoring impact:

**Measurable Improvements:**
- Complexity reduction percentages
- Duplication elimination count
- Test coverage maintenance
- Performance benchmarks
- Code readability scores

## Context Continuity

**Session Management:**
When you return and run `/refactor` or `/refactor resume`:
- I'll load existing plan and state
- Display progress summary
- Continue from last checkpoint
- Maintain all refactoring decisions

**Progress Example:**
```
RESUMING REFACTORING SESSION
├── Session: refactor_2025_08_02_1430
├── Progress: 12 of 20 tasks complete
├── Last Action: Extract UserService methods
└── Next: Simplify PaymentProcessor logic

Continuing from checkpoint...
```

## Practical Examples

**Start Refactoring:**
```
/refactor                    # Analyze entire project
/refactor src/components/    # Focus on specific directory
/refactor UserService.ts     # Target single file
```

**Session Control:**
```
/refactor resume    # Continue existing session
/refactor status    # Check progress without continuing
/refactor new       # Start fresh (archives existing)
/refactor validate  # Validate completeness, compare behavior, find loose ends
```

(The former `finish` / `enhance` / `verify` / `complete` subcommands all did the same thing — they're now the single `validate`.)

## Phase 6: Automatic Final Validation & Refinement

**AUTOMATIC EXECUTION:** This phase runs automatically after all refactorings are complete. You can also trigger it manually with `/refactor validate`.

**Final Validation Process:**

**Deep Validation Analysis:**
1. **Coverage Check** - Find all remaining old patterns
2. **Import Verification** - Detect broken or orphaned imports
3. **Build & Test** - Run full build and test suite
4. **Type Checking** - Verify type safety if applicable
5. **Dead Code Detection** - Identify removable legacy code

**De-Para Mapping:**
```
MIGRATION STATUS REPORT
├── Patterns Migrated: 45/48 (94%)
├── Files Updated: 67/70
├── Tests Status: 3 failing
└── Build Status: Passing

PENDING MIGRATIONS:
- src/legacy/UserHelper.js → Still using old pattern
- api/v1/routes.js → Mixed patterns detected
- tests/old-api.test.js → Needs update

SUGGESTED REFINEMENTS:
1. Remove 12 orphaned files
2. Consolidate duplicate utilities
3. Update 3 missed import paths
4. Optimize bundle size (-15KB possible)
```

**Validation Actions:**
- Generate comprehensive de-para documentation
- Create migration guide for team
- Fix remaining issues automatically
- Ensure 100% pattern consistency

## Validation Process (`/refactor validate`)

When you run `/refactor validate` (or after the automatic final phase), I execute these steps:

1. **Deep Original Code Analysis**
   - Analyze EVERY function, method and class in detail
   - Document ALL behaviors, patterns and logic flows
   - Map complete code structure and dependencies
   - Create comprehensive understanding in `.claude/state/refactor/original-analysis.md`

2. **Complete Migration**
   - Apply ALL remaining refactorings
   - Find and fix ALL instances of old patterns
   - Update ALL imports and references
   - Clean up ALL orphaned code

3. **Deep Code-to-Code Comparison**
   - Analyze refactored code line by line
   - Verify EVERY behavior is preserved
   - Check ALL logic paths match original
   - Ensure error handling is identical

4. **Comprehensive Analysis**
   - Line-by-line code comparison
   - Complexity metrics (before/after)
   - Performance benchmarks
   - Memory usage analysis
   - Test coverage verification

5. **Automatic Fixes**
   - Fix ANY behavioral discrepancies
   - Update broken references
   - Resolve type issues
   - Correct import paths

6. **Final Validation**
   - Run full test suite
   - Execute integration tests
   - Verify build passes
   - Ensure 100% behavior preservation

7. **Complete Report**
   - De-para mapping of ALL changes
   - Migration guide for team
   - Risk assessment
   - Rollback instructions if needed

**The result:** a thorough check that nothing was left behind and behavior is preserved, with any remaining discrepancies surfaced and fixed.

## Safety Guarantees

**Protection Measures:**
- Git checkpoints before changes
- Incremental commits at logical points
- Test validation after each step
- Clear rollback strategy

**Important:** I will NEVER:
- Add AI attribution or signatures
- Modify git configuration
- Break working functionality
- Make changes without validation
- Use emojis in commits, PRs, or git-related content

## Command Integration

When appropriate, I may suggest using other commands:
- `/test` - After major refactoring to verify functionality
- Committing at logical checkpoints in the refactoring process (native commit)

## Execution Guarantee

**My workflow ALWAYS follows this order:**

1. **Setup session** - Check/create state files FIRST
2. **Deep analysis** - Use extended thinking for complex scenarios
3. **Write plan** - Document all changes in `.claude/state/refactor/plan.md`
4. **Get confirmation** - Show plan summary before starting
5. **Execute incrementally** - Follow plan with checkpoints
6. **Validate completeness** - Run validation phase when requested

**I will NEVER:**
- Start refactoring without a written plan
- Make changes before complete analysis
- Skip session file creation
- Proceed without showing the plan first

I'll ensure perfect continuity between sessions, always resuming exactly where we left off with full context and decision history.