import unittest

from pymcutil.command import commands
from pymcutil.position.position import Position
from pymcutil.selector import selectors


class ExecuteCommandTestCase(unittest.TestCase):
    def test_without_position(self):
        cmd = commands.execute(
            target=selectors.SELF,
            command=commands.say(
                message='hi'))
        self.assertEqual(str(cmd), 'execute @s ~ ~ ~ say hi')

    def test_with_absolute_position(self):
        cmd = commands.execute(
            target=selectors.SELF,
            command=commands.say(
                message='hi'),
            position=(1, 2, 3))
        self.assertEqual(str(cmd), 'execute @s 1 2 3 say hi')

    def test_with_relative_position(self):
        cmd = commands.execute(
            target=selectors.SELF,
            command=commands.say(
                message='hi'),
            position=~Position(1, 2, 3))
        self.assertEqual(str(cmd), 'execute @s ~1 ~2 ~3 say hi')

    def test_detect(self):
        cmd = commands.execute_detect(
            target=selectors.SELF,
            command=commands.say(
                message='hi'),
            block_id='minecraft:dropper',
            block_state=dict(facing='up'),
            detect_position=~Position(0, -1, 0))
        self.assertEqual(str(cmd), 'execute @s ~ ~ ~ detect ~ ~-1 ~ minecraft:dropper[facing=up] say hi')
