import unittest

from pymcutil.selector.range import Range


class RangeTestCase(unittest.TestCase):
    def test_undefined(self):
        self.assertEqual(
            '..',
            str(Range(...)))

    def test_exact_int(self):
        self.assertEqual(
            '1',
            str(Range(1)))

    def test_at_least_int(self):
        self.assertEqual(
            '1..',
            str(Range(1, ...)))

    def test_at_most_int(self):
        self.assertEqual(
            '..2',
            str(Range(..., 2)))

    def test_from_to_int(self):
        self.assertEqual(
            '1..2',
            str(Range(1, 2)))

    def test_exact_float(self):
        self.assertEqual(
            '1.234',
            str(Range(1.234)))

    def test_at_least_float(self):
        self.assertEqual(
            '1.234..',
            str(Range(1.234, ...)))

    def test_at_most_float(self):
        self.assertEqual(
            '..2.345',
            str(Range(..., 2.345)))

    def test_from_to_float(self):
        self.assertEqual(
            '1.234..2.345',
            str(Range(1.234, 2.345)))

    def test_zero_conversion(self):
        self.assertEqual(
            Range(0),
            Range.sift(0))

    def test_int_conversion(self):
        self.assertEqual(
            Range(1),
            Range.sift(1))

    def test_float_conversion(self):
        self.assertEqual(
            Range(1.234),
            Range.sift(1.234))

    def test_tuple_conversion_at_least(self):
        self.assertEqual(
            Range(1, ...),
            Range.sift((1, ...)))

    def test_tuple_conversion_at_most(self):
        self.assertEqual(
            Range(..., 2),
            Range.sift((..., 2)))

    def test_tuple_conversion_from_to(self):
        self.assertEqual(
            Range(1, 2),
            Range.sift((1, 2)))

    def test_list_conversion_at_least(self):
        self.assertEqual(
            Range(1, ...),
            Range.sift([1, ...]))

    def test_list_conversion_at_most(self):
        self.assertEqual(
            Range(..., 2),
            Range.sift([..., 2]))

    def test_list_conversion_from_to(self):
        self.assertEqual(
            Range(1, 2),
            Range.sift([1, 2]))

    def test_string_conversion_exact_int(self):
        self.assertEqual(
            Range(1),
            Range.sift('1'))

    def test_string_conversion_at_least_int(self):
        self.assertEqual(
            Range(1, ...),
            Range.sift('1..'))

    def test_string_conversion_at_most_int(self):
        self.assertEqual(
            Range(..., 2),
            Range.sift('..2'))

    def test_string_conversion_from_to_int(self):
        self.assertEqual(
            Range(1, 2),
            Range.sift('1..2'))

    def test_string_conversion_exact_float(self):
        self.assertEqual(
            Range(1.234),
            Range.sift('1.234'))

    def test_string_conversion_at_least_float(self):
        self.assertEqual(
            Range(1.234, ...),
            Range.sift('1.234..'))

    def test_string_conversion_at_most_float(self):
        self.assertEqual(
            Range(..., 2.345),
            Range.sift('..2.345'))

    def test_string_conversion_from_to_float(self):
        self.assertEqual(
            Range(1.234, 2.345),
            Range.sift('1.234..2.345'))
