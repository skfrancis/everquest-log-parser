import re
import logging
from datetime import datetime


class LineParser:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.line_regex = re.compile(r'^\[(.*?)] (.*?)$')
        self.date_format = '%a %b %d %H:%M:%S %Y'

    def parse_line(self, line_data):
        data = {}
        result = re.match(self.line_regex, line_data)
        if result:
            data['timestamp'] = self.convert_date(result.group(1))
            data['text'] = result.group(2)
        else:
            self.logger.debug(f"Parsing Failed: {line_data.rstrip()}")
        return data

    def convert_date(self, date_string):
        try:
            return datetime.strptime(date_string, self.date_format)
        except ValueError:
            return None
