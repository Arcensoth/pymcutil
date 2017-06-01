import unittest

from pymcutil.command import commands
from pymcutil.selector import selectors


class ScoreboardPlayersTagAddCommandTestCase(unittest.TestCase):
    def test(self):
        cmd = commands.scoreboard.players.tag.list(
            target=selectors.PLAYER)
        self.assertEqual(str(cmd), 'scoreboard players tag @p list')
