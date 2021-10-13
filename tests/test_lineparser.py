import pytest
from src.util.lineparser import LineParser
from datetime import datetime


class TestLineParse:
    @pytest.fixture
    def log_file_data(self):
        data = [
            '[Sat Jan 31 23:59:59 2020] Welcome to EverQuest!',
            '[Sat Jan 1 00:00:00 2000]',
            '[] Welcome to Everquest!',
            'Welcome to Everquest!',
            '',
            None
        ]
        return data

    def test_parse_line(self, log_file_data):
        line_parser = LineParser()

        for data in log_file_data:
            parsed_data = line_parser.parse_line(data)
            assert type(parsed_data) == dict
            if parsed_data:
                assert type(parsed_data.get('timestamp')) == datetime
                assert type(parsed_data.get('text')) == str
