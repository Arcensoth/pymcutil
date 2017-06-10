import unittest

from pymcutil.command import commands


class SayCommandTestCase(unittest.TestCase):
    def test_without_spaces(self):
        cmd = commands.say(
            message='hi')
        self.assertEqual(str(cmd), 'say hi')

    def test_with_spaces(self):
        cmd = commands.say(
            message='hello world')
        self.assertEqual(str(cmd), 'say hello world')
