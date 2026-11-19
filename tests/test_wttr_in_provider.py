"""Tests for WttrIn provider — written FIRST per TDD (RED phase).

Orchestrator delegation: Executor Agent implements WttrIn provider with TDD.
Requirement: §5.3 — Weather sources (wttr.in as secondary/fallback).
Issue: #7
"""

import pytest
from unittest.mock import MagicMock, patch

from backend.models.weather import WeatherResponse


@pytest.mark.asyncio
async def test_wttr_in_provider_returns_weather_response():
    """WttrInProvider should return a WeatherResponse for a valid city."""
    from backend.providers.wttr_in import WttrInProvider

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "current_condition": [{
            "temp_C": "15",
            "weatherDesc": [{"value": "Light rain"}],
            "humidity": "82",
            "windspeedKmph": "14",
        }],
        "weather": [
            {"weatherDesc": [{"value": "Light rain"}]},
            {"weatherDesc": [{"value": "Cloudy"}]},
            {"weatherDesc": [{"value": "Sunny"}]},
        ],
    }

    with patch("httpx.AsyncClient.get", return_value=mock_response):
        provider = WttrInProvider()
        result = await provider.get_weather("London")

    assert isinstance(result, WeatherResponse)
    assert result.city == "London"
    assert result.temperature == 15.0
    assert result.humidity == 82
    assert result.wind_speed == 14.0
    assert result.description == "Light rain"


@pytest.mark.asyncio
async def test_wttr_in_provider_raises_for_unknown_city():
    """WttrInProvider should raise ValueError for unknown city."""
    from backend.providers.wttr_in import WttrInProvider

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "current_condition": [],
    }

    with patch("httpx.AsyncClient.get", return_value=mock_response):
        provider = WttrInProvider()
        with pytest.raises(ValueError, match="[Cc]ity not found"):
            await provider.get_weather("Nonexistentcity999")


@pytest.mark.asyncio
async def test_wttr_in_provider_raises_on_api_error():
    """WttrInProvider should raise RuntimeError on API failure."""
    from backend.providers.wttr_in import WttrInProvider

    mock_response = MagicMock()
    mock_response.status_code = 500

    with patch("httpx.AsyncClient.get", return_value=mock_response):
        provider = WttrInProvider()
        with pytest.raises(RuntimeError):
            await provider.get_weather("London")


@pytest.mark.asyncio
async def test_wttr_in_provider_builds_forecast_from_daily():
    """WttrInProvider should build forecast from daily weather data."""
    from backend.providers.wttr_in import WttrInProvider

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "current_condition": [{
            "temp_C": "20",
            "weatherDesc": [{"value": "Sunny"}],
            "humidity": "45",
            "windspeedKmph": "8",
        }],
        "weather": [
            {"weatherDesc": [{"value": "Sunny"}]},
            {"weatherDesc": [{"value": "Partly cloudy"}]},
        ],
    }

    with patch("httpx.AsyncClient.get", return_value=mock_response):
        provider = WttrInProvider()
        result = await provider.get_weather("Paris")

    assert result.forecast is not None
    assert "Sunny" in result.forecast
