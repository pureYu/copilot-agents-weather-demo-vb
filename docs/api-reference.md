# API Reference

This document provides a complete reference for the Weather Forecast Demo REST API.

---

## Base URL

```
http://localhost:8000
```

---

## Endpoints

### GET /api/health

Health check endpoint for monitoring.

**Response** `200 OK`:
```json
{
  "status": "healthy",
  "service": "Weather Forecast Demo"
}
```

---

### GET /api/weather

Retrieve current weather and short forecast for a city.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `city` | string (query) | ✅ | City name to get weather for |

**Success Response** `200 OK`:
```json
{
  "data": {
    "city": "London",
    "temperature": 18.5,
    "description": "Partly cloudy",
    "humidity": 72,
    "wind_speed": 12.3,
    "forecast": "Partly cloudy, Overcast, Mainly clear"
  },
  "error": null
}
```

**Error: City Not Found** `404`:
```json
{
  "data": null,
  "error": "City not found: Nonexistent"
}
```

**Error: Provider Failure** `502`:
```json
{
  "data": null,
  "error": "Weather service unavailable: All providers failed. Primary: ...; Fallback: ..."
}
```

**Error: Missing Parameter** `422`:
```json
{
  "detail": [
    {
      "loc": ["query", "city"],
      "msg": "Field required",
      "type": "missing"
    }
  ]
}
```

---

### GET /

Serves the frontend HTML page (single-page weather app).

**Response** `200 OK`: HTML content with city search form and weather display.

---

### GET /docs

Auto-generated Swagger UI (OpenAPI interactive documentation).

---

### GET /openapi.json

OpenAPI 3.0 JSON schema for all endpoints.

---

## Response Envelope

All API responses use a consistent envelope structure:

```json
{
  "data": { ... } | null,
  "error": "string" | null
}
```

- **Success**: `data` contains the result, `error` is `null`
- **Failure**: `data` is `null`, `error` contains a human-readable message

---

## Data Models

### WeatherResponse

| Field | Type | Description |
|-------|------|-------------|
| `city` | string | Resolved city name |
| `temperature` | float | Current temperature in °C |
| `description` | string | Human-readable weather description |
| `humidity` | integer | Relative humidity percentage |
| `wind_speed` | float | Wind speed in km/h |
| `forecast` | string \| null | Short forecast (next 3 days) |

---

## Weather Providers

The API uses two providers with automatic failover:

| Provider | Role | API |
|----------|------|-----|
| Open-Meteo | Primary | `api.open-meteo.com` |
| wttr.in | Fallback | `wttr.in` |

Fallback is triggered when the primary provider returns a `RuntimeError` (API failure). City-not-found errors (`ValueError`) do NOT trigger fallback.

---

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 404 | City not found |
| 422 | Validation error (missing/invalid parameters) |
| 502 | Weather provider(s) unavailable |
