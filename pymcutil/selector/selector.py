import abc
from typing import Any, Dict, Iterator, Tuple

from pymcutil.position.position import Position


class Selector(abc.ABC):
    """ An abstract base class representing a Minecraft target selector. """

    def __init__(
            self, position: Position.Generic = None, volume: Position.Generic = None, type: str = None, l: int = None,
            lm: int = None, m: int = None, team: str = None, max_scores: Dict[str, int] = None,
            min_scores: Dict[str, int] = None, exact_scores: Dict[str, int] = None, name: str = None, tag: str = None,
            r: int = None, rm: int = None, rx: float = None, rxm: float = None, ry: float = None, rym: float = None,
            c: int = None):

        self.position = Position.sift(position, None)
        self.volume = Position.sift(volume, None)
        self.type = type
        self.l = l
        self.lm = lm
        self.m = m
        self.team = team
        self.max_scores = max_scores or {}
        self.min_scores = min_scores or {}
        self.name = name
        self.tag = tag
        self.r = r
        self.rm = rm
        self.rx = rx
        self.rxm = rxm
        self.ry = ry
        self.rym = rym
        self.c = c

        if exact_scores:
            for k, v in exact_scores.items():
                self.max_scores[k] = v
                self.min_scores[k] = v

    def __str__(self):
        return self.to_str()

    def _arguments_nullable(self):
        # Argument processing order:
        # x/y/z, dx/dy/dz, type, l/lm, m, team, score, name, tag, r/rm, rx/rxm/ry/rym, c

        yield 'x', int(self.position.x) if self.position else None
        yield 'y', int(self.position.y) if self.position else None
        yield 'z', int(self.position.z) if self.position else None
        yield 'dx', int(self.volume.x) if self.volume else None
        yield 'dy', int(self.volume.y) if self.volume else None
        yield 'dz', int(self.volume.z) if self.volume else None
        yield 'type', self.type
        yield 'l', self.l
        yield 'lm', self.lm
        yield 'm', self.m
        yield 'team', self.team

        for objective, score in self.max_scores.items():
            yield 'score_{}'.format(objective), score

        for objective, score in self.min_scores.items():
            yield 'score_{}_min'.format(objective), score

        yield 'name', self.name
        yield 'tag', self.tag
        yield 'r', self.r
        yield 'rm', self.rm
        yield 'rx', round(self.rx, 1) if self.rx is not None else None
        yield 'rxm', round(self.rxm, 1) if self.rxm is not None else None
        yield 'ry', round(self.ry, 1) if self.ry is not None else None
        yield 'rym', round(self.rym, 1) if self.rym is not None else None
        yield 'c', self.c

    def arguments(self) -> Iterator[Tuple[str, Any]]:
        yield from ((k, v) for k, v in self._arguments_nullable() if v is not None)

    def to_str(self) -> str:
        selector_str = '@{}'.format(self.base)
        args_str = ','.join('{}={}'.format(key, value) for key, value in self.arguments())
        if args_str:
            selector_str = '{}[{}]'.format(selector_str, args_str)
        return selector_str

    @property
    @abc.abstractmethod
    def base(self) -> str:
        """ Return the base selector type. """
