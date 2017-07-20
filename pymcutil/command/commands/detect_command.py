from typing import Iterable

from pymcutil.block.block import Block
from pymcutil.block.blockable import Blockable
from pymcutil.command.command import Command
from pymcutil.position.position import Position

CMD = 'detect'


class DetectCommand(Command):
    """
    An objective model of Minecraft's `detect` command:

        detect <x y z> <block> <command>

    http://minecraft.gamepedia.com/Commands#detect
    """

    def __init__(self, position: Iterable, block: Blockable, command: Command):
        self.position: Position = Position.sift(position)
        self.block: Block = Block.sift(block)
        self.command: Command = command

    def params(self):
        yield from (CMD, self.position, self.block, self.command)


detect = DetectCommand
