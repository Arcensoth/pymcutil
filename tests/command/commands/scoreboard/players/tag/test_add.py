import unittest

from pymcutil.command import commands
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.selector import selectors


class ScoreboardPlayersTagAddCommandTestCase(unittest.TestCase):
    def test_without_data_tag(self):
        cmd = commands.scoreboard.players.tag.add(
            target=selectors.PLAYER,
            tag='some_tag')
        self.assertEqual(str(cmd), 'scoreboard players tag @p add some_tag')

    def test_with_data_tag(self):
        cmd = commands.scoreboard.players.tag.add(
            target=selectors.PLAYER,
            tag='on_ground',
            data_tag=CompoundDataTag({'OnGround': True}))
        self.assertEqual(str(cmd), 'scoreboard players tag @p add on_ground {OnGround:1b}')
