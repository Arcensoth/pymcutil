from typing import Iterable

from pymcutil.command.command import Command
from pymcutil.command.target import Target
from pymcutil.position.position import Position, ZERO_OFFSET

CMD = 'execute'


class ExecuteCommand(Command):
    """
    An objective model of Minecraft's `execute` command:

        execute <entity> <x> <y> <z> <command ...>

    http://minecraft.gamepedia.com/Commands#execute
    """

    def __init__(self, target: Target, command: Command, position: Iterable = ZERO_OFFSET):
        self.target: Target = target
        self.position: Position = Position.sift(position)
        self.command = command

    def params(self):
        yield from (CMD, self.target, self.position, self.command)


def execute(target: Target, command: Command, position: Iterable = ZERO_OFFSET) -> ExecuteCommand:
    """ Functional alias for creating `ExecuteCommand` instances. """
    return ExecuteCommand(**locals())
