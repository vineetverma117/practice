import sys
class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.G = [[0 for column in range(self.V)]
                  for row in range(self.V)]
                  
    def minDistance(self, key, sptSet):
        min_val = sys.maxsize
        min_index = None
        
        for v in range(self.V):
            if key[v] < min_val and sptSet[v] == False:
                min_val = key[v]
                min_index = v
        return min_index
        
    def dijkstra_spt(self, source):
        
        key = [sys.maxsize]*self.V #storing distance
        sptSet = [False]* self.V
        parent = [None] * self.V #This only need if you want to print path
        
        key[source] = 0
        
        for cout in range(self.V):
            u = self.minDistance(key, sptSet)
            
            sptSet[u] = True
            
            for v in range(self.V):
                if self.G[u][v] > 0 and sptSet[v] == False and \
                key[v] > key[u] + self.G[u][v]:
                    key[v] = key[u] + self.G[u][v]
                    parent[v] = u #only needed if you want to print path
        
        self.print_spt(source, key)
        self.print_path(parent)
        
    def print_spt(self, source, key):
        print("vertes distance from:")
        for v in range(self.V):
            print(f" {source} ---> {v}: {key[v]}")
            
    def print_path(self, parent):
        for i in range(1, self.V):
            print(f" {parent[i]} --> {i}")


if __name__ == '__main__':
    obj = Graph(9)
    obj.G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
 
    obj.dijkstra_spt(0)
