from src.filters.basicfilter import BasicFilter


class AAFilter(BasicFilter):
    def __init__(self):
        name = 'AA'
        columns = ['Date', 'Time', 'Gained', 'Banked']
        regexes = [
            r"^You have gained (\d+) ability point\(s\)!\s+You now have (\d+) ability point\(s\).$"
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
