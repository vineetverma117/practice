
from collections import deque

class BFS:
    
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]
        self.visited = [False]* self.V
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        
    def bfs(self, node):
        q = deque()
        if self.visited[node] == False:
            self.visited[node] = True
            q.append(node)
        while q:
            q_node = q.popleft()
            print(str(q_node) + " ")
            
            for adj in self.adj_list[q_node]:
                if self.visited[adj] == False:
                    self.visited[adj] = True
                    q.append(adj)
        

if __name__ == '__main__':
    vertices = 5
    obj = BFS(vertices)
    
    obj.add_edge(0, 1)
    obj.add_edge(0, 2)
    obj.add_edge(1, 3)
    obj.add_edge(1, 4)
    obj.add_edge(2, 4)
    obj.bfs(0)
