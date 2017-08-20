from typing import Union

from pymcutil.block.block import Block
from pymcutil.position.position import Position
from .._execute_command import ExecuteCommand


class ExecuteConditionalBlockMixin(object):
    def __init__(self, position: Position.Generic, block: Block.Generic, subcommand: ExecuteCommand = None):
        self.position: Position = Position.sift(position)
        self.block: Block = Block.sift(block)
        self.subcommand: Union[ExecuteCommand, None] = subcommand
