from filters.basicfilter import BasicFilter


class DiceFilter(BasicFilter):
    def __init__(self):
        name = 'Random Rolls'
        columns = ['Date', 'Time', 'Source', 'Minimum', 'Maximum', 'Roll']
        regexes = [
            r"^\*\*A Magic Die .*? by (\w+). .*? from (\d+) to (\d+), .*? a (\d+).$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(2),
            self.columns[4]: result.group(3),
            self.columns[5]: result.group(4)
        }
        return data
