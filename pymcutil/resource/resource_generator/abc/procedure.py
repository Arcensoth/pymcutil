import abc
from typing import Iterable

from pymcutil.command.command import Command
from pymcutil.resource.function import Function
from pymcutil.resource.resource_generator.abc.function_generator import FunctionGenerator
from pymcutil.resource.resource_location.function_location import FunctionLocation
from pymcutil.resource.resource_manager.abc.resource_manager import ResourceManager
from pymcutil.resource.resource_reference.function_reference import FunctionReference
from pymcutil.util.resources import get_resource_trail


class Procedure(FunctionGenerator):
    def __init__(self, namespace: str, root: str = None):
        self.namespace: str = namespace
        self.root: str = root

    def location(self, manager: ResourceManager, reference: FunctionReference):
        return FunctionLocation(namespace=self.namespace, trail=self.trail(manager, reference))

    def generate(self, manager: ResourceManager, reference: FunctionReference):
        return Function(commands=tuple(self.commands(manager, reference)))

    def trail(self, manager: ResourceManager, reference: FunctionReference) -> str:
        return get_resource_trail(self.root, *self.components(manager, reference))

    def components(self, manager: ResourceManager, reference: FunctionReference) -> Iterable:
        """ Yield components making up the trailing portion of the function name. """
        yield from reference.params

    @abc.abstractmethod
    def commands(self, manager: ResourceManager, reference: FunctionReference) -> Iterable[Command]:
        """ Yield commands, in order, making up the function. """
