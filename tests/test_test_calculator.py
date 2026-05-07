import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        """Tests the add function for positive, negative, and mixed numbers."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        """Tests the subtract function for positive, negative, and mixed numbers."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        """Tests the multiply function for positive, negative, and mixed numbers, including zero."""
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(5, 0), 0)

    def test_divide_valid(self):
        """Tests the divide function with valid non-zero divisors."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(0, 5), 0)
        self.assertAlmostEqual(divide(10, 3), 3.3333333333333335)

    def test_divide_by_zero(self):
        """Tests that dividing by zero raises a ZeroDivisionError with the expected message."""
        with self.assertRaisesRegex(ZeroDivisionError, "division by zero is not allowed"):
            divide(10, 0)

    def test_divide_by_zero_edge_cases(self):
        """Tests dividing zero by zero and negative number by zero."""
        with self.assertRaisesRegex(ZeroDivisionError, "division by zero is not allowed"):
            divide(0, 0)
        with self.assertRaisesRegex(ZeroDivisionError, "division by zero is not allowed"):
            divide(-5, 0)

if __name__ == '__main__':
    unittest.main()
