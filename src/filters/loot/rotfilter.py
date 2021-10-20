from filters.basicfilter import BasicFilter


class LootRotFilter(BasicFilter):
    def __init__(self):
        name = 'Rot'
        columns = ['Date', 'Time', 'Source', 'Quantity', 'Item']
        regexes = [
            r"^(No one) was interested in the (\d+) .+: (.+)\. These items .+",
            r"^--(\w+) left (an?|\d+) ([^.]+) on [^.]+?\s?\.--$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        quantity = 1
        if result.group(2).isnumeric():
            quantity = result.group(2)
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: quantity,
            self.columns[4]: result.group(3)
        }
        return data
