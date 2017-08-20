from .._execute_command import ExecuteCommand

CMD = 'unless'


class ExecuteUnlessCommand(ExecuteCommand):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute unless ...

    http://minecraft.gamepedia.com/Commands#execute

    *This command requires a sub-command to be useful.*
    """

    def params(self):
        yield CMD
