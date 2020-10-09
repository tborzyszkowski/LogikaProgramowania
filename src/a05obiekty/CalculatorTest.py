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

    def test_div_1_ident(self):
        self.calculator.add(5)
        self.calculator.div(1)
        self.assertEqual(5, self.calculator.state)

    def test_div_0(self):
        self.calculator.add(5)
        self.calculator.div(0)
        self.assertNotEqual(0, self.calculator.error_state)

    def test_div_6984_by_12(self):
        self.calculator.add(6984)
        self.calculator.div(12)
        self.assertEqual(582, self.calculator.state)

    def test_div_12_by_4(self):
        self.calculator.add(12)
        self.calculator.div(4)
        self.assertEqual(3, self.calculator.state)

    def test_fact_0(self):
        self.calculator.factorial()
        self.assertEqual(1, self.calculator.state)

    def test_fact_3(self):
        self.calculator.state = 3
        self.calculator.factorial()
        self.assertEqual(6, self.calculator.state)

    def test_fact_5(self):
        self.calculator.state = 5
        self.calculator.factorial()
        self.assertEqual(120, self.calculator.state)

    def test_fact_15(self):
        self.calculator.state = 15
        self.calculator.factorial()
        self.assertEqual(1307674368000, self.calculator.state)

if __name__ == '__main__':
    unittest.main()
