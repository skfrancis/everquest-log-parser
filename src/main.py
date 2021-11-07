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
from events.expevent import ExpEvent
from events.lootevent import LootEvent
from events.fightevent import FightEvent
from events.generalevent import GeneralEvent
from events.utilityevent import UtilityEvent
from util.logfilehandler import LogFileHandler


def start_parser(log_handler):
    try:
        for parsed_line in log_handler.run_parser():
            if parsed_line:
                result = event_filter(parsed_line)
                if result:
                    print(result)
    except KeyboardInterrupt:
        log_handler.run_parser().close()
    finally:
        sys.exit()


def event_filter(parsed_line):
    event_list = [FightEvent(), ExpEvent(), LootEvent(), GeneralEvent(), UtilityEvent()]
    for event in event_list:
        result = event.process_event_filter(parsed_line)
        if result:
            return result
    return None


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
