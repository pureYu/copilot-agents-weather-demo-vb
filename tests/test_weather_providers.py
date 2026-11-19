"""Tests for weather providers — written FIRST per TDD."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from backend.models.weather import WeatherResponse


@pytest.mark.asyncio
async def test_open_meteo_provider_returns_weather_response():
    """OpenMeteoProvider should return a WeatherResponse for a valid city."""
    from backend.providers.open_meteo import OpenMeteoProvider

    mock_geocode_response = MagicMock()
    mock_geocode_response.status_code = 200
    mock_geocode_response.json.return_value = {
        "results": [{"name": "London", "latitude": 51.5, "longitude": -0.12}]
    }

    mock_weather_response = MagicMock()
    mock_weather_response.status_code = 200
    mock_weather_response.json.return_value = {
        "current": {
            "temperature_2m": 18.5,
            "relative_humidity_2m": 72,
            "wind_speed_10m": 12.3,
            "weather_code": 2,
        },
        "daily": {
            "weather_code": [2, 3, 1],
        },
    }

    with patch("httpx.AsyncClient.get", side_effect=[mock_geocode_response, mock_weather_response]):
        provider = OpenMeteoProvider()
        result = await provider.get_weather("London")

    assert isinstance(result, WeatherResponse)
    assert result.city == "London"
    assert result.temperature == 18.5
    assert result.humidity == 72
    assert result.wind_speed == 12.3


@pytest.mark.asyncio
async def test_open_meteo_provider_raises_for_unknown_city():
    """OpenMeteoProvider should raise ValueError for unknown city."""
    from backend.providers.open_meteo import OpenMeteoProvider

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"results": []}

    with patch("httpx.AsyncClient.get", return_value=mock_response):
        provider = OpenMeteoProvider()
        with pytest.raises(ValueError, match="City not found"):
            await provider.get_weather("Nonexistentcity123")


@pytest.mark.asyncio
async def test_open_meteo_provider_raises_on_api_error():
    """OpenMeteoProvider should raise RuntimeError on API failure."""
    from backend.providers.open_meteo import OpenMeteoProvider

    mock_geocode_response = MagicMock()
    mock_geocode_response.status_code = 200
    mock_geocode_response.json.return_value = {
        "results": [{"name": "London", "latitude": 51.5, "longitude": -0.12}]
    }

    mock_weather_response = MagicMock()
    mock_weather_response.status_code = 500

    with patch("httpx.AsyncClient.get", side_effect=[mock_geocode_response, mock_weather_response]):
        provider = OpenMeteoProvider()
        with pytest.raises(RuntimeError):
            await provider.get_weather("London")
