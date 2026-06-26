# Code Review

I'll review your code for potential issues.

This is a read-only analysis: I will not modify, stage, or commit any files. Your working tree is left exactly as it is, so no safety checkpoint is needed.

I'll use specialized sub-agents for comprehensive analysis:
- **Security sub-agent**: Credential exposure, input validation, vulnerabilities
- **Performance sub-agent**: Bottlenecks, memory issues, optimization opportunities  
- **Quality sub-agent**: Code complexity, maintainability, best practices
- **Architecture sub-agent**: Layer separation, dependency direction, scalability patterns

I'll examine files using the Read and Grep tools to analyze:
1. **Security Issues** - credential exposure, input validation
2. **Logic Problems** - error handling, edge cases  
3. **Performance Concerns** - inefficient patterns, bottlenecks
4. **Code Quality** - complexity, maintainability

When I find multiple issues, I'll create a todo list to address them systematically.

For each issue, I'll:
- Show exact location with file references
- Explain the problem and potential impact
- Provide specific remediation steps
- Prioritize by severity and effort

After review, I'll ask: "Create GitHub issues for critical findings?"
- Yes: I'll create prioritized issues with detailed descriptions
- Todos only: I'll maintain local tracking for resolution
- Summary: I'll provide actionable report

**Important**: I will NEVER:
- Add "Co-authored-by" or any Claude signatures to commits
- Add "Created by Claude" or any AI attribution to issues
- Include "Generated with Claude Code" in any output
- Modify git config or repository settings
- Add any AI/assistant signatures or watermarks
- Use emojis in commits, PRs, issues, or git-related content

This focuses on real problems that impact your application's reliability and maintainability.