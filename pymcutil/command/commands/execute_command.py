from typing import Iterable, Mapping

from pymcutil.block.block import Block
from pymcutil.command.command import Command
from pymcutil.command.commands.detect_command import DetectCommand
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


def execute_detect(
        target: Target, command: Command, block: Block = None, block_id: str = None, block_state: Mapping = None,
        detect_position: Iterable = ZERO_OFFSET, execute_position: Iterable = ZERO_OFFSET):
    """ Convenience method for alternate execute command syntax. """
    return ExecuteCommand(
        target=target,
        command=DetectCommand(
            command=command,
            block=block,
            block_id=block_id,
            block_state=block_state,
            position=detect_position),
        position=execute_position)
