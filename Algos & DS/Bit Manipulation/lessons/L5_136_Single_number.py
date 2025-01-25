# Refresher using map

from typing import List


class Solution(object): # TC: O(N*log(M) + M) | SC: O(M)   M = (N//2)+1
  def singleNumber(self, nums):
    hm = {}
    
    for num in nums:
      hm[num] = hm.get(num, 0) + 1
      
    for key in hm:
      if hm[key] == 1:
        return key
    
  def singleNumberOneLoop(self, nums):
    hm = {}
    
    for i, num in enumerate(nums):
      if num not in hm:
        hm[num] = i
      else:
        hm.pop(num)
    # return list(hm.keys())[0]
    return next(iter(hm))

  # Using Bit Manipulation
  
  # XOR returns 1 when the two compared bits are different and 0 when they are the same.
  # XOR -> a ^ a = 0
  def singleNumberOneLoop(self, nums: List[int]):
    XOR = 0
    
    for num in nums:
      XOR = XOR ^ num
    return XOR
  
nums = [4,1,2,1,2]

# 1 1 0 1
# 1 1 0 1
# -------
# 0 0 0 0

s = Solution()
print(s.singleNumberOneLoop(nums))