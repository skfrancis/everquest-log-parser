from filters.basicfilter import BasicFilter


class ExpAAFilter(BasicFilter):
    def __init__(self, debug=False):
        name = 'AA'
        columns = ['Date', 'Time', 'Gained', 'Banked']
        regexes = [
            r"^You have gained (\d+) ability point\(s\)!\s+You now have (\d+) ability point\(s\).$"
        ]
        super().__init__(name, columns, regexes, debug)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(2)
        }
        if self.debug:
            data['debug'] = result.string
        return data


class ExpFilter(BasicFilter):
    def __init__(self, debug=False):
        name = 'Experience'
        columns = ['Date', 'Time', 'Type']
        regexes = [
            r"^You gaine?d? (experience|party|raid)"
        ]
        super().__init__(name, columns, regexes, debug)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1)
        }
        if self.debug:
            data['debug'] = result.string
        return data


class SkillUpFilter(BasicFilter):
    def __init__(self, debug=False):
        name = 'Skills'
        columns = ['Date', 'Time', 'Skill', 'Level']
        regexes = [
            r"^You have become better at (.+)! \((\d+)\)$"
        ]
        super().__init__(name, columns, regexes, debug)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(2)
        }
        if self.debug:
            data['debug'] = result.string
        return data
