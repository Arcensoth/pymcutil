from typing import Dict, Iterable, Set, Tuple, Type, Union

from pymcutil.resource.resource_database.abc.resource_database import ResourceDatabase
from pymcutil.resource.resource_generator.abc.resource_generator import ResourceGenerator
from pymcutil.resource.resource_location.abc.resource_location import ResourceName
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager, ResourcePair
from pymcutil.resource.resource_manager.errors import ReferenceNotRegisteredError
from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference

RegistryType = Iterable[Union[
    Tuple[Type[ResourceReference], ResourceGenerator],
    Tuple[Type[ResourceReference], ResourceGenerator, ResourceDatabase]
]]


class StandardResourceManager(ResourceManager):
    def __init__(self, database: ResourceDatabase, registry: RegistryType):
        self.database: ResourceDatabase = database

        self.generator_map: Dict[Type[ResourceReference], ResourceGenerator] = {}
        self.database_map: Dict[Type[ResourceReference], ResourceDatabase] = {}

        self._generating: Set[ResourceReference] = set()

        for item in registry:
            self.register(*item)

    def _get_generator(self, reference: ResourceReference) -> ResourceGenerator:
        try:
            return self.generator_map[type(reference)]
        except KeyError as e:
            raise ReferenceNotRegisteredError(reference) from e

    def _get_database(self, reference: ResourceReference) -> ResourceDatabase:
        return self.database_map.get(type(reference), self.database)

    def register(self, kind: Type[ResourceReference], generator: ResourceGenerator, database: ResourceDatabase = None):
        self.generator_map[kind] = generator
        self.database_map[kind] = database or self.database

    def get(self, reference: ResourceReference) -> ResourcePair:
        generator = self._get_generator(reference)
        database = self._get_database(reference)
        location = generator.location(reference)
        resource = database.get(location)
        return resource, location

    def refer(self, reference: ResourceReference) -> ResourceName:
        resource, location = self.get(reference)

        if not (resource or (reference in self._generating)):
            generator = self._get_generator(reference)
            database = self._get_database(reference)

            self._generating.add(reference)

            new_resource = generator.generate(reference)
            database.put(location, new_resource)

            self._generating.remove(reference)

        return location.name

    def generate(self, *references: ResourceReference) -> Iterable[ResourcePair]:
        for reference in references:
            self.refer(reference)
            yield self.get(reference)
