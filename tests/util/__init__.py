import unittest

from pymcutil.util import default, defaults, first, require


class UtilTestCase(unittest.TestCase):
    def test_default_with_value(self):
        self.assertEqual(default('hello'), 'hello')

    def test_default_with_value_and_default(self):
        self.assertEqual(default('hello', 'world'), 'hello')

    def test_default_with_value_none_and_default(self):
        self.assertEqual(default(None, 'world'), 'world')

    def test_default_with_value_none_and_default_none(self):
        self.assertEqual(default(None, None), None)

    def test_defaults(self):
        self.assertEqual(
            defaults(dict(a='alpha', b='beta'), b='bravo', c='charlie'),
            dict(a='alpha', b='beta', c='charlie'))

    def test_first_immediate(self):
        self.assertEqual(first('a', 'b', 'c'), 'a')

    def test_first_eventually(self):
        self.assertEqual(first(None, None, None, 'a', 'b', 'c'), 'a')

    def test_first_none(self):
        self.assertEqual(first(None, None, None), None)

    def test_require(self):
        self.assertEqual(require(123, 'number'), 123)

    def test_require_error(self):
        with self.assertRaises(ValueError):
            require(None, 'number')
