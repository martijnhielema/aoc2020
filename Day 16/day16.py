from collections import defaultdict


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


rules = process_rules(rules)
my_ticket = process_ticket(ticket.split('\n')[1])

read_list = []
for read_ticket in read_tickets.split('\n')[1:]:
    read_list.append(process_ticket(read_ticket))

tse_rate = 0
for t in read_list:
    tse_rate += validate_ticket_part_1(t, rules)
    

print(tse_rate)