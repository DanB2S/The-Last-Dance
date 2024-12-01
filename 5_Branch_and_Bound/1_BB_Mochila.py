# Check if solution is valid
def checkCapacity(weight, useList, c):
    w_sum = 0
    for i in range(len(useList)):
        if (useList[i]):
            w_sum += weight[i]
    return w_sum <= c

# Calc sum of values add to knapsack
def calcValue(value, useList):
    v_sum = 0
    for i in range(len(useList)):
        if (useList[i]):
            v_sum += value[i]
    return v_sum

# Recursive algorithm
def bb_knapsackAlg(value, weight, c, useList, best):
    # If len of "use list" greater than len itens
    if (len(useList) > len(value)):
        return # Return
    
    # If don't check knapsack capacity, means don't need to continue
    if (not checkCapacity(weight, useList, c)):
        return # Return
    
    # Check if this instance is better then best
    sumValue = calcValue(value, useList)
    if (sumValue > best[0]):
        # Save it
        best[0] = sumValue
        best.pop()
        best.append(useList.copy())
    
    # Count calls
    best[1] += 1

    # Recursive calls
    useList.append(False) # False
    bb_knapsackAlg(value, weight, c, useList, best)
    useList.pop()
    useList.append(True) # True
    bb_knapsackAlg(value, weight, c, useList, best)
    useList.pop()
    pass

# Recusive base
def bb_knapsack(value, weight, c):
    best = [0, 1, []] # List of save values
    # Start Recursive calls
    bb_knapsackAlg(value, weight, c, [], best)
    # Add non used itens to the list
    while (len(best[2]) < len(value)):
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
        output = bb_knapsack(values[i], weights[i], c[i])
        print("Best Value: ", output[0])
        print("Use List: ", output[2])
        print("Number of recursive calls: (", output[1], "/", pow(2, len(values[i])), ")")
        print()