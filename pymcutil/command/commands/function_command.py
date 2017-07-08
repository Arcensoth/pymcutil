from typing import Union

from pymcutil.command.command import Command
from pymcutil.command.target import Target
from pymcutil.resource.resource_reference.function_reference import FunctionReference
from pymcutil.resource.resource_referent.abc.resource_referent import ResourceReferent
from pymcutil.selector import selectors

CMD = 'function'


class FunctionCommand(Command, ResourceReferent):
    """
    An objective model of Minecraft's `function` command:

        function <function> [if|unless] [selector]

    http://minecraft.gamepedia.com/Commands#function
    """

    def __init__(self, function: Union[str, FunctionReference], mode: str = None, mode_target: Target = None):
        self.function: Union[str, FunctionReference] = function
        self.mode: str = mode
        self.mode_target: Target = mode_target

    def params(self):
        yield from (CMD, self.function, (self.mode, 'if'), (self.mode_target, selectors.SELF))

    @property
    def direct_resource_references(self):
        # Yield our function, but only if it's a dynamic function reference.
        if isinstance(self.function, FunctionReference):
            yield self.function

    @property
    def resource_referents(self):
        yield from ()


def function(function: Union[str, FunctionReference], mode: str = None, mode_target: Target = None) -> FunctionCommand:
    """ Functional alias for creating `FunctionCommand` instances. """
    return FunctionCommand(**locals())
