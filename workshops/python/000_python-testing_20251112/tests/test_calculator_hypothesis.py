"""Property-based testing with Hypothesis."""

from hypothesis import given
from hypothesis import strategies as st

from src.testing_workshop.calculator import Calculator

calc = Calculator()


@given(st.floats(allow_nan=False, allow_infinity=False))
def test_add_zero_identity(x):
    """Property test: adding zero doesn't change value."""
    assert calc.add(x, 0) == x


@given(
    st.floats(allow_nan=False, allow_infinity=False),
    st.floats(allow_nan=False, allow_infinity=False),
)
def test_add_commutative(a, b):
    """Property test: addition is commutative."""
    assert calc.add(a, b) == calc.add(b, a)


@given(
    st.floats(min_value=0.1, max_value=1000), st.floats(min_value=0.1, max_value=1000)
)
def test_divide_multiply_inverse(a, b):
    """Property test: division and multiplication are inverse."""
    result = calc.divide(a, b)
    assert abs(result * b - a) < 1e-10
