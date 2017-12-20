from pymcutil.selector.abc.selector import Selector
from pymcutil.symbols import selector_bases
from pymcutil.symbols.selector_bases.selector_bases import SelectorBase


class SelfSelector(Selector):
    @property
    def base(self) -> SelectorBase:
        return selector_bases.self


self = SelfSelector

SELF = self()
