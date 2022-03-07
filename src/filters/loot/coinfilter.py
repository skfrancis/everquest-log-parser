from ..basicfilter import BasicFilter


class CoinFilter(BasicFilter):
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
