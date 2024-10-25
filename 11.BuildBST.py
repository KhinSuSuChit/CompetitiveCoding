class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def Inorder(root, result=[]):
    if root:
        Inorder(root.left, result)
        result.append(root.data)
        Inorder(root.right, result)
    return result

# Create a list of values to insert into the BST
l = [1, 2, 3]
root = None

# Insert values into the BST
for i in l:
    root = insert(root, i)

# Print inorder traversal of the BST
print("Inorder traversal of the BST:")
inorder(root)
print()

# Check if the tree is a Binary Search Tree (BST)
if l == sorted(Inorder(root)):
    print("The tree is a Binary Search Tree (BST).")
else:
    print("The tree is not a Binary Search Tree (BST).")
