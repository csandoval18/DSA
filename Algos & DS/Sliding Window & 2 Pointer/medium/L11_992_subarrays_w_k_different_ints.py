from typing import List


class SolutionBF:
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