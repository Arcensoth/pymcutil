import unittest

from pymcutil import util


class UtilTestCase(unittest.TestCase):
    def test_default_with_value(self):
        self.assertEqual(util.default('hello'), 'hello')

    def test_default_with_value_and_default(self):
        self.assertEqual(util.default('hello', 'world'), 'hello')

    def test_default_with_value_none_and_default(self):
        self.assertEqual(util.default(None, 'world'), 'world')

    def test_default_with_value_none_and_default_none(self):
        self.assertEqual(util.default(None, None), None)

    def test_defaults(self):
        self.assertEqual(
            util.defaults(dict(a='alpha', b='beta'), b='bravo', c='charlie'),
            dict(a='alpha', b='beta', c='charlie'))

    def test_first_immediate(self):
        self.assertEqual(util.first('a', 'b', 'c'), 'a')

    def test_first_eventually(self):
        self.assertEqual(util.first(None, None, None, 'a', 'b', 'c'), 'a')

    def test_first_none(self):
        self.assertEqual(util.first(None, None, None), None)

    def test_require(self):
        self.assertEqual(util.require(123, 'number'), 123)

    def test_require_error(self):
        with self.assertRaises(ValueError):
            util.require(None, 'number')

    def test_get_logger(self):
        log = util.get_logger([], 'mylist')
        self.assertEqual(log.name, 'list:mylist')
