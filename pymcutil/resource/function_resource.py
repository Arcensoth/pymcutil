from typing import Iterable, List

from pymcutil.command.command import Command
from pymcutil.resource.abc.resource import Resource


class FunctionResource(Resource):
    def __init__(self, commands: Iterable[Command]):
        self.commands: List[Command] = list(commands)

    @property
    def lines(self) -> Iterable[str]:
        # Yield commands, one per line, followed by one final blank line.
        yield from (str(command) for command in self.commands)
        yield ''

    def write_to(self, path):
        with open(path, 'w') as fp:
            fp.writelines('\n'.join(self.lines))
