class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left_view(root, level=1):
    global max_level
    if root is None:
        return
    if max_level < level:
        print(root.data, end=" ")
        max_level = level
    left_view(root.left, level + 1)
    left_view(root.right, level + 1)

# Example Usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.right.left = Node(7)
root.left.right.right = Node(8)

max_level = 0
print("Left view of the tree:", end=" ")
left_view(root)
