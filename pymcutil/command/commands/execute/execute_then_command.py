from pymcutil.command.command import Command
from .._execute_command import ExecuteCommand

CMD = 'then'


class ExecuteThenCommand(ExecuteCommand):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute then ...

    http://minecraft.gamepedia.com/Commands#execute
    """

    def __init__(self, command: Command):
        self.command: Command = command

    def params(self):
        yield from super().params()
        yield from (CMD, self.command)


then = ExecuteThenCommand
