class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left_boundary(root):
    if root:
        if root.left:
            print(root.data, end=" ")
            left_boundary(root.left)
        elif root.right:  # Include the case where left is None but right exists
            print(root.data, end=" ")
            left_boundary(root.right)

def right_boundary(root):
    if root:
        if root.right:
            right_boundary(root.right)
            print(root.data, end=" ")
        elif root.left:  # Include the case where right is None but left exists
            right_boundary(root.left)
            print(root.data, end=" ")

def leaf_boundary(root):
    if root:
        if root.left:  # Traverse left subtree
            leaf_boundary(root.left)
        if root.left is None and root.right is None:  # Leaf node
            print(root.data, end=" ")
        if root.right:  # Traverse right subtree
            leaf_boundary(root.right)

def print_boundary(root):
    if root:
        print(root.data, end=" ")  # Print the root
        left_boundary(root.left)  # Print left boundary
        leaf_boundary(root.left)   # Print leaves in the left subtree
        leaf_boundary(root.right)  # Print leaves in the right subtree
        right_boundary(root.right)  # Print right boundary

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Print the boundary order traversal
print("Boundary order traversal is:", end=" ")
print_boundary(root)
