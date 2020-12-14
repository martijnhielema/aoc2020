from math import floor


with open('../input/day13_example.txt', 'r') as f:
    raw = f.readlines()
    timestamp = int(raw[0].strip('\n'))
    buses = set(raw[1].strip('\n').split(','))
    buses.remove('x')
    buses = [int(x) for x in buses]
    buses_part2 = [int(x) for x in raw[1].strip('\n').split(',') if x != 'x']

bus_id = None
min_wait_time = 1000000000000


for bus in buses:
    next_departure = (floor(timestamp/bus) + 1) * bus
    wait_time = next_departure - timestamp
    if wait_time < min_wait_time:
        min_wait_time = wait_time
        bus_id = bus
print('Part 1:')
print(bus_id, min_wait_time)
print(bus_id * min_wait_time)
print('--------------------------')

t = 0
while True:
    break