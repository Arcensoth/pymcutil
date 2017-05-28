import abc
from typing import Iterator, Any


class Command(abc.ABC):
    """ An abstract base class representing a Minecraft command. """

    def __str__(self):
        return self.to_str()

    def to_str(self) -> str:
        # TODO Clean up this mess.
        params = []
        skip = True
        for p in reversed(list(self.params())):
            value, default = p if isinstance(p, tuple) else (p, None)
            if skip:
                skip = value is None
                if skip:
                    continue
            final_value = value if value is not None else default
            if final_value is None:
                raise ValueError('Command parameter required but not given')
            params.append(final_value)
        return ' '.join(str(p) for p in reversed(params))

    @abc.abstractmethod
    def params(self) -> Iterator[Any]:
        """ Yield command parameters as pairs of (value, default). """
