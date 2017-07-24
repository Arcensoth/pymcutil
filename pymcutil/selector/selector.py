import abc
from typing import Any, Dict, Iterator, List, Tuple, Union

from pymcutil.data_tag.compound_data_tag import CompoundDataTag
from pymcutil.position.position import Position

# TODO this whole thing is a mess; clean it up

RepeatableString = Union[str, Tuple[str, ...], List[str]]
RepeatableNBT = Union[CompoundDataTag.Generic, Tuple[CompoundDataTag.Generic, ...], List[CompoundDataTag.Generic]]


def tuplize(obj) -> tuple:
    return tuple(obj) if isinstance(obj, (list, tuple)) else (obj,)


class Selector(abc.ABC):
    """ An abstract base class representing a Minecraft target selector. """

    def __init__(
            self,
            position: Position.Generic = None, volume: Position.Generic = None,
            type: str = None, not_type: RepeatableString = None,
            l: int = None, lm: int = None,
            m: str = None, not_m: RepeatableString = None,
            team: str = None, not_team: RepeatableString = None,
            max_scores: Dict[str, int] = None, min_scores: Dict[str, int] = None,
            exact_scores: Dict[str, int] = None,
            name: str = None, not_name: RepeatableString = None,
            tag: RepeatableString = None, not_tag: RepeatableString = None,
            r: float = None, rm: float = None,
            rx: float = None, rxm: float = None, ry: float = None, rym: float = None,
            nbt: RepeatableNBT = None, not_nbt: RepeatableNBT = None,
            c: int = None):

        self.position = Position.sift(position, None)
        self.volume = Position.sift(volume, None)

        self.type = str(type) if type is not None else None
        self.not_type: Tuple[str] = tuplize(not_type)

        self.l = int(l) if l is not None else None
        self.lm = int(lm) if lm is not None else None

        self.m = str(m) if m is not None else None
        self.not_m: Tuple[str] = tuplize(not_m)

        self.team = str(team) if team is not None else None
        self.not_team: Tuple[str] = tuplize(not_team)

        self.max_scores = max_scores or {}
        self.min_scores = min_scores or {}

        self.name = str(name) if name is not None else None
        self.not_name: Tuple[str] = tuplize(not_name)

        self.tag: Tuple[str] = tuplize(tag)
        self.not_tag: Tuple[str] = tuplize(not_tag)

        self.r = float(r) if r is not None else None
        self.rm = float(rm) if rm is not None else None

        self.rx = float(rx) if rx is not None else None
        self.rxm = float(rxm) if rxm is not None else None
        self.ry = float(ry) if ry is not None else None
        self.rym = float(rym) if rym is not None else None

        # Note that `nbt` is a tuple of DataTag objects, not itself a DataTag.
        self.nbt: Tuple[CompoundDataTag] = (
            CompoundDataTag.sift(obj) for obj in tuplize(nbt)) if nbt else ()
        self.not_nbt: Tuple[CompoundDataTag] = (
            CompoundDataTag.sift(obj) for obj in tuplize(not_nbt)) if not_nbt else ()

        self.c = int(c) if c is not None else None

        if exact_scores:
            for k, v in exact_scores.items():
                self.max_scores[k] = v
                self.min_scores[k] = v

    def __str__(self):
        return self.to_str()

    def _arguments_nullable(self):
        # Argument processing order:
        # x/y/z, dx/dy/dz, type, l/lm, m, team, score, name, tag, r/rm, rx/rxm/ry/rym, nbt, c

        yield 'x=', self.position.x if self.position else None
        yield 'y=', self.position.y if self.position else None
        yield 'z=', self.position.z if self.position else None
        yield 'dx=', self.volume.x if self.volume else None
        yield 'dy=', self.volume.y if self.volume else None
        yield 'dz=', self.volume.z if self.volume else None

        yield 'type=', self.type
        yield from (('type=!', type_) for type_ in self.not_type)

        yield 'l=', self.l
        yield 'lm=', self.lm

        yield 'm=', self.m
        yield from (('m=!', m) for m in self.not_m)

        yield 'team=', self.team
        yield from (('team=!', team) for team in self.not_team)

        yield from (('score_{}='.format(objective), score) for objective, score in self.max_scores.items())
        yield from (('score_{}_min='.format(objective), score) for objective, score in self.min_scores.items())

        # TODO sanitize name and tags in case of spaces

        yield 'name=', self.name
        yield from (('name=!', name) for name in self.not_name)

        yield from (('tag=', tag) for tag in self.tag)
        yield from (('tag=!', tag) for tag in self.not_tag)

        yield 'r=', self.r
        yield 'rm=', self.rm

        # TODO do these still need to be rounded?
        yield 'rx=', round(self.rx, 1) if self.rx is not None else None
        yield 'rxm=', round(self.rxm, 1) if self.rxm is not None else None
        yield 'ry=', round(self.ry, 1) if self.ry is not None else None
        yield 'rym=', round(self.rym, 1) if self.rym is not None else None

        yield from (('nbt=', nbt) for nbt in self.nbt)
        yield from (('nbt=!', nbt) for nbt in self.not_nbt)

        yield 'c=', self.c

    def arguments(self) -> Iterator[Tuple[str, Any]]:
        yield from ((k, v) for k, v in self._arguments_nullable() if v is not None)

    def to_str(self) -> str:
        selector_str = '@{}'.format(self.base)
        args_str = ','.join(''.join((key, str(value))) for key, value in self.arguments())
        if args_str:
            selector_str = '{}[{}]'.format(selector_str, args_str)
        return selector_str

    @property
    @abc.abstractmethod
    def base(self) -> str:
        """ Return the base selector type. """
