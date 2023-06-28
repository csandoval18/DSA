# def generate(numRows):
#   ans = []
#   for i in range(numRows):
#     sub = []
#     for j in range(numRows):
#       if (i or j == 0):
#         sub.append(1)
#         ans.append(sub)
#         continue
#       sub.append(sub[i-1][j] + sub[i][j -1])
#   return ans
      
      
      
def generate(numRows):
  triangle = [[1]]
  
  for i in range(1, numRows):
    
    # if i = 3, then row = [1,1,1,1]
    row = [1] * (i + 1)  # Initialize each row with 1s
    
    # Calculate the values for the current row
    for j in range(1, i):
      row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
      
    triangle.append(row)
    
  return triangle

      
      
numRows = 5        
print(generate(5))
