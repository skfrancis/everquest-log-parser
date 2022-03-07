from src.events.eventfilter import EventFilter
from src.filters.general.chatfilter import ChatFilter
from src.filters.general.dicefilter import DiceFilter
from src.filters.general.locationfilter import LocationFilter
from src.filters.general.partyfilter import PartyFilter
from src.filters.general.systemmessagefilter import SystemMessageFilter
from src.filters.general.tradesfilter import TradesFilter


class GeneralEvent(EventFilter):
    def __init__(self):
        event_filters = [
            ChatFilter(),
            DiceFilter(),
            LocationFilter(),
            PartyFilter(),
            SystemMessageFilter(),
            TradesFilter()
        ]
        super().__init__(event_filters)
