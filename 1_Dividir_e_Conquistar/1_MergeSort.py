def merge(array, l, m, u):
    
    i = l # Start of left side
    j = m + 1 # Start of right side

    sortarry = [] # Aux array
    for _ in range(l, u + 1): # For each value
        # if right index < upper boundary 
        # and left index value < right index value
        # and left index < middle boundary
        if (j <= u and array[i] <= array[j] and i < m + 1):
            sortarry.append(array[i]) # Append left side value
            i += 1
        # Else right index < upper boundary 
        elif (j <= u):
            sortarry.append(array[j]) # Append right side value
            j += 1
        # This is need if the right side finnish
        else:
            sortarry.append(array[i]) # Append left side value
            i += 1

    for k, a in enumerate(range(l, u + 1)):
        array[a] = sortarry[k]

def mergeSortAlg(array, l, u):
    
    if (l == u): # If l == u, the array has size 1
        return
    
    m = (l + u) // 2 # array mid

    mergeSortAlg(array, l, m) # Left array
    mergeSortAlg(array, m + 1, u) # Right array
    merge(array, l, m, u) # Merge both side
        
def mergeSort(array):
    mergeSortAlg(array, 0, len(array) - 1)

if __name__ == "__main__":
    
    test_1 = [9, 3, 0, 5, 2, 6, 4, 7, 8, 1]
    test_2 = [12, 6, 19, 10, 14, 5, 2, 0, 16, 15, 11, 13, 7, 1, 17, 9, 4, 3, 8, 18]
    test_3 = [23, 13, 7, 0, 20, 25, 26, 18, 16, 24, 29, 3, 19, 1, 2, 17, 27, 14, 9, 4, 11, 28, 5, 21, 15, 22, 6, 10, 12, 8]

    mergeSort(test_1)
    mergeSort(test_2)
    mergeSort(test_3)

    print(test_1)
    print(test_2)
    print(test_3)