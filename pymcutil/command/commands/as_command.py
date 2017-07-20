from pymcutil.command.command import Command
from pymcutil.command.target import Target

CMD = 'as'


class AsCommand(Command):
    """
    An objective model of Minecraft's `as` command:

        as <entity> <command>

    http://minecraft.gamepedia.com/Commands#as
    """

    def __init__(self, target: Target, command: Command):
        self.target: Target = target
        self.command: Command = command

    def params(self):
        yield from (CMD, self.target, self.command)


as_ = AsCommand  # TODO Is it possible to have this be just 'as' without keyword conflict?
