from typing import Union

from pymcutil.command.target import Target
from .._execute_command import ExecuteCommand

CMD = 'store'


class ExecuteStoreCommand(ExecuteCommand):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute store ...

    http://minecraft.gamepedia.com/Commands#execute

    *This command requires a sub-command to be useful.*
    """

    def __init__(self, target: Target, objective: str, subcommand: ExecuteCommand = None):
        self.target: Target = target
        self.objective: str = objective
        self.subcommand: Union[ExecuteCommand, None] = subcommand

    def params(self):
        yield from super().params()
        yield CMD
