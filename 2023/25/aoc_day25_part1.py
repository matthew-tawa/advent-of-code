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
        self.children = self.children.union(children)

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

    # using Dijkstra's Algorithm
    def find_all_paths(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph:
            return []
        
        paths = []
        for node in self.graph[start].children:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        
        return paths
    
    # find shortest path
    def min_path(self, start, end):
        paths = self.find_all_paths(start, end)

        mdist = 999999
        mpath = []

        for path in paths:
            dist = len(path)

            if dist < mdist:
                mdist = dist
                mpath = path
        
        return mpath

    def dfs(self, visited: set, node: Node, stop_node: Node):
        if node.data not in visited and node.data != stop_node.data:
            visited.add(node.data)
            for child in node.children:
                self.dfs(visited, child, stop_node)

pattern_text = r"([a-z]{3})"
pattern = re.compile(pattern_text)


# building the tree
tree = Tree()
for component in components:
    matches = pattern.findall(component)

    if len(matches) == 1:
        node = Node(matches[0], {})
    else:
        node = Node(matches[0], set(matches[1:]))
    
    tree.add(node)
    
# NOTE this finds roots, but it seems there are non in my given input
# # finding all nodes with only one connection
# roots = [node for node in tree.graph if len(tree.graph[node].children) == 1]

# finding all paths between any two nodes
# all_paths = tree.find_all_paths('bcf', 'pbp')
all_paths = tree.find_all_paths('jqt', 'bvb')

# count occurences of each node among these paths
# idea is to find peak usage of certain routes
for node in tree.graph:
    print(1)

print("multiply group sizes: " + str(len(all_paths)))
print(1)










