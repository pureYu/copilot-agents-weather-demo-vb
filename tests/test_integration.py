"""End-to-end integration tests — written FIRST per TDD (RED phase).

Orchestrator delegation: Executor Agent validates full application flow.
Requirement: §7.4 — Testability; §10 — Acceptance Criteria
Issue: #8
Skills: tdd-implementation, code-review-standards
Instructions: testing.instructions.md
"""

import pytest
from unittest.mock import MagicMock, patch


@pytest.mark.asyncio
async def test_full_weather_flow_returns_complete_response(client):
    """Full flow: GET /api/weather should return all fields in response envelope."""
    from unittest.mock import AsyncMock as AMock
    from backend.models.weather import WeatherResponse

    mock_response = WeatherResponse(
        city="Berlin",
        temperature=22.0,
        description="Mainly clear",
        humidity=55,
        wind_speed=9.5,
        forecast="Mainly clear, Partly cloudy, Overcast",
    )

    with patch("backend.main.get_weather_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.get_weather = AMock(return_value=mock_response)
        mock_get_service.return_value = mock_service

        response = await client.get("/api/weather", params={"city": "Berlin"})

    assert response.status_code == 200
    data = response.json()

    # Verify envelope structure
    assert "data" in data
    assert "error" in data
    assert data["error"] is None

    # Verify all required weather fields
    weather = data["data"]
    assert weather["city"] == "Berlin"
    assert isinstance(weather["temperature"], (int, float))
    assert isinstance(weather["description"], str)
    assert isinstance(weather["humidity"], int)
    assert isinstance(weather["wind_speed"], (int, float))
    assert "forecast" in weather


@pytest.mark.asyncio
async def test_openapi_docs_accessible(client):
    """OpenAPI documentation should be auto-generated and accessible."""
    response = await client.get("/docs")
    # FastAPI redirects /docs to the Swagger UI
    assert response.status_code in (200, 307)


@pytest.mark.asyncio
async def test_openapi_json_schema_accessible(client):
    """OpenAPI JSON schema should be available at /openapi.json."""
    response = await client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert "paths" in schema
    assert "/api/weather" in schema["paths"]
    assert "/api/health" in schema["paths"]


@pytest.mark.asyncio
async def test_frontend_and_api_coexist(client):
    """Frontend (/) and API (/api/weather) should both be accessible."""
    # Frontend
    frontend_response = await client.get("/")
    assert frontend_response.status_code == 200
    assert "text/html" in frontend_response.headers["content-type"]

    # API health
    api_response = await client.get("/api/health")
    assert api_response.status_code == 200
    assert api_response.json()["status"] == "healthy"


@pytest.mark.asyncio
async def test_weather_endpoint_returns_structured_error_for_invalid_city(client):
    """Weather endpoint should return structured error, never raw exceptions."""
    with patch("backend.main.get_weather_service") as mock_get_service:
        mock_service = MagicMock()

        async def raise_not_found(city):
            raise ValueError(f"City not found: {city}")

        mock_service.get_weather = raise_not_found
        mock_get_service.return_value = mock_service

        response = await client.get("/api/weather", params={"city": "ZZZZZ"})

    assert response.status_code == 404
    data = response.json()
    assert data["data"] is None
    assert data["error"] is not None
    assert isinstance(data["error"], str)
