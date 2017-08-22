from typing import Union

from pymcutil.position.position import Position
from .._execute_command import ExecuteCommand

CMD = 'offset'


class ExecuteOffsetCommand(ExecuteCommand):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute offset <pos: x y z> -> execute

    http://minecraft.gamepedia.com/Commands#execute
    """

    def __init__(self, position: Position.Generic, subcommand: ExecuteCommand = None):
        self.position: Position = Position.sift(position)
        self.subcommand: Union[ExecuteCommand, None] = subcommand

    def params(self):
        yield from super().params()
        yield from (
            CMD, self.position,
            (self.subcommand.substr(), None))


offset = ExecuteOffsetCommand
