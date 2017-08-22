from .._execute_unless_blocks_command import ExecuteUnlessBlocksCommand

CMD = 'masked'


class ExecuteUnlessBlocksMaskedCommand(ExecuteUnlessBlocksCommand):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute unless blocks <start: x y z> <end: x y z> <destination: x y z> masked -> execute

    http://minecraft.gamepedia.com/Commands#execute
    """

    def params(self):
        yield from super().params()
        yield from (
            CMD,
            (self.subcommand.substr(), None))


masked = ExecuteUnlessBlocksMaskedCommand
