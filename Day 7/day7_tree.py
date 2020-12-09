from collections import defaultdict
from anytree import NodeMixin, RenderTree, PreOrderIter
import anytree


class WNode(NodeMixin):
    def __init__(self, foo, parent=None, number = None):
        super(WNode, self).__init__()
        self.name = foo
        self.parent = parent
        self.number = int(number) if parent is not None else 1

    def _post_detach(self, parent):
        self.weight = None


with open('../input/day7_example.txt', 'r') as f:
    raw_rules = [x.strip() for x in f.readlines()]

bags = defaultdict(list)

for raw in raw_rules:
    subject, contents = raw.split(' bags contain ')
    bag = subject.strip(' ')
    for content in contents.split(', '):
        if content == 'no other bags.':
            continue
        else:
            content = content.strip('.')[0:-4]
            number = content[0]
            name = content[2:]
            bags[bag].append((name.strip(), number))

nodes = {}
nodes['shiny gold'] = WNode('shiny gold')
to_process = ['shiny gold']

while len(to_process) > 0:
    for i, name in enumerate(to_process):
        to_process.pop(i)
        search_name = name.split('_')[0].strip()
        for j in bags[search_name]:
            if j[0] in nodes.keys():
                existing_nodes = len([s for s in nodes.keys() if j[0] in s])
                node_name = j[0] + '_' + str(existing_nodes)
            else:
                node_name = j[0]
            nodes[node_name] = WNode(node_name, parent=nodes[name], number=j[1])
            to_process.append(node_name)

for pre, _, node in RenderTree(nodes['shiny gold']):
    print("%s%s (%s)" % (pre, node.name, node.number or 0))

total = 0
for leaf in nodes['shiny gold'].leaves:
    subtotal = 1
    subtotal_non_multiply = 0
    for node in leaf.path:
        subtotal *= node.number
        if not node.is_leaf:
            subtotal_non_multiply += 1
    total += subtotal
    total += subtotal_non_multiply

print(total)

