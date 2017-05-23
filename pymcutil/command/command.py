import abc
from typing import Iterator, Any


class Command(abc.ABC):
    """ An abstract base class representing a Minecraft command. """

    def __str__(self):
        return self.to_str()

    def to_str(self) -> str:
        return ' '.join(str(p) for p in self.params())

    @abc.abstractmethod
    def params(self) -> Iterator[Any]:
        """ Yield command parameters. """
