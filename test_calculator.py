import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(3,4),7)
        self.assertEqual(self.calc.add(7,3),10)
    def test_substract(self) :
        self.assertEqual(self.calc.subtract(3,2), 1)
        self.assertEqual(self.calc.subtract(-1,3), -4)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,7),14)
        self.assertEqual(self.calc.multiply(-1,7),-7)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(6,3),2)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(1,2),1)
        self.assertEqual(self.calc.modulo(7,2),1)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()