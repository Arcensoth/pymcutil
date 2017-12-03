import abc
from typing import Iterable, Union

from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.located_resource.located_resource import LocatedResource
from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation


class ResourceDatabase(abc.ABC):
    @abc.abstractmethod
    def get(self, location: ResourceLocation) -> Union[LocatedResource, None]:
        """ Return the `LocatedResource` at the given `location` if available, otherwise `None`. """

    @abc.abstractmethod
    def put(self, location: ResourceLocation, resource: Resource) -> LocatedResource:
        """ Persist and return a `LocatedResource` consisting of the given `resource` at the given `location`. """

    @abc.abstractmethod
    def all(self) -> Iterable[LocatedResource]:
        """ Iterate through all available `LocatedResource`s. """
