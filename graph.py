import sys
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

    def getMatriceWeight(self):

        # Initialisation de la matrice à 0
        matriceGraph = [[0 for x in range(len(self.Graph))] for i in range(len(self.Graph))]

        i = 0
        j = 0

        # Remplissage de la matrice
        for node1 in self.Graph:
            for node2 in self.Graph:
                matriceGraph[i][j] = self.getWeight(node1, node2)
                j += 1
            j = 0
            i += 1
        
        return matriceGraph

    def printLnMatriceWeight(self):
          matrice = self.getMatriceWeight()

          for elem in matrice:
                print(elem)

    def dijsktra(self, initial, end):
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()
        costWay = 0
        
        while current_node != end:
            visited.add(current_node)
            destinations = self.Graph[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = self.getWeight(current_node, next_node[0]) + weight_to_current_node
                if next_node[0] not in shortest_paths:
                    shortest_paths[next_node[0]] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node[0]][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node[0]] = (current_node, weight)
            
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        
        # Work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            costWay += self.getWeight(current_node, next_node)
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path, costWay

        

    
    


