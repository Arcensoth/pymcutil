from typing import Iterable, List

from pymcutil.command.command import Command
from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.resource_reference.abc.resource_reference import ResourceReference
from pymcutil.resource.resource_referent.abc.resource_referent import ResourceReferent


class Function(Resource):
    def __init__(self, commands: Iterable[Command]):
        self.commands: List[Command] = list(commands)

    @property
    def direct_resource_references(self) -> Iterable[ResourceReference]:
        # A function does not directly reference any resources, only commands.
        yield from ()

    @property
    def resource_referents(self) -> Iterable[ResourceReferent]:
        # Yield all commands that reference resources.
        yield from (command for command in self.commands if isinstance(command, ResourceReferent))

    @property
    def text(self) -> str:
        # Return commands, one per line, followed by one final blank line.
        return '\n'.join((*(str(command) for command in self.commands), ''))
