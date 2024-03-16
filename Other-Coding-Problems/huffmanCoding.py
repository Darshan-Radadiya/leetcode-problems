import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if(other is None):
            return False
        if(not isinstance(other, Node)):
            return False
        return self.freq == other.freq

# Function to build Huffman tree with frequency input
def build_huffman_tree_with_frequency(frequency_dict):
    heap = [Node(char, freq) for char, freq in frequency_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

# Function to encode the characters
def encode(root, string, huffman_code):
    if root is None:
        return

    if root.char is not None:
        huffman_code[root.char] = string
        return

    encode(root.left, string + "0", huffman_code)
    encode(root.right, string + "1", huffman_code)

# Function to perform Huffman Coding with frequency input
def huffman_coding_with_frequency(frequency_dict):
    root = build_huffman_tree_with_frequency(frequency_dict)
    huffman_code = {}
    encode(root, "", huffman_code)
    return huffman_code

# Example usage with frequency input
frequency_data = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45} # {'f': '0', 'c': '100', 'd': '101', 'a': '1100', 'b': '1101', 'e': '111'}
frequency_data = {'b': 1, 'c': 6, 'a': 5, 'd': 3} # {'c': '0', 'b': '100', 'd': '101', 'a': '11'}
frequency_data = {'a': 10, 'e':15, 'i':12, 'o':3, 'u':4, 's':13, 't':1} # {'i': '00', 's': '01', 'e': '10', 'u': '1100', 't': '11010', 'o': '11011', 'a': '111'}
huffman_code_frequency = huffman_coding_with_frequency(frequency_data)

# Output Huffman Codes for the frequency data
print(huffman_code_frequency)
