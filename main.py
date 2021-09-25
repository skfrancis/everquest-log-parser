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

from pathlib import Path
from util.lineparser import LineParser
from util.linefilter import LineFilter
from docopt import docopt


def main():
    log_file = Path(arguments.get('--log'))
    debug = arguments.get('--debug')
    print(debug)
    if log_file:
        parser = LineParser(debug=debug)
        filterer = LineFilter(debug=debug)
        with log_file.open('r', encoding="utf8") as data:
            lines = data.readlines()
            for line in lines:
                result = parser.parse_line(line)
                if result:
                    filtered = filterer.filter_line(result)
                    if filtered:
                        continue
                    else:
                        print(result)


if __name__ == '__main__':
    version = '0.0.1'
    arguments = docopt(__doc__, help=True, options_first=True, version=version)
    main()
