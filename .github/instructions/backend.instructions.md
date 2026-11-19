---
applyTo: "backend/**"
---

# Backend Instructions

## Architecture
- Use a layered architecture: routes → services → providers.
- Weather providers are isolated behind an abstract interface.
- Keep route handlers thin — delegate logic to service layer.
- Use dependency injection via FastAPI's `Depends()`.

## Stack
The backend uses:
- **Framework**: FastAPI (Python 3.11+)
- **HTTP client**: httpx (async, with timeouts)
- **Validation**: Pydantic v2
- **Logging**: structlog with JSON output
- **Testing**: pytest, pytest-asyncio, httpx AsyncClient
- **Package management**: pyproject.toml with pip or uv

## Weather service layer
- Define a `WeatherProvider` protocol/ABC.
- Implement `OpenMeteoProvider` as the primary source.
- Implement `WttrInProvider` as a secondary/fallback source.
- Normalize all provider responses into a canonical `WeatherResponse` model.
- Handle provider failures gracefully (timeout, rate limit, invalid response).

## API design
- `GET /api/weather?city={city}` — retrieve current weather and short forecast.
- `GET /api/health` — health check endpoint.
- Return consistent response envelope: `{"data": ..., "error": null}`.
- Use proper HTTP status codes.
- Auto-generate OpenAPI docs via FastAPI.

## Configuration
- Use environment variables for all configuration.
- Provide sensible defaults for local development.
- Configuration model via Pydantic `BaseSettings`.

## Error handling
- Custom exception handlers for structured error responses.
- Never expose raw stack traces to clients.
- Log errors with structlog for debugging.
- External API failures return 502 with descriptive message.

## Quality
- All code must be developed using TDD (tests first).
- Tests use pytest with async support.
- Mock external HTTP calls in tests using `respx` or `unittest.mock`.
- Use environment variables for secrets and runtime configuration.
- Prefer structured logging and explicit error reporting over silent failure.
