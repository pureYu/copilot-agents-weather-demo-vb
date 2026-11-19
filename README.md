# Weather Forecast Demo

A simple weather forecast application built to demonstrate **GitHub Copilot AI-assisted software development** throughout the entire SDLC.

## Purpose

The **primary deliverable** is a demonstration of how GitHub Copilot Agents, Skills, Instructions, and MCP integrations drive planning, implementation, testing, code review, and documentation.

The weather application is the **secondary deliverable** — a lightweight proof of the AI-assisted workflow.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11+, FastAPI |
| Frontend | HTML, Jinja2, vanilla JavaScript |
| Testing | pytest, pytest-asyncio, httpx |
| Weather APIs | Open-Meteo (primary), wttr.in (fallback) |
| AI Tooling | GitHub Copilot Agent Mode, Skills, Instructions |

## Features

- 🌤️ **Weather Search** — Enter a city and get current weather conditions
- 🔄 **Provider Fallback** — Open-Meteo primary, wttr.in secondary (automatic failover)
- 📊 **Weather Data** — Temperature, description, humidity, wind speed, forecast
- ⚡ **Loading/Error States** — Graceful handling of slow or failing APIs
- 📖 **OpenAPI Docs** — Auto-generated at `/docs`

## Quick Start

### Option 1: Docker (recommended — single command)

```bash
docker compose up --build
```

Open http://localhost:8000. That's it!

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/pureYu/copilot-agents-weather-demo-vb.git
cd copilot-agents-weather-demo-vb

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -e ".[dev]"

# Copy environment config
cp .env.example .env

# Run tests
pytest

# Start the application
uvicorn backend.main:app --reload
```

Open http://localhost:8000 to access the application.

## Project Structure

```
├── .github/
│   ├── agents/          # Copilot Agent definitions
│   ├── skills/          # Copilot Skills (behavior shapers)
│   ├── instructions/    # Path-scoped coding instructions
│   └── copilot-instructions.md  # Global Copilot instructions
├── backend/
│   ├── main.py          # FastAPI application entry point
│   ├── config.py        # Settings from environment variables
│   ├── models/          # Pydantic response/request models
│   ├── services/        # Business logic (weather service)
│   └── providers/       # External API integrations
├── frontend/            # Jinja2 templates and static assets
├── tests/               # pytest test suite
├── docs/                # Project documentation
└── pyproject.toml       # Python project configuration
```

## Development Workflow

This project strictly follows **Test-Driven Development (TDD)**:

1. Write a failing test (RED)
2. Implement minimal code to pass (GREEN)
3. Refactor while keeping tests green (REFACTOR)

## Documentation

| Document | Type | Description |
|----------|------|-------------|
| [Setup Guide](docs/setup-guide.md) | Tutorial | Local development setup |
| [Architecture Overview](docs/architecture-overview.md) | Explanation | System design with diagrams |
| [API Reference](docs/api-reference.md) | Reference | REST endpoint documentation |
| [TDD Workflow Evidence](docs/tdd-workflow-evidence.md) | Reference | RED→GREEN→REFACTOR proof |
| [Copilot Usage Guide](docs/copilot-usage-guide.md) | Explanation | Full AI-assisted workflow |
| [Skills Overview](docs/skills-overview.md) | Explanation | How skills shape agent behavior |
| [Repository Instructions Guide](docs/repository-instructions-guide.md) | Explanation | How instructions enforce standards |
| [Agent Orchestration Workflow](docs/agent-orchestration-workflow.md) | Explanation | Multi-agent coordination |
| [Agent Execution Log](docs/agent-execution-log.md) | Reference | Evidence of agent interactions |
| [MCP Integration Summary](docs/mcp-integration-summary.md) | Explanation | GitHub MCP usage |
| [Planner Agent Evidence](docs/planner-agent-evidence.md) | Reference | Planning workflow evidence |

## GitHub Copilot AI Components

### Agents (`.github/agents/`)
| Agent | Role |
|-------|------|
| Orchestrator | Coordinates all work, enforces TDD |
| Planner | Decomposes requirements into epics/tasks |
| Executor | Implements features using strict TDD |
| QA | Validates against acceptance criteria |
| Code Review | Reviews for quality and standards |
| Documentation | Generates and maintains docs |

### Skills (`.github/skills/`)
| Skill | Behavioral Pattern |
|-------|-------------------|
| `tdd-implementation` | Enforces RED→GREEN→REFACTOR cycle |
| `code-review-standards` | Python best practices, API consistency |
| `requirements-analysis` | Scope validation, testable criteria |
| `documentation-writer` | Diátaxis framework, evidence recording |

### Instructions (`.github/instructions/`)
| Instruction | Applies To |
|-------------|-----------|
| `backend.instructions.md` | `backend/**` — layered architecture, FastAPI patterns |
| `frontend.instructions.md` | `frontend/**` — vanilla JS, accessibility |
| `testing.instructions.md` | `tests/**` — pytest, mocking, naming conventions |

## License

This project is for demonstration purposes.
