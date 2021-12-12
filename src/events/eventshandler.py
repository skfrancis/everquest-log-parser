from events.lootevent import LootEvent
from events.fightevent import FightEvent
from events.benefitevent import BenefitEvent
from events.generalevent import GeneralEvent
from events.utilityevent import UtilityEvent


class EventsHandler:
    def __init__(self):
        self.event_list = [FightEvent(), BenefitEvent(), LootEvent(), GeneralEvent(), UtilityEvent()]

    def process_events(self, parsed_line):
        for event in self.event_list:
            result = event.process_event_filter(parsed_line)
            if result:
                return result
        return None
