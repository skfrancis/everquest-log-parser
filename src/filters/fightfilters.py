from abc import ABC
from string import capwords
from basicfilter import BasicFilter


class FightFilter(BasicFilter, ABC):
    def __init__(self, regexes):
        self.name = 'Fight'
        self.columns = ['Timestamp', 'Source', 'Target', 'Amount', 'Ability', 'Mod', 'Type']
        super().__init__(self.name, self.columns, regexes)


class PhysicalFilter(FightFilter):
    def __init__(self):
        regexes = [
            r"^(?P<source>.+?) (?P<dmgtype>\bhit|shoot|kick|slash|crush|pierce|bash|slam|strike|punch|backstab|"
            r"bite|claw|smash|slice|gore|maul|rend|burn|sting|frenzy on|frenzies on\b)e?s? (?!by non-melee)"
            r"(?P<target>.+?) for (?P<amount>\d+) points? of damage\.(?: \((?P<mod>[\w\s]+)\))?",
            r"^(?P<target>.+?) is \w+ by (?P<source>.+?)'?s? \w+ for (?P<amount>\d+) points? of (?P<dmgtype>non-melee) "
            r"damage\.(?: \((?P<mod>[\w\s]+)\))?",
            r"^(?P<source>.+) \w+ to (?P<dmgtype>\w+)(?: on)? (?P<target>.+?), but .*?(?P<amount>\bmiss|parry|"
            r"parries|dodge|block|blocks with \w\w\w shield|INVULNERABLE|magical skin absorbs the blow)e?s?!"
            r"(?: \((?P<mod>[\w\s]+)\))?"
        ]
        super().__init__(regexes)

    def process_data(self, timestamp, result):
        miss_data = {'parries': 'parry', 'blocks with': 'block', 'magical skin absorbs': 'magical skin'}
        amount = result.group('amount')
        filter_type = 'physical hit' if amount.isnumeric() else 'physical miss'
        updated_amount = miss_data.get(amount) if amount in miss_data else amount
        mod = capwords(result.group('mod')) if result.group('mod') is not None else result.group('mod')
        data = {
            self.columns[0]: timestamp,
            self.columns[1]: capwords(result.group('source').replace('YOUR', 'You')),
            self.columns[2]: capwords(result.group('target')),
            self.columns[3]: capwords(updated_amount),
            self.columns[4]: capwords(result.group('dmgtype')),
            self.columns[5]: mod,
            self.columns[6]: filter_type
        }
        return data


class SpellFilter(FightFilter):
    def __init__(self):
        regexes = [
            r"^(?P<source>.+?) hit (?P<target>.+?) for (?P<amount>\d+) points? of .+? damage by (?P<spell>.+?)"
            r"\.(?: \((?P<mod>[\w\s]+)\))?$",
            r"^(?P<target>.+?) has taken (?P<amount>\d+) damage from (?P<source>you)r (?P<spell>.+?)\."
            r"(?: \((?P<mod>[\w\s]+)\))?",
            r"^(?P<target>.+?) ha(?:s|ve) taken (?P<amount>\d+) damage from (?P<spell>.+?) by (?P<source>.+?)\."
            r"(?: \((?P<mod>[\w\s]+)\))?",
            r"^(?P<target>.+) (?P<amount>resist)ed (?P<source>you)r (?P<spell>.+?)!(?: \((?P<mod>[\w\s]+)\))?",
            r"^(?P<target>You) (?P<amount>resist) (?P<source>.+?)'s (?P<spell>.+)!(?: \((?P<mod>[\w\s]+)\))?"
        ]
        super().__init__(regexes)

    def process_data(self, timestamp, result):
        filter_type = 'spell hit' if result.group('amount').isnumeric() else 'spell miss'
        mod = capwords(result.group('mod')) if result.group('mod') is not None else result.group('mod')
        data = {
            self.columns[0]: timestamp,
            self.columns[1]: capwords(result.group('source').replace('YOUR', 'You')),
            self.columns[2]: capwords(result.group('target')),
            self.columns[3]: capwords(result.group('amount')),
            self.columns[4]: result.group('spell'),
            self.columns[5]: mod,
            self.columns[6]: filter_type
        }
        return data


class HealingFilter(FightFilter):
    def __init__(self):
        regexes = [
            r"^(?P<source>.+?) healed (?P<target>.+?) over time for (?P<actual>\d+)(?: \((?P<max>\d+)\))? "
            r"hit points by (?P<spell>.+?)\.(?: \((?P<mod>.+?)\))?",
            r"^(?P<source>.+?) healed (?P<target>.+?) for (?P<actual>\d+)(?: \((?P<max>\d+)\))? "
            r"hit points(?: by (?P<spell>.+?))?\.(?: \((?P<mod>.+?)\))?"
        ]
        super().__init__(regexes)

    def process_data(self, timestamp, result):
        maximum = result.group('max') if result.group('max') is not None else result.group('actual')
        mod = capwords(result.group('mod')) if result.group('mod') is not None else result.group('mod')
        data = {
            self.columns[0]: timestamp,
            self.columns[1]: capwords(result.group('source').replace('YOUR', 'You')),
            self.columns[2]: capwords(result.group('target')),
            self.columns[3]: (result.group('actual'), maximum),
            self.columns[4]: result.group('spell'),
            self.columns[5]: mod,
            self.columns[6]: 'heal'
        }
        return data


class DeathFilter(FightFilter):
    def __init__(self):
        regexes = [
            r"^(?P<target>.+) (?:have|has) been slain by (?P<source>.+)!$",
            r"^(?P<source>You) have slain (?P<target>.+)!$",
            r"^(?P<source>(?P<target>.+)) dies?d?\.$"
        ]
        super().__init__(regexes)

    def process_data(self, timestamp, result):
        data = {
            self.columns[0]: timestamp,
            self.columns[1]: capwords(result.group('source')),
            self.columns[2]: capwords(result.group('target')),
            self.columns[3]: None,
            self.columns[4]: None,
            self.columns[5]: None,
            self.columns[6]: 'death'
        }
        return data


class BattleFilter:
    def __init__(self):
        self.name = 'Battle'
        self.filters = [
            PhysicalFilter(), SpellFilter(), HealingFilter(), DeathFilter()
        ]

    def filter(self, log_line):
        for battle_filter in self.filters:
            result = battle_filter.filter(log_line)
            if result:
                return result
        return None
