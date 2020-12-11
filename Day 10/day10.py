from functools import reduce
import networkx as nx
import matplotlib.pyplot as plt

with open('../input/day10.txt', 'r') as f:
    adapters = [int(x.strip()) for x in f.readlines()]

adapters.append(0)
adapters = sorted(adapters)

differences = {'1': 0, '2': 0, '3': 1}
for i in range(1, len(adapters)):
    diff = adapters[i] - adapters[i-1]
    differences[str(diff)] += 1
# print(differences)
# print(differences['1'] * differences['3'])

adapters.append(max(adapters)+3)

# Build indices where to split groups
indices = [0]
for i in range(0, len(adapters) - 1):
    if adapters[i+1] - adapters[i] == 3:
        indices.append(i+1)

groups = []

# Build groups
for i in range(0, len(indices) - 1):
    ifrom = indices[i]
    to = indices[i + 1]

    groups.append(adapters[ifrom:to])

# Build DAG for each group and calculate number of possible paths
answerlist = []
for group in groups:
    connected_pairs = []
    for i in range(0, len(group) - 1):
        start = group[i]
        for j in range(i + 1, len(group)):
            if group[j] - start <= 3:
                connected_pairs.append((str(start), str(group[j])))
            else:
                break

    if len(group) > 1:
        graph = nx.DiGraph()
        graph.add_edges_from(connected_pairs)

        paths = tuple(nx.all_simple_paths(graph, str(min(group)), str(max(group))))
        numpaths = len(paths)
    else:
        numpaths = 1
    answerlist.append(numpaths)

print(answerlist)
print(reduce(lambda x, y: x*y, answerlist))
