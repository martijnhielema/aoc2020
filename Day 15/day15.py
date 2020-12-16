import re
from collections import defaultdict

with open("../input/day15_example.txt", 'r') as f:
    numbers = [int(x) for x in f.readline().split(',')]

length = len(numbers)
numdict = defaultdict(list)
for i, val in enumerate(numbers):
    numdict[val].append(i)

last = 6
print(numdict)
for i in range(length, 2020):
    if last not in numdict.keys():
        last = 0
        numdict[0].append(i)
    else:
        last = numdict[last][-1] - numdict[last][-2]
        numdict[last].append(i)

print(last)
