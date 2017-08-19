from .._execute_command import ExecuteCommand

CMD = 'if'


class ExecuteIfCommand(ExecuteCommand):
    """
    An objective model of one of Minecraft's `execute` subcommands:

        execute if ...

    http://minecraft.gamepedia.com/Commands#execute

    *This command requires a sub-command to be useful.*
    """

    def params(self):
        yield CMD
