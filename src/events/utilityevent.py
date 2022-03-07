from src.events.eventfilter import EventFilter
from src.filters.utility.castingfilter import CastingFilter
from src.filters.utility.considerfilter import ConsiderFilter
from src.filters.utility.factionfilter import FactionFilter
from src.filters.utility.petleaderfilter import PetLeaderFilter
from src.filters.utility.whofilter import WhoFilter
from src.filters.utility.zonefilter import ZoneFilter


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
