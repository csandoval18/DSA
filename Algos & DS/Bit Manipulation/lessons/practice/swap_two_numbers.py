from typing import Tuple


class Solution:
  def get(self, a: int, b: int) -> Tuple[int, int]: 
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return (a, b)

a, b = 13, 9
a, b = 15, 8
s = Solution()
print(s.get(a, b))