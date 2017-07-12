from pymcutil.selector.selector import Selector

BASE = 's'


class SelfSelector(Selector):
    @property
    def base(self):
        return BASE


self = SelfSelector

SELF = self()
