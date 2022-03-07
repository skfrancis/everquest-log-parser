from src.filters.basicfilter import BasicFilter


class PetLeaderFilter(BasicFilter):
    def __init__(self):
        name = 'Pet Leader'
        columns = ['Date', 'Time', 'Leader', 'Pet']
        regexes = [
            r"(?P<pet>^[GJKLVXZ]([aeio][bknrs]){0,2}(ab|er|n|tik)) says, 'My leader is (?P<leader>\w+)\.'$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group('leader'),
            self.columns[3]: result.group('pet')
        }
        return data
