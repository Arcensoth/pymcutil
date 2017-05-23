from ..scoreboard_ import ScoreboardCommand


class ScoreboardPlayersCommand(ScoreboardCommand):
    """
    An objective model of one of Minecraft's `scoreboard` subcommands:

        scoreboard players <list|set|add|remove|reset|enable|test|operation|tag> ...

    http://minecraft.gamepedia.com/Scoreboard#Players_commands
    
    *This command requires a sub-command to be useful.*
    """

    CMD = 'players'

    def params(self):
        yield from super().params()
        yield self.CMD
