"""Tests for weather API endpoint — written FIRST per TDD."""

import pytest
from unittest.mock import AsyncMock, patch

from backend.models.weather import WeatherResponse


@pytest.mark.asyncio
async def test_weather_endpoint_returns_200_for_valid_city(client):
    """GET /api/weather?city=London should return 200 with weather data."""
    mock_response = WeatherResponse(
        city="London",
        temperature=18.5,
        description="Partly cloudy",
        humidity=72,
        wind_speed=12.3,
        forecast="Clouds clearing by afternoon",
    )

    with patch("backend.main.get_weather_service") as mock_get_service:
        mock_service = AsyncMock()
        mock_service.get_weather.return_value = mock_response
        mock_get_service.return_value = mock_service

        response = await client.get("/api/weather", params={"city": "London"})

    assert response.status_code == 200
    data = response.json()
    assert data["data"]["city"] == "London"
    assert data["data"]["temperature"] == 18.5
    assert data["error"] is None


@pytest.mark.asyncio
async def test_weather_endpoint_returns_404_for_unknown_city(client):
    """GET /api/weather?city=Unknown should return 404."""
    with patch("backend.main.get_weather_service") as mock_get_service:
        mock_service = AsyncMock()
        mock_service.get_weather.side_effect = ValueError("City not found")
        mock_get_service.return_value = mock_service

        response = await client.get("/api/weather", params={"city": "Nonexistent"})

    assert response.status_code == 404
    data = response.json()
    assert data["data"] is None
    assert "not found" in data["error"].lower()


@pytest.mark.asyncio
async def test_weather_endpoint_returns_502_on_provider_failure(client):
    """GET /api/weather should return 502 when provider fails."""
    with patch("backend.main.get_weather_service") as mock_get_service:
        mock_service = AsyncMock()
        mock_service.get_weather.side_effect = RuntimeError("API timeout")
        mock_get_service.return_value = mock_service

        response = await client.get("/api/weather", params={"city": "London"})

    assert response.status_code == 502
    data = response.json()
    assert data["data"] is None
    assert data["error"] is not None


@pytest.mark.asyncio
async def test_weather_endpoint_returns_400_without_city_param(client):
    """GET /api/weather without city param should return 422 (FastAPI validation)."""
    response = await client.get("/api/weather")
    assert response.status_code == 422
