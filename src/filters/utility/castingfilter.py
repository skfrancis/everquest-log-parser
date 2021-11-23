from filters.basicfilter import BasicFilter


class CastingFilter(BasicFilter):
    def __init__(self):
        name = 'Casting'
        columns = ['Date', 'Time', 'Source', 'Spell']
        regexes = [
            r"^(.+?) begins? (?:casting|singing) (.+)\.$",
            r"^(.+?) activates? (.+)\.$"
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
