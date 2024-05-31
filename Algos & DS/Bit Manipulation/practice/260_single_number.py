from typing import List

def singleNumber(nums: List[int]) -> List[int]:
  # Step 1: XOR all numbers to find the XOR of the two unique numbers
  xor_all = 0
  for num in nums:
    xor_all ^= num
  
  # Step 2: Find a set bit in xor_all (we use the rightmost set bit)
  set_bit = xor_all & -xor_all
  
  # Step 3: Divide numbers into two groups based on the set bit and XOR within each group
  num1, num2 = 0, 0
  for num in nums:
    if num & set_bit:
      num1 ^= num
    else:
      num2 ^= num
  return [num1, num2]