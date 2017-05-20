import unittest

from pymcutil.data_tag.float_data_tag import FloatDataTag


class FloatDataTagTestCase(unittest.TestCase):
    def test_default(self):
        dt = FloatDataTag()
        self.assertEqual(dt.value, 0.0)
        self.assertEqual(dt.to_str(), '0.0f')

    def test_positive(self):
        dt = FloatDataTag(123.5)
        self.assertEqual(dt.value, 123.5)
        self.assertEqual(dt.to_str(), '123.5f')

    def test_negative(self):
        dt = FloatDataTag(-123.5)
        self.assertEqual(dt.value, -123.5)
        self.assertEqual(dt.to_str(), '-123.5f')

    def test_int_conversion(self):
        dt = FloatDataTag(123)
        self.assertEqual(dt.value, 123.0)
        self.assertEqual(dt.to_str(), '123.0f')

    def test_equality(self):
        dt1 = FloatDataTag(123.5)
        dt2 = FloatDataTag(123.5)
        self.assertEqual(dt1, dt2)
