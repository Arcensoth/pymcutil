from pymcutil.selector.selector import Selector

BASE = 'r'


class RandomSelector(Selector):
    @property
    def base(self):
        return BASE


random = RandomSelector

RANDOM = RandomSelector()
