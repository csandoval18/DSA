import heapq
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = [[] for _ in range(n)]
        self.n = n
        
        for u, v, c in edges:
            self.adj[u].append((v, c))
      
    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        self.adj[u].append((v, c))
        return self.adj
            

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float('inf')] * self.n 
        dist[node1] = 0
        pq = [(0, node1)]
        
        while pq:
            uc,  u = heapq.heappop(pq)
            
            if uc > dist[u]:
                continue
                
            for v, vc in self.adj[u]:
                nc = uc + vc
                
                if nc < dist[v]:
                    dist[v] = nc
                    heapq.heappush(pq, (nc, v))
                    
        if dist[node2] != float('inf'):
            return dist[node2]
        return -1
                    
g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
print(g.shortestPath(3, 2)) # 6
print(g.shortestPath(0, 3)) # -1.
print(g.addEdge([1, 3, 4]))
print(g.shortestPath(0, 3))