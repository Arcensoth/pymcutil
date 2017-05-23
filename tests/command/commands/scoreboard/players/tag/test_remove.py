import unittest

from pymcutil.command import commands
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.selector import selectors


class ScoreboardPlayersTagAddCommandTestCase(unittest.TestCase):
    def test_without_data_tag(self):
        self.assertEqual(
            str(commands.scoreboard.players.tag.remove(
                target=selectors.PLAYER,
                tag='some_tag')),
            'scoreboard players tag @p remove some_tag')

    def test_with_data_tag(self):
        self.assertEqual(
            str(commands.scoreboard.players.tag.remove(
                target=selectors.PLAYER,
                tag='on_ground',
                data_tag=CompoundDataTag({'OnGround': False}))),
            'scoreboard players tag @p remove on_ground {OnGround:0b}')
