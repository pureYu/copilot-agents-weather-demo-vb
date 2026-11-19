---
name: documentation-writer
description: Generates and maintains project documentation following Diátaxis framework principles, recording Copilot AI workflow evidence.
metadata:
  category: documentation
  agentskills-pattern: content-generation
---

# Documentation Writer Skill

Use this skill when creating or updating any project documentation.

## Purpose
Maintain clear, accurate, and consistent documentation that serves both as project documentation and as evidence of the GitHub Copilot AI-assisted development workflow.

## Diátaxis framework
All documentation should be categorized into one of four types:
- **Tutorials**: Learning-oriented, step-by-step guides for newcomers.
- **How-to Guides**: Problem-oriented, steps to solve a specific problem.
- **Reference**: Information-oriented, technical descriptions (API docs, schemas).
- **Explanation**: Understanding-oriented, clarifying design decisions and architecture.

## Documentation standards
- Write in clear, concise, unambiguous language.
- Use Markdown formatting consistently.
- Include code examples for technical documentation.
- Keep documents focused — one topic per document.
- Cross-reference related documents with relative links.
- Use consistent terminology across all documents.

## Required documents for this project
| Document | Type | Purpose |
|----------|------|---------|
| README.md | How-to | Quick start and project overview |
| docs/architecture-overview.md | Explanation | System design decisions |
| docs/copilot-usage-guide.md | Explanation | How Copilot was used |
| docs/agent-execution-log.md | Reference | Evidence log of agent interactions |
| docs/mcp-integration-summary.md | Explanation | MCP server usage |
| docs/tdd-workflow-evidence.md | Reference | TDD cycle evidence |
| docs/skills-overview.md | Explanation | How skills shape behavior |
| docs/setup-guide.md | Tutorial | Local development setup |
| docs/api-reference.md | Reference | API endpoint documentation |

## Evidence recording rules
When recording Copilot AI workflow evidence:
- Note which Copilot capability was used (agent, skill, MCP, chat).
- Capture the objective and outcome.
- Record files created or modified.
- Note how the result was validated.
- Be factual — avoid marketing language.
- Include timestamps and agent names.

## Template for agent execution log entries
```markdown
### [Date] — [Task Title]

**Agent**: [agent name]
**Skills used**: [skill names]
**Objective**: [what was requested]
**Outcome**: [what was produced]
**Files changed**: [list]
**Validation**: [how it was verified]
**TDD evidence**: [RED/GREEN/REFACTOR notes]
```
