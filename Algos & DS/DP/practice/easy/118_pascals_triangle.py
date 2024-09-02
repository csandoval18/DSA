from typing import List


class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    res = []
    
    for i in range(numRows):
      row = [1] * (i+1) # Initializ each row with 1s
      
      for j in range(1, i): # Calculate the values for the current row
        row [j] = res[i-1][j-1] + res[i-1][j]