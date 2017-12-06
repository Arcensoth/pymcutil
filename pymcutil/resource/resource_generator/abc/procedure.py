import abc
from typing import Iterable

from pymcutil.command.command import Command
from pymcutil.resource.function_resource import FunctionResource
from pymcutil.resource.resource_generator.abc.function_resource_generator import FunctionResourceGenerator
from pymcutil.resource.resource_location.function_resource_location import FunctionResourceLocation
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager
from pymcutil.resource.resource_reference.function_resource_reference import FunctionResourceReference


class Procedure(FunctionResourceGenerator):
    def __init__(self, namespace: str, root: str = None):
        self.namespace: str = namespace
        self.root: str = root

    def location(self, manager: ResourceManager, reference: FunctionResourceReference):
        return FunctionResourceLocation(namespace=self.namespace, components=self.components(manager, reference))

    def generate(self, manager: ResourceManager, reference: FunctionResourceReference):
        return FunctionResource(commands=tuple(self.commands(manager, reference)))

    def components(self, manager: ResourceManager, reference: FunctionResourceReference) -> Iterable[str]:
        """ Yield components making up the trailing portion of the function name. """
        yield from (str(param) for param in reference.params)

    @abc.abstractmethod
    def commands(self, manager: ResourceManager, reference: FunctionResourceReference) -> Iterable[Command]:
        """ Yield commands, in order, making up the function. """
