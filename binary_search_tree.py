# developed by Jones

# START
# in this binary search tree, there are four functions:
# function for adding an item to the tree; "adding_item()"
# function for finding an item in the tree; "finding_item()"
# function to determine the maximum value in the tree; "finding_maximum_value()"
# function to determine the depth/height of the tree; "finding_depth_of_the_tree()"
 

class binary_search_tree:
    
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value

    def adding_item(self, value):
        # check if there is no root.
        if not self.value:
            self.value = value 
            return
        # check where to add an item.

        else:  
            # to check if the value been inserted is less than the current Node's value. 
            if value < self.value:

                # checks if there is a left node to the current Node, if true then the code recurse.
                if self.left:
                    self.left.adding_item(value)
                    return
                # insert to the left of currentNode when currentNode.left = None.  
                self.left = binary_search_tree(value)    
                return
            # to check if the value been inserted is greater than the current Node's value.  

            else:  
                 # checks if there is a right node to the current Node, if true then the code recurse.
                if self.right:
                    self.right.adding_item(value)
                    return
                 # insert to the right of currentNode when currentNode.right = None. 
                self.right = binary_search_tree(value)            

    def finding_item( self, value):
        # checks if the value equals the parent node.
        if value == self.value:
           return True  
        # checks if the value is less than the parent Node value.
        if value < self.value:
            # checks if the left node exists.
            if self.left == None:
                return False
            # The finding_item function is repeated on the left Node to check for the value been checked.    
            return self.left.finding_item(value)

        else:
            # checks if the right node exists.
            if self.right == None:
                return False
            # The finding_item function is repeated on the right Node to check for the value been searched.
            return self.right.finding_item(value)        

    def finding_maximum_value(self):
        current = self
        # finds the right most leaf in the tree, since its the lagest value.
        while current.right is not None:
            current = current.right
        return current.value

    def finding_depth_of_the_tree(self):
        # checks if both child Nodes exists, if not return 1
        if self.left == None and self.right == None:
            return 1

        # checks if the left child node exists, if not the finding_depth method 
        # is applied on the right Node. 
        elif self.left == None:
            return self.right.finding_depth_of_the_tree() + 1 # plus the parent node

        # checks if the right child node exists, if not the finding_depth method
        # is applied on the left Node.
        elif self.right == None:
            return self.left.finding_depth_of_the_tree() + 1 # plus the parent node

        else:
            # counts the number of levels from the parent to the deepest leaf.
            return max(self.left.finding_depth_of_the_tree(), self.right.finding_depth_of_the_tree()) + 1 


# Driver program to test the above functions
root = binary_search_tree(10)
root.adding_item(12)
root.adding_item(5)
root.adding_item(4)  
root.adding_item(20)
root.adding_item(8)
root.adding_item(7) 
root.adding_item(15)
root.adding_item(13)
print(root.finding_item(3))
print(root.finding_item(15))
print(root.finding_maximum_value())
print(root.finding_depth_of_the_tree())

# The implemented tree
#       10
#      /  \
#     5    12
#    / \   / \
#   4   8     20
#      / \    / \
#     7      15
#            / \
#           13

# END


# COMPLEXITY ANALYSIS
# In the binary search tree, the time complexity is of O(log(n)) for  adding_item, finding_item,
# finding_maximum_value and finding_depth_of_the_tree methods, where n is the number of nodes
#  in the tree.

# The space complexity of all the operations above, is O(n). n is the number of nodes in 
# the tree
#
