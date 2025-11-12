"""Unit tests using unittest library."""

import unittest

from src.testing_workshop.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Fixture: setup before each test."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Unit test: basic addition."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_divide_by_zero_raises_error(self):
        """Unit test: exception handling."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_power_calculation(self):
        """Regression test: ensure power works correctly."""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)


if __name__ == "__main__":
    unittest.main()
