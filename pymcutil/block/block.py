import abc
from collections import Mapping

from pymcutil.block.block_state import BlockState


class Block(abc.ABC):
    """ Represents a Minecraft block. """

    def __init__(self, block_id: str, block_state: Mapping = None):
        self.block_id: str = block_id
        self.block_state: BlockState = BlockState.sift(block_state, {})
