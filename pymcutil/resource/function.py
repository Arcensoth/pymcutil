from typing import Iterable, List

from pymcutil.command.command import Command
from pymcutil.resource.abc.resource import Resource


class Function(Resource):
    def __init__(self, commands: Iterable[Command]):
        self.commands: List[Command] = list(commands)

    @property
    def text(self) -> str:
        # Return commands, one per line, followed by one final blank line.
        return '\n'.join((*(str(command) for command in self.commands), ''))
