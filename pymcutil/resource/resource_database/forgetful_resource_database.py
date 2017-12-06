import logging
import os
from typing import Dict, Iterable, Union

from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.located_resource.located_resource import LocatedResource
from pymcutil.resource.resource_database.abc.resource_database import ResourceDatabase
from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation

log = logging.getLogger(__name__)


class ForgetfulResourceDatabase(ResourceDatabase):
    """
    Never reads, only writes. Relies entirely on an in-memory store for retrieval. Generated resources are written
    to file regardless of whether they already exist.

    Given that it does nothing with existing resources, it's limited to smaller systems and production builds. Better
    to use a more advanced `ResourceDatabase` implementation for anything even remotely complex.
    """

    def __init__(self, data_path: str):
        self.data_path: str = data_path
        self.data: Dict[ResourceLocation, LocatedResource] = {}

    def get(self, location: ResourceLocation) -> Union[LocatedResource, None]:
        result = self.data.get(location, None)
        log.debug('GOT {} from {}'.format(type(result.resource).__name__ if result else None, location.path))
        return result

    def put(self, location: ResourceLocation, resource: Resource) -> LocatedResource:
        log.debug('PUT {} at {}'.format(type(resource).__name__, location.path))

        resource_path = os.path.join(self.data_path, location.path)
        os.makedirs(os.path.dirname(resource_path), exist_ok=True)
        resource.write_to(resource_path)

        self.data[location] = LocatedResource(location, resource)
        return self.get(location)

    def all(self) -> Iterable[LocatedResource]:
        yield from self.data.values()
