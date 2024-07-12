import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(2,3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_multiplication(self):
        """Test the multiplication method"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
    def test_division(self):
        """Test the division method"""
        try:
            self.assertEqual(self.calc.divide(2, 3), 0.66)
        except ZeroDivisionError:
            print("Error: Cannot divide by 0.")
            self.assertEqual(self.calc.divide(6,0), "Error: Cannot divide by 0")

if __name__ == "__name__":
    unittest.main()