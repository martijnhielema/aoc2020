import re


class LuggageRule:
    def __init__(self, raw: str):
        subject, contents = raw.split(' bags contain ')
        self.raw_subject = subject.strip(' ')
        number_match = re.compile('([0-9]+) ([a-z ]+)')
        self.content_bags = []
        for content in contents.split(', '):
            if content == 'no other bags.':
                continue
            else:
                content = content.strip('.').strip('bags')
                m =number_match.match(content)
                number, raw_bag = m.group(1, 2)
                self.content_bags.append({'number': number, 'raw_type': raw_bag.strip(' ')})


def search_rules(rules: list, searchstring: str, match_list: list = []) -> list:
    for luggage_rule in rules:
        for i in luggage_rule.content_bags:
            if i['raw_type'] == searchstring:
                if luggage_rule.raw_subject not in match_list:
                    match_list.append(luggage_rule.raw_subject)
                    search_rules(rules, luggage_rule.raw_subject, match_list)
    return match_list


def count_contents(rules: list, searchstring: str, parent_number: int = 1, total: int = 0):
    for luggage_rule in rules:
        if luggage_rule.raw_subject == searchstring:
            for i in luggage_rule.content_bags:
                    # print(luggage_rule.raw_subject)
                    # print(i)
                    print(f'parent_bags: {parent_number}')
                    print(f'Subtotal: {total}')
                    subtotal = parent_number * int(i['number'])
                    total += count_contents(rules, i['raw_type'], int(i['number']), subtotal)
    return total


with open('../input/day7_example.txt', 'r') as f:
    raw_rules = [x.strip() for x in f.readlines()]

luggage_rules = []
for raw in raw_rules:
    luggage_rules.append(LuggageRule(raw))

li = search_rules(luggage_rules, 'shiny gold')

cnt = count_contents(luggage_rules, 'shiny gold')
print(cnt)
