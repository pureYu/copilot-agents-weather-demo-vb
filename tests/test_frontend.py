"""Tests for frontend pages — written FIRST per TDD (RED phase).

Orchestrator delegation: Executor Agent implements frontend with TDD.
Frontend instructions applied: Jinja2 templates, vanilla JS, accessibility.
"""

import pytest


@pytest.mark.asyncio
async def test_index_page_returns_200(client):
    """Home page should return HTTP 200."""
    response = await client.get("/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_index_page_contains_search_form(client):
    """Home page should contain a city search form."""
    response = await client.get("/")
    html = response.text
    assert '<form' in html
    assert 'name="city"' in html or 'id="city"' in html
    assert '<button' in html or 'type="submit"' in html


@pytest.mark.asyncio
async def test_index_page_contains_weather_display_area(client):
    """Home page should have a container for weather results."""
    response = await client.get("/")
    html = response.text
    assert 'id="weather-result"' in html or 'id="result"' in html


@pytest.mark.asyncio
async def test_index_page_has_accessible_labels(client):
    """Home page should have accessible labels for form inputs."""
    response = await client.get("/")
    html = response.text
    assert '<label' in html


@pytest.mark.asyncio
async def test_index_page_includes_javascript(client):
    """Home page should include JavaScript for fetch interactions."""
    response = await client.get("/")
    html = response.text
    assert '<script' in html
    assert 'fetch(' in html or 'app.js' in html.lower()
