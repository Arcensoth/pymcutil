from pymcutil.selector.selector import Selector

BASE = 's'


class SelfSelector(Selector):
    @property
    def base(self) -> str:
        return BASE


self = SelfSelector

SELF = self()
