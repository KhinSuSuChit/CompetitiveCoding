class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(head1, head2):
    dummy = Node(None)
    tail = dummy
    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    # Connect the remaining nodes
    tail.next = head1 if head1 else head2
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.data, end=" --> ")
        head = head.next
    print("None")

# Create first linked list
node1 = Node(5)
node2 = Node(2)
node3 = Node(3)
node4 = Node(6)
node5 = Node(7)
node6 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print("Linked List 1:")
print_linked_list(node1)

# Create second linked list
node7 = Node(15)
node8 = Node(12)
node9 = Node(13)
node10 = Node(16)
node11 = Node(17)
node12 = Node(11)

node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node12

print("Linked List 2:")
print_linked_list(node7)

# Merge the two sorted linked lists
merged_head = merge_sorted_lists(node1, node7)

# Print the merged linked list
print("Merged linked lists:")
print_linked_list(merged_head)
