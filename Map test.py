import networkx as nx
import matplotlib.pyplot as plt
import sys
from AStar import aStar
from combinationList import allCombinations


# Ikea item list


# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_node("Entrance", pos=(0.5, -0.5), weight=0)
G.add_node("LivingRoom", pos=(-1, 1.5), weight=3.8)
G.add_node("LivingRoomStorage", pos=(0.5, 2), weight=2.5)
G.add_node("Dining", pos=(0.5, 3), weight=3.5)
G.add_node("Bedroom", pos=(-0.5, 3), weight=4.5)
G.add_node("BedroomStorage", pos=(-0.5, 3.5), weight=4.8)
G.add_node("Bathroom", pos=(-0.5, 4), weight=5)
G.add_node("Workspace", pos=(0.5, 4), weight=4.5)
G.add_node("Kitchen", pos=(1, 3.2), weight=4)
G.add_node("ChildrenRoom", pos=(1, 1.8), weight=2.5)
G.add_node("SelfServeHall", pos=(1, 0), weight=1)

# Add nodes to the self serve hall
G.add_node("1_1", pos=(1.3, -1), weight=2)
G.add_node("1_2", pos=(1.6, -1), weight=2.3)
G.add_node("1_3", pos=(1.9, -1), weight=2.6)
G.add_node("1_4", pos=(2.2, -1), weight=2.9)

G.add_node("3_1", pos=(1.3, -1.5), weight=2.5)
G.add_node("3_2", pos=(1.6, -1.5), weight=2.7)
G.add_node("3_3", pos=(1.9, -1.5), weight=2.9)
G.add_node("3_4", pos=(2.2, -1.5), weight=3.1)

G.add_node("2_1", pos=(0.6, -1), weight=1.6)
G.add_node("2_2", pos=(0.3, -1), weight=1.5)
G.add_node("2_3", pos=(0, -1), weight=1.4)
G.add_node("2_4", pos=(-0.3, -1), weight=1.3)

G.add_node("4_1", pos=(0.6, -1.5), weight=2.1)
G.add_node("4_2", pos=(0.3, -1.5), weight=2)
G.add_node("4_3", pos=(0, -1.5), weight=1.9)
G.add_node("4_4", pos=(-0.3, -1.5), weight=1.8)

G.add_node("Exit", pos=(1, -3), weight=3)

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
G.add_edge("ChildrenRoom", "SelfServeHall", weight=1.8)

#Add edges in the self serve hall
G.add_edge("SelfServeHall", "1_1", weight=0.5)
G.add_edge("1_1", "1_2", weight=0.5)
G.add_edge("1_2", "1_3", weight=0.5)
G.add_edge("1_3", "1_4", weight=0.5)
G.add_edge("1_1", "3_1", weight=0.5)
G.add_edge("3_1", "3_2", weight=0.5)
G.add_edge("3_2", "3_3", weight=0.5)
G.add_edge("3_3", "3_4", weight=0.5)

G.add_edge("3_1", "Exit", weight=0.5)

#Shortcut dining to workspace
G.add_edge("Dining", "Workspace", weight=1)
#Shortcut dining to kitchen
G.add_edge("Dining", "Kitchen", weight=1.4)
#Shortcut from entrance to exit/cafe
G.add_edge("Entrance", "SelfServeHall", weight=1)


weight = {}

#Converts graph to list of objects for Astar algorithm
converted_Graph = {}
for node in G.nodes:
    weight[node] = G.nodes[node].get("weight",0)
    converted_Graph[node] = {neighbor: G.edges[node, neighbor]["weight"] for neighbor in G.neighbors(node)}

#Starts at entrance and ends at exit
source = "Entrance"
dest = "Exit"
listOfLocations = ["Entrance","Bathroom", "ChildrenRoom", "Exit"]   # List of locations to visit



listOfCombinations = allCombinations(listOfLocations,source, dest)

#Calculates the shortest path in IKEA with the categories above
length = sys.maxsize
shortestPath = []

for list in listOfCombinations: # Iterates through every permutations
    currentLength = 0
    path = []
    for i in range(0, len(list)-1): # Iterates through the list of a permutation
        print(list[i], list[i+1])   # Prints the current node and the next node
        cost, pred = aStar(converted_Graph, weight, list[i],list[i+1])
        currentLength += cost   # Adds the cost of the current node to the total cost
        path += pred            # Adds the path of the current node to the total path
        print(currentLength)

        #Stores the shortest path
    if currentLength < length:   # Checks if the current path is shorter than the previous
        length = currentLength
        shortestPath = path

print(path + [dest])
print(round(length,1))



# Get positions of nodes
pos = nx.get_node_attributes(G, 'pos')

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, edge_color='gray')

# Draw edge labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Show the graph
plt.show()