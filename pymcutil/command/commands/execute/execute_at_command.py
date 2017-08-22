from typing import Union

from pymcutil.command.target import Target
from .._execute_command import ExecuteCommand

CMD = 'at'


class ExecuteAtCommand(ExecuteCommand):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute at <targets: entities> -> execute

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


at = ExecuteAtCommand
