import graph

# Test
list_node_edge = {
    "A" : [("B",3),("G",8)],
    "B" : [("A",3),("E",6),("G",10),("D",8)],
    "C" : [("G",5),("D",7),("E",10),("F",12)],
    "D" : [("B",8),("G",3),("C",7),("E",4)],
    "E" : [("B",6),("D",4),("C",10),("F",11)],
    "F" : [("C",12),("E",11)],
    "G" : [("A",8),("B",10),("D",3),("C",5)]
    }

graph = graph.Graph(list_node_edge)
print(graph)
mat = graph.getMatriceWeight()
print(mat)

############################################
#                   MAIN                   #
############################################

# # The main purpose is to solve the Travelling Salesman Problem (TSP)

# # initial graph
# graph = [[ 0, 3, 0, 0, 0, 8, 0 ], 
#          [ 3, 0, 0, 8, 6, 10, 0 ], 
#          [ 0, 0, 0, 7, 10, 5, 12 ],
#          [ 0, 8, 7, 0, 4, 3, 0 ], 
#          [ 0, 6, 10, 4, 0, 0, 11 ], 
#          [ 8, 10, 5, 3, 0, 0, 0 ], 
#          [ 0, 0, 12, 0, 11, 0, 0 ]]

# # perform Prim's Algorithm in order to get the Minimum Spanning Tree (MST) 
# v = primMST(graph)
# print(v)

# # create a dynamic matrix
# edges_list = [None] * V
# for i in range(V):
#       edges_list[i] = [None] * V
#       for j in range(V):
#             edges_list[i][j] = 0

# # set up MST as adjacency matrix
# for i in range(len(v)):
#       first_node = v[i][0]
#       second_node = v[i][1]
#       edges_list[first_node][second_node] = 1
#       edges_list[second_node][first_node] = 1

# # inform if the node i is already visited, useful for the DFS's Algorithm
# visited_nodes : bool = [None] * V
# for i in range(V):
#       visited_nodes[i] = False

# # perform DFS's Algorithm in order to get the approximate path
# DFS(edges_list, V, 0, visited_nodes)

# # add the source node to the final path
# final_path.append(final_path[0])

# # display the path
# print("Chemin final :")
# for i in range(len(final_path)):
#       print(final_path[i], "- ", end="")
# print()