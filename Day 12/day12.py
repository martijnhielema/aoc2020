with open('../input/day12.txt', 'r') as f:
    instructions = [x.strip('\n') for x in f.readlines()]

x = 0
y = 0
directions = ('N', 'E', 'S', 'W')
facing = 1
waypoint_x = 10
waypoint_y = 1

for i in instructions:
    direction = directions[facing]
    if i[0] in directions:
        direction = i[0]
    elif i[0] == 'F':
        x += int(i[1:]) * waypoint_x
        y += int(i[1:]) * waypoint_y
        continue
    elif i[0] == 'L':
        steps = int(i[1:]) // 90
        # facing = (facing - steps) % 4
        for i in range(0, steps):
            new_x = -waypoint_y
            new_y = waypoint_x

            waypoint_x = new_x
            waypoint_y = new_y
        continue
    elif i[0] == 'R':
        steps = int(i[1:]) // 90
        # facing = (facing + steps) % 4
        for i in range(0, steps):
            new_x = waypoint_y
            new_y = -waypoint_x

            waypoint_x = new_x
            waypoint_y = new_y
        continue

    if direction == 'N':
        waypoint_y += int(i[1:])
    elif direction == 'S':
        waypoint_y -= int(i[1:])
    elif direction == 'E':
        waypoint_x += int(i[1:])
    elif direction == 'W':
        waypoint_x -= int(i[1:])

print(abs(x) + abs(y))
