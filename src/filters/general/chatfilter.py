from filters.basicfilter import BasicFilter


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
