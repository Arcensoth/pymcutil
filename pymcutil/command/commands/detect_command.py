from typing import Iterable, Mapping

from pymcutil.block.block import Block
from pymcutil.command.command import Command
from pymcutil.command.component.block_command_component import BlockCommandComponent
from pymcutil.position.position import Position, ZERO_OFFSET

CMD = 'detect'


class DetectCommand(Command):
    """
    An objective model of the imaginary `detect` command:

        detect <x> <y> <z> <block> <state> <command ...>

    http://minecraft.gamepedia.com/Commands#execute

    *This is an imaginary command that is currently only utilized in an alternate form of the execute command.*
    """

    def __init__(
            self, command: Command, block: Block = None, block_id: str = None, block_state: Mapping = None,
            position: Iterable = ZERO_OFFSET):
        self.position: Position = Position.sift(position)
        self.block_cc: BlockCommandComponent = BlockCommandComponent(
            block=block, block_id=block_id, block_state=block_state)
        self.command = command

    def params(self):
        yield from (CMD, self.position, self.block_cc.block_id, self.block_cc.block_state, self.command)
