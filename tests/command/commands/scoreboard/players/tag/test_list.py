import unittest

from pymcutil.command import commands
from pymcutil.selector import selectors


class ScoreboardPlayersTagAddCommandTestCase(unittest.TestCase):
    def test(self):
        cmd = commands.scoreboard.players.tag.list(
            target=selectors.SELF)
        self.assertEqual(str(cmd), 'scoreboard players tag @s list')
