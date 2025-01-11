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
    l, cnt = 0, 0
    hm = {}
    
    for r in range(len(nums)):
      hm[nums[r]] += 1
      
      while len(hm) <= k:
        hm[nums[l]] -= 1
      
        if hm[nums] == 0:
          hm.pop(nums[l])
        l += 1

      cnt += r-l+1
    return cnt