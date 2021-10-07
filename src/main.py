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
from src.util.logparser import LogParser
from src.util.linefilter import LineFilter
from docopt import docopt


def testing_parser(log_file):
    if log_file and log_file.is_file():
        parser = LogParser(log_file)
        event_filter = LineFilter()
        try:
            for parsed_line in parser.run():
                if parsed_line:
                    print(parsed_line)
        except KeyboardInterrupt:
            parser.run().close()
        finally:
            sys.exit()


def main():
    log_file = Path(arguments.get('--log'))
    if arguments.get('--debug'):
        logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug(f"Log File: {log_file.name}")
    testing_parser(log_file)


if __name__ == '__main__':
    version = '0.0.4 alpha'
    arguments = docopt(__doc__, help=True, options_first=True, version=version)
    main()
