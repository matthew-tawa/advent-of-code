from pathlib import Path
import re

# ***** IMPORT INPUT FILE *****
# obtaining the proper relative path
script_location = Path(__file__).absolute().parent
file_name = 'components.txt'
# file_name = 'input.txt'
myfile = script_location / file_name

# read the file into a list, split by the newline characters
# note:  read_text() automatically closes file when done 
components = myfile.read_text().split('\n')
# *****************************

"""
this will be the algorithm:
1. pass through the entire input to create the graph
    graph will be a dictionary where we the key is node name, value is node object
    node object will have a node name, list of connections, and number of times visited
2. choose any two nodes
    perform exhaustive depth first search between two nodes
        not sure what the criteria should be to decide that two nodes can be from the seperable sets
"""

class Node:
    def __init__(self, data, children: set):
        self.data = data
        self.children = children

    def addChildren(self, children: set):
        self.children.union(children)

class Tree:
    def __init__(self):
        self.graph: dict = {}

    def add(self, node: Node):
        # add the node to the graph
        if node.data in self.graph: # if node already in graph, add all children
            self.graph[node.data].addChildren(node.children)
        else: # otherwise just add the node
            self.graph[node.data] = node

        # check the added node's children to make sure backwards link is in graph
        if node.children: # if there is at least 1 child
            for child in node.children:
                if child in self.graph: # if child already in graph, add this backwards link
                    self.graph[child].addChildren({node.data})
                else:
                    n = Node(child, {node.data})
                    self.graph[child] = n

    # depth-first search
    def dfs(self, from_node, to_node):

        print(1)


pattern_text = r"([a-z]{3})"
pattern = re.compile(pattern_text)

# set1 = set()
# set2 = set()
# head1 = pattern.findall(components[0])[0]
# set1.add(head1)

# building the tree
tree = Tree()
for component in components:
    matches = pattern.findall(component)

    if len(matches) == 1:
        node = Node(matches[0], {})
    else:
        node = Node(matches[0], set(matches[1:]))
    
    tree.add(node)
    
# traversing through the tree




print("multiply group sizes: " + str(1))









