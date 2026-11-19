# Copilot Instructions for Weather Forecast Demo

## Project purpose
This repository demonstrates how GitHub Copilot AI technologies drive the software delivery lifecycle for a Weather Forecast application. The primary deliverable is the explainable AI-assisted delivery process and evidence. The application is a secondary deliverable used as proof.

## Delivery priorities
1. Prefer clarity, reproducibility, and explainability over cleverness.
2. Keep all AI-assisted work traceable through docs, issues, PRs, logs, and commit history.
3. Whenever implementing functionality, also update the relevant documentation evidence.
4. Break work into small, reviewable steps with explicit acceptance criteria.
5. **Always follow Test-Driven Development (TDD)** — write failing tests first, then implement.

## Technical expectations
- Python backend using FastAPI.
- Simple frontend using HTML/Jinja2/JavaScript.
- Weather forecast retrieval from Open-Meteo API (primary) and wttr.in (secondary).
- REST API with OpenAPI documentation.
- External APIs isolated behind a service layer.
- Do not hardcode secrets; use environment variables.
- Include tests for all critical flows using pytest.

## TDD workflow (mandatory)
Every feature must follow this cycle:
1. Write a failing test that describes the expected behavior.
2. Run the test — confirm it fails.
3. Implement the minimal production code to make the test pass.
4. Run tests — confirm they pass.
5. Refactor if needed while keeping tests green.
6. Commit with evidence of the TDD cycle.

## Implementation behavior
- Before coding, propose a plan.
- Prefer simple, modular architecture.
- Document tradeoffs when choosing libraries or frameworks.
- For every major change, identify:
  - files changed
  - tests added/updated
  - docs updated
  - evidence produced for the Copilot demonstration

## Documentation requirements
Always keep these documents current when relevant:
- docs/copilot-usage-guide.md
- docs/agent-execution-log.md
- docs/mcp-integration-summary.md
- docs/architecture-overview.md
- docs/tdd-workflow-evidence.md

## Output style
- Be explicit and step-by-step.
- When suggesting changes, include rationale.
- When creating plans, map them back to the project requirements.
- Show TDD red-green-refactor evidence in commit messages and logs.
