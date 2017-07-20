from pymcutil.command.command import Command
from pymcutil.position.position import Position

CMD = 'offset'


class OffsetCommand(Command):
    """
    An objective model of Minecraft's `offset` command:

        offset <x y z> <command>

    http://minecraft.gamepedia.com/Commands#offset
    """

    def __init__(self, position: Position.Generic, command: Command):
        self.position: Position = Position.sift(position)
        self.command: Command = command

    def params(self):
        yield from (CMD, self.position, self.command)


offset = OffsetCommand
