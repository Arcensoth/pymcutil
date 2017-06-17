import abc
from collections import Mapping

from pymcutil.data_tag.compound_data_tag import CompoundDataTag


class Entity(abc.ABC):
    """ Represents a Minecraft entity. """

    def __init__(self, entity_id: str, data_tag: Mapping = None):
        self.entity_id: str = entity_id
        self.data_tag: CompoundDataTag = CompoundDataTag.sift(data_tag, {})

    def tag(self, *args, **params):
        new_data_tag = dict(self.data_tag)  # copy
        new_data_tag.update(*args, **params)
        return Entity(entity_id=self.entity_id, data_tag=new_data_tag)
