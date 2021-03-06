import unittest

from pymcutil.command import commands
from pymcutil.selector import selectors


class EffectGiveCommandTestCase(unittest.TestCase):
    def test_without_any_optionals(self):
        cmd = commands.effect.give(
            target=selectors.SELF,
            effect='strength')
        self.assertEqual(str(cmd), 'effect give @s strength')

    def test_default_optionals(self):
        cmd = commands.effect.give(
            target=selectors.SELF,
            effect='strength',
            hide_particles=True)
        self.assertEqual(str(cmd), 'effect give @s strength 1000000 0 true')

    def test_up_to_seconds(self):
        cmd = commands.effect.give(
            target=selectors.SELF,
            effect='strength',
            seconds=60)
        self.assertEqual(str(cmd), 'effect give @s strength 60')

    def test_up_to_amplifier(self):
        cmd = commands.effect.give(
            target=selectors.SELF,
            effect='strength',
            seconds=60,
            amplifier=5)
        self.assertEqual(str(cmd), 'effect give @s strength 60 5')

    def test_up_to_hide_particles(self):
        cmd = commands.effect.give(
            target=selectors.SELF,
            effect='strength',
            seconds=60,
            amplifier=5,
            hide_particles=True)
        self.assertEqual(str(cmd), 'effect give @s strength 60 5 true')
