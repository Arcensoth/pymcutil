import abc
from numbers import Real
from typing import Any, Iterable, Iterator, Tuple, Union

from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.position.position import Position
from pymcutil.selector.advancement_set import AdvancementSet
from pymcutil.selector.range import Range
from pymcutil.selector.score_set import ScoreSet
from pymcutil.selector.selector_sort import SelectorSort
from pymcutil.util import first
from pymcutil.util.gamemode import Gamemode

RepeatableString = Union[str, Iterable[str]]
RepeatableGamemode = Union[Gamemode, Iterable[Gamemode]]
RepeatableNBT = Union[CompoundDataTag.Generic, Iterable[CompoundDataTag.Generic]]


def tuplize(obj) -> tuple:
    if obj is None:
        return ()
    elif isinstance(obj, (str, Gamemode, CompoundDataTag.Generic)):
        return obj,  # wrap in a tuple
    elif isinstance(obj, Iterable):
        return tuple(obj)  # make a copy
    raise ValueError('Invalid selector argument: {}'.format(obj))


class Selector(abc.ABC):
    """
    Represents a Minecraft target selector, with similar arguments and some built-in conveniences.

    Provided arguments cascade such that the most specific value is used. For example, an explicitly provided `x`
    coordinate will take precedence over the `x` component of any given `position`.
    """

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
        # Don't actually save these; just use them for intermediate calculations.
        position = Position.sift(position) if position is not None else None
        volume = Position.sift(volume) if volume is not None else None

        self.x: Real = first(x, position.x if isinstance(position, Position) else None)
        self.y: Real = first(y, position.y if isinstance(position, Position) else None)
        self.z: Real = first(z, position.z if isinstance(position, Position) else None)

        self.dx: Real = first(dx, volume.x if isinstance(volume, Position) else None)
        self.dy: Real = first(dy, volume.y if isinstance(volume, Position) else None)
        self.dz: Real = first(dz, volume.z if isinstance(volume, Position) else None)

        self.x_rotation: Range = Range.sift(x_rotation)
        self.y_rotation: Range = Range.sift(y_rotation)

        self.distance: Range = Range.sift(distance)

        self.level: Range = Range.sift(level)

        self.type: str = type_
        self.not_types: Tuple[str] = tuplize(not_types)

        self.name: str = name
        self.not_names: Tuple[str] = tuplize(not_names)

        self.team: str = team
        self.not_teams: Tuple[str] = tuplize(not_teams)

        self.gamemode: Gamemode = gamemode
        self.not_gamemodes: Tuple[Gamemode] = tuplize(not_gamemodes)

        self.tags: Tuple[str] = tuplize(tags)
        self.not_tags: Tuple[str] = tuplize(not_tags)

        # These are `tuple`s of `DataTag`s, not themselves `DataTag`s.
        self.nbts: Tuple[CompoundDataTag] = (
            CompoundDataTag.sift(obj) for obj in tuplize(nbts)) if nbts else ()
        self.not_nbts: Tuple[CompoundDataTag] = (
            CompoundDataTag.sift(obj) for obj in tuplize(not_nbts)) if not_nbts else ()

        self.scores: ScoreSet = ScoreSet.sift(scores, None)

        self.advancements: AdvancementSet = AdvancementSet.sift(advancements, None)

        self.sort: SelectorSort = sort

        self.limit: int = limit

    def __str__(self):
        return self.to_str()

    def _arguments_nullable(self):
        yield 'x=', self.x
        yield 'y=', self.y
        yield 'z=', self.z

        yield 'dx=', self.dx
        yield 'dy=', self.dy
        yield 'dz=', self.dz

        yield 'distance=', self.distance
        yield 'level=', self.level

        yield 'x_rotation=', self.x_rotation
        yield 'y_rotation=', self.y_rotation

        yield 'type=', self.type
        yield from (('type=!', type_) for type_ in self.not_types)

        # TODO sanitize name and tags in case of spaces

        yield 'name=', self.name
        yield from (('name=!', name) for name in self.not_names)

        yield 'team=', self.team
        yield from (('team=!', team) for team in self.not_teams)

        yield 'gamemode=', self.gamemode
        yield from (('gamemode=!', gamemode) for gamemode in self.not_gamemodes)

        yield from (('tag=', tag) for tag in self.tags)
        yield from (('tag=!', tag) for tag in self.not_tags)

        yield from (('nbt=', nbt) for nbt in self.nbts)
        yield from (('nbt=!', nbt) for nbt in self.not_nbts)

        yield 'scores=', self.scores

        yield 'advancements=', self.advancements

        yield 'sort=', self.sort

        yield 'limit=', self.limit

    def _arguments(self) -> Iterator[Tuple[str, Any]]:
        yield from ((k, v) for k, v in self._arguments_nullable() if v is not None)

    def to_str(self) -> str:
        selector_str = '@{}'.format(self.base)
        args_str = ','.join('='.join((key, str(value))) for key, value in self._arguments())
        if args_str:
            selector_str = '{}[{}]'.format(selector_str, args_str)
        return selector_str

    @property
    @abc.abstractmethod
    def base(self) -> str:
        """ Return the base selector type. """
