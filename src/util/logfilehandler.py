import re
import logging
from os import SEEK_END
from pathlib import Path
from src.util.lineparser import LineParser


class LogFileHandler:
    def __init__(self, config_handler):
        self.logger = logging.getLogger(__name__)
        self.parser = LineParser()
        self.file_name_regex = re.compile(r'^eqlog_(\w+)_(\w+).txt$')
        self.log_file = Path(config_handler.log_file)
        self.character_info = self.parse_file_name()

    def parse_file_name(self):
        player_data = {}
        if self.log_file.exists() and self.log_file.is_file():
            result = re.search(self.file_name_regex, self.log_file.name)
            if result:
                player_data['character'] = result.group(1).capitalize()
                player_data['server'] = result.group(2).capitalize()
                self.logger.debug(f"Log File Parsed Data: {player_data}")
            else:
                self.logger.debug(f"Invalid Log File: {self.log_file.name}")
        else:
            self.logger.debug(f"No Such Log File: {self.log_file.name}")
        return player_data

    def run_parser(self):
        if self.log_file.exists() and self.log_file.is_file() and self.character_info:
            with self.log_file.open('r', encoding="utf8") as open_file:
                open_file.seek(0, SEEK_END)
                while True:
                    line = open_file.readline()
                    if line:
                        parsed_line = self.parser.parse_line(line)
                        self.logger.debug(f"Ignored Line: {parsed_line}")
                        yield parsed_line
        else:
            self.logger.debug(f"Invalid Log File Name: {self.log_file.name}")
            return None

    def load_log_file(self):
        if self.log_file.exists() and self.log_file.is_file() and self.character_info:
            log_line_data = self.process_log_data()
            return self.parse_log_data(log_line_data)
        else:
            self.logger.debug(f"Invalid Log File Name: {self.log_file.name}")

    def process_log_data(self):
        with self.log_file.open('r', encoding="utf8") as open_file:
            log_line_data = open_file.readlines()
            self.logger.debug(f"File has been opened successfully: loaded {len(log_line_data)} total lines")
            open_file.close()
            return log_line_data

    def parse_log_data(self, log_line_data):
        data = []
        for line_data in log_line_data:
            parsed_data = self.parser.parse_line(line_data)
            if parsed_data:
                data.append(parsed_data)
            else:
                self.logger.debug(f"{line_data} failed to be parsed")
        self.logger.debug(f"File has been parsed successfully: parsed {len(data)} total lines")
        return data
