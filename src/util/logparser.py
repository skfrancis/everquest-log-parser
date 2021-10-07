import logging
from os import SEEK_END
from pathlib import Path
from src.util.lineparser import LineParser


class LogParser:
    def __init__(self, log_file):
        self.logger = logging.getLogger(__name__)
        self.log_file = Path(log_file)
        self.parser = LineParser()

    def run(self):
        with self.log_file.open('r', encoding="utf8") as open_file:
            open_file.seek(0, SEEK_END)
            while True:
                line = open_file.readline()
                if line:
                    parsed_line = self.parser.parse_line(line)
                    self.logger.debug(parsed_line)
                    yield parsed_line
