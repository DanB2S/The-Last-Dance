INF = 9223372036854775807

# Return the distance of a path
def calcDist(graph, path):
    sumDist = 0
    for i in range(len(path) - 1):
        sumDist += graph[path[i]][path[i+1]]
    return sumDist + graph[path[-1]][0]

def bb_tspAlg(graph, path, best):
    # If len path grater than n cities, return
    if (len(path) > len(graph)):
        return
    
    # Calc dist of actual non completed path
    dist = calcDist(graph, path)
    # If dist grater than best, don't need to continue
    if (dist >= best[0]):
        return
    # If len path is equal to n cities, we have a complete path, save
    elif (len(path) == len(graph)):
        best[0] = dist
        best.pop()
        best.append(path.copy())

    # Count calls
    best[1] += 1
    
    # Recursive calls
    for i in range(len(graph)):
        # For cities non visited
        if (i not in path):
            path.append(i)
            bb_tspAlg(graph, path, best)
            path.pop()
    
    pass

def bb_tsp(graph):
    best = [INF, 1, []] # List of save values 
    # Start Recursive calls
    bb_tspAlg(graph, [0], best)
    return best

import math

if __name__ == "__main__":

    graphs = [
        [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]],
        
        [[   0, 2770,  389,  497, 1514,  888, 1543],
         [2770,    0, 2314, 2213, 4181, 2105, 1446],
         [ 389, 2314,    0,  112, 1972,  994, 1345],
         [ 497, 2213,  112,    0, 2076, 1057, 1408],
         [1514, 4181, 1972, 2076,    0, 2328, 2986],
         [ 888, 2105,  994, 1057, 2328,    0,  962],
         [1543, 1446, 1345, 1408, 2986,  962,    0]],
        
        [[   0, 2770,  389,  497, 1514,  888, 1543,  102, 3227, 3295],
         [2770,    0, 2314, 2213, 4181, 2105, 1446, 2791, 3206,   97],
         [ 389, 2314,    0,  112, 1972,  994, 1345,  486,  446,  199],
         [ 497, 2213,  112,    0, 2076, 1057, 1408,  590, 2750, 2859],
         [1514, 4181, 1972, 2076,    0, 2328, 2986, 1535, 2649,  588],
         [ 888, 2105,  994, 1057, 2328,    0,  962, 8700, 4617,  692],
         [1543, 1446, 1345, 1408, 2986,  962,    0, 1441, 2417, 1637],
         [ 102, 2791,  486,  590, 1535, 8700, 1441,    0, 1882,  858],
         [3227, 3206,  446, 2750, 2649, 4617, 2417, 1882,    0, 1339],
         [3295,   97,  199, 2859,  588,  692, 1637,  858, 1339,    0]]
    ]

    for graph in graphs:
      output = bb_tsp(graph)
      print("Best Distance: ", output[0])
      print("Path: ", output[2] + [0])
      print("Number of recursive calls: (", output[1], "/", math.factorial(len(graph)), ")")
      print()

    