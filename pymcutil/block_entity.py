from pymcutil.block import Block
from pymcutil.block_state import BlockState
from pymcutil.data_tag import DataTag


class BlockEntity(Block):
    """ Represents a Minecraft block entity. """

    def __init__(self, block_id: str, block_state: BlockState = None, data_tag: DataTag = None):
        super().__init__(block_id=block_id, block_state=block_state)
        self.data_tag: DataTag = data_tag if data_tag is not None else DataTag()
