import networkx as nx
import matplotlib.pyplot as plt
import sys
import time
import math
from AStar import aStar
from combinationList import allCombinations


# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_node("Entrance", pos=(0.5, -0.5), weight=0)
G.add_node("LivingRoom", pos=(-1, 1.5), weight=3.8)
G.add_node("LivingRoomStorage", pos=(0.5, 2), weight=2.5)
G.add_node("Dining", pos=(0.5, 3),weight=3.5)
G.add_node("Bedroom", pos=(-0.5, 3), weight=4.5)
G.add_node("BedroomStorage",pos=(-0.5,3.5), weight=4.8)
G.add_node("Bathroom",pos=(-0.5,4), weight=5)
G.add_node("Workspace",pos=(0.5,4), weight=4.5)
G.add_node("Kitchen",pos=(1,3.2), weight=4)
G.add_node("ChildrenRoom",pos=(1,1.8), weight=2.5)
G.add_node("Exit", pos=(1,0), weight=1)

# Add edges between nodes
G.add_edge("Entrance", "LivingRoom", weight=2.5)
G.add_edge("LivingRoom", "LivingRoomStorage", weight=1.6)
G.add_edge("LivingRoomStorage","Dining", weight=1)
G.add_edge("Dining", "Bedroom", weight=1)
G.add_edge("Bedroom", "BedroomStorage", weight=0.5)
G.add_edge("BedroomStorage", "Bathroom", weight=0.5)
G.add_edge("Bathroom", "Workspace", weight=1)
G.add_edge("Workspace", "Kitchen", weight=1.5)
G.add_edge("Kitchen", "ChildrenRoom", weight=2)
G.add_edge("ChildrenRoom", "Exit", weight=1.8)




#Shortcut dining to workspace
G.add_edge("Dining", "Workspace", weight=1)
#Shortcut dining to kitchen
G.add_edge("Dining", "Kitchen", weight=1.4)
#Shortcut from entrance to exit/cafe
G.add_edge("Entrance", "Exit", weight=1)


weight = {}

#Converts graph to list for Astar algorithm
converted_Graph = {}
for node in G.nodes:
    weight[node] = (G.nodes[node]["weight"])
    converted_Graph[node] = {neighbor: G.edges[node, neighbor]["weight"] for neighbor in G.neighbors(node)}

#Starts at entrance and ends at exit
source = "Entrance"
dest = "Exit"
listOfLocations = ["Entrance","Bathroom", "ChildrenRoom", "Exit"]



listOfCombinations = allCombinations(listOfLocations,source, dest)

#Calculates the shortest path in IKEA with the categories above
distance = sys.maxsize
shortestPath = []
for list in listOfCombinations:
    length = 0
    path = []
    for i in range(0, len(list)-1):
        print(list[i], list[i+1])
        cost, pred = aStar(converted_Graph, weight, list[i],list[i+1])
        length += cost
        path += pred
        print(length)
    #Stores the shortest path
    if length < distance:
        distance = length
        shortestPath = path
print(path + [dest])
print(round(distance,1))



# Get positions of nodes
pos = nx.get_node_attributes(G, 'pos')

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, edge_color='gray')

# Draw edge labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Show the graph
plt.show()