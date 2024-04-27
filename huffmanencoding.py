import heapq

class HuffmanNode:
    
    def __init__(self, symbol, frequency, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right
        #tree direction
        self.huff = ''
        
    def __lt__(self, next):
        return self.frequency < next.frequency
 
class HuffmanTree:
     
    def convert_into_huffman_nodes(self, heap, char_array, freq_array):
        for index in range(len(char_array)):
            heapq.heappush(heap, HuffmanNode(char_array[index], freq_array[index]))
            
    def build_huffman_tree(self, heap):
        while(len(heap) > 1):
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            
            #direction for encode
            left.huff = '0'
            right.huff = '1'
            
            newnode = HuffmanNode(left.symbol+right.symbol, left.frequency+right.frequency, left=left, right=right)
            heapq.heappush(heap, newnode)
   
    def printEncoding(self, node, val=''):
        newVal = val + node.huff
        
        if(node.left):
            self.printEncoding(node.left, newVal)
        if(node.right):
            self.printEncoding(node.right, newVal)
            
        if node.left == None and node.right == None:
            print(f"{node.symbol}: {newVal}")
        

if __name__ == '__main__':
    chars = ['a', 'b', 'c', 'd', 'e', 'f'] 
    freq = [5, 9, 12, 13, 16, 45]
    
    nodes = []
    obj = HuffmanTree()
    obj.convert_into_huffman_nodes(nodes, chars, freq)
    obj.build_huffman_tree(nodes)
    obj.printEncoding(nodes[0], '')


"""
Output:
f: 0
c: 100
d: 101
a: 1100
b: 1101
e: 111
"""
