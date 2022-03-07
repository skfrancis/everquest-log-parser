from src.events.eventfilter import EventFilter
from src.filters.fight.physicalfilter import PhysicalFilter
from src.filters.fight.spellfilter import SpellFilter
from src.filters.fight.healingfilter import HealingFilter
from src.filters.fight.deathfilter import DeathFilter


class FightEvent(EventFilter):
    def __init__(self):
        event_filters = [
            PhysicalFilter(),
            SpellFilter(),
            HealingFilter(),
            DeathFilter()
        ]
        super().__init__(event_filters)
