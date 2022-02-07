from typing import final
import graph
import tsp


############################################
#                   MAIN                   #
############################################

# The main purpose is to solve the Travelling Salesman Problem (TSP)

init_graph = {
    "A" : [("B",3),("G",8)],
    "B" : [("A",3),("E",6),("G",10),("D",8)],
    "C" : [("G",5),("D",7),("E",10),("F",12)],
    "D" : [("B",8),("G",3),("C",7),("E",4)],
    "E" : [("B",6),("D",4),("C",10),("F",11)],
    "G" : [("A",8),("B",10),("D",3),("C",5)],
    "F" : [("C",12),("E",11)]
    }

graph_dict = graph.Graph(init_graph)
print(graph_dict)
graph_mat = graph_dict.getMatriceWeight()
# print(graph_mat)

# initial matrix
# graph = [[ 0, 3, 0, 0, 0, 8, 0 ], 
#          [ 3, 0, 0, 8, 6, 10, 0 ], 
#          [ 0, 0, 0, 7, 10, 5, 12 ],
#          [ 0, 8, 7, 0, 4, 3, 0 ], 
#          [ 0, 6, 10, 4, 0, 0, 11 ], 
#          [ 8, 10, 5, 3, 0, 0, 0 ], 
#          [ 0, 0, 12, 0, 11, 0, 0 ]]

# perform Prim's Algorithm in order to get the Minimum Spanning Tree (MST) 
v = tsp.primMST(graph_mat)
# print("\n", v)

# create a dynamic matrix
edges_list = [None] * tsp.V
for i in range(tsp.V):
      edges_list[i] = [None] * tsp.V
      for j in range(tsp.V):
            edges_list[i][j] = 0

# set up MST as adjacency matrix
for i in range(len(v)):
      first_node = v[i][0]
      second_node = v[i][1]
      edges_list[first_node][second_node] = 1
      edges_list[second_node][first_node] = 1

# inform if the node i is already visited, useful for the DFS's Algorithm
visited_nodes : bool = [None] * tsp.V
for i in range(tsp.V):
      visited_nodes[i] = False

# perform DFS's Algorithm in order to get the approximate path
tsp.DFS(edges_list, tsp.V, 0, visited_nodes)

# add the source node to the final path
tsp.final_path.append(tsp.final_path[0])

# int to char
index_path = tsp.final_path
letter_path = []
for i in range(len(index_path)):
    letter_path.append(chr(ord("A") + index_path[i]))

# display the approximate path
print("Chemin approximatif :")
for i in range(len(letter_path)):
      print(letter_path[i], "- ", end="")
print()

# final path after resolving the problem of the approximate algorithm
final_path = tsp.resolveWithDijkstra(graph_mat, graph_dict, letter_path)

# display the final path
print("\nChemin final :")
for i in range(len(final_path)):
      print(final_path[i], "- ", end="")
print()