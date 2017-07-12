from ..scoreboard_players_tag_command import ScoreboardPlayersTagCommand

CMD = 'list'


class ScoreboardPlayersTagListCommand(ScoreboardPlayersTagCommand):
    """
    An objective model of one of Minecraft's `scoreboard` subcommands:

        scoreboard players tag <player> list

    http://minecraft.gamepedia.com/Scoreboard#Tags_commands
    """

    def params(self):
        yield from super().params()
        yield CMD


list = ScoreboardPlayersTagListCommand
