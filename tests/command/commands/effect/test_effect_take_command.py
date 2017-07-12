import unittest

from pymcutil.command import commands
from pymcutil.selector import selectors


class EffectTakeCommandTestCase(unittest.TestCase):
    def test_without_any_optionals(self):
        cmd = commands.effect.take(
            target=selectors.SELF)
        self.assertEqual(str(cmd), 'effect take @s')

    def test_up_to_effect(self):
        cmd = commands.effect.take(
            target=selectors.SELF,
            effect='strength')
        self.assertEqual(str(cmd), 'effect take @s strength')
