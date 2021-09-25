import re
from datetime import datetime


class LineParser:
    def __init__(self, debug=False):
        self.line_regex = re.compile(r'^\[(.*?)] (.*?)$')
        self.date_format = '%a %b %d %H:%M:%S %Y'
        self.debug = debug

    def parse_line(self, line_data):
        data = {}
        result = re.match(self.line_regex, line_data)
        if result:
            data['timestamp'] = self.convert_date(result.group(1))
            data['text'] = result.group(2)
            if self.debug:
                data['debug'] = line_data
        return data

    def convert_date(self, date_string):
        try:
            return datetime.strptime(date_string, self.date_format)
        except ValueError:
            return None
