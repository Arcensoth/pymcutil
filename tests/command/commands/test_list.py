import unittest

from pymcutil.command import commands


class ScoreboardPlayersTagAddCommandTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            str(commands.scoreboard.players.tag.list(
                target='@p')),
            'scoreboard players tag @p list')
