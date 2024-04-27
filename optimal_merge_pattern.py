import heapq
class FileNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
    
    def __lt__(self, next):
        return self.item < next.item

class OptimalMergePattern:
    
    def build_min_heap(self, array, heap):
        for item in array:
            heapq.heappush(heap, FileNode(item))
        
    def build_min_heap_tree(self, heap):
        while(len(heap) > 1):
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            
            newNode = FileNode(left.item+right.item, left=left, right=right)
            heapq.heappush(heap, newNode)
            
    def get_total_computation(self, node, total=0):
        #count internal node
        if(node.left or node.right):
            if node.left:
                total1 = self.get_total_computation(node.left, total)
            if node.right:
                total2 = self.get_total_computation(node.right, total)
            return  total + node.item + total1 + total2   
        else:
            return 0

    def traverse_tree(self, node):
        if(node):
            print(f"node: {node.item}")
        if node.left:
            self.traverse_tree(node.left)
        if node.right:
            self.traverse_tree(node.right)

if __name__ == '__main__':
    array = [2, 3, 4, 5, 6, 7]
    heap = []
    obj = OptimalMergePattern()
    obj.build_min_heap(array, heap)
    obj.build_min_heap_tree(heap)
    print(obj.get_total_computation(heap[0], 0))
