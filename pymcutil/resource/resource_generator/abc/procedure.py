import abc
from typing import Iterable

from pymcutil.command.command import Command
from pymcutil.resource.function import Function
from pymcutil.resource.resource_generator.abc.function_generator import FunctionGenerator
from pymcutil.resource.resource_location.function_location import FunctionLocation
from pymcutil.util.resources import get_resource_trail


class Procedure(FunctionGenerator):
    def __init__(self, namespace: str, root: str = ''):
        self.namespace: str = namespace
        self.root: str = root

    def trail(self, *params) -> str:
        return get_resource_trail(self.root, *self.keys(*params))

    def location(self, *params) -> FunctionLocation:
        return FunctionLocation(namespace=self.namespace, trail=self.trail(*params))

    def generate(self, *params) -> Function:
        return Function(commands=tuple(self.run(*params)))

    @abc.abstractmethod
    def keys(self, *params) -> Iterable:
        """ Returns key components making up the trailing portion of the function name. """

    @abc.abstractmethod
    def run(self, *params) -> Iterable[Command]:
        """ Yield commands, in order, making up the function. """
