import heapq
import sys

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(self.V)]
        
    def addEdge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        
    def shortestPath(self, src: int):
        heap = []
        heapq.heappush(heap, (0, src))
        
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        
        while heap:
            d, u = heapq.heappop(heap)
            
            for v, weight in self.adj[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(heap, (dist[v], v))
                    
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")
        
# Driver's code
if __name__ == "__main__":
    V = 9
    obj = Graph(V)
 
    obj.addEdge(0, 1, 4)
    obj.addEdge(0, 7, 8)
    obj.addEdge(1, 2, 8)
    obj.addEdge(1, 7, 11)
    obj.addEdge(2, 3, 7)
    obj.addEdge(2, 8, 2)
    obj.addEdge(2, 5, 4)
    obj.addEdge(3, 4, 9)
    obj.addEdge(3, 5, 14)
    obj.addEdge(4, 5, 10)
    obj.addEdge(5, 6, 2)
    obj.addEdge(6, 7, 1)
    obj.addEdge(6, 8, 6)
    obj.addEdge(7, 8, 7)
 
    obj.shortestPath(0)
