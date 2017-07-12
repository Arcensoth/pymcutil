from collections import Mapping

from pymcutil.block.block_state import BlockState


class Block(object):
    """ Represents a Minecraft block. """

    def __init__(self, block_id: str, block_state: Mapping = None):
        self.block_id: str = block_id
        self.block_state: BlockState = BlockState.sift(block_state, {})

    def state(self, *args, **params):
        new_block_state = dict(self.block_state)  # copy
        new_block_state.update(*args, **params)
        return Block(block_id=self.block_id, block_state=new_block_state)
