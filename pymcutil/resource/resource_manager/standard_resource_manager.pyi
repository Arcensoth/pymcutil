from typing import Dict, Iterable, Set, Tuple, Type, Union

from pymcutil.resource.located_resource.located_resource import LocatedResource
from pymcutil.resource.resource_database.abc.resource_database import ResourceDatabase
from pymcutil.resource.resource_generator.abc.resource_generator import ResourceGenerator
from pymcutil.resource.resource_location.abc.resource_location import ResourceLocation, ResourceName, ResourcePath
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager
from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference

RegistryType = Iterable[Union[
    Tuple[Type[ResourceReference], ResourceGenerator],
    Tuple[Type[ResourceReference], ResourceGenerator, ResourceDatabase]
]]


class StandardResourceManager(ResourceManager):
    _database: ResourceDatabase
    _generator_map: Dict[Type[ResourceReference], ResourceGenerator]
    _database_map: Dict[Type[ResourceReference], ResourceDatabase]
    _generating: Set[ResourceReference]

    def __init__(self, database: ResourceDatabase, registry: RegistryType): ...

    def _get_generator(self, reference: ResourceReference) -> ResourceGenerator: ...

    def _get_database(self, reference: ResourceReference) -> ResourceDatabase: ...

    def register(
            self, kind: Type[ResourceReference], generator: ResourceGenerator, database: ResourceDatabase = None): ...

    def get(self, reference: ResourceReference) -> Union[LocatedResource, None]: ...

    def generate(self, reference: ResourceReference) -> LocatedResource: ...

    def locate(self, reference: ResourceReference) -> ResourceLocation: ...

    def name(self, reference: ResourceReference) -> ResourceName: ...

    def path(self, reference: ResourceReference) -> ResourcePath: ...
