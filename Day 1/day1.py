import unittest
import copy


class TestExpenseReport(unittest.TestCase):
    def test_example1_2_numbers(self):
        self.assertEqual(expense_report_fixer_2_numbers([1721, 979, 366, 299, 675, 1456]), 514579)

    def test_example1_3_numbers(self):
        self.assertEqual(expense_report_fixer_3_numbers([1721, 979, 366, 299, 675, 1456]), 241861950)


def expense_report_fixer_2_numbers(entries: list) -> int:
    for i in range(0, len(entries)):
        entry = entries[i]
        for j in range(i+1, len(entries)):
            entry2 = entries[j]
            if 2020 - entry == entry2:
                print(entry, entry2, entry * entry2)
                return entry * entry2


def expense_report_fixer_3_numbers(entries: list) -> int:
    for i in range(0, len(entries)):
        entry = entries[i]
        for j in range(i+1, len(entries)):
            entry2 = entries[j]
            for k in range(i+2, len(entries)):
                entry3 = entries[k]
                if 2020 - entry - entry2 == entry3:
                    print(entry, entry2, entry3, entry * entry2 * entry3)
                    return entry * entry2 * entry3


if __name__ == '__main__':
    with open('../input/day1.txt', 'r') as f:
        data = [int(i.strip()) for i in f.readlines()]
    print(expense_report_fixer_2_numbers(data))
    print(expense_report_fixer_3_numbers(data))
