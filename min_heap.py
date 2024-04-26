#BestCase= O(n) And Aerage case/ worst case = O(nlogn)
class MinHeap:
    
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0]*self.maxsize
        self.heap[0] = 0
        self.Front = 0
        
    def parent(self, pos):
        #Get Parent
        return (pos-1)//2
        
    def isleaf(self, pos):
        #Check if leaf node
        return 2*pos >= self.size
        
    def swap(self, po1, po2):
        self.heap[po1], self.heap[po2] = self.heap[po2], self.heap[po1]
        
    def minheapify(self, pos):
        left = 2 * pos + 1
        right = 2 * pos + 2
        smallest = pos
       
        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != pos:
            self.swap(pos, smallest)
            self.minheapify(smallest)
            
    def insert(self, item):
        if(self.size > self.maxsize):
            return
        
        self.heap[self.size] = item
        current = self.size
        self.size+=1
        
        while(current > 0 and self.heap[current] < self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
        
    def minheap(self):
        for pos in range(self.size//2, 0, -1):
            self.minheapify(pos)
        
    def remove(self):
        elem = self.heap[self.Front]
        self.heap[self.Front] = self.heap[self.size-1]
        self.minheapify(self.Front)
        self.size-=1
        return elem
        
array = [8, 90, 70, 20, 4, 5, 3, 2, 1]
obj = MinHeap(len(array))
for i in range(len(array)):
    obj.insert(array[i])

while(obj.size >=1):
    print(obj.remove())
