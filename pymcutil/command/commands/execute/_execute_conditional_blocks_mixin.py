from typing import Union

from pymcutil.position.position import Position
from .._execute_command import ExecuteCommand


class ExecuteConditionalBlocksMixin(object):
    def __init__(
            self, start: Position.Generic, end: Position.Generic, destination: Position.Generic,
            subcommand: ExecuteCommand = None):
        self.start: Position = Position.sift(start)
        self.end: Position = Position.sift(end)
        self.destination: Position = Position.sift(destination)
        self.subcommand: Union[ExecuteCommand, None] = subcommand
