from typing import List

'''
An integer is called arithmetic if it consists of at least three elements and if the difference
between any two consecutive elements is the same.
'''

class Solution:
  def numberOfArithmeticSlices(self, nums: List[int]) -> int:


nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

nums = [1]
# Output: 0