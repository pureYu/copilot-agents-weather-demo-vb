"""Weather Forecast Demo — Configuration."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    model_config = SettingsConfigDict(env_prefix="WEATHER_", env_file=".env")

    app_name: str = "Weather Forecast Demo"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    # Weather provider settings
    open_meteo_base_url: str = "https://api.open-meteo.com/v1"
    wttr_in_base_url: str = "https://wttr.in"
    http_timeout: float = 10.0
