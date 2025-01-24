from typing import List


# Naive Map Solution
class Solution: # O(N*log(M) + O(M)) | O(M)
  def singleNumber(self, nums: List[int]) -> int:
    hm = {}
    
    for num in nums:
      hm[num] = hm.get(num, 0) + 1
    
    for key in hm:
      if hm[key] == 1:
        return key


  # Bit Manipulation Solution
  def singleNumberBM(self, nums: List[int]) -> int:
    res = 0
    
    # Traverse 32 bits
    for bitIndex in range(32): # Count the number of 1s in the current bit position across all numbers
      cnt = 0
      
      for num in nums:
        if num & (1 << bitIndex): # Use 1 << bitIndex to create the bitmask
          cnt += 1
    
      if cnt % 3 == 1:
        res |= (1 << bitIndex)
      
      # Handle negative numbers explicitly
      if res >= (1 << 31): # If the 31st bit is set, it’s a negative number
        res -= (1 << 32) # Convert to signed integer by subtracting 2^32
    return res 
    
'''
 nums = [5,5,5,6,4,4,4]   
 
      2 1 0 
 ----------
 5 => 1 0 1
 5 => 1 0 1
 5 => 1 0 1
 6 => 1 1 0
 4 => 1 0 0
 4 => 1 0 0
 4 => 1 0 0
'''
    
# nums = [2,2,3,2]
# Output: 3

nums = [0,1,0,1,0,1,99]
# Output: 99

s = Solution()
print(s.singleNumber(nums))
print(s.singleNumberBM(nums))