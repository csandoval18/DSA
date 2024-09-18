from functools import cmp_to_key
from typing import List


class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    # Convert nums to strings
    nums_str = list(map(str, nums))
    
    # Define custom comparator
    def compare(x: int, y: int):
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