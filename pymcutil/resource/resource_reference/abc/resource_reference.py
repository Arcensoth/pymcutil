import abc
from typing import Iterable

from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation


class ResourceReference(abc.ABC):
    def __str__(self):
        return str(self.location)

    @abc.abstractmethod
    def locate(self, location: ResourceLocation):
        """ Resolve this `ResourceReference`s location to the given `location`. """

    @property
    @abc.abstractmethod
    def location(self) -> ResourceLocation:
        """ Return the resolved `ResourceLocation`. """

    @property
    @abc.abstractmethod
    def params(self) -> Iterable:
        """ Yield parameters to be used when generating the resource. """
