from .._execute_conditional_block_mixin import ExecuteConditionalBlockMixin
from .._execute_if_command import ExecuteIfCommand

CMD = 'block'


class ExecuteIfBlockCommand(ExecuteIfCommand, ExecuteConditionalBlockMixin):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute if block <pos: x y z> <block: block> -> execute

    http://minecraft.gamepedia.com/Commands#execute
    """

    def params(self):
        yield from super().params()
        yield from (
            CMD, self.position, self.block,
            (self.subcommand.substr(), None))


block = ExecuteIfBlockCommand
