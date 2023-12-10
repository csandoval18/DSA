# Find the samllest divisor given a threshold
from math import ceil

# Works unnder assumption there is a solution
def smallestDivisor(nums: [int], threshold: int) -> int:
  def sumOfDivs(nums: [int], m: int):
    total_sum = 0
    for num in nums:
      total_sum += ceil(float(num)//m)
    return total_sum
    
  # If immpossible case is possible add this case
  if len(nums) > threshold:
    return -1

  l, r = 1, max(nums)
  res = -1
  
  while l<=r:
    m = (l+r)//2
    
    if sumOfDivs(nums, m) <= threshold:
      res = m
      r = m-1
    else:
      l = m+1
  return l

# Impossible case explanaition
# nums = [1,2,3,9] 
# threshold = 3

# ceil(1/9) = 1
# ceil(1/9) = 1
# ceil(1/9) = 1
# ceil(1/9) = 1
# total =  4 = n = len(nums)

# if n > threshold:
# return -1
# solution not possible since the sum will always be greater than the threshold
