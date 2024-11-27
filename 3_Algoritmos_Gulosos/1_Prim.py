from Test import *

# Prim's algorithm creates a tree with a local optimum edges distance
# from a start point

def prim(graph, start):

    visited = [start] # List of visited nodes
    path = [] # Saved path

    # While not visited every node
    while (len(visited) < len(graph)):
        
        next = None
        min = INF
        st_node = None

        for node in visited:
            for i in range(len(graph)):
                if (graph[node][i] < min and (i not in visited)):
                    min = graph[node][i]
                    next = i
                    st_node = node
        
        if next == None:
            return "Invalid Graph"
        
        visited.append(next)
        path.append([st_node, next])

    # Calc the final distance
    weight = 0
    for ed in path:
        weight += graph[ed[0]][ed[1]]

    return weight, path

if __name__ == "__main__":

    for graph in graphs:
        dist, edges = prim(graph, 0)
        print("Distancia da arvore: ", dist)
        print("Arestas: ", edges)
        print()