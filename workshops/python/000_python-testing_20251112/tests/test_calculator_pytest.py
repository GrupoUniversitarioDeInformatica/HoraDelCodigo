"""Pytest tests with fixtures and parameterization."""

import pytest

from src.testing_workshop.calculator import Calculator


@pytest.fixture
def calculator():
    """Fixture: provides calculator instance."""
    return Calculator()


@pytest.mark.parametrize(
    "a,b,expected", [(2, 3, 5), (0, 0, 0), (-1, 1, 0), (10.5, 2.5, 13.0)]
)
def test_add_parameterized(calculator, a, b, expected):
    """Parameterized test: multiple test cases."""
    assert calculator.add(a, b) == expected


def test_divide_by_zero(calculator):
    """Unit test: exception with pytest."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)


@pytest.mark.smoke
def test_basic_operations_work(calculator):
    """Smoke test: basic functionality."""
    assert calculator.add(1, 1) == 2
    assert calculator.divide(4, 2) == 2
