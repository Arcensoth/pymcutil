import abc
from typing import Any


class Serializable(abc.ABC):
    """ An object that can be serialized into a composition of basic values. """

    @property
    @abc.abstractmethod
    def serialized(self) -> Any:
        """ Returns a serialized representation of the object. This *serialized representation* should be composed
        entirely of atomic values (ints, strs, bools, etc), lists, and dicts. Simply put, it should be serializable into
        JSON using `json.dump()`. """
