from typing import Union, Mapping

from pymcutil.command.target import Target
from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from ..scoreboard_players_tag_command import ScoreboardPlayersTagCommand

CMD = 'remove'


class ScoreboardPlayersTagRemoveCommand(ScoreboardPlayersTagCommand):
    """
    An objective model of one of Minecraft's `scoreboard` subcommands:

        scoreboard players tag <player> remove <tagName> [dataTag]

    http://minecraft.gamepedia.com/Scoreboard#Tags_commands
    """

    def __init__(self, target: Target, tag: str, data_tag: Mapping = None):
        super().__init__(target)
        self.tag: str = tag
        self.data_tag: Union[CompoundDataTag, None] = CompoundDataTag.sift(data_tag, None)

    def params(self):
        yield from super().params()
        yield from (
            CMD, self.tag,
            (self.data_tag, CompoundDataTag()))


def remove(target: Target, tag: str, data_tag: Mapping = None) -> ScoreboardPlayersTagRemoveCommand:
    """ Functional alias for creating `ScoreboardPlayersTagRemoveCommand` instances. """
    return ScoreboardPlayersTagRemoveCommand(**locals())
