
import sys
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.G = [[0 for column in range(vertices)]
                  for row in range(vertices)]
          
    def minKey(self, key, mstSet):
        min = sys.maxsize
        min_index = None
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index       
    
    def prim_mst(self):
        
        key =[sys.maxsize]*self.V
        mstSet = [False]*self.V
        
        key[0] = 0 #start from first vertex
        parent = [None]*self.V
        parent[0] = -1
        
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            
            mstSet[u] = True
            
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and\
                key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    
        self.print_data(parent)

    def print_data(self, parent):
        print("Edge  Weight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "  ", self.graph[i][parent[i]])
    
# Driver's code
if __name__ == '__main__':
    obj = Graph(5)
    obj.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]
 
    obj.prim_mst()  
