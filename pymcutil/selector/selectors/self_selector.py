from typing import Dict

from pymcutil.position.position import Position
from pymcutil.selector.selector import Selector

BASE = 's'


class SelfSelector(Selector):
    @property
    def base(self):
        return BASE


def self(
        position: Position = None, volume: Position = None, type: str = None, l: int = None, lm: int = None,
        m: int = None, team: str = None, max_scores: Dict[str, int] = None, min_scores: Dict[str, int] = None,
        exact_scores: Dict[str, int] = None, name: str = None, tag: str = None, r: int = None, rm: int = None,
        rx: float = None, rxm: float = None, ry: float = None, rym: float = None, c: int = None) -> SelfSelector:
    """ Functional alias for creating `SelfSelector` instances. """
    return SelfSelector(
        position=position, volume=volume, type=type, l=l, lm=lm, m=m, team=team,
        max_scores=max_scores, min_scores=min_scores, exact_scores=exact_scores, name=name, tag=tag,
        r=r, rm=rm, rx=rx, rxm=rxm, ry=ry, rym=rym, c=c)


SELF = SelfSelector()
