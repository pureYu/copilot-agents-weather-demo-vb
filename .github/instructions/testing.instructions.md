---
applyTo: "tests/**,**/test_*.py,**/*_test.py"
---

# Testing Instructions

## TDD is mandatory
All tests in this project follow Test-Driven Development. Tests are written BEFORE the production code they verify.

## Test framework
- Use pytest as the primary test framework.
- Use pytest-asyncio for async test functions.
- Use httpx.AsyncClient for API endpoint testing.
- Use respx or unittest.mock for mocking external HTTP calls.

## Test organization
```
tests/
├── test_weather_service.py      # Service layer tests
├── test_weather_providers.py    # Provider abstraction tests
├── test_api_endpoints.py        # API route tests
├── test_models.py               # Pydantic model tests
└── conftest.py                  # Shared fixtures
```

## Test naming convention
- File: `test_<module>.py`
- Function: `test_<behavior>_<scenario>`
- Examples:
  - `test_get_weather_returns_temperature_for_valid_city`
  - `test_get_weather_returns_error_for_unknown_city`
  - `test_provider_handles_timeout_gracefully`

## Test design principles
- Each test tests ONE behavior.
- Tests are independent — no shared mutable state.
- Tests are deterministic — no network calls, no randomness.
- External services are always mocked.
- Use fixtures for common test setup.
- Include both happy path and error scenarios.

## Fixtures pattern
```python
@pytest.fixture
def mock_weather_response():
    return {"temperature": 22.5, "description": "Sunny", ...}

@pytest.fixture
async def client(app):
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c
```

## Coverage expectations
- Service layer: high coverage (success, failure, edge cases)
- API endpoints: all routes tested (valid input, invalid input, errors)
- Weather providers: mocked responses for all scenarios
- Models: validation edge cases

## Anti-patterns to avoid
- Tests that require network access.
- Tests that depend on execution order.
- Tests with unclear assertions (`assert result is not None`).
- Tests that test implementation details instead of behavior.
- Overly broad tests that verify multiple behaviors at once.
