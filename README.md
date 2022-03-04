[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/skfrancis/everquest-log-parser/blob/main/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/skfrancis/everquest-log-parser)](https://github.com/skfrancis/everquest-log-parser/graphs/commit-activity)
[![Pytest](https://github.com/skfrancis/everquest-log-parser/actions/workflows/pytests.yml/badge.svg)](https://github.com/skfrancis/everquest-log-parser/actions/workflows/pytests.yml)
# Everquest Log Parser 

### Planned Functionality
- Custom Alert Filters
- Fight Encounters
- Archiving Log Data

### Built Functionality
- Log File Handler
  - Live log file reading
  - Log file processor
- Text to Speech Utility
- Parse Filters:

| Benefit      | Fight    | General        | Loot  | Utility     |
|--------------|----------|----------------|-------|-------------|
| AAs          | Physical | Chats          | Coin  | Casting     |
| Skills       | Spells   | Randoms        | Items | Consider    |
| Experience   | Healing  | Location       | Rot   | Faction     |
| Achievements | Death    | Party          |       | Pet Leader  |
|              |          | System Message |       | Who Command |
|              |          | Tradeskills    |       | Zoning      |

### Working Functionality
- Parses Live log entry into a basic parse object 
  - {date, log text}
- Filters parse object through parse filters above to create event object 
  - {name, columns, filter object}
- Prints event object to standard output