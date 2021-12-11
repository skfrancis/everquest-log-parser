from events.eventfilter import EventFilter
from filters.benefit.aafilter import AAFilter
from filters.benefit.expfilter import ExpFilter
from filters.benefit.skillsfilter import SkillsFilter
from filters.benefit.achievementfilter import AchievementFilter


class BenefitEvent(EventFilter):
    def __init__(self):
        event_filters = [
            AAFilter(),
            ExpFilter(),
            AchievementFilter(),
            SkillsFilter()
        ]
        super().__init__(event_filters)
