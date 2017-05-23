from typing import Dict

from pymcutil.position.position import Position
from pymcutil.selector.selector import Selector

BASE = 's'


class SelfSelector(Selector):
    @property
    def base(self):
        return BASE


def self(
        position: Position = None, volume: Position = None, entity_type: str = None,
        l: int = None, lm: int = None, m: int = None, team: str = None,
        min_scores: Dict[str, int] = None, max_scores: Dict[str, int] = None,
        name: str = None, tag: str = None, r: int = None, rm: int = None,
        rx: float = None, rxm: float = None, ry: float = None, rym: float = None,
        c: int = None, exact_scores: Dict[str, int] = None) -> SelfSelector:
    """ Functional alias for creating `SelfSelector` instances. """
    return SelfSelector(**locals())
