import unittest

from pymcutil.selector.selector_arguments import SelectorArguments


class SelectorArgumentsTestCase(unittest.TestCase):
    def test(self):
        args = SelectorArguments(limit=5)
        print(args.limit)
