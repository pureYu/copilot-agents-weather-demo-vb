"""Weather response models."""

from pydantic import BaseModel


class WeatherResponse(BaseModel):
    """Canonical weather response returned by all providers."""

    city: str
    temperature: float
    description: str
    humidity: int
    wind_speed: float
    forecast: str | None = None
