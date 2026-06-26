---
description: Security scan with tracked, resumable remediation across sessions
argument-hint: "[path | focus area | resume | status | new]"
allowed-tools: Read, Grep, Glob, Bash, Edit, Task
---

# Security Analysis

I'll perform comprehensive security analysis with tracking and remediation continuity across sessions.

Arguments: `$ARGUMENTS` - specific paths or security focus areas

For the detection pass I delegate to the **security-reviewer** sub-agent (Task tool) — it runs in isolated context with read-only tools and returns ranked findings. This command then owns what the agent does not: prioritizing, applying fixes, and tracking remediation progress across sessions.

## Session Intelligence

I'll maintain security remediation progress:

**Session Files (kept OUT of your project tree):**
- `.claude/state/security-scan/plan.md` - All vulnerabilities and fixes
- `.claude/state/security-scan/state.json` - Remediation progress

**IMPORTANT:** Session files are stored under `.claude/state/security-scan/`, never in your project root. This vulnerability list is a sensitive, exploitable inventory — it must not land where `git add` could stage and push it. Ensure `.claude/state/` is gitignored (I'll add it if missing).

**Auto-Detection:**
- If session exists: Show fixed vs pending vulnerabilities
- If no session: Perform new security scan
- Commands: `resume`, `status`, `new`

## Phase 1: Security Assessment

### Extended Thinking for Security Analysis

For complex security scenarios, I'll use extended thinking to identify sophisticated vulnerabilities:

<think>
When analyzing security:
- Attack vectors that aren't immediately obvious
- Chain vulnerabilities that individually seem harmless
- Business logic flaws that enable exploitation
- Timing attacks and race conditions
- Supply chain vulnerabilities in dependencies
- Architectural weaknesses that enable lateral movement
</think>

**Triggers for Extended Analysis:**
- Authentication and authorization systems
- Financial transaction processing
- Cryptographic implementations
- Multi-tenant architectures
- API security boundaries

**MANDATORY FIRST STEPS:**
1. Check if `.claude/state/security-scan/` directory exists
2. If directory exists, check for session files:
   - Look for `.claude/state/security-scan/state.json`
   - Look for `.claude/state/security-scan/plan.md`
   - If found, resume from existing session
3. If no directory or session exists:
   - Ensure `.claude/state/` is gitignored, then create `.claude/state/security-scan/`
   - Perform full security scan
   - Create vulnerability report
   - Initialize tracking
4. Show risk summary before remediation

**Note:** Always store session files under `.claude/state/security-scan/`, never in the project root or at absolute paths. The plan contains exploitable vulnerability details and must stay out of the committed tree.

I'll analyze security across dimensions:

**Vulnerability Detection:**
- Hardcoded secrets and credentials
- Dependency vulnerabilities
- Insecure configurations
- Input validation issues
- Authentication weaknesses

**Risk Categorization:**
- **Critical**: Immediate exploitation possible
- **High**: Serious vulnerabilities
- **Medium**: Should be addressed
- **Low**: Best practice improvements

## Phase 2: Remediation Planning

Based on findings, I'll create remediation plan:

**Priority Order:**
1. Critical credential exposures
2. High-risk vulnerabilities
3. Dependency updates
4. Configuration hardening
5. Code pattern improvements

I'll write this plan to `.claude/state/security-scan/plan.md` with:
- Each vulnerability details
- Risk assessment
- Remediation approach
- Verification method

## Phase 3: Intelligent Remediation

I'll fix vulnerabilities appropriately:

**Remediation Patterns:**
- Secrets → Environment variables
- Hardcoded values → Configuration files
- Weak validation → Strong patterns
- Outdated deps → Safe updates

**Safe Practices:**
- Never log sensitive data
- Use secure defaults
- Apply principle of least privilege
- Implement defense in depth

## Phase 4: Incremental Fixing

I'll remediate systematically:

**Execution Process:**
1. Create git checkpoint
2. Fix vulnerability safely
3. Verify fix doesn't break functionality
4. Update plan with completion
5. Move to next vulnerability

**Progress Tracking:**
- Mark each fix in plan
- Update state with decisions
- Create security-focused commits

## Phase 5: Verification

After each remediation:
- Test functionality preserved
- Verify vulnerability resolved
- Check for new issues introduced
- Update security documentation

## Context Continuity

**Session Resume:**
When you return and run `/security-scan` or `/security-scan resume`:
- Load vulnerability list and progress
- Show remediation statistics
- Continue from last fix
- Maintain fix decisions

**Progress Example:**
```
RESUMING SECURITY REMEDIATION
├── Total Vulnerabilities: 23
├── Fixed: 15 (65%)
├── Critical: 0 remaining
├── High: 3 remaining
└── Next: SQL injection in UserQuery

Continuing remediation...
```

## Practical Examples

**Start Scanning:**
```
/security-scan                # Full project scan
/security-scan src/api/       # Focus on API
/security-scan "credentials"  # Credential focus
```

**Session Control:**
```
/security-scan resume    # Continue remediation
/security-scan status    # Check progress
/security-scan new       # Fresh scan
```

## Safety Guarantees

**Protection Measures:**
- Git checkpoint before fixes
- Functionality preservation
- No security regression
- Clear audit trail

**Important:** I will NEVER:
- Expose secrets in commits
- Break existing security
- Add AI attribution
- Log sensitive data

## Command Integration

When appropriate for critical security fixes:
- `/test` - Verify functionality after security patches
- `/commit` - Create security-focused commits with proper messages

## What I'll Actually Do

1. **Deep analysis** - Use extended thinking for complex threats
2. **Scan thoroughly** - Find all vulnerabilities
3. **Prioritize wisely** - Critical issues first
4. **Fix safely** - Preserve functionality
5. **Track completely** - Perfect continuity
6. **Verify constantly** - Ensure security improved

I'll maintain complete continuity between sessions, always resuming exactly where we left off with full remediation context.