from collections import Counter
import heapq
class Node:
    def __init__(self,char,freq,left=None,right=None):
        self.char=char
        self.freq=freq
        self.left=left
        self.right=right
    def __lt__(self,other):
        return self.freq < other.freq
def make_tree(text):
    freq=Counter(text)
    heap=[Node(c, f) for c, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        a=heapq.heappop(heap)
        b=heapq.heappop(heap)
        merged=Node(None, a.freq + b.freq, a, b)
        heapq.heappush(heap, merged)
    return heap[0]
def make_code(node, code="", codes=None):
    if codes is None:
        codes={}
    if node.char is not None:
        codes[node.char]=code
    else:
        make_code(node.left, code+"0", codes)
        make_code(node.right, code+"1", codes)
    return codes
def encode(text,codes):
    return "".join(codes[c] for c in text)
def decode(encoded, tree):
    node=tree
    out=""
    for bit in encoded:
        node=node.left if bit=="0" else node.right
        if node.char is not None:
            out+=node.char
            node=tree
    return out
text="hello huffman"
tree=make_tree(text)
codes=make_code(tree)
encoded=encode(text,codes)
decoded=decode(encoded,tree)
print("Original :",text)
print("Encoded :",encoded)
print("Decoded :",decoded)
