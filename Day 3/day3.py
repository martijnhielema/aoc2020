with open('../input/day3.txt', 'r') as f:
    layout = [line.strip() for line in f.readlines()]

down_steps = 1
right_steps = 3
slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))
answer = 1
for right_steps, down_steps in slopes:
    trees = 0
    down = 0
    right = 0
    while down < len(layout):
        right %= len(layout[0])
        if layout[down][right] == '#':
            trees += 1

        down += down_steps
        right += right_steps

    print(f'Right: {right_steps}, Down: {down_steps}, Trees: {trees}')
    answer *= trees

print(f'Multiplication: {answer}')
