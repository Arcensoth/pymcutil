import unittest

from pymcutil.command import commands
from pymcutil.data_tag.compound_data_tag import CompoundDataTag


class ScoreboardPlayersTagAddCommandTestCase(unittest.TestCase):
    def test_without_data_tag(self):
        self.assertEqual(
            str(commands.scoreboard.players.tag.add(
                target='@p',
                tag='some_tag')),
            'scoreboard players tag @p add some_tag')

    def test_with_data_tag(self):
        self.assertEqual(
            str(commands.scoreboard.players.tag.add(
                target='@p',
                tag='on_ground',
                data_tag=CompoundDataTag({'OnGround': True}))),
            'scoreboard players tag @p add on_ground {OnGround:1b}')
