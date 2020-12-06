with open('../input/day6.txt', 'r') as f:
    answers = [x.replace('\n', '') for x in f.read().split('\n\n')]

distinct = [*map(lambda x: len(set(x)), answers)]
print(f'Anyone answered sum: {sum(distinct)}')

