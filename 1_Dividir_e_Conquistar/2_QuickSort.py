def quickSortAlg(array, l, u):

    # If lower boundary >= upper boundary
    if (l >= u):
        return

    pivo = u  # Pivo = last value
    i = l - 1 # i = first - 1
    j = l     # j = first

    while (j < pivo): # While j < pivo
        # if j value greater then pivo, ignore
        if (array[j] >= array[pivo]): 
            j += 1
        # if j value less then pivo, switch
        else:
            i += 1 
            array[j], array[i] = array[i], array[j]
            j += 1 
    
    
    i += 1 # Pivo value position = i + 1
    array[pivo], array[i] = array[i], array[pivo]

    # Call quick sort to left side
    quickSortAlg(array, l, i - 1)
    # Call quick sort to right side
    quickSortAlg(array, i + 1, u)

def quickSort(array):
    quickSortAlg(array, 0, len(array) - 1)


if __name__ == "__main__":
    
    test_1 = [9, 3, 0, 5, 2, 6, 4, 7, 8, 1]
    test_2 = [12, 6, 19, 10, 14, 5, 2, 0, 16, 15, 11, 13, 7, 1, 17, 9, 4, 3, 8, 18]
    test_3 = [23, 13, 7, 0, 20, 25, 26, 18, 16, 24, 29, 3, 19, 1, 2, 17, 27, 14, 9, 4, 11, 28, 5, 21, 15, 22, 6, 10, 12, 8]

    quickSort(test_1)
    quickSort(test_2)
    quickSort(test_3)

    print(test_1)
    print(test_2)
    print(test_3)