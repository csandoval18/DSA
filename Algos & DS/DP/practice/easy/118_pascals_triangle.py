from typing import List

# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1]

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    triangle = [] # Empty triangle to store the rows of Pascal's Triangle
    
    # A loop is started that will iterate 'numRows' times.
    # Each iteration represents the construction of a new row in Pascal's Triangle.
    for i in range(numRows): 
      # A new row is initialized with '1's. The number of 1's is equal to (i+1),
      # where
      row = [1] * (i+1) 
      
      for j in range(1, i): # Calculate the middle values for the current row
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
      triangle.append(row)
    return triangle
    
class Solution1:
  def generate(self, numRows: int) -> List[List[int]]:
    triangle = []
    
    for x in range(numRows):
      row = [1] * (x+1)
      
      for y in range(1, y):
        row[y] = triangle[x-1][y-1] + triangle[x-1][y]
      triangle.append(row)
    return triangle