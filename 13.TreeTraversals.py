class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Inorder(root):
    # Left - Root - Right
    if root:
        Inorder(root.left)
        print(root.data, end=" --> ")
        Inorder(root.right)

def Preorder(root):
    # Root - Left - Right
    if root:
        print(root.data, end=" --> ")
        Preorder(root.left)
        Preorder(root.right)

def Postorder(root):
    # Left - Right - Root
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data, end=" --> ")

# Create the binary tree
Root = Node(6)
Root.left = Node(2)
Root.right = Node(3)
Root.left.left = Node(4)
Root.left.right = Node(9)
Root.right.left = Node(7)

# Perform traversals
print("Inorder:")
Inorder(Root)
print("None\n")

print("Preorder:")
Preorder(Root)
print("None\n")

print("Postorder:")
Postorder(Root)
print("None\n")
