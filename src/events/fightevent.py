from events.eventfilter import EventFilter
from filters.fight.physicalfilter import PhysicalFilter
from filters.fight.spellfilter import SpellFilter
from filters.fight.healingfilter import HealingFilter
from filters.fight.deathfilter import DeathFilter


class FightEvent(EventFilter):
    def __init__(self):
        event_filters = [
            PhysicalFilter(),
            SpellFilter(),
            HealingFilter(),
            DeathFilter()
        ]
        super().__init__(event_filters)
