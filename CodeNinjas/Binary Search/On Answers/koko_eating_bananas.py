# Koko eating bananas

# Return the MIN int k such that Koko can eat all bananas within h hours

# piles = [3,6,7,11]
# h = 8

# piles = [3,6,7,11]
#        1h 2h 3h 4h = 10h

from ast import List
import math

# Dont need this since I can just use max(piles) to get the max el val
# as shown in lines 2 for starting r pointer
def findMax(piles: List[int]) -> int:
  maxVal = float('-inf')
  n = len(piles)
  
  for num in piles: 
    maxVal = max(maxVal, num)
  return maxVal

def calcRequiredTime(piles, h):
  n = len(piles)
  total_hours = 0
  
  for i in range(n):
    total_hours += math.ceil(piles[i] / h)
  return total_hours

def minEatingSpeed(piles: List[int], h: int) -> int:
  n = len(piles)
  l, r = 1, max(piles)
  res = float('inf')
  
  while l<=r:
    m = (l+r)//2
    # Find total hours to eat all bananas with a rate of piles[m] bananas / hour
    # total_hours = math.ceil(piles[i] / h)
    total_hours = calcRequiredTime(piles, m)
    
    if total_hours <= h:
      r = m-1
    else:
      l = m+1
  return l
  
