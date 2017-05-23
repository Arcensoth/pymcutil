from pymcutil.command.target import Target
from ..players_ import ScoreboardPlayersCommand

CMD = 'tag'


class ScoreboardPlayersTagCommand(ScoreboardPlayersCommand):
    """
    An objective model of one of Minecraft's `scoreboard` subcommands:

        scoreboard players tag <player> <add|remove|list> ...

    http://minecraft.gamepedia.com/Scoreboard#Tags_commands
    
    *This command requires a sub-command to be useful.*
    """

    def __init__(self, target: Target):
        self.target: Target = target

    def params(self):
        yield from super().params()
        yield from (CMD, self.target)
