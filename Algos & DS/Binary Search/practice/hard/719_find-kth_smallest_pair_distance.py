from typing import List


class Solution:
  def smallestDistancePair(self, nums: List[int], k: int) -> int:
    def countPairs(nums: List[int], m: int):
      cnt, l = 0,0
      for r in range(len(nums)):
        while nums[r] - nums[l] > m:
          l += 1
        cnt += r-l
      return cnt

    nums.sort()
    l, r = 0, nums[-1] - nums[0]

    while l < r:
      m = (l+r)//2

      if countPairs(nums, m) < k:
        l  = m+1
      else:
        r = m
    
    return l