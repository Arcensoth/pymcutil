import unittest

from pymcutil.data_tag.double_data_tag import DoubleDataTag


class DoubleDataTagTestCase(unittest.TestCase):
    def test_default(self):
        dt = DoubleDataTag()
        self.assertEqual(dt.value, 0.0)
        self.assertEqual(dt.to_str(), '0.0d')

    def test_positive(self):
        dt = DoubleDataTag(456.5)
        self.assertEqual(dt.value, 456.5)
        self.assertEqual(dt.to_str(), '456.5d')

    def test_negative(self):
        dt = DoubleDataTag(-456.5)
        self.assertEqual(dt.value, -456.5)
        self.assertEqual(dt.to_str(), '-456.5d')

    def test_int_conversion(self):
        dt = DoubleDataTag(456)
        self.assertEqual(dt.value, 456.0)
        self.assertEqual(dt.to_str(), '456.0d')

    def test_equality(self):
        dt1 = DoubleDataTag(456.5)
        dt2 = DoubleDataTag(456.5)
        self.assertEqual(dt1, dt2)
