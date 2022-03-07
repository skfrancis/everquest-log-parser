from src.filters.basicfilter import BasicFilter


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
