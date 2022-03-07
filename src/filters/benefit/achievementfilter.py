from src.filters.basicfilter import BasicFilter


class AchievementFilter(BasicFilter):
    def __init__(self):
        name = 'Achievement'
        columns = ['Date', 'Time', 'Target', 'Achievement']
        regexes = [
            r"^(?:Your guildmate )?(.+?)(?: have| has) completed(?: achievement:)? (.+?)(?:$| achievement.$)"
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
