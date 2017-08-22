from .._execute_if_blocks_command import ExecuteIfBlocksCommand

CMD = 'masked'


class ExecuteIfBlocksMaskedCommand(ExecuteIfBlocksCommand):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute if blocks <start: x y z> <end: x y z> <destination: x y z> masked -> execute

    http://minecraft.gamepedia.com/Commands#execute
    """

    def params(self):
        yield from super().params()
        yield from (
            CMD,
            (self.subcommand.substr(), None))


masked = ExecuteIfBlocksMaskedCommand
