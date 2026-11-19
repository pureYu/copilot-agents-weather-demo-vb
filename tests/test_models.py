"""Tests for weather response models — written FIRST per TDD."""

import pytest
from pydantic import ValidationError


def test_weather_response_contains_required_fields():
    """WeatherResponse model should contain all required weather fields."""
    from backend.models.weather import WeatherResponse

    response = WeatherResponse(
        city="London",
        temperature=18.5,
        description="Partly cloudy",
        humidity=72,
        wind_speed=12.3,
        forecast="Expect clouds clearing by afternoon",
    )
    assert response.city == "London"
    assert response.temperature == 18.5
    assert response.description == "Partly cloudy"
    assert response.humidity == 72
    assert response.wind_speed == 12.3
    assert response.forecast == "Expect clouds clearing by afternoon"


def test_weather_response_rejects_missing_city():
    """WeatherResponse should reject missing city field."""
    from backend.models.weather import WeatherResponse

    with pytest.raises(ValidationError):
        WeatherResponse(
            temperature=18.5,
            description="Sunny",
            humidity=50,
            wind_speed=5.0,
            forecast="Clear skies",
        )


def test_weather_response_allows_optional_forecast():
    """WeatherResponse should allow forecast to be None."""
    from backend.models.weather import WeatherResponse

    response = WeatherResponse(
        city="Paris",
        temperature=22.0,
        description="Sunny",
        humidity=45,
        wind_speed=8.0,
        forecast=None,
    )
    assert response.forecast is None
