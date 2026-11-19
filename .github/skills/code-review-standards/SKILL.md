---
name: code-review-standards
description: Enforces Python best practices, API consistency, readability, and maintainability standards during code review.
metadata:
  category: quality-assurance
  agentskills-pattern: verification-checklist
---

# Code Review Standards Skill

Use this skill when reviewing code changes, pull requests, or implementation outputs.

## Purpose
Ensure all code in this repository meets consistent quality standards for readability, maintainability, Python best practices, and API consistency.

## Python standards

### Style and formatting
- Follow PEP 8 naming conventions.
- Use type hints for function parameters and return values.
- Use docstrings for public functions and classes (Google style).
- Maximum function length: 20 lines of logic (excluding docstrings).
- Maximum file length: 300 lines (split if larger).

### Architecture standards
- External APIs must be accessed through a service layer abstraction.
- Configuration must come from environment variables, never hardcoded.
- Use dependency injection via FastAPI's `Depends()`.
- Models/schemas use Pydantic v2 with explicit field definitions.
- HTTP clients use httpx with proper timeout configuration.

### Error handling
- All API endpoints return structured error responses (not raw exceptions).
- Use custom exception classes for domain errors.
- External API failures are handled gracefully with fallback behavior.
- Log errors with structured logging (structlog).

### API consistency
- RESTful endpoint naming (plural nouns, not verbs).
- Consistent response envelope: `{"data": ..., "error": null}` or `{"data": null, "error": {...}}`.
- HTTP status codes used correctly (200, 201, 400, 404, 500, 502).
- OpenAPI documentation auto-generated via FastAPI.

## Review severity levels
- **Blocking**: Security issues, missing tests, broken functionality, hardcoded secrets.
- **Non-blocking**: Style inconsistencies, minor naming issues, missing docstrings.
- **Suggestion**: Alternative approaches, performance improvements, code simplification.

## TDD compliance check
During review, verify:
- Tests exist for the changed code.
- Tests cover both success and failure paths.
- Tests were committed before or alongside implementation.
- Test names clearly describe the behavior being tested.
- Mocks are used for external service calls.

## Review output format
- Summary verdict (approved / needs changes / blocked)
- Findings with severity and location
- TDD compliance status
- Positives (what was done well)
- Required actions before merge
