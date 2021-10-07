from src.filters.fightfilters import BattleFilter
from src.filters.lootfilters import LootFilter, LootCoinFilter, LootRotFilter
from src.filters.expfilters import ExpFilter, ExpAAFilter, SkillUpFilter
from src.filters.utilityfilters import CastingFilter, ConsiderFilter, FactionFilter, PetLeaderFilter, WhoFilter, ZoneFilter
from src.filters.generalfilters import ChatFilter, DiceFilter, LocationFilter
from src.filters.generalfilters import PartyFilter, TradesFilter, SystemMessageFilter


class LineFilter:
    def __init__(self):
        self.filters = [
            BattleFilter(), PetLeaderFilter(), CastingFilter(),
            LootFilter(), LootCoinFilter(), LootRotFilter(),
            ExpFilter(), ExpAAFilter(), SkillUpFilter(),
            FactionFilter(), ConsiderFilter(), PartyFilter(),
            WhoFilter(), ZoneFilter(), ChatFilter(),
            LocationFilter(), TradesFilter(), SystemMessageFilter(),
            DiceFilter()
        ]

    def filter_line(self, parsed_line):
        for line_filter in self.filters:
            event = line_filter.filter(parsed_line)
            if event:
                return event
        return None

