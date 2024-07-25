from typing import List


class Solution:
  def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
    def map_number(num):
      mapped_num = int(''.join(str(mapping[int(digit)]) for digit in str(num)))
      return mapped_num
    
    nums.sort(key=map_number)
    return nums

#     i =  0 1 2 3 4 5 6 7 8 9
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
# Output: [338,38,991]