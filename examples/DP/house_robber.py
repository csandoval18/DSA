from typing import List

def rob(nums: List[int]) -> int:
  def backtrack(idx: int) -> int:
    if idx == 0:
      return nums[idx]
    if idx < 0:
      return 0
    
    pick = nums[idx] + backtrack(idx-2)
    not_pick = 0 + backtrack(idx-1)
    return max(pick, not_pick)
    
  n = len(nums)
  return backtrack(n-1)