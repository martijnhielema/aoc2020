from collections import defaultdict
from anytree import NodeMixin, RenderTree, PreOrderIter
import anytree


class WNode(NodeMixin):
    def __init__(self, foo, parent=None, number = None):
        super(WNode, self).__init__()
        self.name = foo
        self.parent = parent
        self.number = int(number) if parent is not None else 1
        self.bags_children_plus1 = 1

    def _post_detach(self, parent):
        self.weight = None


with open('../input/day7.txt', 'r') as f:
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

# for pre, _, node in RenderTree(nodes['shiny gold']):
#     print("%s%s (%s, level: %s)" % (pre, node.name, node.number or 0, node.depth))

leaves = list(nodes['shiny gold'].leaves)
max_depth = max([leaf.depth for leaf in leaves])
while max_depth > 0:
    deepest_leaves = [leaf for leaf in leaves if leaf.depth == max_depth]
    print(max_depth)
    print([(l.name, l.number, l.parent.name, l.bags_children_plus1) for l in deepest_leaves])
    for leaf in deepest_leaves:
        node_total = 0
        node_total += leaf.number * leaf.bags_children_plus1
        for sibling in leaf.siblings:
            node_total += sibling.number * sibling.bags_children_plus1
            deepest_leaves.remove(sibling)
            sibling.parent = None

        leaf.parent.bags_children_plus1 = node_total + 1
        # print(leaf.parent.bags_children_plus1)
        leaf.parent = None
    leaves = list(nodes['shiny gold'].leaves)
    max_depth = max([leaf.depth for leaf in leaves])

print('Answer:')
print(nodes['shiny gold'].bags_children_plus1 - 1)
