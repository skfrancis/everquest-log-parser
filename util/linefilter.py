from filters.fightfilters import BattleFilter
from filters.lootfilters import LootFilter, LootCoinFilter, LootRotFilter
from filters.expfilters import ExpFilter, ExpAAFilter, SkillUpFilter
from filters.utilityfilters import CastingFilter, ConsiderFilter, FactionFilter, PetLeaderFilter, WhoFilter, ZoneFilter
from filters.generalfilters import ChatFilter, DiceFilter, LocationFilter
from filters.generalfilters import PartyFilter, TradesFilter, SystemMessageFilter


class LineFilter:
    def __init__(self, debug=False):
        self.debug = debug
        self.filters = [
            BattleFilter(self.debug), PetLeaderFilter(self.debug), CastingFilter(self.debug),
            LootFilter(self.debug), LootCoinFilter(self.debug), LootRotFilter(self.debug),
            ExpFilter(self.debug), ExpAAFilter(self.debug), SkillUpFilter(self.debug),
            FactionFilter(self.debug), ConsiderFilter(self.debug), PartyFilter(self.debug),
            WhoFilter(self.debug), ZoneFilter(self.debug), ChatFilter(self.debug),
            LocationFilter(self.debug), TradesFilter(self.debug), SystemMessageFilter(self.debug),
            DiceFilter(self.debug)
        ]

    def filter_line(self, parsed_line):
        for line_filter in self.filters:
            event = line_filter.filter(parsed_line)
            if event:
                return event
        return None

