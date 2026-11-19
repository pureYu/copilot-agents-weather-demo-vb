"""Weather service — business logic layer."""

import structlog

from backend.models.weather import WeatherResponse
from backend.providers.base import WeatherProvider

logger = structlog.get_logger()


class WeatherService:
    """Service layer for weather operations.

    Delegates to a primary WeatherProvider, with optional fallback.
    """

    def __init__(
        self,
        provider: WeatherProvider,
        fallback_provider: WeatherProvider | None = None,
    ):
        self._provider = provider
        self._fallback = fallback_provider

    async def get_weather(self, city: str) -> WeatherResponse:
        """Get weather for a city via the configured provider(s).

        Falls back to secondary provider if primary raises RuntimeError.
        Does NOT fallback on ValueError (city not found is definitive).

        Args:
            city: City name to look up.

        Returns:
            WeatherResponse with weather data.

        Raises:
            ValueError: If city is not found (no fallback attempted).
            RuntimeError: If all providers fail.
        """
        try:
            return await self._provider.get_weather(city)
        except ValueError:
            raise
        except RuntimeError as primary_error:
            if self._fallback is None:
                raise

            logger.warning(
                "primary_provider_failed",
                city=city,
                error=str(primary_error),
            )
            try:
                return await self._fallback.get_weather(city)
            except Exception as fallback_error:
                raise RuntimeError(
                    f"All providers failed. Primary: {primary_error}; "
                    f"Fallback: {fallback_error}"
                ) from fallback_error
