# You have 'n' empty pens whose refills have been used up.
# You have 'R' rupees in your pocket.

# You have two choices of operations that you can perform each time.
# 1. Recycle 1 empty pen and get 'K' rupees as a reward.
# 2. Buy 1 refill for 'C' rupees and combine it with 1 empty pen to make
# one usable pen.


# This seems like a greedy algo
# n = # of empty pens
# r = # amount of cash or ruppees
# k = reward for reclying empty pen
# c = cost of refill

# Your task is to find the max number of usable pens that you can get.

def recyclePens(n, r, k, c):
  left, right = 0, n
  
  while left<right:
    mid = (left+right+1)//2
    
    recycleCost = (n-mid)*k
    totalCost = recycleCost+r
    if totalCost >= mid*c:
      left = mid
    else:
      right = mid-1
  return left
  
  