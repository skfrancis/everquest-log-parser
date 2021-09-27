from filters.basicfilter import BasicFilter


class LootCoinFilter(BasicFilter):
    def __init__(self):
        name = 'Looted Coin'
        columns = ['Date', 'Time', 'Looter', 'Platinum', 'Gold', 'Silver', 'Copper']
        regexes = [
            r"^(?:(You) receive) (?:(\d+) (\w+?), )?(?:(\d+) (\w+?), )?(?:(\d+) (\w+?) and )?"
            r"(?:(\d+) (\w+?) )(?:from the corpse|as your split)\.$",
            r"^The master looter, (\w+?), looted (?:(\d+) (\w+?), )?(?:(\d+) (\w+?), )?(?:(\d+) "
            r"(\w+?) and )?(?:(\d+) (\w+?) )(?:from the corpse|as your split)\.$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: None,
            self.columns[4]: None,
            self.columns[5]: None,
            self.columns[6]: None,
            result.group(9).capitalize(): result.group(8)
        }
        if result.group(7):
            data[result.group(7).capitalize()] = result.group(6)
        if result.group(5):
            data[result.group(5).capitalize()] = result.group(4)
        if result.group(3):
            data[result.group(3).capitalize()] = result.group(2)
        return data


class LootFilter(BasicFilter):
    def __init__(self):
        name = 'Loot'
        columns = ['Date', 'Time', 'Looter', 'Quantity', 'Item', 'Source']
        regexes = [
            r"^--(\w+) \w+ looted (an?|\d+) ([^.]+) from ([^.]+)?\s?\.--$",
            r"^(\w+) grabbed a (.+) from ([^.]+?)\s?\.$"
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
            self.columns[4]: result.group(3),
            self.columns[5]: result.group(4).replace('\'s corpse', '')
        }
        return data


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
