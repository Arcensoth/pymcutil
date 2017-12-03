from typing import Dict, Iterable, Union

from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.located_resource.located_resource import LocatedResource
from pymcutil.resource.resource_database.abc.resource_database import ResourceDatabase
from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation


class DummyResourceDatabase(ResourceDatabase):
    """ Never reads and never writes. Stores generated resources in-memory and that's about it. """

    def __init__(self):
        self.data: Dict[ResourceLocation, LocatedResource] = {}

    def get(self, location: ResourceLocation) -> Union[LocatedResource, None]:
        return self.data.get(location, None)

    def put(self, location: ResourceLocation, resource: Resource) -> LocatedResource:
        self.data[location] = LocatedResource(location, resource)
        return self.get(location)

    def all(self) -> Iterable[LocatedResource]:
        yield from self.data.values()
