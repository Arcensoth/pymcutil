import unittest

from pymcutil.data_tag.string_data_tag import StringDataTag


class StringDataTagTestCase(unittest.TestCase):
    def test_default(self):
        dt = StringDataTag()
        self.assertEqual(dt.value, '')
        self.assertEqual(dt.to_str(), '""')

    def test_empty_string(self):
        dt = StringDataTag('')
        self.assertEqual(dt.value, '')
        self.assertEqual(dt.to_str(), '""')

    def test_simple_string(self):
        dt = StringDataTag('mystring')
        self.assertEqual(dt.value, 'mystring')
        self.assertEqual(dt.to_str(), 'mystring')

    def test_int_conversion(self):
        dt = StringDataTag(123)
        self.assertEqual(dt.value, '123')
        self.assertEqual(dt.to_str(), '123')

    def test_float_conversion(self):
        dt = StringDataTag(12.34)
        self.assertEqual(dt.value, '12.34')
        self.assertEqual(dt.to_str(), '12.34')

    def test_breaking_str(self):
        dt = StringDataTag('my:string')
        self.assertEqual(dt.value, 'my:string')
        self.assertEqual(dt.to_str(), '"my:string"')

    def test_quoted_str(self):
        dt = StringDataTag('"mystring"')
        self.assertEqual(dt.value, '"mystring"')
        self.assertEqual(dt.to_str(), r'"\"mystring\""')

    def test_equality(self):
        dt1 = StringDataTag('hello')
        dt2 = StringDataTag('hello')
        self.assertEqual(dt1, dt2)
