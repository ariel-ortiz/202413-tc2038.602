import unittest
from euclidean import gcd

class TestGCD(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(101, 10), 1)

    def test_edge_case_zero_zero(self):
        with self.assertRaises(ValueError):
            gcd(0, 0)

    def test_one_zero_input(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)

    def test_same_inputs(self):
        self.assertEqual(gcd(7, 7), 7)
        self.assertEqual(gcd(100, 100), 100)

if __name__ == '__main__':
    unittest.main()
