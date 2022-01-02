"""Everquest Log Parser

Usage:
  main.py [-hl Log_file] [--debug]
  main.py --version

Options:
  -h --help          Show this screen
  -l --log log_file  Load specified log file
  --debug            Debug Mode
  --version          Show Version

"""


import sys
import time
import logging
from pathlib import Path
from docopt import docopt
from db.dbhandler import DBHandler
from util.confighandler import ConfigHandler
from events.eventshandler import EventsHandler
from util.logfilehandler import LogFileHandler


def start_parser(log_handler, db_handler):
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
    app_path = Path.cwd()
    config = ConfigHandler(app_path)
    arguments = docopt(__doc__, help=True, options_first=True, version=config.version)
    if arguments.get('--debug'):
        logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    config.log_file = Path(arguments.get('--log'))
    logger.debug(f"Log File: {config.log_file.name}")
    log_handler = LogFileHandler(config)
    if log_handler.character_info:
        config.log_table_config(log_handler.character_info)
    else:
        sys.exit(f"Log File: {config.log_file} is Invalid or Does Not Exist")
    print(f"Everquest Log Parser ({config.version}): {config.character_info['character']} - "
          f"{config.character_info['server']}")
    db_handler = DBHandler(config)
    start_parser(log_handler, db_handler)


if __name__ == '__main__':
    main()
