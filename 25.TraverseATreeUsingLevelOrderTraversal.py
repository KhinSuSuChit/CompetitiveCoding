class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Create the tree
root = Node(1)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)

print("Level order traversal of the BST is:", end=" ")
level_order(root)
