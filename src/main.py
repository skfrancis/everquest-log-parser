"""Everquest Log Parser

Usage:
  main.py [-hl Log_file] [--debug]
  main.py --version

Options:
  -h --help          Show this screen
  -l --log Log_file  Load specific log file
  --debug            Debug Mode
  --version          Show Version

"""

import logging
import sys
import time
from pathlib import Path
from util.logfilehandler import LogFileHandler
from docopt import docopt


def start_parser(log_handler):
    try:
        for parsed_line in log_handler.run_parser():
            if parsed_line:
                print(parsed_line)
    except KeyboardInterrupt:
        log_handler.run_parser().close()
    finally:
        sys.exit()


def main():
    version = '0.0.5 alpha'
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
