import unittest

from pymcutil.command import commands
from pymcutil.position.position import ZERO_OFFSET


class OffsetCommandTestCase(unittest.TestCase):
    def test(self):
        cmd = commands.offset(
            position=ZERO_OFFSET,
            command=commands.say(message='hello'))
        self.assertEqual(str(cmd), 'offset ~ ~ ~ say hello')
