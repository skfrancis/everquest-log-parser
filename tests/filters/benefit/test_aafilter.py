import pytest
from util.lineparser import LineParser
from filters.benefit.aafilter import AAFilter


class TestAAFilter:
    @pytest.fixture
    def parse_data(self):
        parser = LineParser()
        log_data = [
            '[Sat Jan 31 23:59:59 2020] Welcome to EverQuest!',
            '[Sat Jan 31 23:59:59 2020] You have gained 2 ability point(s)!  You now have 39 ability point(s).'
        ]
        parsed_data = []
        for line in log_data:
            parsed_data.append(parser.parse_line(line))
        return parsed_data

    def test_process_data(self, parse_data):
        filterer = AAFilter()
        assert filterer.filter(parse_data[0]) is None
        filtered_data = filterer.filter(parse_data[1])
        assert type(filtered_data) == dict
        assert filtered_data.get('Banked') == '39'
        assert filtered_data.get('Gained') == '2'

