with open('../input/dad.txt', 'r') as f:
    adapters = [int(x.strip()) for x in f.readlines()]

adapters.append(0)
adapters = sorted(adapters)

differences = {'1': 0, '2': 0, '3': 1}
for i in range(1, len(adapters)):
    diff = adapters[i] - adapters[i-1]
    differences[str(diff)] += 1

print(differences)
print(differences['1'] * differences['3'])
