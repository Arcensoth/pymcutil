from .._execute_conditional_block_mixin import ExecuteConditionalBlockMixin
from .._execute_unless_command import ExecuteUnlessCommand

CMD = 'block'


class ExecuteUnlessBlockCommand(ExecuteUnlessCommand, ExecuteConditionalBlockMixin):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute unless block <pos: x y z> <block: block> -> execute

    http://minecraft.gamepedia.com/Commands#execute
    """

    def params(self):
        yield from super().params()
        yield from (
            CMD, self.position, self.block,
            (self.subcommand.substr(), None))


block = ExecuteUnlessBlockCommand
