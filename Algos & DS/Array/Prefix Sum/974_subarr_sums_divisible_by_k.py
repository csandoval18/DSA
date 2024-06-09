from typing import List


class Solution:
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    remainder_count = {0: 1}
    curr_sum = 0
    count = 0
    
    for num in nums:
      curr_sum += num
      remainder = curr_sum % k
      
      # Adjust negative remainders to be positive
      if remainder < 0:
        remainder += k
      if remainder in remainder_count:
        count += remainder_count[remainder]
        remainder_count[remainder] += 1
      else:
        remainder_count[remainder] = 1
        
    return count