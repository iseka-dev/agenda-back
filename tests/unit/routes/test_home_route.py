"""Test for home route."""

from fastapi import status
from fastapi.testclient import TestClient


def test_get_home_route(client: TestClient) -> None:
    """Test for home route."""
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"Message": "Agendapp"}
