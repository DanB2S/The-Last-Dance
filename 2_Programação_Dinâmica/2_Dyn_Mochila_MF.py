import numpy as np

def MFKnapsack(values, weights, memory, i, j, best):
    # Calls counter
    best[1] += 1
    # if F[i, j] < 0
    if (memory[i][j] < 0):
        # if j < Weights[i]
        if (j < weights[i - 1]):
            # value ← MFKnapsack(i − 1, j)
            vAux = MFKnapsack(values, weights, memory, i - 1, j, best)
        # else
        else:
            # value ← max(MFKnapsack(i − 1, j ),
            #             Values[i] + MFKnapsack(i − 1, j − Weights[i]))
            vAux = max(MFKnapsack(values, weights, memory, i - 1, j, best),
                       values[i - 1] + MFKnapsack(values, weights, memory, i - 1, j - weights[i - 1], best))
        # F[i, j] ← value
        memory[i][j] = vAux
    # return F[i, j]
    return memory[i][j]

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

    # Start recursive call
    MFKnapsack(values, weights, memory, n, capacity, best)

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