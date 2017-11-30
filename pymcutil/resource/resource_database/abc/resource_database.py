import abc
from typing import Union

from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation


class ResourceDatabase(abc.ABC):
    @abc.abstractmethod
    def get(self, location: ResourceLocation) -> Union[Resource, None]:
        """ Return a `Resource` representation of the resource at `Location`. """

    @abc.abstractmethod
    def put(self, location: ResourceLocation, resource: Resource) -> Resource:
        """ Persist and return a `Resource` representation of the resource at `Location`. """
