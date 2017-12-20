from pymcutil.util.symbol import Symbol


class SelectorBase(Symbol):
    pass


all_players = SelectorBase('all_players')
entities = SelectorBase('entities')
player = SelectorBase('player')
random = SelectorBase('random')
self = SelectorBase('self')
