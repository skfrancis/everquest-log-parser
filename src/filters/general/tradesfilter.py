from src.filters.basicfilter import BasicFilter


class TradesFilter(BasicFilter):
    def __init__(self):
        name = 'Tradeskills'
        columns = ['Date', 'Time', 'Source', 'Created', 'Item']
        regexes = [
            r"^(.+?) (have fashioned the items together to create [^:]+:) ([^.]+)\.$",
            r"^(.+?) (has fashioned) ([^.]+)\.$",
            r"^(.+?) (lacked the skills to fashion) ([^.]+)\.$",
            r"^(.+?) (was not successful in making) ([^.]+)\.$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        created = False
        if 'fashioned' in result.group(2):
            created = True
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: str(created),
            self.columns[4]: result.group(3)
        }
        return data
