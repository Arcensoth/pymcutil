from pymcutil.selector.selector import Selector

BASE = 'e'


class EntitiesSelector(Selector):
    @property
    def base(self):
        return BASE


entities = EntitiesSelector

ENTITIES = EntitiesSelector()
