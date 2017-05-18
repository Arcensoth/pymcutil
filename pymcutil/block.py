import abc

from pymcutil.block_state import BlockState


class Block(abc.ABC):
    """ Represents a Minecraft block. """

    def __init__(self, block_id: str, block_state: BlockState = None):
        self.block_id: str = block_id
        self.block_state: BlockState = block_state if block_state is not None else BlockState()
