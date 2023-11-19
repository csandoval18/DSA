from typing import List

def maxProduct(nums: List) -> int:
  n = len(nums)
  for i in range(n):
    for j in range(i, n):
      print(nums[j], end="->")
    print()
        
arr = [2,3,-2,4]
maxProduct(arr)