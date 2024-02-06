from typing import List

def rob(nums: List[int]) -> int:
  def robHelper(idx: int) -> int:
    if idx == 0:
      return nums[idx]
    if idx < 0:
      return 0
    
    pick = nums[idx] + robHelper(idx-2)
    not_pick = 0 + robHelper(idx-1)
    return max(pick, not_pick)
    
  n = len(nums)
  return robHelper(n-1)