from ast import List

# So aparently using a set in python is not as efficient since the python set doesn't directly support operations
# for finding and removing the smallest distance efficiently. This is for demonstraition purposes
def dijstraSet(V: int, adj: List[List[int]], S: int) -> List[int]:
  dist = [float('inf')]*V
  dist[S] = 0
  
  st = set()
  st.add((0, S))
  
  while st:
    node_tuple = min(st, key = lambda x: x[0])
    st.remove(node_tuple)
    node_wt = node_tuple[0]
    node = node_tuple[1]
    
    for it in adj[node]:
      adjNode = it[0]
      wt = it[1]
      
      if node_wt + wt < dist[adjNode]:
        if dist[adjNode] != float('inf'):
          st.discard((dist[adjNode], adjNode))
          
        # Update distance
        dist[adjNode] = node_wt + wt
        st.add((dist[adjNode], adjNode))
        
  return dist