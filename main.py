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
from util.logloader import LogLoader
from util.logparser import LogParser
from util.linefilter import LineFilter
from docopt import docopt


def testing_loader(log_file):
    if log_file and log_file.is_file():
        loader = LogLoader(log_file)
        line_count = loader.get_line_count()
        tic = time.perf_counter()
        file_data = loader.parse_log_file()
        toc = time.perf_counter()
        process_time = toc - tic
        logger.debug(f"Processed the log in {process_time:0.4f} seconds")
        logger.debug(f"Processed {line_count / process_time} lines per second")
        filterer = LineFilter()
        for line in file_data:
            event = filterer.filter_line(line)
            print(event)


def testing_parser(log_file):
    if log_file and log_file.is_file():
        parser = LogParser(log_file)
        try:
            for parsed_line in parser.run():
                continue
        except KeyboardInterrupt:
            parser.close()
        finally:
            sys.exit()


def main():
    log_file = Path(arguments.get('--log'))
    if arguments.get('--debug'):
        logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug(f"Log File: {log_file.name}")
    # testing_loader(log_file)
    testing_parser(log_file)


if __name__ == '__main__':
    version = '0.0.3'
    arguments = docopt(__doc__, help=True, options_first=True, version=version)
    main()
