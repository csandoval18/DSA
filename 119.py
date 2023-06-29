def getRow(self, numRows):
  triangle = []
  
  for i in range(numRows + 1):
    
    # if i = 3, then row = [1,1,1,1]
    row = [1] * (i + 1)  # Initialize each row with 1s
    
    # Calculate the values for the current row
    for j in range(1, i):
      row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
      
    triangle.append(row)
    
  return triangle[numRows]
  
  
class Solution:
  def getRow(self, rowIndex):
    row = [1] * (rowIndex + 1)

    for i in range(1, rowIndex):
      for j in range(i, 0, -1):
        row[j] += row[j - 1]

    return row

      
numRows = 3        
print(getRow(numRows))