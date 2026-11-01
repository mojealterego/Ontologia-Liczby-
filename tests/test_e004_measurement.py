"""Tests of arithmetic and geometric invariants used in E0-04."""
import unittest
from fractions import Fraction


class MeasurementE004(unittest.TestCase):
    def test_length_conversion(self):
        for cm in range(1001):
            self.assertEqual(Fraction(cm, 100) * 100, cm)

    def test_area_conversion(self):
        for a in range(1, 50):
            for b in range(1, 50):
                self.assertEqual(Fraction(100 * a * 100 * b, 10000), a * b)

    def test_volume_conversion(self):
        self.assertEqual(10 ** 3, 1000)
        self.assertEqual(20 * 10 * 5, 1000)

    def test_scale_area(self):
        for n in (10, 100, 200, 50000):
            for a, b in ((3, 5), (4, 7), (8, 11)):
                self.assertEqual((a * n) * (b * n), a * b * n * n)

    def test_triangle_inequality(self):
        for x in range(-10, 11):
            for y in range(-10, 11):
                for z in range(-10, 11):
                    self.assertLessEqual(abs(x - z), abs(x - y) + abs(y - z))

    def test_interval_addition(self):
        for x in range(9, 12):
            for y in range(14, 17):
                self.assertTrue(23 <= x + y <= 27)

    def test_examples(self):
        self.assertEqual(3 * 50000, 150000)
        self.assertEqual(Fraction(1800, 35), Fraction(360, 7))
        self.assertEqual(8 * 25000, 200000)
        self.assertEqual(3 * 200 * 5 * 200, 600000)

    def test_time_midnight(self):
        self.assertEqual((24 * 60 - 23 * 60 - 50) + 20, 30)
        self.assertEqual((24 * 60 - 22 * 60 - 50) + 10, 80)


if __name__ == "__main__":
    unittest.main(verbosity=2)
