from .._execute_conditional_entity_mixin import ExecuteConditionalEntityMixin
from .._execute_unless_command import ExecuteUnlessCommand

CMD = 'entity'


class ExecuteUnlessEntityCommand(ExecuteUnlessCommand, ExecuteConditionalEntityMixin):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute unless entity <condition: entities> -> execute

    http://minecraft.gamepedia.com/Commands#execute
    """

    def params(self):
        yield from super().params()
        yield from (
            CMD, self.target,
            (self.subcommand.substr(), None))


entity = ExecuteUnlessEntityCommand
