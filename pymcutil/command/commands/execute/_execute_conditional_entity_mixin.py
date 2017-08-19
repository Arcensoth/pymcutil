from typing import Union

from pymcutil.command.target import Target
from .._execute_command import ExecuteCommand


class ExecuteConditionalEntityMixin(object):
    def __init__(self, target: Target, subcommand: ExecuteCommand = None):
        self.target: Target = target
        self.subcommand: Union[ExecuteCommand, None] = subcommand
