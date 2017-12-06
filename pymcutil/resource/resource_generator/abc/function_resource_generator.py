import abc

from pymcutil.resource.function_resource import FunctionResource
from pymcutil.resource.resource_generator.abc.resource_generator import ResourceGenerator
from pymcutil.resource.resource_location.function_resource_location import FunctionResourceLocation
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager
from pymcutil.resource.resource_reference.function_resource_reference import FunctionResourceReference


class FunctionResourceGenerator(ResourceGenerator):
    @abc.abstractmethod
    def location(self, manager: ResourceManager, reference: FunctionResourceReference) -> FunctionResourceLocation: ...

    @abc.abstractmethod
    def generate(self, manager: ResourceManager, reference: FunctionResourceReference) -> FunctionResource: ...
