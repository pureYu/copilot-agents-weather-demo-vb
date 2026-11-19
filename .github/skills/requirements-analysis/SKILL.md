---
name: requirements-analysis
description: Analyzes requirements, identifies gaps, clarifies ambiguities, and produces implementation plans aligned with project goals.
metadata:
  category: planning
  agentskills-pattern: analytical-workflow
---

# Requirements Analysis Skill

Use this skill when converting requirements into actionable work items, validating scope, or identifying gaps.

## Purpose
Ensure the repository work stays aligned with the documented requirements, especially the distinction between:
- the primary deliverable: evidence of GitHub Copilot AI-assisted delivery
- the secondary deliverable: the working Weather Forecast application

## Instructions
- Read the requirements summary before proposing work.
- Distinguish in-scope work from out-of-scope requests.
- Map tasks back to specific requirement areas when possible.
- Produce observable, testable acceptance criteria.
- Call out assumptions, unknowns, and risk areas.
- Separate MVP tasks from later enhancements.
- Ensure implementation tasks include TDD test specifications.
- Ensure implementation tasks also include documentation and evidence expectations.

## Analysis checklist
For each requirement:
- [ ] Is the requirement clear and unambiguous?
- [ ] Can it be verified with an automated test?
- [ ] Is it in scope per the requirements document?
- [ ] Are there dependencies on other requirements?
- [ ] What are the acceptance criteria?
- [ ] What tests should be written FIRST (TDD)?

## Preferred outputs
- Backlog proposals with TDD test plans
- Milestone breakdowns
- Epic/task decomposition
- Acceptance criteria (testable)
- Dependency analysis
- Implementation sequencing recommendations
- Risk assessment

## Scope boundaries
Always reference Section 3 of REQUIREMENTS_SUMMARY.md:
- **In scope**: Python backend, simple frontend, weather API integration, REST API, agents, skills, instructions, TDD, GitHub App integration
- **Out of scope**: authentication, databases, user accounts, background workers, caching, complex UI, mobile, production deployment, weather history
