import logging
from pathlib import Path
from util.lineparser import LineParser


class LogLoader:
    def __init__(self, log_file):
        self.logger = logging.getLogger(__name__)
        self.log_file = Path(log_file)
        self.log_line_count = self.file_line_count()
        self.log_data = self.process_log_file()
        self.parser = LineParser()

    def file_line_count(self):
        line_count = 0
        buffer_size = 1024 * 1024
        with self.log_file.open('rb') as open_file:
            read_file = open_file.raw.read
            buffer = read_file(buffer_size)
            while buffer:
                line_count += buffer.count(b'\n')
                buffer = read_file(buffer_size)
        open_file.close()
        self.logger.debug(f"File has {line_count} lines total")
        return line_count

    def get_line_count(self):
        return self.log_line_count

    def process_log_file(self):
        with self.log_file.open('r', encoding="utf8") as open_file:
            log_lines = open_file.readlines()
            self.logger.debug(f"File has been opened successfully: {len(log_lines)} total lines")
            open_file.close()
            return log_lines

    def parse_log_file(self):
        data = []
        for log_line in self.log_data:
            parsed_line = self.parser.parse_line(log_line)
            if parsed_line:
                data.append(parsed_line)
        self.logger.debug(f"File has been parsed successfully: {len(data)} total lines")
        return data
