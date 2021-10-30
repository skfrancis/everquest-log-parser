import pytest
from util.lineparser import LineParser
from filters.exp.skillsfilter import SkillsFilter


class TestSkillsFilter:
    @pytest.fixture
    def parse_data(self):
        parser = LineParser()
        log_data = [
            '[Sat Jan 31 23:59:59 2020] Welcome to EverQuest!',
            '[Sat Jan 31 23:59:59 2020] You have become better at 1H Slashing! (11)'
        ]
        parsed_data = []
        for line in log_data:
            parsed_data.append(parser.parse_line(line))
        return parsed_data

    def test_process_data(self, parse_data):
        filterer = SkillsFilter()
        assert filterer.filter(parse_data[0]) is None
        filtered_data = filterer.filter(parse_data[1])
        assert type(filtered_data) == dict
        assert filtered_data.get('Skill') == '1H Slashing'
        assert filtered_data.get('Level') == '11'
