from typing import Iterable, List

from pymcutil.command.command import Command
from pymcutil.resource.abc.resource import Resource
from pymcutil.resource.resource_referent.abc.resource_referent import ResourceReferent


class Function(Resource):
    def __init__(self, commands: Iterable[Command]):
        self.commands: List[Command] = list(commands)

    @property
    def direct_resource_references(self):
        # A function does not directly reference any resources, only commands.
        yield from ()

    @property
    def resource_referents(self):
        # Yield all commands that reference resources.
        yield from (command for command in self.commands if isinstance(command, ResourceReferent))

    @property
    def resource_lines(self):
        # Yield commands to be printed one per line.
        yield from self.commands
