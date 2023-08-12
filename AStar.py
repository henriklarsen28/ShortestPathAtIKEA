import sys
import math
from heapq import heapify, heappush, heappop

def searchWeightDictionary(weight,source, node):
    nextNode = next(item for item in weight[source] if node in item)
    return nextNode[node]

def aStar(graph, weight, src, dest):
    inf = sys.maxsize

    node_data = {}
    for nodes in graph:
        node_data[nodes] = {"fn": inf,"cost": inf, "pred": []}

    node_data[src]["cost"] = 0
    node_data[src]["fn"] = weight[src]


    min_heap = []
    min_heap.append((searchWeightDictionary(weight,src,src), 0, src))

    visited = []


    while node_data[dest]["cost"] == inf:

        heapify(min_heap)
        f , current_distance, current_node = heappop(min_heap)

        #Adds node to visited list
        visited.append(current_node)

        # Add neighbors
        for i in graph[current_node]:

            # Checks if the the node visited before
            if i not in visited:

                # Check if method is closer than earlier
                cost = node_data[current_node]["cost"] + graph[current_node][i]

                # Finds the weight between the current node and the next node
                nextNode = next(item for item in weight[current_node] if i in item)
                nextNodeWeight = nextNode[i]

                # Checks sum of distance and weight
                fn = cost + nextNodeWeight

                node_data[i]["cost"] = cost
                node_data[i]["pred"] = node_data[current_node]["pred"] + [current_node]
                node_data[i]["fn"] = fn
                heappush(min_heap, (node_data[i]["fn"], node_data[i]["cost"], i))

    #print("Shortest distance: " + str(node_data[dest]["cost"]))
    #print("Shorted path: " + str(node_data[dest]["pred"]))
    return [node_data[dest]["cost"], node_data[dest]["pred"]]



