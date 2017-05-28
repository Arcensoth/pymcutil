import unittest

from pymcutil.command import commands
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.selector import selectors


class ScoreboardPlayersTagRemoveCommandTestCase(unittest.TestCase):
    def test_without_data_tag(self):
        cmd = commands.scoreboard.players.tag.remove(
            target=selectors.PLAYER,
            tag='some_tag')
        self.assertEqual(str(cmd), 'scoreboard players tag @p remove some_tag')

    def test_with_data_tag(self):
        cmd = commands.scoreboard.players.tag.remove(
            target=selectors.PLAYER,
            tag='on_ground',
            data_tag=CompoundDataTag({'OnGround': False}))
        self.assertEqual(str(cmd), 'scoreboard players tag @p remove on_ground {OnGround:0b}')
