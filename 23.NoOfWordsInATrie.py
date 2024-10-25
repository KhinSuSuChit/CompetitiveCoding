class TrieNode:
    def __init__(self):
        self.children = {}  # A dictionary to hold the children of this node
        self.is_end_of_word = False  # True if the node represents the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root of the Trie

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True  # Mark the end of the word

    def count_words(self):
        return self._count_words_recursive(self.root)

    def _count_words_recursive(self, node):
        count = 0
        if node.is_end_of_word:
            count += 1
        for child_node in node.children.values():
            count += self._count_words_recursive(child_node)
        return count

if __name__ == "__main__":
    trie = Trie()
    
    # Insert words into the Trie
    words = ["apple", "app", "banana", "bat", "ball", "batman"]
    for word in words:
        trie.insert(word)

    # Count the number of words in the Trie
    print(f"Number of words in the Trie: {trie.count_words()}")
