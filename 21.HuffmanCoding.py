import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char          # Character
        self.freq = freq          # Frequency of the character
        self.left = None          # Left child (for 0)
        self.right = None         # Right child (for 1)

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def build_huffman_tree(char_freq):  
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(node, current_code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
        return
    generate_huffman_codes(node.left, current_code + "0", codes)
    generate_huffman_codes(node.right, current_code + "1", codes)

def huffman_encode(data, codes):
    encoded_data = ''.join([codes[char] for char in data])
    return encoded_data

def huffman_decode(encoded_data, root):
    decoded_string = []
    current_node = root

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_string.append(current_node.char)
            current_node = root
            
    return ''.join(decoded_string)

def huffman_coding(data):
    char_freq = Counter(data)
    root = build_huffman_tree(char_freq)
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)
    encoded_data = huffman_encode(data, huffman_codes)
    return encoded_data, huffman_codes, root

if __name__ == "__main__":
    data = "huffman coding in python"
    print(f"Original Data: {data}")
    encoded_data, huffman_codes, root = huffman_coding(data)
    print(f"Encoded Data: {encoded_data}")
    print(f"Huffman Codes: {huffman_codes}")
    decoded_data = huffman_decode(encoded_data, root)
    print(f"Decoded Data: {decoded_data}")
