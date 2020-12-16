from collections import defaultdict
from copy import deepcopy
from itertools import chain


with open('../input/day16.txt', 'r') as f:
    rules, ticket, read_tickets = f.read().split('\n\n')


def process_rules(rules:str) -> defaultdict[list]:
    rules = rules.split('\n')
    ruledict = defaultdict(list)
    for rule in rules:
        rulename, ruleval = rule.split(': ')
        for subrule in ruleval.split(' or '):
            val_from, val_to = subrule.split('-')
            ruledict[rulename].extend([x for x in range(int(val_from), int(val_to) + 1)])

    return ruledict


def process_ticket(ticket: str) -> list:
    return [int(x) for x in ticket.split(',')]


def validate_ticket_part_1(ticket: list, rules: dict):
    tse_rate = 0
    for field in ticket:
        in_rule = False
        for rule in rules:
            if field in rules[rule]:
                in_rule = True
                continue
        if not in_rule:
            tse_rate += field

    return tse_rate


def process_fields(tickets: list, rules: dict) -> defaultdict[list]:
    length = len(tickets[0])
    candidates = defaultdict(list)
    for i in range(length):
        field_values = []
        for j in tickets:
            field_values.append(j[i])

        for rule in rules.keys():
            if all(x in rules[rule] for x in field_values):
                candidates[i].append(rule)

    return candidates


def eliminate_candidates(candidates: dict[list], fixed_fields: dict[str]) -> dict[list]:
    all_vals = list(chain.from_iterable(candidates.values()))
    all_uniques = set(all_vals)
    for val in all_uniques:
        if all_vals.count(val) == 1:
            key = [key for (key, value) in candidates.items() if val in value]
            if len(key) == 1:
                fixed_fields[key[0]] = val
                candidates[key[0]] = [val]

    pinned = []
    for pos, val in deepcopy(candidates).items():
        if len(val) == 1:
            fixed_fields[pos] = val[0]
            pinned.append(val[0])
            # del candidates[pos]

    for j in candidates.keys():
        for p in pinned:
            try:
                if len(candidates[j]) > 1:
                    candidates[j].remove(p)
            except ValueError:
                pass

    return candidates, fixed_fields


rules = process_rules(rules)
my_ticket = process_ticket(ticket.split('\n')[1])

read_list = []
for read_ticket in read_tickets.split('\n')[1:]:
    read_list.append(process_ticket(read_ticket))

tse_rate = 0
invalid_tickets = []
for i, t in enumerate(read_list):
    ticket_rr = validate_ticket_part_1(t, rules)
    if ticket_rr > 0:
        invalid_tickets.append(i)
        tse_rate += validate_ticket_part_1(t, rules)

print(f'Part one TSE rate: {tse_rate}')

#######################################################
valid_tickets = []
for i in range(0, len(read_list)):
    if i not in invalid_tickets:
        valid_tickets.append(read_list[i])

candidates = process_fields(valid_tickets, rules)

allocated = list(chain.from_iterable(candidates.values()))
all_rules = rules.keys()
print([i for i in all_rules if i not in allocated])




orig_candidates = deepcopy(candidates)
i = 0
fixed_fields = {}
while max((len(x) for x in candidates.values())) > 1 and i < 100000:
    old_candidates = deepcopy(candidates)
    candidates, fixed_fields = eliminate_candidates(deepcopy(old_candidates), fixed_fields)
    if old_candidates == candidates:
        break
    i += 1

allocated = list(chain.from_iterable(candidates.values()))
all_rules = rules.keys()
print(i)
print([i for i in all_rules if i not in allocated])
print(candidates)
departure_keys = [key for (key, value) in fixed_fields.items() if value.startswith('departure')]
print(departure_keys)
# for i in departure_keys:
#     orig_candidates[i] = candidates[i]
#
# for i in [x for x in range(len(my_ticket)) if x not in candidates.keys()]:
#     orig_candidates[i] = list(rules.keys())
#
# i = 0
# fixed_fields = {}
# candidates = deepcopy(orig_candidates)
#
# while max((len(x) for x in candidates.values())) > 1 and i < 100000:
#     old_candidates = deepcopy(candidates)
#     candidates, fixed_fields = eliminate_candidates(deepcopy(old_candidates), fixed_fields)
#     if old_candidates == candidates:
#         break
#     i += 1
#
#
# allocated = list(chain.from_iterable(candidates.values()))
# all_rules = rules.keys()
# print(i)
# print([i for i in all_rules if i not in allocated])
# print(candidates)
# departure_keys = [key for (key, value) in fixed_fields.items() if value.startswith('departure')]
# print(departure_keys)

print(fixed_fields)
solved = [7, 13, 16, 17, 19]
answer = 1
for i in solved:
    answer *= int(my_ticket[i])

print(answer * int(my_ticket[4]))
print(answer * int(my_ticket[9]))
print(answer * int(my_ticket[10]))

