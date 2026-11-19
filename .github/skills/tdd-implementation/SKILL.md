---
name: tdd-implementation
description: Enforces strict Test-Driven Development workflow. Ensures tests are written before production code following the Red-Green-Refactor cycle.
metadata:
  category: engineering-standards
  agentskills-pattern: behavioral-constraint
---

# TDD Implementation Skill

Use this skill whenever implementing any feature, endpoint, service, or component.

## Purpose
Ensure all code in this repository is developed using strict Test-Driven Development. This skill shapes agent behavior to always prioritize test design before implementation.

## Behavioral rules

### 1. RED phase — Write failing tests first
- Identify the behavior to implement from the acceptance criteria.
- Write one or more test functions that describe the expected behavior.
- Tests must be specific, isolated, and deterministic.
- Run the test suite — all new tests MUST fail.
- If a test passes without new code, the test is not testing new behavior.

### 2. GREEN phase — Minimal implementation
- Write the smallest amount of production code that makes the failing tests pass.
- Do not add functionality beyond what the tests require.
- Do not optimize or refactor during this phase.
- Run the test suite — all tests MUST pass.

### 3. REFACTOR phase — Improve while green
- Improve code structure, naming, and clarity.
- Remove duplication.
- Ensure tests still pass after every refactoring step.
- Do not add new behavior during refactoring.

## Commit discipline
- Commit after each complete Red-Green-Refactor cycle.
- Use commit messages that indicate the TDD phase:
  - `test: add failing test for <feature>` (RED)
  - `feat: implement <feature> to pass tests` (GREEN)
  - `refactor: improve <component> structure` (REFACTOR)

## Test design standards
- Use pytest as the test framework.
- Use httpx.AsyncClient for API endpoint testing.
- Use unittest.mock or pytest-mock for external service isolation.
- Test file naming: `test_<module>.py`
- Test function naming: `test_<behavior>_<scenario>`
- Each test should test one behavior.
- Include both success and failure scenarios.

## Anti-patterns to prevent
- Writing production code before any test exists.
- Writing tests after implementation is complete.
- Skipping the refactor phase.
- Writing tests that depend on external services without mocking.
- Large implementation steps that span multiple behaviors.
