from copy import deepcopy


def acc(arg):
    global accumulator
    accumulator += arg
    return


with open('../input/day8.txt', 'r') as f:
    bootcode = [[op, int(val.strip('\n'))] for op, val in [x.split(' ') for x in f.readlines()]]

original_bootcode = deepcopy(bootcode)

for pos, op in enumerate(bootcode):
    bootcode = deepcopy(original_bootcode)
    if op[0] == 'jmp':
        bootcode[pos][0] = 'nop'
    elif op[0] == 'nop':
        bootcode[pos][0] = 'jmp'
    else:
        continue

    accumulator = 0
    processed_instructions = []
    i = 0
    while True:
        try:
            if i == 634:
                print('woohoo')
                print(accumulator)
                exit(0)
            if i in processed_instructions:
                break
            processed_instructions.append(i)
            if bootcode[i][0] == 'nop':
                i += 1
                continue
            elif bootcode[i][0] == 'acc':
                acc(bootcode[i][1])
                i += 1
                continue
            elif bootcode[i][0] == 'jmp':
                i += bootcode[i][1]
        except IndexError:
            print('indexerror')
