class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        node = self.table[index]
        
        if node is None:
            self.table[index] = HashNode(key, value)
            self.size += 1
        else:
            prev = None
            while node is not None:
                if node.key == key:
                    node.value = value  # Update existing key
                    return
                prev = node
                node = node.next
            prev.next = HashNode(key, value)  # Add to the end of the chain
            self.size += 1

    def delete(self, key):
        index = self._hash(key)
        node = self.table[index]
        prev = None
        while node is not None:
            if node.key == key:
                if prev is None:  # Deleting the head node
                    self.table[index] = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return True  # Key found and deleted
            prev = node
            node = node.next
        return False  # Key not found

    def search(self, key):
        index = self._hash(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value  # Key found
            node = node.next
        return None  # Key not found

    def __repr__(self):
        output = []
        for i, node in enumerate(self.table):
            chain = []
            while node is not None:
                chain.append(f"{node.key}: {node.value}")
                node = node.next
            output.append(f"Bucket {i}: " + " -> ".join(chain) if chain else f"Bucket {i}: Empty")
        return "\n".join(output)

# Example usage
hash_table = HashTable()
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 30)
hash_table.insert("banana", 50)  # Update the value for "banana"

print("Search apple:", hash_table.search("apple"))  # Output: 10
print("Search banana:", hash_table.search("banana"))  # Output: 50

hash_table.delete("orange")

print("\nHash Table:")
print(hash_table)
