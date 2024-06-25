from typing import List


class Solution:
  def minKBitFlips(self, nums: List[int], k: int) -> int:
    n = len(nums)
    is_flipped = [0]*n
    flip = 0
    flips = 0
    
    for i in range(n):
      if i >= k:
        flip ^= is_flipped[i-k]
      if (nums[i] ^ flip) == 0:
        if i + k > n:
          return -1
        
        flip ^= 1
        is_flipped[i] = 1
        flips += 1
      
    return flips