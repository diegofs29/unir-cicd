import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(6, self.calc.add(4, 2))
        self.assertEqual(6, self.calc.add(2, 4))
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(1, self.calc.add(0, 1))

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.substract(4, 2))
        self.assertEqual(-2, self.calc.substract(2, 4))
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(2, self.calc.substract(2, 0))
        self.assertEqual(-2, self.calc.substract(0, 2))

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(8, self.calc.multiply(4, 2))
        self.assertEqual(8, self.calc.multiply(2, 4))
        self.assertEqual(9, self.calc.multiply(3, 3))
        self.assertEqual(-9, self.calc.multiply(3, -3))
        self.assertEqual(-9, self.calc.multiply(-3, 3))
        self.assertEqual(0, self.calc.multiply(2, 0))
        self.assertEqual(0, self.calc.multiply(0, 2))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertAlmostEqual(0.66, self.calc.divide(2, 3), places=1)
        self.assertEqual(0, self.calc.divide(0, 2))
        self.assertEqual(-1, self.calc.divide(-2, 2))
        self.assertEqual(-1, self.calc.divide(2, -2))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(9, self.calc.power(3, 2))
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(4, self.calc.power(-2, 2))
        self.assertEqual(-8, self.calc.power(-2, 3))
        self.assertEqual(0, self.calc.power(0, 2))
        self.assertEqual(1, self.calc.power(0, 0))
        self.assertEqual(1, self.calc.power(2, 0))
    
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(3, self.calc.sqrt(9))
        self.assertAlmostEqual(2.8, self.calc.sqrt(8), places=1)
        self.assertEqual(1, self.calc.sqrt(1))
        self.assertEqual(0, self.calc.sqrt(0))
    
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(3, self.calc.log10(1000))
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(0, self.calc.log10(10))
        self.assertAlmostEqual(1.4, self.calc.log10(25), places=1)

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())
    
    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, object(), 2)
        self.assertRaises(TypeError, self.calc.divide, 2, object())
    
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())
    
    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "2", 2)
        self.assertRaises(TypeError, self.calc.sqrt, 2, "2")
        self.assertRaises(TypeError, self.calc.sqrt, "2", "2")
        self.assertRaises(TypeError, self.calc.sqrt, None, 2)
        self.assertRaises(TypeError, self.calc.sqrt, 2, None)
        self.assertRaises(TypeError, self.calc.sqrt, object(), 2)
        self.assertRaises(TypeError, self.calc.sqrt, 2, object())
    
    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "2", 2)
        self.assertRaises(TypeError, self.calc.log10, 2, "2")
        self.assertRaises(TypeError, self.calc.log10, "2", "2")
        self.assertRaises(TypeError, self.calc.log10, None, 2)
        self.assertRaises(TypeError, self.calc.log10, 2, None)
        self.assertRaises(TypeError, self.calc.log10, object(), 2)
        self.assertRaises(TypeError, self.calc.log10, 2, object())

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_power_method_fails_with_zero_and_negative_power(self):
        self.assertRaises(TypeError, self.calc.power, 0, -2)
        self.assertRaises(TypeError, self.calc.power, -0, -2)
        self.assertRaises(TypeError, self.calc.power, "0", -2)

    def test_sqrt_method_fails_with_negative_value(self):
        self.assertRaises(TypeError, self.calc.sqrt, -1)

    def test_log10_method_fails_with_zero_or_negative_value(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -1)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
