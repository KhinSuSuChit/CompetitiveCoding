class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

def merge_sorted_linked_lists(head1, head2):
    dummy_head = Node(None)
    curr = dummy_head
    while head1 and head2:
        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    curr.next = head1 or head2
    return dummy_head.next

def merge_linked_lists(head1, head2):
    dummy_head = Node(None)
    curr = dummy_head
    while head1 and head2:
        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    curr.next = head1 or head2
    return dummy_head.next

def sort_linked_list(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sort_linked_list(head)
    right = sort_linked_list(mid)
    return merge_sorted_linked_lists(left, right)

# Create and populate two linked lists
head1 = None
head1 = insert_at_end(head1, 5)
head1 = insert_at_end(head1, 10)
head1 = insert_at_end(head1, 2)
head1 = insert_at_end(head1, 8)

head2 = None
head2 = insert_at_end(head2, 3)
head2 = insert_at_end(head2, 1)
head2 = insert_at_end(head2, 9)
head2 = insert_at_end(head2, 7)

# Sort the linked lists
head1 = sort_linked_list(head1)
head2 = sort_linked_list(head2)

# Print the sorted linked lists
print("Linked List 1:", end=" ")
print_linked_list(head1)

print("Linked List 2:", end=" ")
print_linked_list(head2)

# Merge the sorted linked lists and print the result
merged_head = merge_linked_lists(head1, head2)
print("Merged Linked List:", end=" ")
print_linked_list(merged_head)
