class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

# Example usage:
hash_table = HashTable(10)

# Inserting key-value pairs
hash_table.insert("apple", 5)
hash_table.insert("banana", 10)
hash_table.insert("orange", 15)

# Retrieving values
print("Value for 'apple':", hash_table.search("apple"))
print("Value for 'banana':", hash_table.search("banana"))
print("Value for 'orange':", hash_table.search("orange"))
