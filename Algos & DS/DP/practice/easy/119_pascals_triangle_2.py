from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    prev = []
    
    for x in range(rowIndex+1):
      row = [1] * (x+1)
      for y in range(1, x):
        row[y] = prev[y-1] + prev[y]
      prev = row
    return prev
      
rowIndex = 3
s = Solution()
print(s.getRow(rowIndex))