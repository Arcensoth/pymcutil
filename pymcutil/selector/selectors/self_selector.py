from pymcutil.selector.selector import Selector

BASE = 's'


class SelfSelector(Selector):
    @classmethod
    def base(cls) -> str:
        return BASE


self = SelfSelector

SELF = self()
