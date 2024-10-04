from typing import List


class Solution:
  def minSubarray(self, nums: List[int], p: int) -> int:
    total_sum = sum(nums)
    