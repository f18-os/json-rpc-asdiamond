from graph.node import Node
from graph.node import increment

leaf1 = Node("leaf1")
leaf2 = Node("leaf2")

root = Node("root", [leaf1, leaf1, leaf2])

print("graph before increment")
root.show()

# do this increment remotely:
increment(root)

print("graph after increment")
root.show()

