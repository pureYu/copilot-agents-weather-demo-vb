"""Open-Meteo weather provider implementation."""

import httpx

from backend.config import Settings
from backend.models.weather import WeatherResponse
from backend.providers.base import WeatherProvider

# WMO Weather interpretation codes to descriptions
WMO_CODES: dict[int, str] = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


class OpenMeteoProvider(WeatherProvider):
    """Weather provider using the Open-Meteo API."""

    def __init__(self, settings: Settings | None = None):
        self._settings = settings or Settings()
        self._geocode_url = "https://geocoding-api.open-meteo.com/v1/search"

    async def get_weather(self, city: str) -> WeatherResponse:
        """Fetch weather from Open-Meteo API.

        Args:
            city: City name to look up.

        Returns:
            WeatherResponse with normalized data.

        Raises:
            ValueError: If city is not found in geocoding.
            RuntimeError: If the API request fails.
        """
        async with httpx.AsyncClient(timeout=self._settings.http_timeout) as client:
            # Step 1: Geocode the city
            geo_response = await client.get(
                self._geocode_url, params={"name": city, "count": 1}
            )
            geo_data = geo_response.json()

            results = geo_data.get("results", [])
            if not results:
                raise ValueError(f"City not found: {city}")

            location = results[0]
            lat = location["latitude"]
            lon = location["longitude"]
            city_name = location["name"]

            # Step 2: Fetch weather data
            weather_response = await client.get(
                f"{self._settings.open_meteo_base_url}/forecast",
                params={
                    "latitude": lat,
                    "longitude": lon,
                    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
                    "daily": "weather_code",
                    "forecast_days": 3,
                },
            )

            if weather_response.status_code != 200:
                raise RuntimeError(
                    f"Open-Meteo API error: status {weather_response.status_code}"
                )

            weather_data = weather_response.json()
            current = weather_data["current"]
            weather_code = current.get("weather_code", 0)

            return WeatherResponse(
                city=city_name,
                temperature=current["temperature_2m"],
                description=WMO_CODES.get(weather_code, "Unknown"),
                humidity=current["relative_humidity_2m"],
                wind_speed=current["wind_speed_10m"],
                forecast=self._build_forecast(weather_data.get("daily", {})),
            )

    def _build_forecast(self, daily: dict) -> str | None:
        """Build a short forecast summary from daily weather codes."""
        codes = daily.get("weather_code", [])
        if not codes:
            return None
        descriptions = [WMO_CODES.get(c, "Unknown") for c in codes[:3]]
        return ", ".join(descriptions)
