import heapq
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = [[] for _ in range(n)]
        self.n = n
        
        for u, v, c in edges:
            self.adj[u].append((v, c))
      
    def addEdge(self, edge: List[int]) -> None:
        for u, v, c in edge:
            self.adj[u].append((v, c))
            

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float('inf')] * self.n 
        pq = [(node1, 0)]
        
        while pq:
            uc,  u = heapq.heappop(pq)
            
            if uc > dist[u]:
                continue
                
            for v, vc in self.adj[u]:
                nc = uc + vc
                
                if nc < dist[v]:
                    dist[v] = nc
                    
        if dist[node1] != float('inf'):
            return dist[node1]
        return -1
                    