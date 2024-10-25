class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isValid(root, left=None, right=None):
    if root is None:
        return True
    if left is not None and root.data <= left.data:
        return False
    if right is not None and root.data >= right.data:
        return False
    return isValid(root.left, left, root) and isValid(root.right, root, right)

# Create the binary tree
root = Node(10)
root.left = Node(8)
root.right = Node(19)

# Check if it's a valid BST
if isValid(root):
    print("Valid BST")
else:
    print("Invalid BST")
