class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def swap_pairs(self):
        temp = self.head
        while temp and temp.next:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")

# Create a linked list
l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)

print("Linked list before swapping pairs:")
l.print_list()

l.swap_pairs()

print("Linked list after swapping pairs:")
l.print_list()
