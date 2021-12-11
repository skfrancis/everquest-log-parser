"""Everquest Log Parser

Usage:
  main.py [-hl Log_file] [--debug]
  main.py --version

Options:
  -h --help          Show this screen
  -l --log log_file  Load specific log file
  --debug            Debug Mode
  --version          Show Version

"""


import sys
import time
import logging
from pathlib import Path
from docopt import docopt
from events.eventshandler import EventsHandler
from util.logfilehandler import LogFileHandler


def start_parser(log_handler):
    events_handler = EventsHandler()
    try:
        for parsed_line in log_handler.run_parser():
            if parsed_line:
                result = events_handler.process_events(parsed_line)
                if result:
                    print(result)
    except KeyboardInterrupt:
        log_handler.run_parser().close()
    finally:
        sys.exit()


def main():
    version = '0.0.6 alpha'
    arguments = docopt(__doc__, help=True, options_first=True, version=version)
    if arguments.get('--debug'):
        logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    log_file = Path(arguments.get('--log'))
    log_handler = LogFileHandler(log_file)
    player_data = log_handler.parse_file_name()
    print(f"Everquest Log Parser ({version}) - {player_data['character']} : {player_data['server']}")
    logger.debug(f"Log File: {log_file.name}")
    start_parser(log_handler)


if __name__ == '__main__':
    main()
