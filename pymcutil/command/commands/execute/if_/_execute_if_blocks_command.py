from .._execute_conditional_blocks_mixin import ExecuteConditionalBlocksMixin
from .._execute_if_command import ExecuteIfCommand

CMD = 'blocks'


class ExecuteIfBlocksCommand(ExecuteIfCommand, ExecuteConditionalBlocksMixin):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute if blocks <start: x y z> <end: x y z> <destination: x y z> ...

    http://minecraft.gamepedia.com/Commands#execute

    *This command requires a sub-command to be useful.*
    """

    def params(self):
        yield from super().params()
        yield from (CMD, self.start, self.end, self.destination)
