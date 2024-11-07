import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calc.add(5, 2), 7)
    
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(6,  5), 1)
    
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(17,  5), 12)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(5,  6), 30)
    
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(7,  6), 42)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(18,6), 3)
    
    def test_divide2(self):
        self.assertEqual(self.calc.divide(100,7), 14)
        
    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(17,5), 2)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(25,6), 1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()