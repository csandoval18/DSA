from collections import deque
from typing import List

# 2 Pointers Solution
# O(1) space | O(n) tc
def trap(height: List[int]) -> int:
  n = len(height)
  
  if not height:
    return 0
  
  l, r = 0, n-1
  l_max, r_max = height[l], height[r]
  water_trapped = 0
  
  while l < r:
    if l_max <= r_max:
      l += 1
      l_max = max(l_max, height[l])
      water_trapped += l_max - height[l]
    else:
      r -= 1
      r_max = max(r_max, height[r])
      water_trapped += r_max - height[r]
      
  return water_trapped
  

# Stack Solution
def tgrap(height: List[int]) -> int:
  n = len(height)
  queue = deque()
  
  if not height:
    return 0
  
  stack = []
  water_trapped = 0
  curr = 0
  
  while curr < n:
    # While there is a bar that forms a boundary and the current bar:
    while stack and height[curr] > height[[stack][-1]]: 
      top = stack.pop() # This is the min height of the water trap area (middle boundary)
      
      if not stack: # If the stack is empty, no left boundary
        break
      
      distance = curr - stack[-1] - 1 # Distance between the new stack top and curr
      bounded_height = min(height[stack[-1]], height[curr]) - height[top]
      water_trapped += distance * bound_height
      
    stack.append(curr)
    curr += 1
    
  return water_trapped