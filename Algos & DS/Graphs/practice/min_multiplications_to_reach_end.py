from collections import deque
from typing import List
 
class Solution:
  def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
    n = len(arr)
    if n == 1:  # If the array has only one element, no multiplication is needed
        return 0
    
    # BFS initialization
    queue = deque([(0, 0)])  # (current_index, current_steps)
    visited = set([0])
    
    while queue:
        current_index, current_steps = queue.popleft()
        
        # Iterate through all possible multiplications
        for multiplier in range(1, arr[current_index] + 1):
            new_index = current_index + (current_index * multiplier)
            
            # If new index is the end of the array, return steps
            if new_index >= n - 1:
                return current_steps + 1
            
            # If new index is within bounds and not visited
            if 0 <= new_index < n and new_index not in visited:
                visited.add(new_index)
                queue.append((new_index, current_steps + 1))
    
    return -1  # If no path is found
  
start = 2
end = 12
arr = [2, 3]
s = Solution()
print(s.minimumMultiplications(arr, start, end))