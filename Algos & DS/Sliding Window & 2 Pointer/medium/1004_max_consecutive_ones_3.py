from asyncio import Queue
from collections import deque
from typing import List

'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

- ie: Find the subarray with at most k zeroes
'''

class SolutionBF:
  def longestOnes(self, nums: List[int], k: int) -> int:
    maxLen = 0
    
    for i in range(len(nums)):
      zeroes = 0
      for j in range(i, len(nums)):
        if nums[j] == 0:
          zeroes += 1
        if zeroes <= k:
          maxLen = max(maxLen, j-i+1)
        else:
          break
    return maxLen
    
class SolutionBetter:
  def longestOnes(self, nums: List[int], k: int) -> int:
    l, maxLen = 0, 0
    zeroes = 0
    
    for r in range(len(nums)):
      if nums[r] == 0:
        zeroes += 1
      
      while zeroes > k:
        if nums[l] == 0:
          zeroes -= 1
          l += 1
      
      if zeroes <= k:
        maxLen = max(maxLen, r-l+1)
    return maxLen
    
# Attempt to use a hash map instead of using while loop to track first zero seen to remove from the left when zeroes surpasses k
  
class SolutionOP:
  def longestOnes(self, nums: List[int], k: int) -> int:
    l, maxLen = 0, 0
    zeroes = 0
    q = deque()
    
    for r in range(len(nums)):
      print(q)
      if nums[r] == 0:
        zeroes += 1
        q.append(r)
      
      if q and zeroes > k:
        l = q.popleft() + 1
        zeroes -= 1
      
      if zeroes <= k:
        maxLen = max(maxLen, r-l+1)
    return maxLen
        
        
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
      l, maxLen = 0, 0
      zeroes = 0

      for r in range(len(nums)):
        if nums[r] == 0:
          zeroes += 1
        
        if zeroes > k:
          if nums[l] == 0:
            zeroes -= 1
          l += 1
        
        if zeroes <= k:
          maxLen = max(maxLen, r-l+1)

      return maxLen
      
      
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
s = SolutionOP()
print(s.longestOnes(nums, k))

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.