from src.events.eventfilter import EventFilter
from src.filters.benefit.aafilter import AAFilter
from src.filters.benefit.expfilter import ExpFilter
from src.filters.benefit.skillsfilter import SkillsFilter
from src.filters.benefit.achievementfilter import AchievementFilter


class BenefitEvent(EventFilter):
    def __init__(self):
        event_filters = [
            AAFilter(),
            ExpFilter(),
            AchievementFilter(),
            SkillsFilter()
        ]
        super().__init__(event_filters)
