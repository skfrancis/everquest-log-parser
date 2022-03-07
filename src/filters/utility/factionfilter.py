from src.filters.basicfilter import BasicFilter


class FactionFilter(BasicFilter):
    def __init__(self):
        name = 'Faction'
        columns = ['Date', 'Time', 'Faction', 'Amount']
        regexes = [
            r"^Your faction standing with ([^.]+) has been adjusted by (-?\d+)\.$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(2)
        }
        return data
