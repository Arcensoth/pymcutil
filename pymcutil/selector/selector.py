import abc
from numbers import Real
from typing import Iterable, Mapping, Union

from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.position.position import Position
from pymcutil.selector.advancement_set import AdvancementSet
from pymcutil.selector.range import Range
from pymcutil.selector.repeatable_argument import RepeatableArgument
from pymcutil.selector.score_set import ScoreSet
from pymcutil.selector.selector_arguments import SelectorArguments
from pymcutil.symbols.gamemodes.gamemode import Gamemode
from pymcutil.symbols.selector_sorts.selector_sort import SelectorSort
from pymcutil.util import first
from pymcutil.util.siftable import SiftableMapping

RepeatableString = Union[str, Iterable[str]]
RepeatableGamemode = Union[Gamemode, Iterable[Gamemode]]
RepeatableNBT = Union[CompoundDataTag.Generic, Iterable[CompoundDataTag.Generic]]


class Selector(SiftableMapping):
    """
    Represents a Minecraft target selector, with similar arguments and some built-in conveniences.

    Provided arguments cascade such that the most specific value is used. For example, an explicitly provided `x`
    coordinate will take precedence over the `x` component of any given `position`.
    """

    Generic = ['Selector', Mapping]

    def __init__(
            self,
            position: Position.Generic = None, x: Real = None, y: Real = None, z: Real = None,
            volume: Position.Generic = None, dx: Real = None, dy: Real = None, dz: Real = None,
            x_rotation: Range.Generic = None, y_rotation: Range.Generic = None,
            distance: Range.Generic = None,
            level: Range.Generic = None,
            type_: str = None, not_types: RepeatableString = None,
            name: str = None, not_names: RepeatableString = None,
            team: str = None, not_teams: RepeatableString = None,
            gamemode: Gamemode = None, not_gamemodes: RepeatableGamemode = None,
            tags: RepeatableString = None, not_tags: RepeatableString = None,
            nbts: RepeatableNBT = None, not_nbts: RepeatableNBT = None,
            scores: ScoreSet.Generic = None,
            advancements: AdvancementSet.Generic = None,
            sort: SelectorSort = None,
            limit: int = None,
    ):
        # These are only used for intermediate calculations.
        position = Position.sift(position, None)
        volume = Position.sift(volume, None)

        self.arguments = SelectorArguments(
            x=first(x, position.x if isinstance(position, Position) else None),
            y=first(y, position.y if isinstance(position, Position) else None),
            z=first(z, position.z if isinstance(position, Position) else None),

            dx=first(dx, volume.x if isinstance(volume, Position) else None),
            dy=first(dy, volume.y if isinstance(volume, Position) else None),
            dz=first(dz, volume.z if isinstance(volume, Position) else None),

            x_rotation=Range.sift(x_rotation, None),
            y_rotation=Range.sift(y_rotation, None),

            distance=Range.sift(distance, None),

            level=Range.sift(level, None),

            type_=type_,
            not_types=RepeatableArgument.expand(not_types),

            name=name,
            not_names=RepeatableArgument.expand(not_names),

            team=team,
            not_teams=RepeatableArgument.expand(not_teams),

            gamemode=gamemode,
            not_gamemodes=RepeatableArgument.expand(not_gamemodes, converter=Gamemode.sift),

            tags=RepeatableArgument.expand(tags),
            not_tags=RepeatableArgument.expand(not_tags),

            nbts=RepeatableArgument.expand(nbts, CompoundDataTag.sift),
            not_nbts=RepeatableArgument.expand(not_nbts, CompoundDataTag.sift),

            scores=ScoreSet.sift(scores, None),

            advancements=AdvancementSet.sift(advancements, None),

            sort=SelectorSort.sift(sort, None),

            limit=limit,
        )

    def __str__(self):
        innards = ','.join(('{}={}'.format(k, v) for k, v in self.expanded_items()))
        return ''.join((
            '@',
            self.base,
            *(('[', innards, ']') if innards else ()),
        ))

    def expanded_items(self):
        # We need to expand `RepeatableArguments` to get several items per key.
        for k, v in self.arguments:
            if isinstance(v, RepeatableArgument):
                yield from ((k, rv) for rv in v.values)
            else:
                yield k, v

    @classmethod
    @abc.abstractmethod
    def base(cls) -> str:
        """ Return the base selector type. For example, the `s` in `@s`. """
