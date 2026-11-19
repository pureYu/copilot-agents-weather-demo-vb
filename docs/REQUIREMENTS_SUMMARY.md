# Requirements: GitHub Copilot AI Demo - Weather Forecast App

## 1. Purpose

This document defines the requirements for creating a simple Weather Forecast application that demonstrates the practical use of GitHub Copilot AI technologies throughout the software development lifecycle.

The **primary deliverable** is **not** the weather application itself.

The primary deliverable is a demonstration of how GitHub Copilot can be used to:

- plan software development
- analyze requirements
- implement features
- follow Test-Driven Development (TDD)
- review code
- generate documentation
- enforce engineering standards through reusable Agents, Skills, and Instructions

The Weather Forecast application serves as a lightweight example for showcasing these AI-assisted engineering practices.

---

# 2. Project Objectives

The project should demonstrate:

1. GitHub Copilot Agent Mode throughout the SDLC.
2. Reuse of Agents created in the previous News Reader project.
3. Design of reusable Copilot Skills that shape agent behavior.
4. Repository Instructions that define engineering standards.
5. Test-Driven Development (TDD) as the default development workflow.
6. Integration with the official GitHub App.
7. Demonstrate orchestration of specialized Agents through an Orchestrator Agent.
8. Delivery of a small but complete Python web application.

---

# 3. Scope

## 3.1 In Scope

- Simple Python backend.
- Simple frontend.
- Weather forecast retrieval from one or two public APIs.
- REST API.
- GitHub Copilot Agents.
- Copilot Skills.
- Repository Instructions.
- Test Driven Development.
- GitHub App integration.
- Documentation explaining how AI technologies were used.

## 3.2 Out of Scope

- User authentication.
- Databases.
- User accounts.
- Background workers.
- Caching.
- Complex UI.
- Mobile applications.
- Production deployment.
- Weather history or analytics.

---

# 4. Primary Deliverable: GitHub Copilot AI Demonstration

The project should clearly demonstrate how GitHub Copilot contributes to software development.

The application exists only to provide a realistic example.

## 4.1 GitHub Copilot Agent Usage

Reuse Agents from the previous News Reader project wherever possible.

Possible Agents include:

- Requirements Analysis Agent
- Planner Agent
- Orchestrator Agent
- Backend Implementation Agent
- QA Agent
- Documentation Agent
- Code Review Agent

The Orchestrator Agent should:

- understand the user's request
- decompose work into smaller tasks
- delegate work to appropriate agents
- collect agent outputs
- verify completion
- coordinate the overall implementation workflow

The project documentation should describe:

- responsibilities
- inputs
- outputs
- interaction between agents

---

## 4.2 Skills

Create **3–4 reusable Skills** inspired by:

https://agentskills.io/home

The goal is to demonstrate how Skills influence agent behavior rather than implement application logic.

Suggested Skills:

### Requirements Analysis

Responsible for:

- identifying missing requirements
- clarifying ambiguities
- producing implementation plans

---

### TDD Implementation

Responsible for:

- writing failing tests first
- implementing minimal production code
- refactoring after tests pass

---

### Code Review

Responsible for verifying:

- readability
- maintainability
- Python best practices
- API consistency
- simplicity

---

### Documentation

Responsible for generating:

- README
- API documentation
- architecture overview
- setup instructions

---

Documentation should explain how every Agent consumes these Skills.

---

## 4.3 Repository Instructions

Repository Instructions should define:

- coding standards
- project architecture
- naming conventions
- testing strategy
- preferred libraries
- TDD workflow

All agents should consistently follow these instructions.

---

## 4.4 GitHub App Integration

Use the official GitHub App:

https://github.com/github/app

Demonstrate repository-aware development through features such as:

- repository context
- issue awareness
- pull request context
- code navigation

Document where GitHub App capabilities were used during development.

---

## 4.5 Model Context Protocol (MCP) Usage

The project should demonstrate practical use of one or more MCP servers to extend GitHub Copilot with external capabilities.

Possible MCP servers include:

- GitHub MCP
- Filesystem MCP
- Playwright MCP
- Documentation/Search MCP

At minimum, the project should demonstrate the GitHub MCP.

Example GitHub MCP capabilities:

- create Issues
- create Epics
- create Pull Requests
- read repository context
- search code
- inspect commits
- review Pull Requests

---

# 5. Secondary Deliverable: Weather Forecast Application

The application should be intentionally simple.

## 5.1 Backend Requirements

Backend technology:

- Python
- FastAPI

The backend should provide:

- endpoint to retrieve weather forecast
- integration with one or two public weather APIs
- normalized weather response
- error handling
- OpenAPI documentation

---

## 5.2 Frontend Requirements

Provide a lightweight frontend that allows the user to:

- enter a city
- retrieve weather information
- display:

  - temperature
  - weather description
  - humidity
  - wind speed
  - short forecast

Loading and error states should be handled gracefully.

---

## 5.3 Weather Sources

Use only one or two open weather providers.

Examples:

- Open-Meteo API (recommended)
- WeatherAPI (free tier)
- wttr.in

The application should isolate external APIs behind a service layer.

---

# 6. Test Driven Development

All implementation should follow Test-Driven Development.

Each feature should follow:

1. Write failing tests.
2. Run tests.
3. Implement minimal code.
4. Make tests pass.
5. Refactor.
6. Repeat.

The repository should include evidence of this workflow.

---

# 7. Non-Functional Requirements

## 7.1 Simplicity

The application should remain intentionally small.

The emphasis is demonstrating Copilot workflows rather than application complexity.

---

## 7.2 Explainability

A reviewer should understand:

- why each Agent exists
- which Skills were used
- how Repository Instructions affected development
- how TDD was followed

---

## 7.3 Reusability

Agents and Skills should be reusable in future projects with minimal changes.

---

## 7.4 Testability

Critical components should include automated tests.

Recommended coverage:

- service layer
- API endpoints
- weather provider abstraction

---

## 7.5 Security

Configuration should use environment variables.

Secrets must never be stored in source code.

---

# 8. Technology Stack

Backend

- Python
- FastAPI

Frontend

- HTML
- Jinja2 templates
- JavaScript

Testing

- pytest
- httpx

Development

- GitHub Copilot Agent Mode
- GitHub App

---

# 9. Documentation Deliverables

The repository should include:

1. Requirements
2. README
3. Architecture Overview
4. Agent Overview
5. Skills Overview
6. Repository Instructions
7. TDD Workflow
8. GitHub App Usage
9. Setup Guide
10. MCP Server configuration guide
11. Agent orchestration workflow
12. Examples of MCP interactions

---

# 10. Acceptance Criteria

The project is considered complete when:

1. A working Weather Forecast application exists.
2. Weather data is retrieved from at least one public weather API.
3. Backend exposes REST endpoints.
4. Frontend displays weather information.
5. Repository Instructions guide all AI-assisted development.
6. Existing Agents from the previous project are reused.
7. Three or four reusable Skills shape agent behavior.
8. Test-Driven Development is followed throughout implementation.
9. GitHub App integration is demonstrated.
10. Documentation clearly explains how GitHub Copilot contributed to planning, implementation, testing, review, and documentation.
11. Documentation explains how Agents, Skills, Repository Instructions, and MCP servers work together during development.