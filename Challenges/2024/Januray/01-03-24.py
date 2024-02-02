from collections import Counter
import math


def minOperations(nums: [int]) -> int:
  cnt = Counter(nums)
  res = 0
  
  for n, c in cnt.items():
    if c == 1:
      return  -1
    res += math.ceil(c/3)
  return res