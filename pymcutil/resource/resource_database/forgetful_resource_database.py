import os
from typing import Dict

from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.resource_database.abc.resource_database import ResourceDatabase
from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation, ResourceName


class ForgetfulResourceDatabase(ResourceDatabase):
    """
    Never reads, only writes. Relies entirely on an in-memory store for retrieval. Generated resources are written
    to file regardless of whether they already exist.

    Given that it does nothing with existing resources, it's limited to smaller systems and production builds. Better
    to use a more advanced `ResourceDatabase` implementation for anything even remotely complex.
    """

    def __init__(self, data_path: str):
        self.data_path: str = data_path
        self.data: Dict[ResourceName, Resource] = {}

    def get(self, location: ResourceLocation):
        return self.data.get(location.name, None)

    def put(self, location: ResourceLocation, resource: Resource):
        self.data[location.name] = resource

        resource_path = os.path.join(self.data_path, location.path)
        os.makedirs(os.path.dirname(resource_path), exist_ok=True)
        with open(resource_path, 'w') as resource_file:
            resource_file.write(resource.text)

        return self.get(location)
