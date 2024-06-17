from collections import deque
from typing import List
 
class Solution:
  def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
    if start == end:
      return 0
    
    # Initialize BFS queue and visited set
    q = deque([(start, 0)])
    visited = set([start])
    
    while q:
      curr, steps = q.popleft()
      
      for multiplier in arr:
        new_number = curr * multiplier
      
      # If we reach the end number, return the steps count
      if new_number == end:
        return steps + 1
      
      # If new_number is not visited, add to the queue
      if new_number not in visited:
        visited.add(new_number)
        q.append((new_number, steps + 1))
    
    return -1
  
start = 2
end = 12
arr = [2, 3]
s = Solution()
print(s.minimumMultiplications(arr, start, end))