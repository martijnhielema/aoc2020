from copy import deepcopy


with open('../input/day11.txt.txt', 'r') as f:
    layout = tuple(tuple(x.strip('\n')) for x in f.readlines())


def apply_rules(layout):
    new_layout = list(list(x) for x in layout)
    for col in range(0, len(layout)):
        for row in range(0, len(layout[0])):
            pos = layout[col][row]
            if pos == '.':
                continue
            occupied_seats_adjacent = 0
            try:
                if col - 1 < 0:
                    pass
                elif row + 1 >= len(layout[0]):
                    pass
                elif layout[col - 1][row + 1] == '#':
                    occupied_seats_adjacent += 1
            except IndexError:
                pass
            try:
                if row + 1 >= len(layout[0]):
                    pass
                elif layout[col][row + 1] == '#':
                    occupied_seats_adjacent += 1
            except IndexError:
                pass
            try:
                if col + 1 >= len(layout):
                    pass
                elif row + 1 >= len(layout[0]):
                    pass
                elif layout[col + 1][row + 1] == '#':
                    occupied_seats_adjacent += 1
            except IndexError:
                pass
            try:
                if col - 1 < 0:
                    pass
                elif layout[col - 1][row] == '#':
                    occupied_seats_adjacent += 1
            except IndexError:
                pass
            try:
                if col + 1 >= len(layout):
                    pass
                elif layout[col + 1][row] == '#':
                    occupied_seats_adjacent += 1
            except IndexError:
                pass
            try:
                if col - 1 < 0:
                    pass
                elif row - 1 < 0:
                    pass
                elif layout[col - 1][row - 1] == '#':
                    occupied_seats_adjacent += 1
            except IndexError:
                pass
            try:
                if row - 1 < 0:
                    pass
                elif layout[col][row - 1] == '#':
                    occupied_seats_adjacent += 1
            except IndexError:
                pass
            try:
                if col + 1 >= len(layout):
                    pass
                elif row - 1 < 0:
                    pass
                elif layout[col + 1][row - 1] == '#':
                    occupied_seats_adjacent += 1
            except IndexError:
                pass

            if occupied_seats_adjacent == 0 and pos == 'L':
                new_layout[col][row] = '#'
            elif occupied_seats_adjacent >= 4 and pos == '#':
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

occupied_seats = 0
for i in new_layout:
    occupied_seats += i.count('#')
print(occupied_seats)
