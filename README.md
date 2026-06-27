

## 🚨 V2 in Development

CCPlugins V2 is currently in active development due to recent Anthropic updates (SDK improvements, native subagents, context memory, and enhanced CLI capabilities). Several slash commands have become redundant as Claude Code CLI now handles them natively.

V2 will be a complete architectural redesign focusing on what Claude Code still can't do efficiently.

**Current version (v1) remains stable and functional.**


[![V2 Teaser](https://raw.githubusercontent.com/brennercruvinel/AutoSauce/99df4833a19bd85aa3058765f2d9a68e89a55685/auto-sauce-brenner-cruvinel-claude-code.png)](https://github.com/brennercruvinel/AutoSauce)

---



```
 ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗     ██████╗ ██████╗ ██████╗ ███████╗
██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║     ██║     ███████║██║   ██║██║  ██║█████╗      ██║     ██║   ██║██║  ██║█████╗  
██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝      ██║     ██║   ██║██║  ██║██╔══╝  
╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗    ╚██████╗╚██████╔╝██████╔╝███████╗
 ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                                         
██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗                               
██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝                               
██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗                               
██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║                               
██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║                               
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝                               
```

# Automate the `Boring Stuff`
![GitHub Repo stars](https://img.shields.io/github/stars/brennercruvinel/CCPlugins?style=social)
[![Version](https://img.shields.io/badge/version-2.5.2-blue.svg)](https://github.com/brennercruvinel/CCPlugins)
[![Claude Code CLI](https://img.shields.io/badge/for-Claude%20Code%20CLI-purple.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Tested on](https://img.shields.io/badge/tested%20on-Opus%204%20%26%20Sonnet%204-orange.svg)](https://claude.ai)
[![Also works with](https://img.shields.io/badge/also%20works%20with-Kimi%20K2-1783ff.svg)](https://github.com/MoonshotAI/Kimi-K2)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/brennercruvinel/CCPlugins/blob/main/CONTRIBUTING.md)

## What is `CCPlugins`?

Professional commands for Claude Code CLI that save 2-3 hours per week on repetitive development tasks.

### The Problem

😊 Ask Claude to fix a bug → Get 15 test files  
😤 Request a simple refactor → Receive a dissertation on clean code  
🤪 "Please add a button" → Complete UI framework rewrite  
😭 Every conversation → "Act like a senior engineer who doesn't overengineer"

**Active Development Notice**: CCPlugins is continuously evolving based on real-world usage. We thoroughly test each command and refine them as we discover gaps and opportunities. This ensures you're always getting battle-tested, production-ready tools that solve actual developer problems.

CCPlugins is a curated set of 16 professional commands (plus specialized subagents, a skill, and a hook) that extend Claude Code CLI with enterprise-grade development workflows. These commands leverage Claude's contextual understanding while providing structured, predictable outcomes optimized for Opus 4 and Sonnet 4 models.

## Quick Links

- [Installation](#installation) - Get started in 30 seconds
- [Commands](#commands) - See all available commands
- [How It Works](#how-it-works) - Understanding the magic
- [Technical Notes](#technical-notes) - Why conversational design matters
- [Contributing](#contributing) - Help make it better

## Installation

### Recommended: install as a plugin

CCPlugins ships as a Claude Code plugin. This is the only method that installs the **full** package — commands **plus** the subagents, skills, and the commit-guard hook — and gives you versioning, clean updates, and namespaced commands (`/ccplugins:*`):

```
/plugin marketplace add brennercruvinel/CCPlugins
/plugin install ccplugins
```

Commands then appear namespaced, e.g. `/ccplugins:refactor`, `/ccplugins:review`.

### Legacy: install scripts (commands only)

The shell/Python installers copy the slash **commands** into `~/.claude/commands/`. They do **not** install the subagents, skills, or hook — use the plugin method above for those.

**Mac/Linux:**
```bash
curl -sSL https://raw.githubusercontent.com/brennercruvinel/CCPlugins/main/install.sh | bash
```

**Windows/Cross-platform (from a clone):**
```bash
git clone https://github.com/brennercruvinel/CCPlugins.git
cd CCPlugins
python install.py
```

### Uninstall
```bash
# Plugin install
/plugin uninstall ccplugins

# Legacy script install
./uninstall.sh        # Mac/Linux
python uninstall.py    # Windows/Cross-platform
```

## Commands
16 professional commands optimized for Claude Code CLI's native capabilities, backed by specialized subagents, a skill, and a hook.

### Development Workflow

```bash
/cleanproject                    # Remove debug artifacts with a non-destructive checkpoint
/format                          # Auto-detect and apply project formatter
/scaffold feature-name           # Generate complete features from patterns
/test                            # Run tests with intelligent failure analysis
/implement url/path/feature      # Import and adapt code from any source with validation phase
/refactor                        # Restructure code (also: refactor pretty | comments for cosmetic cleanups)
/validate                        # Pre-commit gate: build + tests + lint + types in one pass
```

### Code Quality & Security

```bash
/review                # Multi-agent analysis (delegates to security/performance/quality/architecture subagents)
/security-scan         # Vulnerability analysis with tracked, resumable remediation
/predict-issues        # Proactive problem detection with timeline estimates
/fix-imports           # Repair broken imports after refactoring
/batch-fix             # Apply one fix consistently across many files, with preview
/todos                 # Find / create / fix / file TODOs (find | create | fix | to-issues)
```

### Analysis & Workflow

```bash
/contributing          # Complete contribution readiness analysis
/resume                # Find and continue an in-flight CCPlugins session
/undo                  # Safe rollback with git checkpoint restore
```

### Subagents

Shipped under `agents/` and invoked automatically by the commands above (or on demand):

```text
security-reviewer  performance-reviewer  quality-reviewer  architecture-reviewer
architecture-explorer   # map an unfamiliar codebase (replaces the old /understand)
refactor-planner        # produce a safe, ordered refactor plan
```

### Skills

Shipped under `skills/` and invoked automatically when relevant (progressive disclosure):

```text
docs   # keep README/CHANGELOG/API docs in sync with code (replaces the old /docs command)
```

### Hooks

Shipped under `hooks/`: a `PreToolUse` guard blocks any `git commit` that carries AI attribution (Co-Authored-By: Claude, "Generated with Claude Code", claude.ai/code links) — centralizing a rule that used to be copy-pasted into every command body. It only blocks; it never modifies files.

> **Migrating from v1?** `/commit` → native commit · `/session-start` / `/session-end` → native memory + compaction · `/understand` → `architecture-explorer` agent or `/init` · `/find-todos` / `/create-todos` / `/fix-todos` / `/todos-to-issues` → `/todos <find|create|fix|to-issues>` · `/make-it-pretty` → `/refactor pretty` · `/remove-comments` → `/refactor comments` · `/docs` → the `docs` skill (auto-invoked).


## Enhanced Features

### 🔍 Validation & Refinement
Complex commands now include validation phases to ensure completeness:
```bash
/refactor validate   # Find remaining old patterns, verify 100% migration
/implement validate  # Check integration completeness, find loose ends
```

### Extended Thinking
Advanced analysis for complex scenarios:
- **Refactoring**: Deep architectural analysis for large-scale changes
- **Security**: Sophisticated vulnerability detection with chain analysis

### Pragmatic Command Integration
Natural workflow suggestions without over-engineering:
- Suggests `/test` after major changes
- Recommends a commit at logical checkpoints (via native commit)
- Maintains user control, no automatic execution

## Real World Example

### Before `/cleanproject`:
```
src/
├── UserService.js
├── UserService.test.js
├── UserService_backup.js    # Old version
├── debug.log               # Debug output
├── test_temp.js           # Temporary test
└── notes.txt              # Dev notes
```

### After `/cleanproject`:
```
src/
├── UserService.js          # Clean production code
└── UserService.test.js     # Actual tests preserved
```

## 🔧 How It Works

### High-Level Architecture

CCPlugins transforms Claude Code CLI into an intelligent development assistant through a sophisticated yet elegant architecture:

```
Developer → /command → Claude Code CLI → Command Definition → Intelligent Execution
    ↑                                                                       ↓
    ←←←←←←←←←←←←←←←←← Clear Feedback & Results ←←←←←←←←←←←←←←←←←←←
```

### Execution Flow

When you type a command:

1. **Command Loading**: Claude reads the markdown definition from `~/.claude/commands/`
2. **Context Analysis**: Analyzes your project structure, technology stack, and current state
3. **Intelligent Planning**: Creates execution strategy based on your specific situation
4. **Safe Execution**: Performs actions with automatic checkpoints and validation
5. **Clear Feedback**: Provides results, next steps, and any warnings

### Core Architecture Components

**Intelligent Instructions**
- First-person conversational design activates collaborative reasoning
- Strategic thinking sections (`<think>`) for complex decision-making
- Context-aware adaptations without hardcoded assumptions

**Native Tool Integration**
- **Grep**: Lightning-fast pattern matching across codebases
- **Glob**: Intelligent file discovery and project mapping
- **Read**: Content analysis with full context understanding
- **Write**: Safe file modifications with automatic backups
- **TodoWrite**: Progress tracking and task management
- **Task**: Sub-agent orchestration for specialized analysis

**Safety-First Design**
- Automatic git checkpoints before destructive operations
- Session persistence for cross-context continuity
- Rollback capabilities with clear recovery paths
- No AI attribution in commits or generated content

**Universal Compatibility**
- Framework-agnostic with intelligent auto-detection
- Cross-platform support (Windows, Linux, macOS)
- Works with any programming language or stack
- Adapts to your project's conventions and patterns

### Advanced Features

**Session Continuity**
Commands like `/implement` and `/refactor` maintain state across Claude sessions. State lives under `.claude/state/` (gitignored), **never** in your source tree — so plans and progress are never accidentally committed:
```
.claude/state/
├── refactor/        # plan.md + state.json — refactoring roadmap & completed transformations
├── implement/       # plan.md + state.json — implementation progress & decisions
├── fix-imports/     # plan.md + state.json — import fixes & resolution progress
├── security-scan/   # plan.md + state.json — findings & remediation progress
├── scaffold/        # plan.md + state.json — scaffolding plan & created files
└── todos/           # plan.md + state.json — TODO resolution progress
```

**Multi-Agent Architecture**
Complex commands delegate to real subagents (shipped under `agents/`):
- Security analysis agent for vulnerability detection
- Performance optimization agent for bottleneck identification
- Architecture review agent for design pattern analysis
- Code quality agent for maintainability assessment

**Performance Optimizations**
- Reduced verbosity for senior developer efficiency
- Smart caching of project analysis results
- Incremental processing for large codebases
- Parallel execution of independent tasks

##Technical Notes

### Design Philosophy

**Why This Approach Works** (Based on Anthropic's Research):
- **Conversational Commands**: First-person language ("I'll help...") activates Claude's collaborative reasoning
- **Build-Agnostic Instructions**: No hardcoded tools = works everywhere
- **Think Tool Integration**: Strategic thinking improves decisions by 50%+ (Anthropic, 2025)
- **Native Tools Only**: Uses Claude Code's actual capabilities, not imaginary APIs

**Key Principles:**
- **Simplicity > Complexity**: Start simple, add only when proven necessary
- **Context Awareness**: Commands adapt to YOUR project, not vice versa
- **Safety First**: Git checkpoints before any destructive operation
- **Pattern Recognition**: Learn from your codebase, not assumptions

### Technical Architecture

**Native Tool Integration:**
All commands leverage Claude Code CLI's native capabilities:
- Grep tool for efficient pattern matching
- Glob tool for file discovery
- Read tool for content analysis
- TodoWrite for progress tracking
- Sub-agents for specialized analysis

**Safety-First Design:**
```bash
git add -A
git commit -m "Pre-operation checkpoint" || echo "No changes to commit"
```

**Conversational Interface:**
Commands use first-person collaborative language ("I'll analyze your code...") rather than imperative commands, creating a natural partnership interaction that improves model performance.

**Framework Agnostic:**
Intelligent detection without hardcoded assumptions enables universal compatibility across technology stacks.

### User Commands Indicator
Custom commands appear with a `(user)` tag in Claude Code CLI to distinguish them from built-in commands. This is normal and indicates your commands are properly installed.

```
/refactor
    Intelligent code restructuring (user)    ← Your custom command
/help
    Show help                                ← Built-in command
```

## Performance Metrics

| Task | Manual Time | With CCPlugins | Time Saved |
|------|-------------|----------------|------------|
| Security analysis | 45-60 min | 3-5 min | ~50 min |
| Architecture review | 30-45 min | 5-8 min | ~35 min |
| Feature scaffolding | 25-40 min | 2-3 min | ~30 min |
| Git commits | 5-10 min | 30 sec | ~9 min |
| Code cleanup | 20-30 min | 1 min | ~25 min |
| Import fixing | 15-25 min | 1-2 min | ~20 min |
| Code review | 20-30 min | 2-4 min | ~20 min |
| Issue prediction | 60+ min | 5-10 min | ~50 min |
| TODO resolution | 30-45 min | 3-5 min | ~35 min |
| Code adaptation | 40-60 min | 3-5 min | ~45 min |

**Total: 4-5 hours saved per week with professional-grade analysis**

## Requirements

- Claude Code CLI
- Python 3.6+ (for installer)
- Git (for version control commands)

## Advanced Usage

### Creating Custom Commands
Create your own commands by adding markdown files to `~/.claude/commands/`:

```markdown
# My Custom Command

I'll help you with your specific workflow.

[Your instructions here]
```

### Using Arguments
Commands support arguments via `$ARGUMENTS`:

```bash
/mycommand some-file.js
# $ARGUMENTS will contain "some-file.js"
```

### CI/CD Integration
Use commands in automated workflows:

```bash
# Quality pipeline
claude "/security-scan" && claude "/review" && claude "/test"

# Pre-commit validation
claude "/format" && claude "/test"

# Feature development
claude "/scaffold api-users" && claude "/test"

# Complete workflow
claude "/security-scan" && claude "/todos create" && claude "/todos to-issues"

# TODO resolution workflow
claude "/todos find" && claude "/todos fix" && claude "/test"
```

### Manual Workflow Integration
Perfect for development routines:

```bash
# Start of day
claude "/security-scan"

# During development
claude "/scaffold user-management"
claude "/review" 
claude "/format"

# End of day
claude "/test"
```

## Security & Git Instructions

All commands that interact with git include security instructions to prevent AI attribution:

**Commands with git protection:**
- `/scaffold`, `/make-it-pretty`, `/cleanproject`, `/fix-imports`, `/review`, `/security-scan`
- `/contributing`, `/predict-issues`, `/todos`

These commands will NEVER:
- Add "Co-authored-by" or AI signatures
- Include "Generated with Claude Code" messages
- Modify git config or credentials
- Add AI attribution to commits/issues

You can modify these instructions in individual command files if needed.

## Contributing

We welcome contributions that help developers save time. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) file for details.
*Built by a developer tired of typing "please act like a senior engineer" in every conversation.*

## Community

[![Star History Chart](https://api.star-history.com/svg?repos=brennercruvinel/CCPlugins&type=Date)](https://star-history.com/#brennercruvinel/CCPlugins&Date)

---

**Last Updated:** August 2, 2025 (Based on Anthropic Claude Code CLI documentation v2025.08.01)
