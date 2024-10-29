from heapq import heappush, heapreplace
from typing import List


class KthLargest:
  def __init__(self, k: int, nums: List[int]) -> None:
    self.k = k
    self.pq = []
    
    for num in nums:
      self.add(num)
    
    def add(self, val: int) -> int:
      if len(self.pq) < self.k:
        heappush(self.pq, val)
      elif val > self.pq[0]:
        heapreplace(self.pq, val) # More efficient than using heappop() and heappush() consecutively
      return self.pq[0]