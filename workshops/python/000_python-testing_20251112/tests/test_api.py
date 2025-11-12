"""FastAPI integration and end-to-end tests."""

from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from src.testing_workshop.api import app


@pytest.fixture
def client():
    """Fixture: FastAPI test client."""
    return TestClient(app)


def test_root_endpoint(client):
    """Integration test: API root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Testing Workshop API"}


def test_calculator_endpoint(client):
    """Integration test: calculator API endpoint."""
    response = client.get("/calculate/add/2/3")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


@patch("src.testing_workshop.api.user_service.get_user")
def test_user_endpoint_success(mock_get_user, client):
    """Integration test with mocking: user endpoint."""
    mock_get_user.return_value = {"id": 1, "name": "John"}

    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John"}


@patch("src.testing_workshop.api.user_service.get_user")
def test_user_endpoint_not_found(mock_get_user, client):
    """Integration test: user not found."""
    mock_get_user.return_value = None

    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


@pytest.mark.e2e
def test_full_workflow(client):
    """End-to-end test: complete user workflow."""
    # Test root
    root_response = client.get("/")
    assert root_response.status_code == 200

    # Test calculator
    calc_response = client.get("/calculate/add/10/5")
    assert calc_response.status_code == 200
    assert calc_response.json()["result"] == 15.0
