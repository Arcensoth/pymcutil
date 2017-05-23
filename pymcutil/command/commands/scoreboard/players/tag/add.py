from typing import Union

from pymcutil.command.target import Target
from pymcutil.data_tag import DataTag
from ..tag_ import ScoreboardPlayersTagCommand


class ScoreboardPlayersTagAddCommand(ScoreboardPlayersTagCommand):
    """
    An objective model of one of Minecraft's `scoreboard` subcommands:

        scoreboard players tag <player> add <tagName> [dataTag]

    http://minecraft.gamepedia.com/Scoreboard#Tags_commands
    """

    CMD = 'add'

    def __init__(self, target: Target, tag: str, data_tag: DataTag = None):
        super().__init__(target)
        self.tag: str = tag
        self.data_tag: Union[DataTag, None] = data_tag

    def params(self):
        yield from super().params()
        yield from (self.CMD, self.tag)

        if self.data_tag is not None:
            yield self.data_tag


def add(target: Target, tag: str, data_tag: DataTag = None) -> ScoreboardPlayersTagAddCommand:
    """ Functional alias for creating `ScoreboardPlayersTagAddCommand` instances. """
    return ScoreboardPlayersTagAddCommand(**locals())
