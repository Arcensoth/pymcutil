import abc
import collections
from typing import Tuple


class ResourceReference(abc.ABC, collections.Hashable):
    @property
    @abc.abstractmethod
    def params(self) -> Tuple:
        """ Return parameters to be used when generating the resource. """
