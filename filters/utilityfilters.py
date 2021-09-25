from filters.basicfilter import BasicFilter


class CastingFilter(BasicFilter):
    def __init__(self, debug=False):
        name = 'Casting'
        columns = ['Date', 'Time', 'Source', 'Spell']
        regexes = [
            r"^(.+?) begins? (?:casting|singing) (.+)\.$",
            r"^(.+?) activates? (.+)\.$"
        ]
        super().__init__(name, columns, regexes, debug)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(2)
        }
        if self.debug:
            data['debug'] = result.string
        return data


class ConsiderFilter(BasicFilter):
    def __init__(self, debug=False):
        name = 'Consider'
        columns = ['Date', 'Time', 'Target', 'Level', 'Consider', 'Difficulty', 'Rare']
        regexes = [
            r"(.+) (-.+)? ((?:scowls|glares|glowers|regards|looks|judges|kindly) .+?) -- (.+) \(Lvl: (\d+)\)$",
            r"(.+)( -.+)? ((?:scowls|glares|glowers|regards|looks|judges|kindly) .+?) -- (.+) \(Lvl: (\d+)\)$"
        ]
        super().__init__(name, columns, regexes, debug)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(5),
            self.columns[4]: result.group(3),
            self.columns[5]: result.group(4),
            self.columns[6]: bool(result.group(2))
        }
        if self.debug:
            data['debug'] = result.string
        return data


class FactionFilter(BasicFilter):
    def __init__(self, debug=False):
        name = 'Faction'
        columns = ['Date', 'Time', 'Faction', 'Amount']
        regexes = [
            r"^Your faction standing with ([^.]+) has been adjusted by (-?\d+)\.$"
        ]
        super().__init__(name, columns, regexes, debug)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1),
            self.columns[3]: result.group(2)
        }
        if self.debug:
            data['debug'] = result.string
        return data


class PetLeaderFilter(BasicFilter):
    def __init__(self, debug=False):
        name = 'Pet Leader'
        columns = ['Date', 'Time', 'Leader', 'Pet']
        regexes = [
            r"(?P<pet>^[GJKLVXZ]([aeio][bknrs]){0,2}(ab|er|n|tik)) says, 'My leader is (?P<leader>\w+)\.'$"
        ]
        super().__init__(name, columns, regexes, debug)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group('leader'),
            self.columns[3]: result.group('pet')
        }
        if self.debug:
            data['debug'] = result.string
        return data


class WhoFilter(BasicFilter):
    def __init__(self, debug=False):
        name = 'Who'
        columns = ['Date', 'Time', 'Name', 'Class', 'Level']
        regexes = [
            r"^[A-Z\s]*\[(?:(ANONYMOUS)|(?P<lvl>\d+) (?P<class>[\w\s]+)|(?P<lvl>\d+)"
            r" .+? \((?P<class>[\w\s]+)\))\](?:\s+(?P<name>\w+))"
        ]
        super().__init__(name, columns, regexes, debug)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group('name'),
            self.columns[3]: result.group('class'),
            self.columns[4]: result.group('lvl')
        }
        if self.debug:
            data['debug'] = result.string
        return data


class ZoneFilter(BasicFilter):
    def __init__(self, debug=False):
        name = 'Zoning'
        columns = ['Date', 'Time', 'Zone']
        regexes = [
            r"^You have entered (.+)\.$"
        ]
        super().__init__(name, columns, regexes, debug)
        self.non_zones = [
            'an area where levitation effects do not function',
            'an Arena (PvP) area',
            'an area where Bind Affinity is allowed',
            'the Drunken Monkey stance adequately'
        ]

    def process_data(self, timestamp, result):
        for non_zone in self.non_zones:
            if non_zone in result.group(1):
                return None
        data = {
            self.columns[0]: timestamp.strftime('%x'),
            self.columns[1]: timestamp.strftime('%X'),
            self.columns[2]: result.group(1)
        }
        if self.debug:
            data['debug'] = result.string
        return data
