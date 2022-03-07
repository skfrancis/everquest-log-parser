from src.filters.basicfilter import BasicFilter


class ConsiderFilter(BasicFilter):
    def __init__(self):
        name = 'Consider'
        columns = ['Date', 'Time', 'Target', 'Level', 'Consider', 'Difficulty', 'Rare']
        regexes = [
            r"(.+) (-.+)? ((?:scowls|glares|glowers|regards|looks|judges|kindly) .+?) -- (.+) \(Lvl: (\d+)\)$",
            r"(.+)( -.+)? ((?:scowls|glares|glowers|regards|looks|judges|kindly) .+?) -- (.+) \(Lvl: (\d+)\)$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(5),
            self.columns[4]: result.group(3),
            self.columns[5]: result.group(4),
            self.columns[6]: bool(result.group(2))
        }
        return data
