from typing import List


class Solution:
  def readBinaryWatch(self, turnedOn: int) -> List[str]:
    def count_bits(x: int):
      # Bin method return the binary representaition of an integer
      return bin(x).count('1')
    
    times = []
    for h in range(12):
      for m in  range(60):
        if count_bits(h) + count_bits(m) == turnedOn:
          times.append(f"{h}:{m:02d}")
    return times