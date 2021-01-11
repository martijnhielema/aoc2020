import pprint
from collections import defaultdict
from copy import deepcopy
from itertools import chain
from functools import reduce


def count_neighbours(cube, x, y, z) -> int:
    neighbours = 0
    for plane in (z-1, z, z+1):
        for col in (y-1, y, y+1):
            for row in (x-1, x, x+1):
                if x == row and y == col and z == plane:
                    # skip own cell
                    continue
                else:
                    neighbours += cube[z][y][x]
    return neighbours


def extend_cube(cube):
    max_z = max(cube.keys())
    for z in range(- abs(max_z + 1), max_z + 1 + 1):
        max_y = max(cube[max_z].keys())
        for y in range(- abs(max_y + 1), max_y + 1 + 1):
            max_x = max(cube[max_z][max_y].keys())
            for x in range(- abs(max_x + 1), max_x + 1 + 1):
                print(z,y,x)
                print(cube[z][y][x])
                if cube[z][y][x] is None:
                    cube[z][y][x] = 0


def update_cube(old_cube):
    update_cube = deepcopy(old_cube)
    z_keys = list(update_cube.keys())
    z_keys.append(min(z_keys) - 1)
    z_keys.append(max(z_keys) + 1)
    for z in z_keys:
        y_keys = list(update_cube[z].keys())
        y_keys.append(min(y_keys) - 1)
        y_keys.append(max(y_keys) + 1)
        for y in y_keys:
            x_keys = list(update_cube[z][y].keys())
            x_keys.append(min(x_keys) - 1)
            x_keys.append(max(x_keys) + 1)
            for x in x_keys:
                nb = count_neighbours(update_cube, x, y, z)
                cell = update_cube[z][y][x]
                if cell == 1:
                    if nb == 2 or nb == 3:
                        # cube[z][y][x] = 1
                        pass
                    else:
                        update_cube[z][y][x] = 0
                elif cell == 0:
                    if nb == 3:
                        update_cube[z][y][x] = 1
                    else:
                        pass
    return update_cube


with open('../input/day17_example.txt', 'r') as f:
    initial_state = f.readlines()

cube = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

for y, xs in enumerate(initial_state):
    for x, val in enumerate(xs.strip('\n')):
        if val == '#':
            val = 1
        elif val == '.':
            val = 0
        cube[0][y][x] = val

print(cube)
for i in range(0, 1):
    cube = update_cube(cube)


# print(cube)
values = []
for z in cube.keys():
    for y in cube[z].keys():
        values.extend(cube[z][y].values())

print(sum(values))