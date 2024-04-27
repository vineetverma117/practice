class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.G = []
        
    def addEdge(self, u, v, w):
        self.G.append([u, v, w])
        
    #cycle detection based on disjoint set
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
        
    def union(self, u, v, rank, parent):
        if rank[u] < rank[v]:
            rank[u] = rank[v]
            parent[u] = v
        elif rank[v] < rank[u]:
            rank[v] = rank[u]
            parent[v] = u
        else:
            #if both of have same rank. make one parent and increase rank
            parent[u] = v
            rank[v] +=1
            
    def kruskal_mst(self):
        result = []
        i = 0 #track sorted edges
        e = 0 #track spanning tree edges, max could be v-1
        
        self.G = sorted(self.G, key= lambda x: x[2]) #sorting based on weight in increasing order
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        while e < self.V-1:
            u, v, w = self.G[i]
            
            urep = self.find(parent, u)
            vrep = self.find(parent, v)
            
            if urep != vrep:
                e +=1
                result.append(self.G[i])
                self.union(u, v, rank, parent)
            i += 1
            
        print(f" number of edges: {len(result)}") 
        minimum_cost = 0
        for u, v, w in result:
            print("%d --- %d: cost: %d"% (u, v, w))
            minimum_cost += w
        return minimum_cost       
            
# Driver code 
if __name__ == '__main__': 
    obj = Graph(4) 
    obj.addEdge(0, 1, 10) 
    obj.addEdge(0, 2, 6) 
    obj.addEdge(0, 3, 5) 
    obj.addEdge(1, 3, 15) 
    obj.addEdge(2, 3, 4) 
  
    # Function call 
    print(obj.kruskal_mst())
