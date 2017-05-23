from pymcutil.command.command import Command


class ScoreboardCommand(Command):
    """
    An objective model of Minecraft's `scoreboard` command:

        scoreboard <objectives|players|teams> ...

    http://minecraft.gamepedia.com/Scoreboard#Command_reference
    
    *This command requires a sub-command to be useful.*
    """

    CMD = 'scoreboard'

    def params(self):
        yield self.CMD
