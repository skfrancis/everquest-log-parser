from events.eventhandler import EventHandler
from filters.fight.physicalfilter import PhysicalFilter
from filters.fight.spellfilter import SpellFilter
from filters.fight.healingfilter import HealingFilter
from filters.fight.deathfilter import DeathFilter


class FightEvent(EventHandler):
    def __init__(self):
        event_filters = [
            PhysicalFilter(),
            SpellFilter(),
            HealingFilter(),
            DeathFilter()
        ]
        super().__init__(event_filters)
