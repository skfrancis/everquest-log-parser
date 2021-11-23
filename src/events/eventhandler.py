class EventHandler:
    def __init__(self, event_filters):
        self.event_filters = event_filters

    def process_event_filter(self, log_line):
        for event_filter in self.event_filters:
            processed_data = event_filter.filter(log_line)
            if processed_data:
                return event_filter.name, event_filter.columns, processed_data


