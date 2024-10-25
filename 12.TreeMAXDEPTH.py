class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def MXDepth(root):
    if root is None:
        return 0
    else:
        LD = MXDepth(root.left)
        RD = MXDepth(root.right)
        return max(LD, RD) + 1

# Create the binary tree
Root = Node(6)
Root.left = Node(2)
Root.right = Node(3)
Root.left.left = Node(4)
Root.left.right = Node(9)
Root.right.left = Node(7)

# Print the maximum depth of the tree
print(MXDepth(Root), "is the depth of the tree.")
