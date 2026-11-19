# Setup Guide

This guide walks you through setting up the Weather Forecast Demo for local development.

## Quick Start with Docker

If you have Docker installed, run a single command:

```bash
docker compose up --build
```

The app will be available at http://localhost:8000. No Python installation required.

To stop: `Ctrl+C` or `docker compose down`.

---

## Local Development Setup

### Prerequisites

- **Python 3.11+** — [Download](https://www.python.org/downloads/)
- **Git** — [Download](https://git-scm.com/)
- **GitHub Copilot** (optional but recommended) — for the AI-assisted workflow

## Step 1: Clone the Repository

```bash
git clone https://github.com/epam-mbg-demo/copilot-agents-weather-demo.git
cd copilot-agents-weather-demo
```

## Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

| Platform | Command |
|----------|---------|
| Linux/macOS | `source .venv/bin/activate` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (cmd) | `.venv\Scripts\activate.bat` |

## Step 3: Install Dependencies

```bash
# Install with development dependencies
pip install -e ".[dev]"
```

This installs:
- **Runtime**: FastAPI, uvicorn, httpx, pydantic, structlog, jinja2
- **Dev**: pytest, pytest-asyncio, respx, ruff

## Step 4: Configure Environment

```bash
cp .env.example .env
```

Edit `.env` if needed. Default values work for local development:

| Variable | Default | Description |
|----------|---------|-------------|
| `WEATHER_DEBUG` | `true` | Enable debug mode |
| `WEATHER_HOST` | `127.0.0.1` | Server bind address |
| `WEATHER_PORT` | `8000` | Server port |

> **Note on weather providers**: The app uses [Open-Meteo](https://open-meteo.com/) as its primary weather API and [wttr.in](https://wttr.in/) as an automatic fallback. Both are free, public APIs — no API keys required.

## Step 5: Run Tests

```bash
pytest
```

All tests should pass. If they don't, check your Python version and dependencies.

## Step 6: Start the Application

```bash
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

- Application: http://localhost:8000
- API docs (Swagger): http://localhost:8000/docs
- Health check: http://localhost:8000/api/health

## Step 7: Verify

```bash
curl http://localhost:8000/api/health
# Expected: {"status":"healthy","service":"Weather Forecast Demo"}
```

## Development Commands

| Command | Purpose |
|---------|---------|
| `pytest` | Run all tests |
| `pytest -v` | Run tests with verbose output |
| `pytest --tb=short` | Run tests with short tracebacks |
| `ruff check .` | Lint the codebase |
| `ruff format .` | Format the codebase |

## Troubleshooting

### `ModuleNotFoundError: No module named 'backend'`
Ensure you installed with `pip install -e ".[dev]"` (editable mode).

### Tests fail with async errors
Ensure `pytest-asyncio` is installed and `asyncio_mode = "auto"` is in `pyproject.toml`.
