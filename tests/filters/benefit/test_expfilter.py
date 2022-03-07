import pytest
from src.util.lineparser import LineParser
from src.filters.benefit.expfilter import ExpFilter


class TestExpFilter:
    @pytest.fixture
    def parse_data(self):
        parser = LineParser()
        log_data = [
            '[Sat Jan 31 23:59:59 2020] Welcome to EverQuest!',
            '[Sat Jan 31 23:59:59 2020] You gain experience!',
            '[Sat Jan 31 23:59:59 2020] You gain experience (with a bonus)!',
            '[Sat Jan 31 23:59:59 2020] You gain party experience!',
            '[Sat Jan 31 23:59:59 2020] You gain party experience (with a bonus)!',
            '[Sat Jan 31 23:59:59 2020] You gain raid experience!',
            '[Sat Jan 31 23:59:59 2020] You gain raid experience (with a bonus)!'
        ]
        parsed_data = []
        for line in log_data:
            parsed_data.append(parser.parse_line(line))
        return parsed_data

    def test_process_data(self, parse_data):
        filterer = ExpFilter()
        assert filterer.filter(parse_data[0]) is None
        for index in range(1, 6):
            filtered_data = filterer.filter(parse_data[index])
            assert type(filtered_data) == dict
            if 0 < index < 3:
                assert filtered_data.get('Type') == 'solo'
            if 2 < index < 5:
                assert filtered_data.get('Type') == 'party'
            if 4 < index < 7:
                assert filtered_data.get('Type') == 'raid'

