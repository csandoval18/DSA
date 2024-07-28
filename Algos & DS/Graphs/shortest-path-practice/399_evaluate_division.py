from collections import defaultdict
from typing import List


class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    adj = defaultdict(dict)
 
    # Build the graph
    for (a, b), value in zip(equations, values):
      adj[a][b] = value
      adj[b][a] = 1 / value
    
    def dfs(start: int, end: int, visited: set):
      # If either the start or end variable is not in the graph, return -1.0
      if start not in adj or end not in adj:
        return -1.0
      # If the start and end are the same, return 1.0 (identity division)
      if start == end:
        return 1.0
      
      visited.add(start)
      for v, val in adj[start].items():
        if v not in visited:
          wt = dfs(v, end, visited)
          # If a valid path is found, return the product of values along the path
          if wt != -1.0:
            return wt * val
      # If no valid path is found, return -1.0
      return -1
    
    res = []
    # Step 3: Evaluate each query
    for a, b in queries:
      # Correspondence: `start` is `a` and `end` is `b`
      if a in adj and b in adj:
        res.append(dfs(a, b, set()))
      else:
        res.append(-1.0)
        
    return res
    
# Example usage
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["c", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
s = Solution()
print(s.calcEquation(equations, values, queries))  
# Output: [6.0, 0.16666666666666666, -1.0, 1.0, -1.0]