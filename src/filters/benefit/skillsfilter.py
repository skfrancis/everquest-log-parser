from src.filters.basicfilter import BasicFilter


class SkillsFilter(BasicFilter):
    def __init__(self):
        name = 'Skills'
        columns = ['Date', 'Time', 'Skill', 'Level']
        regexes = [
            r"^You have become better at (.+)! \((\d+)\)$"
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
