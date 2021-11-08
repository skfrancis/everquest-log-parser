import pytest
from util.lineparser import LineParser
from filters.loot.lootfilter import LootFilter


class TestFilter:
    @pytest.fixture
    def parse_data(self):
        parser = LineParser()
        log_data = [
            '[Sat Jan 31 23:59:59 2020] Welcome to EverQuest!',
            "[Sat Jan 31 23:59:59 2020] --You have looted a Rat Whiskers from a large rat's corpse.--",
            "[Sat Jan 31 23:59:59 2020] --Tester have looted 2 Snake Scales from a snake's corpse.--",
            "[Sat Jan 31 23:59:59 2020] --You have looted 5 Snake Scales from a frozen chest .--",
            "[Sat Jan 31 23:59:59 2020] Tester grabbed a Bone Chips from a dry bones skeleton.",
            "[Sat Jan 31 23:59:59 2020] --Tester has looted a Salil's Writ Pg. 64 from a wan ghoul knight's corpse.--"
        ]
        parsed_data = []
        for line in log_data:
            parsed_data.append(parser.parse_line(line))
        return parsed_data

    def test_process_data(self, parse_data):
        filterer = LootFilter()
        assert filterer.filter(parse_data[0]) is None
        filtered_data = filterer.filter(parse_data[1])
        assert type(filtered_data) == dict
        assert filtered_data.get('Looter') == 'You'
        assert filtered_data.get('Quantity') == '1'
        assert filtered_data.get('Item') == 'Rat Whiskers'
        assert filtered_data.get('Source') == 'a large rat'
        filtered_data = filterer.filter(parse_data[2])
        assert type(filtered_data) == dict
        assert filtered_data.get('Looter') == 'Tester'
        assert filtered_data.get('Quantity') == '2'
        assert filtered_data.get('Item') == 'Snake Scales'
        assert filtered_data.get('Source') == 'a snake'
        filtered_data = filterer.filter(parse_data[3])
        assert type(filtered_data) == dict
        assert filtered_data.get('Looter') == 'You'
        assert filtered_data.get('Quantity') == '5'
        assert filtered_data.get('Item') == 'Snake Scales'
        assert filtered_data.get('Source') == 'a frozen chest'
        filtered_data = filterer.filter(parse_data[4])
        assert type(filtered_data) == dict
        assert filtered_data.get('Looter') == 'Tester'
        assert filtered_data.get('Quantity') == '1'
        assert filtered_data.get('Item') == 'Bone Chips'
        assert filtered_data.get('Source') == 'a dry bones skeleton'
        filtered_data = filterer.filter(parse_data[5])
        assert type(filtered_data) == dict
        assert filtered_data.get('Looter') == 'Tester'
        assert filtered_data.get('Quantity') == '1'
        assert filtered_data.get('Item') == "Salil's Writ Pg. 64"
        assert filtered_data.get('Source') == 'a wan ghoul knight'
