import unittest

from pymcutil.command import commands
from pymcutil.selector import selectors


class AtCommandTestCase(unittest.TestCase):
    def test(self):
        cmd = commands.at(
            selectors.SELF,
            command=commands.say(message='hello'))
        self.assertEqual(str(cmd), 'at @s say hello')
