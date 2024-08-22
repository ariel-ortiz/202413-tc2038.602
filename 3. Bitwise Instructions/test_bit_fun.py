import unittest
from bit_fun import is_even, is_power_of_2, twos_complement, \
    int_mul, bin_with_num_bits

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

    def test_negative_numbers_is_power_of_2(self):
        self.assertFalse(is_power_of_2(-1))
        self.assertFalse(is_power_of_2(-2))
        self.assertFalse(is_power_of_2(-4))

    def test_positive_numbers_twos_complement(self):
        self.assertEqual(twos_complement(1), -1)
        self.assertEqual(twos_complement(2), -2)
        self.assertEqual(twos_complement(10), -10)

    def test_negative_numbers_twos_complement(self):
        self.assertEqual(twos_complement(-1), 1)
        self.assertEqual(twos_complement(-2), 2)
        self.assertEqual(twos_complement(-10), 10)

    def test_zero_twos_complement(self):
        self.assertEqual(twos_complement(0), 0)

    def test_positive_numbers_int_mul(self):
        self.assertEqual(int_mul(3, 4), 12)
        self.assertEqual(int_mul(7, 5), 35)
        self.assertEqual(int_mul(0, 5), 0)
        self.assertEqual(int_mul(666, 12345), 8221770)

    def test_negative_numbers_int_mul(self):
        self.assertEqual(int_mul(-3, 4), -12)
        self.assertEqual(int_mul(3, -4), -12)
        self.assertEqual(int_mul(-3, -4), 12)
        self.assertEqual(int_mul(666, -12345), -8221770)
        self.assertEqual(int_mul(-666, 12345), -8221770)

    def test_zero_int_mul(self):
        self.assertEqual(int_mul(0, 0), 0)
        self.assertEqual(int_mul(0, 5), 0)
        self.assertEqual(int_mul(5, 0), 0)

    def test_positive_numbers_bin_with_num_bits(self):
        self.assertEqual(bin_with_num_bits(3, 3), '011')
        self.assertEqual(bin_with_num_bits(5, 4), '0101')
        self.assertEqual(bin_with_num_bits(7, 4), '0111')
        self.assertEqual(bin_with_num_bits(255, 8), '11111111')

    def test_negative_numbers_bin_with_num_bits(self):
        self.assertEqual(bin_with_num_bits(-1, 3), '111')
        self.assertEqual(bin_with_num_bits(-2, 3), '110')
        self.assertEqual(bin_with_num_bits(-4, 4), '1100')
        self.assertEqual(bin_with_num_bits(-1, 16), '1111111111111111')
        self.assertEqual(bin_with_num_bits(-666, 16), '1111110101100110')

    def test_zero_bin_with_num_bits(self):
        self.assertEqual(bin_with_num_bits(0, 3), '000')
        self.assertEqual(bin_with_num_bits(0, 8), '00000000')

    def test_value_error_bin_with_num_bits(self):
        with self.assertRaises(ValueError):
            bin_with_num_bits(8, 3)  # 8 cannot fit in 3 bits
        with self.assertRaises(ValueError):
            bin_with_num_bits(-5, 3)  # -5 cannot fit in 3 bits
        with self.assertRaises(ValueError):
            bin_with_num_bits(16, 4)  # 16 cannot fit in 4 bits
        with self.assertRaises(ValueError):
            bin_with_num_bits(1, 0)  # 1 cannot fit in 0 bits


if __name__ == '__main__':
    unittest.main()
