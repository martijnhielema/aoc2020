with open('../input/day6.txt', 'r') as f:
    answers = [x.split('\n') for x in f.read().split('\n\n')]
    answers1 = [''.join(x) for x in answers]

distinct = [*map(lambda x: len(set(x)), answers1)]
print(f'Anyone answered sum: {sum(distinct)}')

total = 0
for group in answers:
    group_answers = set(''.join(group))

    all_answered = 0
    for item in group_answers:
        if all(item in person for person in group):
            all_answered += 1

    total += all_answered

print(f'Everyone answered sum: {total}')
