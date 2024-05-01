
class DFS:
    
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]
        self.visited = []
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        
    def dfs(self, node):
        
        self.visited.append(node)
        print(str(node) + ' ')
        
        for adj in self.adj_list[node]:
            if adj not in self.visited:
                self.dfs(adj)
        

if __name__ == '__main__':
    vertices = 5
    obj = DFS(vertices)
    
    obj.add_edge(0, 1)
    obj.add_edge(0, 2)
    obj.add_edge(1, 3)
    obj.add_edge(1, 4)
    obj.add_edge(2, 4)
    obj.dfs(0)
    
    print(" 2nd")
    obj1 = DFS(4) 
    obj1.add_edge(0, 1)
    obj1.add_edge(0, 2)
    obj1.add_edge(1, 2)
    obj1.add_edge(2, 0)
    obj1.add_edge(2, 3)
    obj1.add_edge(3, 3)
    obj1.dfs(2)
