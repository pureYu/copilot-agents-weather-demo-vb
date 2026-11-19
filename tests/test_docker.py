"""Tests for Docker container build and configuration."""

import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).parent.parent


class TestDockerConfiguration:
    """Verify Docker files are valid and correctly configured."""

    def test_dockerfile_exists(self):
        """Dockerfile must exist at project root."""
        assert (REPO_ROOT / "Dockerfile").is_file()

    def test_dockerignore_exists(self):
        """.dockerignore must exist to keep image lean."""
        assert (REPO_ROOT / ".dockerignore").is_file()

    def test_docker_compose_exists(self):
        """docker-compose.yml must exist for one-command launch."""
        assert (REPO_ROOT / "docker-compose.yml").is_file()

    def test_dockerfile_exposes_port_8000(self):
        """Dockerfile must expose port 8000."""
        content = (REPO_ROOT / "Dockerfile").read_text()
        assert "EXPOSE 8000" in content

    def test_dockerfile_uses_uvicorn_cmd(self):
        """Dockerfile CMD must run uvicorn with the correct app."""
        content = (REPO_ROOT / "Dockerfile").read_text()
        assert "uvicorn" in content
        assert "backend.main:app" in content

    def test_dockerignore_excludes_tests(self):
        """.dockerignore must exclude tests/ to keep image small."""
        content = (REPO_ROOT / ".dockerignore").read_text()
        assert "tests/" in content

    def test_dockerignore_excludes_git(self):
        """.dockerignore must exclude .git directory."""
        content = (REPO_ROOT / ".dockerignore").read_text()
        assert ".git" in content

    def test_docker_compose_maps_port_8000(self):
        """docker-compose.yml must map port 8000."""
        content = (REPO_ROOT / "docker-compose.yml").read_text()
        assert "8000:8000" in content

    def test_docker_compose_has_healthcheck(self):
        """docker-compose.yml must include a healthcheck."""
        content = (REPO_ROOT / "docker-compose.yml").read_text()
        assert "healthcheck" in content
        assert "/api/health" in content
