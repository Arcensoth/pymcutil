from pymcutil.command.command import Command

CMD = 'say'


class SayCommand(Command):
    """
    An objective model of Minecraft's `say` command:

        say <message ...>

    http://minecraft.gamepedia.com/Commands#say
    """

    def __init__(self, message: str):
        self.message: str = message

    def params(self):
        yield from (CMD, self.message)


say = SayCommand
