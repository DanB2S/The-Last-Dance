
def checkCapacity(weight, useList, c):
    w_sum = 0
    for i in range(len(useList)):
        if (useList[i]):
            w_sum += weight[i]
    return c > w_sum

def calcValue(value, useList):
    v_sum = 0
    for i in range(len(useList)):
        if (useList[i]):
            v_sum += value[i]
    return v_sum

def bb_knapsackAlg(value, weight, c, useList, best):
    if (not checkCapacity(weight, useList, c) or 
        len(useList) >= len(value)):
        return
    if (calcValue(value, useList) > best):
        best = calcValue(value, useList)
    useList.append(False)
    bb_knapsackAlg(value, weight, c, useList, best)
    useList.pop()
    useList.append(True)
    bb_knapsackAlg(value, weight, c, useList, best)
    useList.pop()
    pass

def bb_knapsack(value, weight, c):
    best = 0
    output = []
    bb_knapsackAlg(value, weight, c, output, best)
    return best, output


if __name__ == "__main__":

    value = [6, 4, 3, 7, 8, 1, 3, 5, 7, 5]
    weight = [3, 6, 9, 4, 6, 4, 8, 6, 5, 7]
    c = 25

    print(bb_knapsack(value, weight, c))