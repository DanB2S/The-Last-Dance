from Test import *

# Dijkstra's algorithm find the shortest distance to every node
# in a graph

# Return min index non visited
def nextMin(dist, visited):
    min_i = 0
    min = INF
    for node in range(len(dist)):
        if dist[node] < min and node not in visited:
            min_i = node
            min = dist[node]
    return min_i

def dijkstra(graph, start):

    # List of distance
    dist = [INF for _ in range(len(graph))]
    dist[start] = 0 # Start with 0

    visited = [] # List of visited
    actual = start # Actual = start

    # While i not visited all nodes
    while (len(visited) < len(graph)):
        # For each next node
        for node in range(len(graph)): 
            # Check if there is a short way      
            if dist[actual] + graph[actual][node] < dist[node]:
                dist[node] = dist[actual] + graph[actual][node]
        # Set as visited
        visited.append(actual)
        # Next node is the smallest path distance non visited node
        actual = nextMin(dist, visited)

    return dist

if __name__ == "__main__":

    for graph in graphs:
        dist = dijkstra(graph, 0)
        print("Distancias do grafo: ", dist)
        print()