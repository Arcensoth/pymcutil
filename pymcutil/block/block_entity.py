from collections import Mapping

from pymcutil.block.block import Block
from pymcutil.data_tag.compound_data_tag import CompoundDataTag


class BlockEntity(Block):
    """ Represents a Minecraft block entity. """

    def __init__(self, block_id: str, block_state: Mapping = None, data_tag: Mapping = None):
        super().__init__(block_id=block_id, block_state=block_state)
        self.data_tag: CompoundDataTag = CompoundDataTag.sift(data_tag, {})

    def __str__(self):
        return ''.join(
            (super().__str__(),
             str(self.data_tag) if self.data_tag else ''))

    def tag(self, *args, **params):
        new_data_tag = dict(self.data_tag)  # copy
        new_data_tag.update(*args, **params)
        return BlockEntity(block_id=self.block_id, block_state=self.block_state, data_tag=new_data_tag)
