import numpy as np

def knapsack_dynamic(values, weights, capacity):

    # Aux to save values
    best = [0, 1, []]

    n = len(weights) # Number of items

    # Memory matrix
    memory = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # It is convenient to define the initial conditions as follows:
    # F (0, j) = 0 for j ≥ 0 and F (i, 0) = 0 for i ≥ 0
    for i in range(n + 1):
        memory[i][0] = 0
    for j in range(capacity + 1):
        memory[0][j] = 0

    # F (i, j ) = { max{F (i − 1, j), v[i] + F (i − 1, j − w[i])} ---> if (j − w[i] ≥ 0),
    #             { F (i − 1, j)                                  ---> if (j − w[i] < 0)
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            best[1] += 1 # Count calls
            if (j - weights[i - 1] >= 0):
                memory[i][j] = max(memory[i - 1][j], values[i - 1] + memory[i - 1][j - weights[i - 1]])
            else:
                memory[i][j] = memory[i - 1][j]

    # Best value is the last value of the matrix
    best[0] = memory[n][capacity]

    # Just to plot the used items
    # Traceback to find the items included
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if memory[i][j] != memory[i - 1][j]:  # Item i is included
            selected_items.append(i)  # Add item index (1-based)
            j -= weights[i - 1]       # Reduce the capacity
        i -= 1  # Move to the previous item
    # Transform to True or False
    for i in range(len(values)):
        if ((i + 1) in selected_items):
            best[2].append(True)
        else:
            best[2].append(False)

    return best


if __name__ == "__main__":

    values = [
        [6, 4, 3, 7, 8, 1, 3, 5, 7, 5],
        [50, 100, 80, 90, 75, 70, 50, 40, 65, 55, 45, 35],
        [60, 100, 120, 90, 75, 80, 50, 40, 65, 55, 200, 150, 85, 95, 110, 70, 45, 30, 25, 10]
    ]
    weights = [
        [3, 6, 9, 4, 6, 4, 8, 6, 5, 7],
        [10, 20, 30, 25, 15, 22, 12, 8, 18, 17, 10, 12],
        [10, 20, 30, 25, 15, 22, 12, 8, 18, 17, 50, 40, 35, 20, 28, 10, 15, 5, 8, 3]
    ]
    c = [25, 75, 100]

    for i in range(len(c)):
        output = knapsack_dynamic(values[i], weights[i], c[i])
        print("Best Value: ", output[0])
        print("Use List: ", output[2])
        print("Number of recursive calls: (", output[1], "/", pow(2, len(values[i])), ")")
        print()