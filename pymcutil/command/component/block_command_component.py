from typing import Union, Mapping

from pymcutil.block.block import Block
from pymcutil.block.block_entity import BlockEntity
from pymcutil.block.block_state import BlockState
from pymcutil.command.component.command_component import CommandComponent
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.util import first, require


class BlockCommandComponent(CommandComponent):
    def __init__(
            self, block: Block = None, block_id: str = None, block_state: Mapping = None, data_tag: Mapping = None):
        self.block_id: str = require(first(block_id, block.block_id if block else None), 'block_id')
        self.block_state: Union[BlockState, None] = BlockState.sift(
            first(block_state, block.block_state if block else None), None)
        self.data_tag: Union[CompoundDataTag, None] = CompoundDataTag.sift(
            first(data_tag, block.data_tag if isinstance(block, BlockEntity) else None), None)

    def __str__(self):
        return ''.join((
            self.block_id,
            '[{}]'.format(self.block_state) if self.block_state is not None else '',
            str(self.data_tag) if self.data_tag is not None else ''))

    @property
    def block_state_safe(self) -> BlockState:
        return first(self.block_state, BlockState())

    @property
    def data_tag_safe(self) -> CompoundDataTag:
        return first(self.data_tag, CompoundDataTag())
