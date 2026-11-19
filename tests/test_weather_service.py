"""Tests for weather service layer — written FIRST per TDD."""

import pytest
from unittest.mock import AsyncMock, patch

from backend.models.weather import WeatherResponse


@pytest.mark.asyncio
async def test_weather_service_returns_data_from_provider():
    """WeatherService should return provider result on success."""
    from backend.services.weather_service import WeatherService

    mock_provider = AsyncMock()
    mock_provider.get_weather.return_value = WeatherResponse(
        city="Berlin",
        temperature=20.0,
        description="Clear sky",
        humidity=55,
        wind_speed=10.0,
        forecast="Sunny all day",
    )

    service = WeatherService(provider=mock_provider)
    result = await service.get_weather("Berlin")

    assert result.city == "Berlin"
    assert result.temperature == 20.0
    mock_provider.get_weather.assert_called_once_with("Berlin")


@pytest.mark.asyncio
async def test_weather_service_propagates_value_error_for_unknown_city():
    """WeatherService should propagate ValueError for unknown cities."""
    from backend.services.weather_service import WeatherService

    mock_provider = AsyncMock()
    mock_provider.get_weather.side_effect = ValueError("City not found")

    service = WeatherService(provider=mock_provider)
    with pytest.raises(ValueError, match="City not found"):
        await service.get_weather("Nonexistent")


@pytest.mark.asyncio
async def test_weather_service_raises_runtime_error_on_provider_failure():
    """WeatherService should raise RuntimeError when provider fails."""
    from backend.services.weather_service import WeatherService

    mock_provider = AsyncMock()
    mock_provider.get_weather.side_effect = RuntimeError("API unavailable")

    service = WeatherService(provider=mock_provider)
    with pytest.raises(RuntimeError, match="API unavailable"):
        await service.get_weather("London")
