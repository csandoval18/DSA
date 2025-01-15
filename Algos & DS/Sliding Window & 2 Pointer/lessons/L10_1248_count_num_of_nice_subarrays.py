from typing import List

'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
'''

class SolutionBF:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    cnt = 0
    
    for l in range(len(nums)):
      odds = 0
      for r in range(l, len(nums)):
        if nums[r] % 2 != 0:
          odds += 1
        if odds == k:
          cnt += 1
        elif odds > k:
          break
    return cnt


class SolutionInclusionExclusion:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    def helper(x: int) -> int: 
      if x < 0:
        return 0
        
      l, odds = 0, 0
      cnt = 0
      
      for r in range(len(nums)):
        odds += nums[r] % 2 # Will give a 1 when odd, and a 0 when even
        
        while odds > x:
          odds -= nums[l] % 2
          l += 1
        
        cnt += r-l+1
      return cnt
    return helper(k) - helper(k-1)
    
    
nums = [1,1,2,1,1] 
k = 3
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
s = SolutionBF()
print(s.numberOfSubarrays(nums, k))
s = SolutionInclusionExclusion()
print(s.numberOfSubarrays(nums, k))