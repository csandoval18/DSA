from typing import List


class Solution:
  def frequencySort(self, nums: List[int]) -> List[int]:
    hm = {}
    
    for num in nums:
      hm[num] = hm.get(num, 0)+1
    
    # sorted_nums = sorted(nums, key=lambda x: (hm[x], -x))
    sorted_nums = sorted()
    return sorted_nums