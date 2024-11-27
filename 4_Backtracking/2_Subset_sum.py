# Recursive Algorithm
def subsetAlg(A, i, subset, d, output):
    # If sum subset == target
    if (sum(subset) == d):
        output.append(subset.copy()) # Append answer
        return # Not need to continue
    # If i greater then len of numbers
    # or sum subset greater then target
    if (i >= len(A) or sum(subset) > d):
        return # Invalid solution dont need to continue
    
    # Try solutions without actual number
    subsetAlg(A, i+1, subset, d, output)
    
    # Try solutions with actual number
    subset.append(A[i]) 
    subsetAlg(A, i+1, subset, d, output)

    # After try, pop it
    subset.pop()

# Recursive start
def subset_sum(A, d):
    output = []
    subsetAlg(A, 0, [], d, output)
    return output
    
if __name__ == "__main__":

    print()
    print(subset_sum([1, 2, 5, 6, 8], 9))
    print()
    print(subset_sum([3, 5, 6, 7], 15))
    print()
    print(subset_sum([5, 10, 12, 13, 15, 18], 30))
    print()
    print(subset_sum([1, 3, 6, 8, 10, 15, 20, 25, 30, 40], 58))
    print() 