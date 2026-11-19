"""Weather Forecast Demo — FastAPI application entry point."""

import os
from pathlib import Path

from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from backend.config import Settings
from backend.models.weather import WeatherResponse
from backend.providers.open_meteo import OpenMeteoProvider
from backend.providers.wttr_in import WttrInProvider
from backend.services.weather_service import WeatherService

settings = Settings()

# Resolve frontend directory relative to this file
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app = FastAPI(
    title=settings.app_name,
    description="A simple weather forecast application demonstrating GitHub Copilot AI-assisted development.",
    version="0.1.0",
)


def get_weather_service() -> WeatherService:
    """Dependency: create a WeatherService with primary and fallback providers."""
    primary = OpenMeteoProvider(settings=settings)
    fallback = WttrInProvider(settings=settings)
    return WeatherService(provider=primary, fallback_provider=fallback)


@app.get("/", response_class=HTMLResponse)
async def index():
    """Serve the frontend index page."""
    index_path = FRONTEND_DIR / "index.html"
    return HTMLResponse(content=index_path.read_text(encoding="utf-8"))


@app.get("/api/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy", "service": settings.app_name}


@app.get("/api/weather")
async def get_weather(city: str = Query(..., description="City name to get weather for")):
    """Get weather forecast for a city.

    Returns a consistent envelope: {"data": ..., "error": null}
    """
    service = get_weather_service()
    try:
        result = await service.get_weather(city)
        return {"data": result.model_dump(), "error": None}
    except ValueError as e:
        return JSONResponse(
            status_code=404,
            content={"data": None, "error": str(e)},
        )
    except RuntimeError as e:
        return JSONResponse(
            status_code=502,
            content={"data": None, "error": f"Weather service unavailable: {e}"},
        )
