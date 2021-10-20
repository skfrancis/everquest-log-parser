from string import capwords
from filters.fightfilter import FightFilter


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
