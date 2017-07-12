from pymcutil.command.command import Command

CMD = 'effect'


class EffectCommand(Command):
    """
    An objective model of Minecraft's `effect` command:

        effect <give|take> ...

    http://minecraft.gamepedia.com/Commands#effect

    *This command requires a sub-command to be useful.*
    """

    def params(self):
        yield CMD
