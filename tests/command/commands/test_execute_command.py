import unittest

from pymcutil.command import commands
from pymcutil.position.position import Position
from pymcutil.selector import selectors


class ExecuteCommandTestCase(unittest.TestCase):
    def test_without_position(self):
        cmd = commands.execute(
            target=selectors.PLAYER,
            command=commands.say(
                message='hi'))
        self.assertEqual(str(cmd), 'execute @p ~ ~ ~ say hi')

    def test_with_absolute_position(self):
        cmd = commands.execute(
            target=selectors.PLAYER,
            command=commands.say(
                message='hi'),
            position=(1, 2, 3))
        self.assertEqual(str(cmd), 'execute @p 1 2 3 say hi')

    def test_with_relative_position(self):
        cmd = commands.execute(
            target=selectors.PLAYER,
            command=commands.say(
                message='hi'),
            position=~Position(1, 2, 3))
        self.assertEqual(str(cmd), 'execute @p ~1 ~2 ~3 say hi')
