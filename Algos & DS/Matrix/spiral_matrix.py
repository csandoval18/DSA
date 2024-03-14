from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[List[int]]:
  left, right = 0, len(matrix[0])-1
  top, bottom = 0, len(matrix)-1
  res = []
  
  while left <= right and top <= bottom:
    for j in range(left, right+1):
      res.append(matrix[top][j])
    top += 1
    
    for i in range(top, bottom+1):
      res.append(matrix[i][right])
    right -= 1
    
    if top <= bottom:
      for j in range(right, left-1, -1):
        res.append(matrix[bottom][j])
      bottom -= 1
    
    if left <= right:
      for i in range(bottom, top-1, -1):
        res.append(matrix[i][left])
    left += 1
  return res

def spiralOrder1(matrix: List[List[int]]) -> List[List[int]]:
  l, r = 0, len(matrix[0])-1
  t, b = 0, len(matrix)-1
  res = []

  while l <= r and t <= b:
    for j in range(l, r+1):
      res.append(matrix[t][j])
    t += 1
    
    for i in range(t, b+1):
      res.append(matrix[i][r])
    r -= 1
    
    if t <= b:
      for j in range(r, l-1, -1):
        res.append(matrix[b][j])
      b  -= 1
    
    if l <= r:
      for i in range(b, t-1, -1):
        res.append(matrix[i][l])
      l += 1
    
  return res
    
  

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]
print(spiralOrder(matrix))