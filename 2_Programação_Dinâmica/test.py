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

def greedKnapsack(value, weight, c):

    domain = [0, 1]
    L = [[0], [1]]
    best = 0
    bestL = None

    while(L):
        aux = L.pop()
        #print (aux, values)
        if (len(aux) == len(value)):
            if (checkCapacity(weight, aux, c)):
                val = calcValue(value, aux)
                if (best < val):
                    best = val
                    bestL = aux.copy()
        else:
            for d in domain:
                L.append(aux + [d])

    return best, bestL

if __name__ == "__main__":

    print(checkCapacity([10, 20, 30, 25, 15, 22, 12, 8, 18, 17, 10, 12], 
                        [True, True, False, False, True, False, True, True, False, False, True, False], 
                        75))

    
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
        output = greedKnapsack(values[i], weights[i], c[i])
        print("Best Value: ", output)#[0])
        #print("Use List: ", output[2])
        #print("Number of recursive calls: (", output[1], "/", pow(2, len(values[i])), ")")
        #print()
    