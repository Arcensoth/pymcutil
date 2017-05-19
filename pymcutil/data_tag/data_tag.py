import abc


class DataTag(abc.ABC):
    """ A generic data tag, to be used as an interface for all TAG types. """

    def __str__(self):
        return self.to_str()

    @abc.abstractmethod
    def to_str(self) -> str:
        """ Return a string serialization of the data tag, for example with quotes or a type suffix. """
