from typing import List

class Solution:
  def subsetXORSum(self, nums: List[int]) -> int:
    n = len(nums)
    def bt(idx: int, curr_xor: int) -> None:
      # Add the current XOR to the total sum
      self.total_sum += curr_xor
      
      # Iterate over the remaining elements to create new subsets
      for i in range(idx, n):
        # Include nums[i] in the 
        bt(i + 1, curr_xor ^ nums[i])
    
    # Initialize total sum to be 0
    self.total_sum = 0
    bt(0, 0)
    # Return the total sum of all subset xor totals
    return self.total_sum