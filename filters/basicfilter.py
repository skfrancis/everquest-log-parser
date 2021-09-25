import regex
from abc import ABC, abstractmethod


class BasicFilter(ABC):
    def __init__(self, name, columns, regexes, debug=False):
        self.name = name
        self.columns = columns
        self.regexes = regexes
        self.debug = debug

    def filter(self, log_line):
        for expression in self.regexes:
            result = regex.search(expression, log_line.get('text'))
            if result:
                timestamp = log_line.get('timestamp')
                filtered_data = self.process_data(timestamp, result)
                if self.debug:
                    print(filtered_data)
                return filtered_data
        return None

    @abstractmethod
    def process_data(self, timestamp, result):
        pass
