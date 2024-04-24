from collections import deque
from typing import List

def openLock(deadends: List[str], target: str) -> int:
  if "0000" in deadends:
    return -1
  
  visited = set(deadends) # All deadends are added to visited to avoid them
  queue = deque()
  queue.append(("0000", 0)) # Queue holds tuples of (current combination, depth)
  visited.add("0000") # Mark the start position as visited
  
  def neighbors(combination):
    for i in range(4):
      digit = int(combination[i])
      
      # Produce next and prev digits for the current position
      for move in (-1, 1):
        next_digit = (digit + move) % 10
        