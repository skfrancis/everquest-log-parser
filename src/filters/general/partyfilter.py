from src.filters.basicfilter import BasicFilter


class PartyFilter(BasicFilter):
    def __init__(self):
        name = 'Party'
        columns = ['Date', 'Time', 'Member', 'Status', 'Type']
        regexes = [
            r"^(?P<player>.+?)(?: have| has)? (?P<status>join)ed the (?P<type>group|raid)\.$",
            r"^(?P<player>You) notify \w+ that you agree to (join) the (?P<type>group|raid)\.$",
            r"^(?P<player>.+?) (?:have been|has been|has|were) (?P<status>left|removed from)"
            r" the (?P<type>group|raid)\.",
            r"^You (?P<status>remove) (?P<player>.+?) from the (?P<type>group|party|raid)\.$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(2),
            self.columns[4]: result.group(3)
        }
        return data
