import sys
import re
from collections import deque

input_list = [int(num) for num in re.findall('\d+',open(sys.argv[1]).readline())]


# Build the tree
class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def __repr__(self):
        return 'Node with Children: {}, Metadata {}'.format(self.children,
             self.metadata)

def parse_input(_iter):
    n_childern = next(_iter)
    n_metadata = next(_iter)
    children = []
    for i in range(n_childern):
        children += [parse_input(_iter)]

    metadata = [ next(_iter) for i in range(n_metadata)]

    return Node(children, metadata)



root_node = parse_input(iter(input_list))
nodes = deque([root_node])

total = 0
while len(nodes) > 0:
    # Get the fist node on the queue
    node = nodes.pop()
    for n_node in node.children:
        nodes.append(n_node)
    # Add up the total for that node
    total += sum(node.metadata)

print('Sum of metadata is: {}'.format(total))
