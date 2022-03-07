from src.events.eventfilter import EventFilter
from src.filters.loot.lootfilter import LootFilter
from src.filters.loot.coinfilter import CoinFilter
from src.filters.loot.rotfilter import RotFilter


class LootEvent(EventFilter):
    def __init__(self):
        event_filters = [
            LootFilter(),
            RotFilter(),
            CoinFilter()
        ]
        super().__init__(event_filters)
