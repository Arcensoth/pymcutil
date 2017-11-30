from typing import Dict

from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.resource_database.abc.resource_database import ResourceDatabase
from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation, ResourceName


class DummyResourceDatabase(ResourceDatabase):
    """ Never reads and never writes. Stores generated resources in-memory and that's about it. """

    def __init__(self):
        self.data: Dict[ResourceName, Resource] = {}

    def get(self, location: ResourceLocation):
        return self.data.get(location.name, None)

    def put(self, location: ResourceLocation, resource: Resource):
        self.data[location.name] = resource
        return self.get(location)
