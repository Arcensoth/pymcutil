from typing import Mapping, Iterable, Union

from pymcutil.block.block import Block
from pymcutil.command.command import Command
from pymcutil.command.component.block_command_component import BlockCommandComponent
from pymcutil.position.position import Position
from pymcutil.util import first

CMD = 'setblock'


class SetblockCommand(Command):
    """
    An objective model of Minecraft's `setblock` command:

        setblock <x> <y> <z> <block> [state] [oldBlockHandling] [dataTag]

    http://minecraft.gamepedia.com/Commands#setblock
    """

    def __init__(
            self, position: Iterable, block: Block = None, block_id: str = None, block_state: Mapping = None,
            old_block_handling: str = None, data_tag: Mapping = None):
        self.position: Position = Position.sift(position)
        self.block_cc: BlockCommandComponent = BlockCommandComponent(
            block=block, block_id=block_id, block_state=block_state, data_tag=data_tag)
        self.old_block_handling: Union[str, None] = old_block_handling

    def params(self):
        yield from (CMD, self.position, self.block_cc.block_id)

        if self.block_cc.data_tag is not None:
            yield from (self.block_cc.block_state_safe, self.old_block_handling_safe, self.block_cc.data_tag)

        elif self.old_block_handling is not None:
            yield from (self.block_cc.block_state_safe, self.old_block_handling)

        elif self.block_cc.block_state is not None:
            yield self.block_cc.block_state

    @property
    def old_block_handling_safe(self) -> str:
        return first(self.old_block_handling, 'replace')


def setblock(
        position: Iterable, block: Block = None, block_id: str = None, block_state: Mapping = None,
        old_block_handling: str = None, data_tag: Mapping = None) -> SetblockCommand:
    """ Functional alias for creating `SetblockCommand` instances. """
    return SetblockCommand(**locals())
