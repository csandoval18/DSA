from typing import List

'''
Return the two numbers with a frequency of 1.
'''

class Solution: # TC: O(NlogM + M) | SC: O(M)
  # Naive Solution using extra DS
  def singleNumber(self, nums: List[int]) -> List[int]:
    hm = {}
    res = []
    
    for num in nums: # N log(M) => M = len of map
      hm[num] = hm.get(num, 0) + 1
    
    for key in hm: # O(M)
      if hm[key] == 1:
        res.append(key)
    return res
    
  # Using XOR bitwise operator and concept of buckets
  def singleNumberOP(self, nums: List[int]) -> List[int]: # TC: O(2N) | O(1)
    # XOR all nums in nums to cancel out repeating numbers, the result will be the XOR of the nums appearing once
    XOR = 0
    for num in nums:
      XOR ^= num
    
    rightmost = (XOR & XOR-1) ^ XOR # Find right-most '1' bit
    
    b1, b2 = 0, 0
    for num in nums:
      if num & rightmost:
        b1 ^= num
      else:
        b2 ^= num
    return [b1, b2]

'''
Refresher: 
1. a ^ a = 0
2. (num & num-1) ^ num => Returns rightmost turned on bit. Remember num-1 turns on all bit from right-most bit in num to 1's
  Ex: n   = 1 1 0 0 
      n-1 = 1 0 1 1
3. Since the 2 digits that have a freq of 1 will be XOR'ed together, we can use buckets to keep track of their difference by
   separating them based on if they have the right-most bit as 1 or 0.
'''
      
nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer. Only 3 and 5 appear once, the rest appear twice.
s = Solution()
print(s.singleNumberOP(nums))