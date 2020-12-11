from copy import deepcopy


with open('../input/day11.txt', 'r') as f:
    layout = tuple(tuple(x.strip('\n')) for x in f.readlines())


def apply_rules(layout):
    new_layout = list(list(x) for x in layout)
    for col in range(0, len(layout)):
        for row in range(0, len(layout[0])):
            pos = layout[col][row]
            if pos == '.':
                continue
            occupied_seats_adjacent = 0

            i = 1
            j = 1
            while True:
                if col - i < 0:
                    break
                elif row + j >= len(layout[0]):
                    break
                elif layout[col - i][row + j] == '#':
                    occupied_seats_adjacent += 1
                    break
                elif layout[col - i][row + j] == 'L':
                    break
                else:
                    i += 1
                    j += 1

            i = 1
            j = 1
            while True:
                if row + j >= len(layout[0]):
                    break
                elif layout[col][row + j] == '#':
                    occupied_seats_adjacent += 1
                    break
                elif layout[col][row + j] == 'L':
                    break
                else:
                    i += 1
                    j += 1

            i = 1
            j = 1
            while True:
                if col + j >= len(layout):
                    break
                elif row + j >= len(layout[0]):
                    break
                elif layout[col + i][row + j] == '#':
                    occupied_seats_adjacent += 1
                    break
                elif layout[col + i][row + j] == 'L':
                    break
                else:
                    i += 1
                    j += 1

            i = 1
            j = 1
            while True:
                if col - i < 0:
                    break
                elif layout[col - i][row] == '#':
                    occupied_seats_adjacent += 1
                    break
                elif layout[col - i][row] == 'L':
                    break
                else:
                    i += 1
                    j += 1

            i = 1
            j = 1
            while True:
                if col + i >= len(layout):
                    break
                elif layout[col + i][row] == '#':
                    occupied_seats_adjacent += 1
                    break
                elif layout[col + i][row] == 'L':
                    break
                else:
                    i += 1
                    j += 1

            i = 1
            j = 1
            while True:
                if col - i < 0:
                    break
                elif row - j < 0:
                    break
                elif layout[col - i][row - j] == '#':
                    occupied_seats_adjacent += 1
                    break
                elif layout[col - i][row - j] == 'L':
                    break
                else:
                    i += 1
                    j += 1

            i = 1
            j = 1
            while True:
                if row - j < 0:
                    break
                elif layout[col][row - j] == '#':
                    occupied_seats_adjacent += 1
                    break
                elif layout[col][row - j] == 'L':
                    break
                else:
                    i += 1
                    j += 1

            i = 1
            j = 1
            while True:
                if col + i >= len(layout):
                    break
                elif row - j < 0:
                    break
                elif layout[col + i][row - j] == '#':
                    occupied_seats_adjacent += 1
                    break
                elif layout[col + i][row - j] == 'L':
                    break
                else:
                    i += 1
                    j += 1

            if occupied_seats_adjacent == 0 and pos == 'L':
                new_layout[col][row] = '#'
            elif occupied_seats_adjacent >= 5 and pos == '#':
                new_layout[col][row] = 'L'

    return tuple(tuple(x) for x in new_layout)


def pretty_print_layout(layout):
    for i in layout:
        print(''.join(i))
    print('')


old_layout = layout
# pretty_print_layout(old_layout)
new_layout = apply_rules(layout)
# pretty_print_layout(new_layout)
i = 1
while old_layout != new_layout:
    old_layout = new_layout
    new_layout = apply_rules(old_layout)
    # pretty_print_layout(new_layout)
    i += 1

# print(i)
occupied_seats = 0
for i in new_layout:
    occupied_seats += i.count('#')
print(occupied_seats)
