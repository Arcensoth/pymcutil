from pymcutil.command.command import Command

CMD = 'execute'


class ExecuteCommand(Command):
    """
    An objective model of Minecraft's `execute` command:

        execute ...

    http://minecraft.gamepedia.com/Commands#execute

    *This command requires a sub-command to be useful.*
    """

    def params(self):
        yield CMD
