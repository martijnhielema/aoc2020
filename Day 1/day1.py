import unittest


class TestExpenseReport(unittest.TestCase):
    def test_example1_2_numbers(self):
        self.assertEqual(expense_report_fixer_2_numbers([1721, 979, 366, 299, 675, 1456]), 514579)


def expense_report_fixer_2_numbers(entries: list) -> int:
    while len(entries) > 0:
        entry = entries.pop()
        for i in entries:
            if 2020 - entry == i:
                print(entry, i, entry * i)
                return entry * i


if __name__ == '__main__':
    with open('../input/day1.txt', 'r') as f:
        data = [int(i.strip()) for i in f.readlines()]
    print(expense_report_fixer_2_numbers(data))
