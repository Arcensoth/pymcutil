import unittest

from pymcutil.command import commands
from pymcutil.selector import selectors


class ScoreboardPlayersTagAddCommandTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            str(commands.scoreboard.players.tag.list(
                target=selectors.PLAYER)),
            'scoreboard players tag @p list')
