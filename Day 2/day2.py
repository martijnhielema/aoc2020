import unittest


class PolicyAndPassword:
    def __init__(self, line: str):
        self.min_occurs, self.max_occurs = [int(val) for val in line.split(' ')[0].split('-')]
        self.character = str(line.split(' ')[1][0])
        self.password = str(line.split(':')[1].strip())

    @property
    def occurences(self) -> int:
        return self.password.count(self.character)

    def is_valid(self) -> bool:
        valid = False
        if self.min_occurs <= self.occurences <= self.max_occurs:
            valid = True

        return valid

    def is_valid_new_interpretation(self) -> bool:
        valid = False
        first_match = self.password[self.min_occurs - 1] == self.character
        second_match = self.password[self.max_occurs - 1] == self.character

        if first_match or second_match:
            if first_match and second_match:
                pass
            else:
                valid = True

        return valid


class Day2TestsPolicyAndPassword(unittest.TestCase):
    def test_validity_1(self):
        self.assertEqual(True, PolicyAndPassword('1-3 a: abcde').is_valid())

    def test_validity_2(self):
        self.assertEqual(False, PolicyAndPassword('1-3 b: cdefg').is_valid())

    def test_validity_3(self):
        self.assertEqual(True, PolicyAndPassword('2-9 c: ccccccccc').is_valid())


class Day2TestsPolicyAndPassword2(unittest.TestCase):
    def test_validity_1(self):
        self.assertEqual(True, PolicyAndPassword('1-3 a: abcde').is_valid_new_interpretation())

    def test_validity_2(self):
        self.assertEqual(False, PolicyAndPassword('1-3 b: cdefg').is_valid_new_interpretation())

    def test_validity_3(self):
        self.assertEqual(False, PolicyAndPassword('2-9 c: ccccccccc').is_valid_new_interpretation())


def policy_checker(inputs: list) -> int:
    valid_passwords = 0
    for line in inputs:
        if PolicyAndPassword(line).is_valid():
            valid_passwords += 1

    return valid_passwords


def policy_checker_new_interpretation(inputs: list) -> int:
    valid_passwords = 0
    for line in inputs:
        if PolicyAndPassword(line).is_valid_new_interpretation():
            valid_passwords += 1

    return valid_passwords


if __name__ == '__main__':
    with open('../input/day2.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    print('Part 1: ', policy_checker(lines))
    print('Part 2: ', policy_checker_new_interpretation(lines))
