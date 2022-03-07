from ..basicfilter import BasicFilter


class LootFilter(BasicFilter):
    def __init__(self):
        name = 'Loot'
        columns = ['Date', 'Time', 'Looter', 'Quantity', 'Item', 'Source']
        regexes = [
            r"--(\w+) \w+ looted (an?|\d+) (.+?) from (.+?)?\s?\.--$",
            r"^(\w+) grabbed (an?|\d+) (.+) from ([^.]+?)\s?\.$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        quantity = '1'
        if result.group(2).isnumeric():
            quantity = result.group(2)
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: quantity,
            self.columns[4]: result.group(3),
            self.columns[5]: result.group(4).replace('\'s corpse', '').rstrip()
        }
        return data
