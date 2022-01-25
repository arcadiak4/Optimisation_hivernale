import pprint
from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, list_node_edge, directed=False):
        self.Graph = list_node_edge
        self.Directed = directed

    def addNode(self, node1, node2, weight):
      if not node1 in self.Graph:
        self.Graph[node1] = []

      self.Graph[node1].append((node2, weight))

      if not node2 in self.Graph:
          self.Graph[node2] = []
      
      if not self.Directed:
        self.Graph[node2].append((node1, weight))

    def removeNode(self, node):
      pass
    
    def __str__(self):
        str_return = ""
        for node in self.Graph:
            str_return += node + " : " + str(self.Graph[node]) + '\n'
        return str_return
    
# Test
list_node_edge = {
    "A" : [("H",6),("B",12),("C",6),("D",10),("G",8)],
    "B" : [("H",6),("I",2),("A",12),("C",6)],
    "C" : [("B",6),("I",3),("A",6),("D",1)],
    "D" : [("A",10),("C",1),("E",2),("F",4)],
    "F" : [("D",4),("G",2)],
    "G" : [("A",8),("F",2)],
    "H" : [("A",6),("B",6)],
    "I" : [("B",2),("C",3)]
    }

graph = Graph(list_node_edge, True)
graph.addNode("L", "J", 5)
print(graph)

    


