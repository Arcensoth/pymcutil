import abc
from typing import Tuple


class ResourceReference(abc.ABC):
    @property
    @abc.abstractmethod
    def params(self) -> Tuple:
        """ Return parameters to be used when generating the resource. """
