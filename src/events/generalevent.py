from events.eventfilter import EventFilter
from filters.general.chatfilter import ChatFilter
from filters.general.dicefilter import DiceFilter
from filters.general.locationfilter import LocationFilter
from filters.general.partyfilter import PartyFilter
from filters.general.systemmessagefilter import SystemMessageFilter
from filters.general.tradesfilter import TradesFilter


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
