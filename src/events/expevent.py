from events.eventhandler import EventHandler
from filters.exp.aafilter import AAFilter
from filters.exp.expfilter import ExpFilter
from filters.exp.skillsfilter import SkillsFilter


class ExpEvent(EventHandler):
    def __init__(self):
        event_filters = [
            AAFilter(),
            ExpFilter(),
            SkillsFilter()
        ]
        super().__init__(event_filters)
