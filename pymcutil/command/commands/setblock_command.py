from typing import Union

from pymcutil.block.block import Block
from pymcutil.command.command import Command
from pymcutil.position.position import Position

CMD = 'setblock'


class SetblockCommand(Command):
    """
    An objective model of Minecraft's `setblock` command:

        setblock <x y z> <block> [oldBlockHandling]

    http://minecraft.gamepedia.com/Commands#setblock
    """

    def __init__(self, position: Position.Generic, block: Block.Generic, old_block_handling: str = None):
        self.position: Position = Position.sift(position)
        self.block: Block = Block.sift(block)
        self.old_block_handling: Union[str, None] = old_block_handling

    def params(self):
        yield from (
            CMD, self.position, self.block,
            (self.old_block_handling, 'replace'))


setblock = SetblockCommand
