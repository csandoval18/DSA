from functools import cmp_to_key
from typing import List

# This approach works because lexicographical comparison directly reflects
# how string concatenation will behave. When you compare two numbers as strings, the 
# lexicographical ordering tells you which combination of the two strings will yield a 
# larger number when placed next to each other.

class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    # Convert nums to strings
    nums_str = list(map(str, nums))
    
    # Define custom comparator
    def compare(x: str, y: str):
      if x + y > y + x:
        return -1
      else:
        return 1
    
    # Sort numbers with the custom comparator
    nums_str.sort(key=cmp_to_key(compare))
    # Join the sorted array to form the largest number
    res = ''.join(nums_str)
    # Handle case where the result might be all zeroes
    return '0' if res[0] == '0' else res
    
nums = [9, 34, 5, 30]
strings = [9, 34, 5, 30]

# Compare "9" and "34":
# - x + y = "934"

