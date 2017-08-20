from .._execute_conditional_blocks_mixin import ExecuteConditionalBlocksMixin
from .._execute_unless_command import ExecuteUnlessCommand

CMD = 'blocks'


class ExecuteUnlessBlocksCommand(ExecuteUnlessCommand, ExecuteConditionalBlocksMixin):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute unless blocks <start: x y z> <end: x y z> <destination: x y z> ...

    http://minecraft.gamepedia.com/Commands#execute

    *This command requires a sub-command to be useful.*
    """

    def params(self):
        yield from super().params()
        yield from (CMD, self.start, self.end, self.destination)
