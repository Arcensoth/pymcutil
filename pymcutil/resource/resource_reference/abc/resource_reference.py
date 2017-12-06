import abc
import collections
import typing


class ResourceReference(abc.ABC, collections.Hashable):
    @property
    @abc.abstractmethod
    def params(self) -> typing.Iterable:
        """ Yield parameters to be used when generating the resource. """
