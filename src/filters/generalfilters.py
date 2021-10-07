from src.filters.basicfilter import BasicFilter


class ChatFilter(BasicFilter):
    def __init__(self):
        name = 'Chat'
        columns = ['Date', 'Time', 'Channel', 'Source', 'Target', 'Message']
        regexes = [
            r"^(.+?) (?:say to your|told|tell your|tells the|tells?) (.+?),\s(?:in .+, )?\s?'(.+)'$",
            r"^(.+?) (says? out of character|says?|shouts?|auctions?),\s(?:in .+, )?'(.+)'$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        target = None
        channel = result.group(2).capitalize()
        if result.group(2) == 'you' or result.string.startswith('You told'):
            target = channel
            channel = 'Tell'
        if 'out of character' in result.group(2):
            channel = 'OoC'
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: channel.rstrip('s'),
            self.columns[3]: result.group(1),
            self.columns[4]: target,
            self.columns[5]: result.group(3)
        }
        return data


class DiceFilter(BasicFilter):
    def __init__(self):
        name = 'Random Rolls'
        columns = ['Date', 'Time', 'Source', 'Minimum', 'Maximum', 'Roll']
        regexes = [
            r"^\*\*A Magic Die .*? by (\w+). .*? from (\d+) to (\d+), .*? a (\d+).$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(2),
            self.columns[4]: result.group(3),
            self.columns[5]: result.group(4)
        }
        return data


class LocationFilter(BasicFilter):
    def __init__(self):
        name = 'Location'
        columns = ['Date', 'Time', 'Y', 'X', 'Z']
        regexes = [
            r"^Your Location is (-?\d+.+?), (-?\d+.+?), (-?\d+.+?)$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(2),
            self.columns[4]: result.group(3),
        }
        return data


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


class TradesFilter(BasicFilter):
    def __init__(self):
        name = 'Tradeskills'
        columns = ['Date', 'Time', 'Source', 'Created', 'Item']
        regexes = [
            r"^(.+?) (have fashioned the items together to create [^:]+:) ([^.]+)\.$",
            r"^(.+?) (has fashioned) ([^.]+)\.$",
            r"^(.+?) (lacked the skills to fashion) ([^.]+)\.$",
            r"^(.+?) (was not successful in making) ([^.]+)\.$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        created = False
        if 'fashioned' in result.group(2):
            created = True
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: str(created),
            self.columns[4]: result.group(3)
        }
        return data


class SystemMessageFilter(BasicFilter):
    def __init__(self):
        name = 'System Message'
        columns = ['Date', 'Time', 'Message']
        regexes = [
            r"^<SYSTEMWIDE_MESSAGE>: ?(.+?)$"
        ]
        super().__init__(name, columns, regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1)
        }
        return data
