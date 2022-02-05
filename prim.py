import sys
from typing import List

############################################
#             GLOBAL VARIABLES             #
############################################

# Number of nodes in the graph 
V = 5 

# Dynamic array to store the final path
final_path = []

############################################
#                FUNCTIONS                 #
############################################

# from the current node, get the node with the lowest cost
def minimum_key(key : List[int], visitedMST : List[int]) -> int:
      min = sys.maxsize
      min_index = -1
      
      for v in range(V):
            if (visitedMST[v] == False and key[v] < min):
                  min = key[v]
                  min_index = v
 
      return min_index

# give the resulting MST
def MST(parent : List[int], graph : List[List[int]]) -> List[List[int]]:
      v = []

      for i in range(1, V):
            p = []
            p.append(parent[i])
            p.append(i)
            v.append(p)

      return v
 
# get the Minimum Spanning Tree from the given graph using Prim's Algorithm
def primMST(graph : List[List[int]]) -> List[List[int]]:
      parent: List[int] = [None] * V 
      key: List[int] = [None] * V 

      # to keep track of nodes already in MST 
      visitedMST: List[int] = [None] * V

      # initialize key value to INFINITE & false for all visitedMST
      for i in range(V):
            key[i] = sys.maxsize
            visitedMST[i] = False

      # pick up the first node and assign it to 0
      key[0] = 0
      parent[0] = -1

      # The Loop
      for current_node in range(V-1):
            # from the current node, get the node with the lowest cost
            u = minimum_key(key, visitedMST) 
            visitedMST[u] = True

            for v in range(V):
                  if (graph[u][v] and visitedMST[v] == False and graph[u][v] < key[v]): 
                        parent[v] = u
                        key[v] = graph[u][v] 

      return MST(parent, graph)

# get the preorder walk of the MST using DFS
def DFS(edges_list : List[List[int]], nb_nodes : int, starting_vertex : int, visited_nodes : bool) -> None:
    # add the node to the final path
    final_path.append(starting_vertex)

    # check if the node is already visited
    visited_nodes[starting_vertex] = True

    # use a recursive call
    for i in range(nb_nodes):
        if (i == starting_vertex):
            continue

        if (edges_list[starting_vertex][i] == 1):
            if (visited_nodes[i]):
                continue
            DFS(edges_list, nb_nodes, i, visited_nodes)

############################################
#                   MAIN                   #
############################################

# The main purpose is to solve the Travelling Salesman Problem (TSP)

# initial graph
graph = [[ 0, 10, 18, 40, 20 ], 
         [ 10, 0, 35, 15, 12 ], 
         [ 18, 35, 0, 25, 25 ], 
         [ 40, 15, 25, 0, 30 ],
         [ 20, 13, 25, 30, 0 ]]

# perform Prim's Algorithm in order to get the Minimum Spanning Tree (MST) 
v = primMST(graph)

# create a dynamic matrix
edges_list = [None] * V
for i in range(V):
      edges_list[i] = [None] * V
      for j in range(V):
            edges_list[i][j] = 0

# set up MST as adjacency matrix
for i in range(len(v)):
      first_node = v[i][0]
      second_node = v[i][1]
      edges_list[first_node][second_node] = 1
      edges_list[second_node][first_node] = 1

# inform if the node i is already visited, useful for the DFS's Algorithm
visited_nodes : bool = [None] * V
for i in range(V):
      visited_nodes[i] = False

# perform DFS's Algorithm in order to get the approximate path
DFS(edges_list, V, 0, visited_nodes)

# add the source node to the final path
final_path.append(final_path[0])

# print the path
for i in range(len(final_path)):
      print(final_path[i], "- ", end="")
print()