"""Tests with mocking for external dependencies."""

from unittest.mock import Mock, patch

import pytest

from src.testing_workshop.user_service import UserService


@pytest.fixture
def user_service():
    return UserService()


def test_get_user_success(user_service):
    """Unit test with mocking: successful API call."""
    with patch("src.testing_workshop.user_service.requests.get") as mock_get:
        # Mock setup
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 1, "name": "John"}
        mock_get.return_value = mock_response

        # Test
        result = user_service.get_user(1)

        # Assertions
        assert result == {"id": 1, "name": "John"}
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")


def test_get_user_not_found(user_service):
    """Unit test with mocking: user not found."""
    with patch("src.testing_workshop.user_service.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = user_service.get_user(999)
        assert result is None


@pytest.mark.integration
def test_create_user_integration(user_service):
    """Integration test: actual API call."""
    result = user_service.create_user("Test User", "test@example.com")
    assert "name" in result
