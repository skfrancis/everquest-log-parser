from filters.basicfilter import BasicFilter


class ExpFilter(BasicFilter):
    def __init__(self):
        name = 'Experience'
        columns = ['Date', 'Time', 'Type']
        regexes = [
            r"^You gaine?d? (experience|party|raid)"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        exp_type = result.group(1)
        if exp_type == 'experience':
            exp_type = 'solo'
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: exp_type
        }
        return data
