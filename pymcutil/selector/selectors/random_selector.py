from pymcutil.selector.abc.selector import Selector
from pymcutil.symbols import selector_bases
from pymcutil.symbols.selector_bases.selector_bases import SelectorBase


class RandomSelector(Selector):
    @property
    def base(self) -> SelectorBase:
        return selector_bases.random


random = RandomSelector

RANDOM = RandomSelector()
