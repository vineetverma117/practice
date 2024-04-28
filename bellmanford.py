import sys
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = []
    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        
        
    def BellmanFord(self, src):
        
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        
        parent = [None]*self.V #only if you want to print path
        
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    
        for u, v, w in self.graph:
            if dist[u] != sys.maxsize and dist[u] + w < dist[v]:
                print("negative cycle")
                return
            
        self.print_data(dist)
            
    def print_data(self, dist):
        for i in range(self.V):
            print("{0}--->{1}".format(i, dist[i]))
        
if __name__ == '__main__':
    obj = Graph(5)
    obj.addEdge(0, 1, -1)
    obj.addEdge(0, 2, 4)
    obj.addEdge(1, 2, 3)
    obj.addEdge(1, 3, 2)
    obj.addEdge(1, 4, 2)
    obj.addEdge(3, 2, 5)
    obj.addEdge(3, 1, 1)
    obj.addEdge(4, 3, -3)

    # function call
    obj.BellmanFord(0)
