import unittest
import re


class TestPassportParser(unittest.TestCase):
    def test_example(self):
        self.assertEqual(4, len(process_input('../input/day4_example.txt')))


class TestPassportProcessor(unittest.TestCase):
    def test_example_1(self):
        passport = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm"""
        self.assertEqual(8, len(process_passport(passport)))


class TestPassportValidator(unittest.TestCase):
    def test_example_1(self):
        passport = process_passport("""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm""")
        self.assertEqual(True, test_passport_validity(passport))

    def test_example_2(self):
        passport = process_passport("""iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929""")
        self.assertEqual(False, test_passport_validity(passport))


def process_input(filename: str) -> list:
    with open(filename, 'r') as f:
        contents = f.read()
    return contents.split('\n\n')


def process_passport(input: str):
    input = input.replace('\n', ' ')
    items = input.split(' ')
    passport = {}
    for item in items:
        property, value = item.split(':')
        passport[property] = value

    return passport


def hcl(hcl: str) -> bool:
    pattern_hcl = re.compile('^#[a-f0-9]{6}$')
    return pattern_hcl.match(hcl) is not None


def hgt(hgt: str) -> bool:
    pattern_hgt = re.compile('^([0-9]{2,3})(in|cm)$')
    m = pattern_hgt.match(hgt)
    if m is None:
        return False

    val, unit = m.group(1, 2)
    if unit == 'in':
        if not (59 <= int(val) <= 76):
            return False
    elif unit == 'cm':
        if not (150 <= int(val) <= 193):
            return False

    return True


def test_passport_validity(passport: dict):
    properties = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid = all(prop in passport.keys() for prop in properties)
    if valid:
        if not (1920 <= int(passport['byr']) <= 2002):
            # print(f"{int(passport['byr'])} is an invalid birth year")
            return False
        elif not (2010 <= int(passport['iyr']) <= 2020):
            # print(f"{int(passport['iyr'])} is an invalid issue year")
            return False
        elif not (2020 <= int(passport['eyr']) <= 2030):
            # print(f"{int(passport['eyr'])} is an invalid expiration year")
            return False
        elif passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False

        valid = hcl(passport['hcl'])
        if not valid:
            return False
        valid = hgt(passport['hgt'])
        if not valid:
            return False

        pattern_pid = re.compile('^[0-9]{9}$')
        if pattern_pid.match(passport['pid']) is None:
            return False
    return valid


def process_all_passports(inputfile):
    raw = process_input(inputfile)
    passports = []
    for raw_pass in raw:
        passports.append(process_passport(raw_pass))

    print(len(passports))
    valid_passports = 0
    valids = []
    for passport in passports:
        if test_passport_validity(passport):
            valids.append(passport)
            valid_passports += 1
    return valid_passports, valids


if __name__ == '__main__':
    num, vals = process_all_passports('../input/day4.txt')
    props = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    print(', '.join(props))
    for i in vals:
        items = []
        for j in props:
            items.append(i[j])
        print(', '.join(items))

    print(num)
