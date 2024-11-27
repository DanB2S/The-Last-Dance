# Try to find a possible solution for the next queen
def findProxPos(pos, start, n, i):
    if (start >= n):
        return -1
    for j in range(start, n):
        can = True
        # Horizontal
        for p in pos:
            if j == p[1]:
                can = False
        # Diagonal
        for p in pos:
            # Right
            if (p[0] + j == p[1] + i):
                can = False
            # Left
            if (p[0] - j == -(p[1] - i)):
                can = False
        if (can):
            return j
    return -1

# Backtrack
def backtrack(pos, n, i):
    # While there is queens to remove
    while (len(pos) > 0):
        aux = pos.pop() # Remove the last
        i -= 1 # Try to find
        nextpos = findProxPos(pos, aux[1] + 1, n, i)
        if nextpos != -1:
            pos.append((i, nextpos))
            return aux[0] + 1

def nQueens(n):

    # Start position
    pos = [(0, 0)]
    i = 1 # Pos trying to find

    # While all the queen not been placed
    while (len(pos) < n):
        # Try to find next position
        nextPos = findProxPos(pos, 0, n, i)
        if nextPos != -1: # If is possible
            pos.append((i, nextPos)) # Add queen position
            i += 1 # Try next queen
        else: # If is impossible
            i = backtrack(pos, n, i) # Backtrack the positions

    return pos


# Print the table with the answer
def drawTable(pos, n):
    print()
    for i in range(n):
        for j in range(n):
            hasQ = False
            for p in pos:
                if (p[0] == i and p[1] == j):
                    hasQ = True
            if (hasQ):
                print("|Q", end='')
            else:
                print("| ", end='')
            if (j == n-1):
                print("|", end='')
        print()
    print()

if __name__ == "__main__":

    drawTable(nQueens(4), 4)
    drawTable(nQueens(8), 8)
    drawTable(nQueens(10), 10)