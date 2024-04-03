# Dijkstra's Algorithm

# This algorithm is used to find the shortest path in a weighted graph.
# There are 3 methods of implementaition: 
# 1. Using a Queue
# 2. Using a Priority Queue
# 3. Using a Set (fastest method)

from typing import List
import heapq

def dijkstraPriorityQueue(V: int, adj: List[List[int]], S: int) -> List[int]:
  # Create a priority queue (min heap) pq to store vertices as (dist, node)
  #     wt node
  pq = [(0, S)] # Distance of source node to itself is 0
  
  # Initialize distance from S to all other vertices as a large value
  dist = [float('inf')]*V
  dist[S] = 0
  
  
  while pq:
    # Pop a vertx with the smallest distance from pq
    current_dist, node = heapq.heappop(pq)
    
    # If the popped vertex distance is greater than the current distance, skip processing
    if current_dist > dist[node]:
      continue
    
    # Check all the vertices adjacent to the dequeued vertex
    for it in adj[node]:
      adjNode = it[0]
      wt = it[1]
    
      # If shorter path to adjNode is found
      if dist[node] + wt < dist[adjNode]:
        dist[adjNode] = dist[node] + wt
        # Push the adj node with the updated distance to the priority queue
        heapq.heappush(pq, (dist[adjNode], adjNode))
    
    # Return the calculated shortest distances
    return dist

def dijkstraPQ(V: int, adj: List[List[int]], S: int) -> List[int]:
  pq = [(0, S)]
  dist = [float('inf')]*V
  dist[S] = 0
  
  while pq:
    current_dist, node = heapq.heappop(pq)
    
    if current_dist > dist[node]:
      continue
      
    for it in adj[node]:
      adjNode = it[0]
      wt = it[1]
      
      if dist[node] + wt < dist[adjNode]:
        dist[adjNode] = dist[node] + wt
        heapq.heappush(pq, (dist[adjNode], adjNode))
  return dist