from events.eventfilter import EventFilter
from filters.utility.castingfilter import CastingFilter
from filters.utility.considerfilter import ConsiderFilter
from filters.utility.factionfilter import FactionFilter
from filters.utility.petleaderfilter import PetLeaderFilter
from filters.utility.whofilter import WhoFilter
from filters.utility.zonefilter import ZoneFilter


class UtilityEvent(EventFilter):
    def __init__(self):
        event_filters = [
            CastingFilter(),
            ConsiderFilter(),
            FactionFilter(),
            PetLeaderFilter(),
            WhoFilter(),
            ZoneFilter()
        ]
        super().__init__(event_filters)
