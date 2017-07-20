import unittest

from pymcutil.command import commands
from pymcutil.selector import selectors


class AsCommandTestCase(unittest.TestCase):
    def test(self):
        cmd = commands.as_(
            selectors.SELF,
            command=commands.say(message='hello'))
        self.assertEqual(str(cmd), 'as @s say hello')
