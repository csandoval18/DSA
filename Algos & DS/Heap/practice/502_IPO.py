import heapq
from typing import List


# Capital = list containing min capital required to start each project
# Profits = list containing the profits associated with each project

# Heap solution
class Solution:
  def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    projects = list(zip(capital, profits))
    projects.sort()
    
    pq = []
    curr = 0
    
    for _ in range(k):
      while curr < len(projects) and projects[curr][0] <= w:
        heapq.heappush(pq, -projects[curr][1])
        curr += 1
      if not pq:
        break
      w -= heapq.heappop(pq)
    
    return w