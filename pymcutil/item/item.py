import abc
from collections import Mapping

from pymcutil.data_tag.compound_data_tag import CompoundDataTag


class Item(abc.ABC):
    """ Represents a Minecraft item. """

    def __init__(self, item_id: str, data_tag: Mapping = None):
        self.item_id: str = item_id
        self.data_tag: CompoundDataTag = CompoundDataTag.sift(data_tag, {})

    def tag(self, *args, **params):
        new_data_tag = dict(self.data_tag)  # copy
        new_data_tag.update(*args, **params)
        return Item(item_id=self.item_id, data_tag=new_data_tag)
