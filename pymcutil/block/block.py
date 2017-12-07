from collections import Mapping
from typing import Union

from pymcutil.block.block_state import BlockState
from pymcutil.util.siftable import Siftable


class Block(Siftable):
    """ Represents a Minecraft block. """

    Generic = Union['Block', str]

    def __init__(self, block_id: str, block_state: Mapping = None):
        self.block_id: str = block_id
        self.block_state: BlockState = BlockState.sift(block_state, {})

    def __str__(self):
        return ''.join((
            self.block_id,
            '[{}]'.format(self.block_state) if self.block_state else ''))

    @classmethod
    def _from_other(cls, obj):
        if isinstance(obj, str):
            return Block(block_id=obj)  # TODO parse state and nbt

    def state(self, *args, **params):
        new_block_state = dict(self.block_state)  # copy
        new_block_state.update(*args, **params)
        return Block(block_id=self.block_id, block_state=new_block_state)
