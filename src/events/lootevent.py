from events.eventhandler import EventHandler
from filters.loot.lootfilter import LootFilter
from filters.loot.coinfilter import CoinFilter
from filters.loot.rotfilter import RotFilter


class LootEvent(EventHandler):
    def __init__(self):
        event_filters = [
            LootFilter(),
            RotFilter(),
            CoinFilter()
        ]
        super().__init__(event_filters)
