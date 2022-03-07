from src.filters.basicfilter import BasicFilter


class ZoneFilter(BasicFilter):
    def __init__(self):
        name = 'Zoning'
        columns = ['Date', 'Time', 'Zone']
        regexes = [
            r"^You have entered (.+)\.$"
        ]
        super().__init__(name, columns, regexes)
        self.non_zones = [
            'an area where levitation effects do not function',
            'an Arena (PvP) area',
            'an area where Bind Affinity is allowed',
            'the Drunken Monkey stance adequately'
        ]

    def process_data(self, timestamp, result):
        for non_zone in self.non_zones:
            if non_zone in result.group(1):
                return None
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1)
        }
        return data
