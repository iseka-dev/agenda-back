"""Test for health check route."""

from fastapi import status
from fastapi.testclient import TestClient


def test_get_health_check_route(client: TestClient) -> None:
    """Test health_check_route."""
    response = client.get("/health-check")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "check": {"server": "OK", "database": "OK"}
    }
