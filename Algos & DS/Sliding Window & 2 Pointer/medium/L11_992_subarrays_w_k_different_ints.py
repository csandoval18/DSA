from typing import List


class SolutionBF: # TC: O(N^2)
  def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    cnt = 0
    
    for l in range(len(nums)):
      hm = {}
      
      for r in range(len(nums)):
        hm[nums[r]] = hm.get(nums[r], 0) + 1
        
        if len(hm) == k:
          cnt += 1
        elif len(hm) > k:
          break
    return cnt

class SolutionBetter:
  def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    def helper(k: int) -> int:
      l, cnt = 0, 0
      hm = {}
      
      for r in range(len(nums)):
        hm[nums[r]] = hm.get(nums[r], 0) + 1
        
        while len(hm) > k: # Shrink window if distinct count exceeds k
          hm[nums[l]] -= 1
        
          if hm[nums[l]] == 0:
            del hm[nums[l]]
          l += 1

        cnt += r-l+1 # Count subarrays with at most k distinct elements
      return cnt
    return helper(k) - helper(k-1)
  
nums = [1,2,1,2,3]
k = 2
# Explanation: Subarrays formed with exactly 2 different integers: 
# [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
s = SolutionBetter() 
print(s.subarraysWithKDistinct(nums, k))