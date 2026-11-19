"""Weather provider protocol — abstract interface for weather sources."""

from abc import ABC, abstractmethod

from backend.models.weather import WeatherResponse


class WeatherProvider(ABC):
    """Abstract base class for weather data providers."""

    @abstractmethod
    async def get_weather(self, city: str) -> WeatherResponse:
        """Fetch weather data for a given city.

        Args:
            city: Name of the city to get weather for.

        Returns:
            WeatherResponse with normalized weather data.

        Raises:
            ValueError: If the city is not found.
            RuntimeError: If the provider API fails.
        """
        ...
