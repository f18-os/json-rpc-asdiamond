class Node:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children
        self.val = 0

    def show(self, level=0):
        print(f"{level*'  '}{self.name} val={self.val:d}:")
        for c in self.children:
            c.show(level + 1)


def increment(graph):
    graph.val += 1
    for c in graph.children:
        increment(c)
