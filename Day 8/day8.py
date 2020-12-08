
def acc(arg):
    global accumulator
    accumulator += arg
    return

with open('../input/day8.txt', 'r') as f:
    bootcode = [(op, int(val.strip('\n'))) for op, val in [x.split(' ') for x in f.readlines()]]


accumulator = 0
processed_instructions = []
i = 0
while True:
    if i in processed_instructions:
        print(accumulator)
        print(processed_instructions)
        exit(0)
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