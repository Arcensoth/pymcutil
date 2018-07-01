import abc
from numbers import Real
from typing import Iterable, Mapping, Optional, Tuple, Union

from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.position.position import Position
from pymcutil.selector.advancement_set import AdvancementSet
from pymcutil.selector.range import Range
from pymcutil.selector.score_set import ScoreSet
from pymcutil.symbols.entity_ids.entity_ids import EntityID
from pymcutil.symbols.gamemodes.gamemode import Gamemode
from pymcutil.symbols.selector_bases.selector_bases import SelectorBase
from pymcutil.symbols.selector_sorts.selector_sort import SelectorSort
from pymcutil.util import first
from pymcutil.util.nullability import nullable_float, nullable_int, nullable_str, nullable_tuple
from pymcutil.util.siftable import MappingSiftable

RepeatableString = Iterable[str]
RepeatableEntityID = Iterable[EntityID.Generic]
RepeatableGamemode = Iterable[Gamemode.Generic]
RepeatableNBT = Iterable[CompoundDataTag.Generic]


class Selector(MappingSiftable):
    """
    Represents a Minecraft target selector, with similar arguments and some built-in conveniences.

    Provided arguments cascade such that the most specific value is used. For example, an explicitly provided `x`
    coordinate will take precedence over the `x` component of any given `position`.
    """

    Generic = Union['Selector', Mapping]

    def __init__(
            self,
            position: Position.Generic = None, x: Real = None, y: Real = None, z: Real = None,
            volume: Position.Generic = None, dx: Real = None, dy: Real = None, dz: Real = None,
            x_rotation: Range.Generic = None, y_rotation: Range.Generic = None,
            distance: Range.Generic = None,
            level: Range.Generic = None,
            type_: EntityID = None, not_types: RepeatableEntityID = None,
            name: str = None, not_names: RepeatableString = None,
            team: str = None, not_teams: RepeatableString = None,
            gamemode: Gamemode.Generic = None, not_gamemodes: RepeatableGamemode = None,
            tags: RepeatableString = None, not_tags: RepeatableString = None,
            nbts: RepeatableNBT = None, not_nbts: RepeatableNBT = None,
            scores: ScoreSet.Generic = None,
            advancements: AdvancementSet.Generic = None,
            sort: SelectorSort = None,
            limit: int = None,
    ):
        # Intermediates used for calculations.

        position = Position.sift(position, None)
        volume = Position.sift(volume, None)

        x = first(x, position.x if isinstance(position, Position) else None)
        y = first(y, position.y if isinstance(position, Position) else None)
        z = first(z, position.z if isinstance(position, Position) else None)

        dx = first(dx, volume.x if isinstance(volume, Position) else None)
        dy = first(dy, volume.y if isinstance(volume, Position) else None)
        dz = first(dz, volume.z if isinstance(volume, Position) else None)

        # Actual instance attributes.

        self.x: Optional[float] = nullable_float(x)
        self.y: Optional[float] = nullable_float(y)
        self.z: Optional[float] = nullable_float(z)

        self.dx: Optional[float] = nullable_float(dx)
        self.dy: Optional[float] = nullable_float(dy)
        self.dz: Optional[float] = nullable_float(dz)

        self.x_rotation: Optional[Range] = Range.sift(x_rotation, None)
        self.y_rotation: Optional[Range] = Range.sift(y_rotation, None)
        self.distance: Optional[Range] = Range.sift(distance, None)
        self.level: Optional[Range] = Range.sift(level, None)

        self.type_: Optional[EntityID] = nullable_str(type_)
        self.not_types: Optional[Tuple[EntityID]] = nullable_tuple(not_types, converter=EntityID.sift)

        self.name: Optional[str] = nullable_str(name)
        self.not_names: Optional[Tuple[str]] = nullable_tuple(not_names, converter=str)

        self.team: Optional[str] = nullable_str(team)
        self.not_teams: Optional[Tuple[str]] = nullable_tuple(not_teams, converter=str)

        self.gamemode: Optional[Gamemode] = Gamemode.sift(gamemode, None)
        self.not_gamemodes: Optional[Tuple[Gamemode]] = nullable_tuple(not_gamemodes, converter=Gamemode.sift)

        self.tags: Optional[Tuple[str]] = nullable_tuple(tags, converter=str)
        self.not_tags: Optional[Tuple[str]] = nullable_tuple(not_tags, converter=str)

        self.nbts: Optional[Tuple[CompoundDataTag]] = nullable_tuple(nbts, converter=CompoundDataTag.sift)
        self.not_nbts: Optional[Tuple[CompoundDataTag]] = nullable_tuple(not_nbts, converter=CompoundDataTag.sift)

        self.scores: Optional[ScoreSet] = ScoreSet.sift(scores, None)

        self.advancements: Optional[AdvancementSet] = AdvancementSet.sift(advancements, None)

        self.sort: Optional[SelectorSort] = SelectorSort.sift(sort, None)

        self.limit: Optional[int] = nullable_int(limit)

    def __str__(self):
        arguments = tuple(self.arguments)
        argument_str = ''.join(('[', ','.join(['{}={}'.format(k, v) for k, v in arguments]), ']')) if arguments else ''
        return '@{}{}'.format(self.base, argument_str or '')

    @property
    def arguments(self) -> Iterable[Tuple[str, str]]:
        # TODO This is disguesting. Has it always been this way?
        if self.x is not None:
            yield 'x', str(self.x)
        if self.y is not None:
            yield 'y', str(self.y)
        if self.z is not None:
            yield 'z', str(self.z)

        if self.dx is not None:
            yield 'dx', str(self.dx)
        if self.dy is not None:
            yield 'dy', str(self.dy)
        if self.dz is not None:
            yield 'dz', str(self.dz)

        if self.x_rotation is not None:
            yield 'x_rotation', str(self.x_rotation)
        if self.y_rotation is not None:
            yield 'y_rotation', str(self.y_rotation)

        if self.distance is not None:
            yield 'distance', str(self.distance)

        if self.level is not None:
            yield 'level', str(self.level)

        if self.type_ is not None:
            yield 'type', str(self.type_)
        if self.not_types is not None:
            yield from (('type', '!{}'.format(type_)) for type_ in self.not_types)

        if self.name is not None:
            yield 'name', str(self.name)
        if self.not_names is not None:
            yield from (('name', '!{}'.format(name)) for name in self.not_names)

        if self.team is not None:
            yield 'team', str(self.team)
        if self.not_teams is not None:
            yield from (('team', '!{}'.format(team)) for team in self.not_teams)

        if self.gamemode is not None:
            yield 'gamemode', str(self.gamemode)
        if self.not_gamemodes is not None:
            yield from (('gamemode', '!{}'.format(gamemode)) for gamemode in self.not_gamemodes)

        if self.tags is not None:
            yield from (('tag', '{}'.format(tag)) for tag in self.tags)
        if self.not_tags is not None:
            yield from (('tag', '!{}'.format(tag)) for tag in self.not_tags)

        if self.nbts is not None:
            yield from (('nbt', '{}'.format(nbt)) for nbt in self.nbts)
        if self.not_nbts is not None:
            yield from (('nbt', '!{}'.format(nbt)) for nbt in self.not_nbts)

        if self.scores is not None:
            yield 'scores', str(self.scores)

        if self.advancements is not None:
            yield 'advancements', str(self.advancements)

        if self.sort is not None:
            yield 'sort', str(self.sort)

        if self.limit is not None:
            yield 'limit', str(self.limit)

    @property
    @abc.abstractmethod
    def base(self) -> SelectorBase:
        """ Return the base selector type as a `SelectorBase`. For example, the `s` in `@s`. """
