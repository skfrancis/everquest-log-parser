from abc import ABC
from basicfilter import BasicFilter


class FightFilter(BasicFilter, ABC):
    def __init__(self, regexes):
        self.name = 'Fight'
        self.columns = ['Timestamp', 'Source', 'Target', 'Amount', 'Ability', 'Mod', 'Type']
        super().__init__(self.name, self.columns, regexes)
