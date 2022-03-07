from src.filters.basicfilter import BasicFilter


class LocationFilter(BasicFilter):
    def __init__(self):
        name = 'Location'
        columns = ['Date', 'Time', 'Y', 'X', 'Z']
        regexes = [
            r"^Your Location is (-?\d+.+?), (-?\d+.+?), (-?\d+.+?)$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(2),
            self.columns[4]: result.group(3),
        }
        return data
