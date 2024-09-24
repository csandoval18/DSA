from typing import List

# Gray Code is a binary numeral system where two successive values differ by
# exactly one bit. In other words, when you move from one number to the next, only 
# one of the bits changes (either from 0 to 1 or from 1 to 0).

class Solution:
  def grayCode(self, n: int) -> List[int]:
    