"""Tests for weather service fallback logic — written FIRST per TDD (RED phase).

Orchestrator delegation: Executor Agent implements fallback with TDD.
Requirement: §5.3 — Use one or two providers with fallback.
Issue: #7
"""

import pytest
from unittest.mock import AsyncMock

from backend.models.weather import WeatherResponse


@pytest.mark.asyncio
async def test_weather_service_uses_primary_when_available():
    """WeatherService should use primary provider when it succeeds."""
    from backend.services.weather_service import WeatherService

    primary = AsyncMock()
    primary.get_weather.return_value = WeatherResponse(
        city="London", temperature=18.0, description="Sunny",
        humidity=50, wind_speed=10.0, forecast="Clear",
    )
    secondary = AsyncMock()

    service = WeatherService(provider=primary, fallback_provider=secondary)
    result = await service.get_weather("London")

    assert result.city == "London"
    primary.get_weather.assert_called_once_with("London")
    secondary.get_weather.assert_not_called()


@pytest.mark.asyncio
async def test_weather_service_falls_back_to_secondary_on_runtime_error():
    """WeatherService should try fallback when primary raises RuntimeError."""
    from backend.services.weather_service import WeatherService

    primary = AsyncMock()
    primary.get_weather.side_effect = RuntimeError("Primary API down")

    secondary = AsyncMock()
    secondary.get_weather.return_value = WeatherResponse(
        city="London", temperature=17.0, description="Cloudy",
        humidity=65, wind_speed=12.0, forecast="Overcast",
    )

    service = WeatherService(provider=primary, fallback_provider=secondary)
    result = await service.get_weather("London")

    assert result.city == "London"
    assert result.temperature == 17.0
    primary.get_weather.assert_called_once()
    secondary.get_weather.assert_called_once_with("London")


@pytest.mark.asyncio
async def test_weather_service_raises_when_both_providers_fail():
    """WeatherService should raise RuntimeError when both providers fail."""
    from backend.services.weather_service import WeatherService

    primary = AsyncMock()
    primary.get_weather.side_effect = RuntimeError("Primary down")

    secondary = AsyncMock()
    secondary.get_weather.side_effect = RuntimeError("Secondary down")

    service = WeatherService(provider=primary, fallback_provider=secondary)
    with pytest.raises(RuntimeError):
        await service.get_weather("London")


@pytest.mark.asyncio
async def test_weather_service_does_not_fallback_on_value_error():
    """WeatherService should NOT fallback when primary raises ValueError (city not found)."""
    from backend.services.weather_service import WeatherService

    primary = AsyncMock()
    primary.get_weather.side_effect = ValueError("City not found")
    secondary = AsyncMock()

    service = WeatherService(provider=primary, fallback_provider=secondary)
    with pytest.raises(ValueError, match="City not found"):
        await service.get_weather("Nonexistent")

    secondary.get_weather.assert_not_called()
