import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        # The previous line `self.assertEqual(divide(5, 0), 0)` was a placeholder and is now replaced by a specific test for ZeroDivisionError.

    def test_divide_by_zero(self):
        # Test that dividing by zero raises a ZeroDivisionError with a specific message
        with self.assertRaisesRegex(ZeroDivisionError, "division by zero is not allowed"):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()