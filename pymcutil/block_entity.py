from collections import Mapping

from pymcutil.block import Block
from pymcutil.data_tag import DataTag
from pymcutil.data_tag.compound_data_tag import CompoundDataTag


class BlockEntity(Block):
    """ Represents a Minecraft block entity. """

    def __init__(self, block_id: str, block_state: Mapping = None, data_tag: Mapping = None):
        super().__init__(block_id=block_id, block_state=block_state)
        self.data_tag: DataTag = CompoundDataTag(**(data_tag or {}))
