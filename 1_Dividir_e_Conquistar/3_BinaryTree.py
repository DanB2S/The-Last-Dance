class Node:
    def __init__(self, data):
        self.left = None  # Left node
        self.right = None # Right node
        self.data = data  # Data
        pass
    
    def insert(self, data):
        # If data < node.data, add data to left side
        if (data < self.data):
            if (self.left == None): # If left is None
                self.left = Node(data) # Create
            else:
                self.left.insert(data) # Else left recursive insert
        # Else data > node.data, add data to right side
        else:
            if (self.right == None): # If right is None
                self.right = Node(data) # Create
            else:
                self.right.insert(data) # Else right recursive insert
        pass
    
    def printPreOrder(self):
        print(self.data, end=" ") # Print first
        if (self.left != None):
            self.left.printPreOrder() # Recursive Left 
        if (self.right != None):
            self.right.printPreOrder() # Recursive Right
        pass
    
    def printPosOrder(self):
        if (self.left != None): # Recursive Left 
            self.left.printPosOrder()
        if (self.right != None): # Recursive Right
            self.right.printPosOrder()
        print(self.data, end=" ") # Print Last
        pass
    
    def printInOrder(self):
        if (self.left != None): # Recursive Left
            self.left.printInOrder()
        print(self.data, end=" ") # Print 
        if (self.right != None): # Recursive Right
            self.right.printInOrder()
        pass

if __name__ == "__main__":
    
    test_1 = [9, 3, 0, 5, 2, 6, 4, 7, 8, 1]
    test_2 = [12, 6, 19, 10, 14, 5, 2, 0, 16, 15, 11, 13, 7, 1, 17, 9, 4, 3, 8, 18]
    test_3 = [23, 13, 7, 0, 20, 25, 26, 18, 16, 24, 29, 3, 19, 1, 2, 17, 27, 14, 9, 4, 11, 28, 5, 21, 15, 22, 6, 10, 12, 8]

    root_1 = Node(test_1[0])
    for i in range(1, len(test_1)):
        root_1.insert(test_1[i])
    
    root_2 = Node(test_2[0])
    for i in range(1, len(test_2)):
        root_2.insert(test_2[i])
    
    root_3 = Node(test_3[0])
    for i in range(1, len(test_3)):
        root_3.insert(test_3[i])
    
    print("Test 1:")
    print("In Order: ", end="")
    root_1.printInOrder()
    print()
    print("Pre Order: ", end="")
    root_1.printPreOrder()
    print()
    print("Pos Order: ", end="")
    root_1.printPosOrder()
    print()
    print()
    
    print("Test 2:")
    print("In Order: ", end="")
    root_2.printInOrder()
    print()
    print("Pre Order: ", end="")
    root_2.printPreOrder()
    print()
    print("Pos Order: ", end="")
    root_2.printPosOrder()
    print()
    print()
    
    print("Test 3:")
    print("In Order: ", end="")
    root_3.printInOrder()
    print()
    print("Pre Order: ", end="")
    root_3.printPreOrder()
    print()
    print("Pos Order: ", end="")
    root_3.printPosOrder()
    print()
    print()