import unittest
from bit_fun import is_even, is_power_of_2, twos_complement

class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(100))

    def test_odd_number(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(101))

    def test_power_of_2(self):
        self.assertTrue(is_power_of_2(1))
        self.assertTrue(is_power_of_2(2))
        self.assertTrue(is_power_of_2(4))
        self.assertTrue(is_power_of_2(8))
        self.assertTrue(is_power_of_2(16))
        self.assertTrue(is_power_of_2(1024))

    def test_not_power_of_2(self):
        self.assertFalse(is_power_of_2(0))
        self.assertFalse(is_power_of_2(3))
        self.assertFalse(is_power_of_2(5))
        self.assertFalse(is_power_of_2(6))
        self.assertFalse(is_power_of_2(9))
        self.assertFalse(is_power_of_2(1023))

    def test_negative_numbers(self):
        self.assertFalse(is_power_of_2(-1))
        self.assertFalse(is_power_of_2(-2))
        self.assertFalse(is_power_of_2(-4))

    def test_positive_numbers(self):
        self.assertEqual(twos_complement(1), -1)
        self.assertEqual(twos_complement(2), -2)
        self.assertEqual(twos_complement(10), -10)

    def test_negative_numbers_twos_complement(self):
        self.assertEqual(twos_complement(-1), 1)
        self.assertEqual(twos_complement(-2), 2)
        self.assertEqual(twos_complement(-10), 10)

    def test_zero(self):
        self.assertEqual(twos_complement(0), 0)

if __name__ == '__main__':
    unittest.main()
