"""
Question 9: Implement lossless compression techniques (e.g., Huffman coding) and lossy compression
techniques (e.g., JPEG compression) using Python.
"""

from collections import Counter
import heapq

class Node:
    """Node class for Huffman tree construction"""
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def make_tree(text):
    """
    Build Huffman tree from input text.
    Args:
        text: Input string to compress
    Returns:
        Root node of Huffman tree
    """
    freq = Counter(text)
    heap = [Node(c, f) for c, f in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = Node(None, a.freq + b.freq, a, b)
        heapq.heappush(heap, merged)
    
    return heap[0]

def make_code(node, code="", codes=None):
    """
    Generate Huffman codes by traversing the tree.
    Args:
        node: Current node in tree
        code: Current code string
        codes: Dictionary to store codes
    Returns:
        Dictionary mapping characters to their Huffman codes
    """
    if codes is None:
        codes = {}
    
    if node.char is not None:
        codes[node.char] = code
    else:
        make_code(node.left, code + "0", codes)
        make_code(node.right, code + "1", codes)
    
    return codes

def encode(text, codes):
    """
    Encode text using Huffman codes.
    Args:
        text: Input text to encode
        codes: Dictionary of character to code mappings
    Returns:
        Encoded binary string
    """
    return "".join(codes[c] for c in text)

def decode(encoded, tree):
    """
    Decode binary string using Huffman tree.
    Args:
        encoded: Encoded binary string
        tree: Root node of Huffman tree
    Returns:
        Decoded original text
    """
    node = tree
    out = ""
    for bit in encoded:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            out += node.char
            node = tree
    return out

# Example usage
text = "hello huffman"
tree = make_tree(text)
codes = make_code(tree)
encoded = encode(text, codes)
decoded = decode(encoded, tree)

print("Original :", text)
print("Encoded :", encoded)
print("Decoded :", decoded)

