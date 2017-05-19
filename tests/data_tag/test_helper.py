import unittest

from pymcutil.data_tag.helper import data_taggify


class ByteDataTagTestCase(unittest.TestCase):
    def test_convert_data_tag(self):
        dt1 = data_taggify('hello')
        dt2 = data_taggify(dt1)
        self.assertEqual(dt1, dt2)

    def test_unconvertible(self):
        with self.assertRaises(TypeError):
            data_taggify(None)
