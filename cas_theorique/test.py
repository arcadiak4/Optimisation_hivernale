import graph

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

graph = graph.Graph(list_node_edge)
graph.removeNode("A")
graph.addNode("A", "B",12)
print(graph)