import unittest

from pymcutil.command import commands
from pymcutil.selector import selectors


class ExecuteAsCommandTestCase(unittest.TestCase):
    def test_without_data_tag(self):
        cmd = commands.execute.as_(
            target=selectors.SELF,
            subcommand=commands.execute.then(commands.say('hello')))
        self.assertEqual(str(cmd), 'execute as @s then say hello')
