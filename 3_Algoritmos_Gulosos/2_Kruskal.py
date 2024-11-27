from Test import *

# Kruskal algorithm creates a tree with a local optimum edges distance

# Find the min edge distance
def getMin(graph, visited):
    min_i = 0
    min_j = 0
    min = INF
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if (graph[i][j] < min and not visited[i][j]):
                min_i = i
                min_j = j
                min = graph[i][j]
    visited[min_i][min_j] = True
    return min_i, min_j

# Check if adding this edge will create a cicle
def willCreateCicle(mst_Edges, i, j):
    # For all set in the list
    for edge_set in mst_Edges:
        has_i = False
        has_j = False
        # If the set has both values, will create a cicle
        for node in edge_set:
            if (node == i):
                has_i = True
            if (node == j):
                has_j = True
        if (has_i and has_j):
            return True
    return False

# Disjoint Set Union
# Add connected nodes to the same set
# Useful for checking cicles
def mstUnion(mst_Edges, i, j):
    aux = None
    # Find the set to remove
    for e_i, edge_set in enumerate(mst_Edges):
        for node in edge_set:
            if node == j:
                aux = mst_Edges.pop(e_i)
                break
    # Append it to the new set
    for e_i, edge_set in enumerate(mst_Edges):
        for node in edge_set:
            if node == i:
                for v in aux:
                    edge_set.append(v)
    pass


def kruskal(graph):

    # Matrix of visited edges
    visited = [[False for _ in range(len(graph))] for _ in range(len(graph))]
    edges = [] # List of best edges
    mst_Edges = [[i] for i in range(len(graph))] # List of set of nodes
    
    # A tree with V vertices always has exactly V-1 edges.
    while (len(edges) < len(graph) - 1):
        i, j = getMin(graph, visited) # Find the min edge distance
        if (not willCreateCicle(mst_Edges, i, j)): # Check if will create a cicle
            edges.append((i, j)) # If not save edge
            mstUnion(mst_Edges, i, j) # Add connected nodes to the same set

    # Calc the final distance
    weight = 0
    for ed in edges:
        weight += graph[ed[0]][ed[1]]

    return weight, edges

if __name__ == "__main__":
    
    for graph in graphs:
        dist, edges = kruskal(graph)
        print("Distancia da arvore: ", dist)
        print("Arestas: ", edges)
        print()