import unittest

from pymcutil.command import commands
from pymcutil.selector import selectors


class FunctionCommandTestCase(unittest.TestCase):
    def test_without_any_optionals(self):
        cmd = commands.function(
            function='foo')
        self.assertEqual(str(cmd), 'function foo')

    def test_default_optionals(self):
        cmd = commands.function(
            function='foo',
            mode_target=selectors.SELF)
        self.assertEqual(str(cmd), 'function foo if @s')

    def test_up_to_mode(self):
        cmd = commands.function(
            function='foo',
            mode='if')
        self.assertEqual(str(cmd), 'function foo if')

    def test_up_to_mode_target(self):
        cmd = commands.function(
            function='foo',
            mode='if',
            mode_target=selectors.SELF)
        self.assertEqual(str(cmd), 'function foo if @s')
