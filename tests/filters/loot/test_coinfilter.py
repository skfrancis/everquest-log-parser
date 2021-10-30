import pytest
from util.lineparser import LineParser
from filters.loot.coinfilter import LootCoinFilter


class TestCoinFilter:
    @pytest.fixture
    def parse_data(self):
        parser = LineParser()
        log_data = [
            '[Sat Jan 31 23:59:59 2020] Welcome to EverQuest!',
            '[Sat Jan 31 23:59:59 2020] You receive 129 platinum, 2 gold, 5 silver and 1 copper as your split.',
            '[Sat Jan 31 23:59:59 2020] You receive 2 gold, 5 silver and 1 copper as your split.',
            '[Sat Jan 31 23:59:59 2020] You receive 5 silver and 1 copper as your split.',
            '[Sat Jan 31 23:59:59 2020] You receive 1 copper as your split.',
            '[Sat Jan 31 23:59:59 2020] The master looter, Tester, looted 129 platinum, 2 gold, 5 silver '
            'and 1 copper from the corpse.',
            '[Sat Jan 31 23:59:59 2020] The master looter, Tester, looted 2 gold, 5 silver '
            'and 1 copper from the corpse.',
            '[Sat Jan 31 23:59:59 2020] The master looter, Tester, looted 5 silver and 1 copper from the corpse.',
            '[Sat Jan 31 23:59:59 2020] The master looter, Tester, looted 1 copper from the corpse.'
        ]
        parsed_data = []
        for line in log_data:
            parsed_data.append(parser.parse_line(line))
        return parsed_data

    def test_process_data(self, parse_data):
        filterer = LootCoinFilter()
        assert filterer.filter(parse_data[0]) is None
        for index in range(1, 9):
            filtered_data = filterer.filter(parse_data[index])
            assert type(filtered_data) == dict
            if index < 5:
                assert filtered_data.get('Looter') == 'You'
            else:
                assert filtered_data.get('Looter') == 'Tester'
            if filtered_data.get('Platinum') is not None:
                assert filtered_data.get('Platinum') == '129'
            if filtered_data.get('Gold') is not None:
                assert filtered_data.get('Gold') == '2'
            if filtered_data.get('Silver') is not None:
                assert filtered_data.get('Silver') == '5'
            if filtered_data.get('Copper') is not None:
                assert filtered_data.get('Copper') == '1'

