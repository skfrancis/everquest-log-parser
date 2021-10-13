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
        parsed = False
        if line_data:
            result = re.match(self.line_regex, line_data)
            if result:
                try:
                    data['timestamp'] = datetime.strptime(result.group(1), self.date_format)
                    data['text'] = result.group(2)
                    parsed = True
                except ValueError:
                    self.logger.debug(f"Invalid Value: {result.group(1)}")
        if not parsed:
            self.logger.debug(f"Parsing Failed: {line_data}")
        return data

