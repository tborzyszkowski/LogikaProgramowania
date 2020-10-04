import unittest
from .Calculator import *

class CalculatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self):
        self.calculator.add(1)
        self.assertEqual(1, self.calculator.state)

    def test_mult_0(self):
        self.calculator.mult(0)
        self.assertEqual(0, self.calculator.state)

    def test_mult_0_after_operations(self):
        self.calculator.add(5)
        self.calculator.add(10)
        self.calculator.mult(0)
        self.assertEqual(0, self.calculator.state)

    def test_mult_2_after_operations(self):
        self.calculator.add(5)
        self.calculator.mult(2)
        self.assertEqual(10, self.calculator.state)


if __name__ == '__main__':
    unittest.main()
