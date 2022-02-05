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
      
      #Suppretion node
      if node in self.Graph:
        del self.Graph[node]

      # Suppression des intersections
      for _node in self.Graph:
        for _next in self.Graph[_node]:
          if _next[0] == node:
            self.Graph[_node].remove(_next)
    
    def __str__(self):
        str_return = ""
        for node in self.Graph:
            str_return += node + " : " + str(self.Graph[node]) + '\n'
        return str_return

    def getWeight(self, node1, node2):
          
        # Si la node n'existe pas, retourne -1
        if(node1 not in self.Graph):
            return -1

        # Trouve la position du voisin s'il existe
        i = 0
        while(i < len(self.Graph[node1]) and self.Graph[node1][i][0] != node2):
            i += 1
        
        # Si les deux sommets ne sont pas voisins, retourne 0
        if (i >= len(self.Graph[node1])):
            return 0
        
        # Si les sommets sont voisins, retourne leur poids
        else:
            return self.Graph[node1][i][1]
        

    

    


