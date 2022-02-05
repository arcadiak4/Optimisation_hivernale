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

        
###DJIKSTRA incomplet malheuresement...
   #pour meux comprendre ce que j'ai tenté de faire : 
   #"https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra#Impl%C3%A9mentation_de_l'algorithme"
       
    def get_nodes(self):#return a list of all the nodes
        list_nodes=[]
        for _node in self.Graph:
            list_nodes.append(_node)
        return list_nodes     
            
    def initalization(self, node):
        #on initialise les sommets à infini(= sys.maxsize)
        for _node in self.Graph:
            for _next in self.Graph[_node]:
                lnext = list(_next)
                lnext[1] = sys.maxsize   
                _next = tuple(lnext)
        #from node to node -> dist = 0        
        #self.Graph[node].append((node,0))
        
        
    def find_min(self, node): #retourne le sommet avec le poids minimum -> le plus petit des poids(node,sommet) 
        mini = sys.maxsize
        n = None
        for t in self.Graph[node]:
            if t[1] < mini:
                mini = t[1]
                n = t[0]
       
        return n

    def maj_dist(self,node,node1,node2):
        for t in self.Graph[node1]:
            if t[0] == node2:
                d12=t[1] #poids(node,node1)
        for t in self.Graph[node]:
            if t[0] == node1 :
                d1=t[1] #poids(node,node1)
            if t[0] == node2:
                d2= t[1] #poids(node,node2)

        #if d2 > (d1 + d12) :
        #  predecesseur[node2]=node1
            
   
    def djikstra(self, node):    
        #initializatoin(self,node)
        list_nodes = self.Graph.get_nodes()
        list_nodes.remove(node)
        #tant que liste n'est pas vide
        #while len(list_nodes) > 0:
            




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

    


