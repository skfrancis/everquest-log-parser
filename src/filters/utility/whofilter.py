from filters.basicfilter import BasicFilter


class WhoFilter(BasicFilter):
    def __init__(self):
        name = 'Who'
        columns = ['Date', 'Time', 'Name', 'Class', 'Level']
        regexes = [
            r"^[A-Z\s]*\[(?:(ANONYMOUS)|(?P<lvl>\d+) (?P<class>[\w\s]+)|(?P<lvl>\d+)"
            r" .+? \((?P<class>[\w\s]+)\))\](?:\s+(?P<name>\w+))"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group('name'),
            self.columns[3]: result.group('class'),
            self.columns[4]: result.group('lvl')
        }
        return data
