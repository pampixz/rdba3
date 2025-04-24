import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 2), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(16), 4)
        with self.assertRaises(ValueError):
            self.calc.sqrt(-4)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

    def test_sin(self):
        self.assertAlmostEqual(self.calc.sin(30), 0.5, places=2)

    def test_cos(self):
        self.assertAlmostEqual(self.calc.cos(60), 0.5, places=2)

    def test_tan(self):
        self.assertAlmostEqual(self.calc.tan(45), 1, places=2)


if __name__ == "__main__":
    unittest.main()