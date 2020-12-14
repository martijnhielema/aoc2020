import re
from functools import reduce
from itertools import combinations
from math import pow

with open('../input/day14.txt', 'r') as f:
    program = [x.strip('\n') for x in f.readlines()]


def to_binstr(value: int) -> str:
    binstr = str(bin(value))[2:]
    return '0b' + binstr.zfill(36)


def mask(maskstr: str, binstr: str):
    binlist = list(binstr)

    for i, c in enumerate(maskstr):
        if c == '1':
            binlist[i + 2] = 1
        elif c == '0':
            binlist[i + 2] = 0

    return ''.join([str(x) for x in binlist])


def mask2(maskstr: str, binstr: str):
    binlist = list(binstr)
    for i, c in enumerate(maskstr):
        if c == '1':
            binlist[i + 2] = 1
        elif c == '0':
            pass
        elif c == 'X':
            binlist[i + 2] = 'X'

    return ''.join([str(x) for x in binlist])


def possible_addresses(address: str):
    adlist = list(address[2:])
    adlist.reverse()

    reverse_address = ''.join(adlist)

    xs = [m.start() for m in re.finditer('X', reverse_address)]
    int_add = tuple(int(pow(2, x)) for x in xs)
    possible_integers = list(int_add)
    for i in range(2, len(int_add) + 1):
        combs = list(combinations(int_add, i))
        comb_ints = [sum(x) for x in combs]
        possible_integers.extend(comb_ints)

    ints = set(possible_integers)
    zeroes_address = address.replace('X', '0')

    addresses = [int(zeroes_address, 2), ]
    addresses.extend([int(x) + int(zeroes_address, 2) for x in ints])
    return addresses


memory = {}
maskstr = ''
memory_regex = re.compile('mem\[([0-9]+)\] = ([0-9]+)')

for line in program:
    if line.startswith('mask'):
        maskstr = line.split(' = ')[1]
    else:
        m = re.match(memory_regex, line)
        mempos, value = m.group(1, 2)

        binstr = to_binstr(int(value))
        memory[mempos] = int(mask(maskstr, binstr), 2)

print('Part 1:')
print(reduce(lambda x, y: x+y, memory.values()))
memory = {}
maskstr = ''
for line in program:
    if line.startswith('mask'):
        maskstr = line.split(' = ')[1]
    else:
        m = re.match(memory_regex, line)
        mempos, value = m.group(1, 2)

        memstr = to_binstr(int(mempos))
        address = mask2(maskstr, memstr)
        addresses = possible_addresses(address)
        for mem in addresses:
            memory[mem] = int(value)

print('Part 2:')
print(reduce(lambda x, y: x+y, memory.values()))
