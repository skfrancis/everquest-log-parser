from string import capwords
from src.filters.fightfilter import FightFilter


class DeathFilter(FightFilter):
    def __init__(self):
        regexes = [
            r"^(?P<target>.+) (?:have|has) been slain by (?P<source>.+)!$",
            r"^(?P<source>You) have slain (?P<target>.+)!$",
            r"^(?P<source>(?P<target>.+)) dies?d?\.$"
        ]
        super().__init__(regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp,
            self.columns[1]: capwords(result.group('source')),
            self.columns[2]: capwords(result.group('target')),
            self.columns[3]: None,
            self.columns[4]: None,
            self.columns[5]: None,
            self.columns[6]: 'death'
        }
        return data
