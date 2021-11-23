from string import capwords
from filters.fightfilter import FightFilter


class HealingFilter(FightFilter):
    def __init__(self):
        regexes = [
            r"^(?P<source>.+?) healed (?P<target>.+?) over time for (?P<actual>\d+)(?: \((?P<max>\d+)\))? "
            r"hit points by (?P<spell>.+?)\.(?: \((?P<mod>.+?)\))?",
            r"^(?P<source>.+?) healed (?P<target>.+?) for (?P<actual>\d+)(?: \((?P<max>\d+)\))? "
            r"hit points(?: by (?P<spell>.+?))?\.(?: \((?P<mod>.+?)\))?"
        ]
        super().__init__(regexes)

    def process_data(self, timestamp, result):
        maximum = result.group('max') if result.group('max') is not None else result.group('actual')
        mod = capwords(result.group('mod')) if result.group('mod') is not None else result.group('mod')
        data = {
            self.columns[0]: timestamp,
            self.columns[1]: capwords(result.group('source').replace('YOUR', 'You')),
            self.columns[2]: capwords(result.group('target')),
            self.columns[3]: (result.group('actual'), maximum),
            self.columns[4]: result.group('spell'),
            self.columns[5]: mod,
            self.columns[6]: 'heal'
        }
        return data
