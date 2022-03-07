from string import capwords
from src.filters.fightfilter import FightFilter


class SpellFilter(FightFilter):
    def __init__(self):
        regexes = [
            r"^(?P<source>.+?) hit (?P<target>.+?) for (?P<amount>\d+) points? of .+? damage by (?P<spell>.+?)"
            r"\.(?: \((?P<mod>[\w\s]+)\))?$",
            r"^(?P<target>.+?) has taken (?P<amount>\d+) damage from (?P<source>you)r (?P<spell>.+?)\."
            r"(?: \((?P<mod>[\w\s]+)\))?",
            r"^(?P<target>.+?) ha(?:s|ve) taken (?P<amount>\d+) damage from (?P<spell>.+?) by (?P<source>.+?)\."
            r"(?: \((?P<mod>[\w\s]+)\))?",
            r"^(?P<target>.+) (?P<amount>resist)ed (?P<source>you)r (?P<spell>.+?)!(?: \((?P<mod>[\w\s]+)\))?",
            r"^(?P<target>You) (?P<amount>resist) (?P<source>.+?)'s (?P<spell>.+)!(?: \((?P<mod>[\w\s]+)\))?"
        ]
        super().__init__(regexes)

    def process_data(self, timestamp, result):
        filter_type = 'spell hit' if result.group('amount').isnumeric() else 'spell miss'
        mod = capwords(result.group('mod')) if result.group('mod') is not None else result.group('mod')
        data = {
            self.columns[0]: timestamp,
            self.columns[1]: capwords(result.group('source').replace('YOUR', 'You')),
            self.columns[2]: capwords(result.group('target')),
            self.columns[3]: capwords(result.group('amount')),
            self.columns[4]: result.group('spell'),
            self.columns[5]: mod,
            self.columns[6]: filter_type
        }
        return data
