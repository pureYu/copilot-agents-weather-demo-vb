"""wttr.in weather provider implementation."""

import httpx

from backend.config import Settings
from backend.models.weather import WeatherResponse
from backend.providers.base import WeatherProvider


class WttrInProvider(WeatherProvider):
    """Weather provider using the wttr.in API (fallback/secondary)."""

    def __init__(self, settings: Settings | None = None):
        self._settings = settings or Settings()

    async def get_weather(self, city: str) -> WeatherResponse:
        """Fetch weather from wttr.in JSON API.

        Args:
            city: City name to look up.

        Returns:
            WeatherResponse with normalized data.

        Raises:
            ValueError: If city is not found.
            RuntimeError: If the API request fails.
        """
        url = f"{self._settings.wttr_in_base_url}/{city}"
        params = {"format": "j1"}

        async with httpx.AsyncClient(timeout=self._settings.http_timeout) as client:
            response = await client.get(url, params=params)

            if response.status_code != 200:
                raise RuntimeError(
                    f"wttr.in API error: status {response.status_code}"
                )

            data = response.json()
            current_conditions = data.get("current_condition", [])

            if not current_conditions:
                raise ValueError(f"City not found: {city}")

            current = current_conditions[0]

            return WeatherResponse(
                city=city,
                temperature=float(current["temp_C"]),
                description=current["weatherDesc"][0]["value"],
                humidity=int(current["humidity"]),
                wind_speed=float(current["windspeedKmph"]),
                forecast=self._build_forecast(data.get("weather", [])),
            )

    def _build_forecast(self, daily: list) -> str | None:
        """Build a short forecast summary from daily weather data."""
        if not daily:
            return None
        descriptions = [
            day["weatherDesc"][0]["value"]
            for day in daily[:3]
            if day.get("weatherDesc")
        ]
        return ", ".join(descriptions) if descriptions else None
