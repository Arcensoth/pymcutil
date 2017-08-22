from typing import Union

from pymcutil.command.target import Target
from .._execute_command import ExecuteCommand

CMD = 'as'


class ExecuteAsCommand(ExecuteCommand):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute as <targets: entities> -> execute

    http://minecraft.gamepedia.com/Commands#execute
    """

    def __init__(self, target: Target, subcommand: ExecuteCommand = None):
        self.target: Target = target
        self.subcommand: Union[ExecuteCommand, None] = subcommand

    def params(self):
        yield from super().params()
        yield from (
            CMD, self.target,
            (self.subcommand.substr(), None))


as_ = ExecuteAsCommand  # work around keyword conflict
