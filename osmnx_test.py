import osmnx as ox 
# G = ox.graph_from_place('Montreal, Canada', network_type='drive')
# ox.plot_graph(G)

# define a point at the corner of California St and Mason St in SF
location_point = (45.517457, -73.568499)
# create network from point, inside bounding box of N, S, E, W each 750m from point
G = ox.graph_from_point(location_point, dist=750, dist_type="bbox", network_type="drive")
ox.plot_graph(G)