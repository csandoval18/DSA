import heapq
from typing import List


# Capital = list containing min capital required to start each project
# Profits = list containing the profits associated with each project
# k = Number of projects able to be completed before IPO
# w = Starting capital

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
    
class SolutionExplained:
  def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    projects = list(zip(capital, profits)) # Create a list of projects where each project is a tuple: (capital, profit)
    projects.sort() # Sort projects by their capital requirements
    
    pq = []
    curr = 0
    
    for _ in range(k):
      # Add all projects that can be started with the current capital to the max heap
      while curr < len(projects) and projects[curr][0] <= w:
        heapq.heappush(pq, -projects[curr][1]) # Remember that heapq is a min heap by default. We need to use negative values to make it work as a max heap
        curr += 1
      
      # If heap is empty, no more projects can be selected
      if not pq:
        break
      
      # Select the most profitable project available
      w -= heapq.heappop(pq)
    
    return w
    
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
s = Solution()
print(s.findMaximizedCapital(k, w, profits, capital))