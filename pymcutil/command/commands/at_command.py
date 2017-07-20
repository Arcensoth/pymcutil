from pymcutil.command.command import Command
from pymcutil.command.target import Target

CMD = 'at'


class AtCommand(Command):
    """
    An objective model of Minecraft's `at` command:

        at <entity> <command>

    http://minecraft.gamepedia.com/Commands#at
    """

    def __init__(self, target: Target, command: Command):
        self.target: Target = target
        self.command: Command = command

    def params(self):
        yield from (CMD, self.target, self.command)


at = AtCommand
