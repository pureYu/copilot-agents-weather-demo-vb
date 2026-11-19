"""Tests for health check endpoint — written FIRST per TDD."""

import pytest


@pytest.mark.asyncio
async def test_health_check_returns_200(client):
    """Health endpoint should return HTTP 200."""
    response = await client.get("/api/health")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_health_check_returns_healthy_status(client):
    """Health endpoint should include status=healthy."""
    response = await client.get("/api/health")
    data = response.json()
    assert data["status"] == "healthy"


@pytest.mark.asyncio
async def test_health_check_returns_service_name(client):
    """Health endpoint should include the service name."""
    response = await client.get("/api/health")
    data = response.json()
    assert data["service"] == "Weather Forecast Demo"
