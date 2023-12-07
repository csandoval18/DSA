# Koko eating bananas

# Return the min int k such that Koko can eat all bananas within h hours

# piles = [3,6,7,11]
# h = 8

# piles = [3,6,7,11]
#        1h 2h 3h 4h = 10h

from ast import List


def minEatingSpeed(piles: List[int], h: int) -> int:
  n = len(piles)
  l, r = 1, piles[n-1]
  
  while l<=r:
    m = (l+r)//2
    
    # Base case
    