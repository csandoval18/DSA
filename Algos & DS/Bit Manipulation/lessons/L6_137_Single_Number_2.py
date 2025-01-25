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


  # Bit Manipulation Solution (Not Optimized)
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
  def singleNumberBM(self, nums: List[int]) -> int: # TC: O(N*32) | SC: O(1)
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
    
    
  # Bit Manipulation Solution (Better Approach)
  def singleNumberOP(self, nums: List[int]) -> int: # TC: O(NlogN + N/3) | SC: O(1)
    nums.sort() # O(Nlog(N))
    
    for i in range(0, len(nums), 3):
      if nums[i] != nums[i-1]:
        return nums[i-1]
    return nums[len(nums)-1]
  
  
  # Best solution using buckets (Not intuitive)
  '''
  nums = [2,2,3,2]
  
  nums[i] will go to ones, if not in twos
  nums[i] will go to twos, if it is in ones
  nums[i] will go to threes, if it is in twos
  
  
  ones = (ones ^ num) & ~twos
  twos = (twos ^ num) & ~ones
  
  1. Intialize:
  ones = 0, twos = 0
  
  2. First 2:
  - ones = (0 ^ 2) & ~0 = 2 & -1 = 2 (binary:10)
  - twos = (0 ^ 2) & ~2 = 2 & -3 = 2 (binary:00)
  
  3. Second 2:
  - ones = (2 ^ 2) & ~0 = 0 & -1 = 0 (binary:00)
  - twos = (0 ^ 2) & ~0 = 2 & -1 = 2 (binary:10)
  
  4. Third 2:
  - ones = (0 ^ 2) & ~2 = 2 & -3 = 0 (binary:00)
  - ones = (2 ^ 2) & ~0 = 0 & -1 = 0 (binary:00)
  
  5. First 3: 
  - ones = (0 ^ 3) & ~0 = 3 & -1 = 3 (binary: 11)
  - twos = (0 ^ 3) & ~3 = 3 & -4 = 0 (binary: 00)
  
  6. Result:
  - ones = 3, which is the single number
  
  Why this works:
  * XOR operator toggles bits between 0 and 1.
  * The & ~twos and & ~ones ensures that bits are only added to ones or twos if they haven't been seen twince or once, respectively.
  * After three ocurrences, the bits are rest to 0 in both ones and twos.
  
  
  Step	Num	ones (binary)	twos (binary)
  0	     -	00	          00
  1	     2	10	          00
  2	     2	00	          10
  3	     2	00	          00
  4	     3	11	          00
  
  ones:
  - Tracks bits that have appeared an odd number of times
  - If a bit is set to 1, in ones it means that the bit has appeared once in the numbers processed so far.
  twos:
  - Tracks bits that have appeared twice so far.
  - If a bit is set to 1 in twos, it means that bit has appeared twice in the numbers processed so far.
  

  '''
  def singleNumberOptimal(self, nums: List[int]) -> int: # TC: O(N) | SC: O(1)
    ones = 0
    twos = 0
    
    for num in nums:
      ones = (ones ^ num) & ~twos
      twos = (twos ^ num) & ~ones
    return ones
    
# nums = [2,2,3,2]
# Output: 3

nums = [0,1,0,1,0,1,99]
# Output: 99

s = Solution()
print(s.singleNumber(nums))
print(s.singleNumberBM(nums))
