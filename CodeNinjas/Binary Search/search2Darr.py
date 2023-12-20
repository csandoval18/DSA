def searchMatrix(mat:  [[int]], target: int) -> bool:
  n = len(mat)
  for i in range(len(mat)):
    m = len(mat[i])
    if mat[i][0] <= target <= mat[i][m-1]:
      l, r = 0, m-1
      
      while l<=r:
        mid = (l+r)//2
        
        if mat[i][mid] == target:
          return True
        elif mat[i][mid] <= target:
          l = mid+1
        else:
          r = mid-1
          
  return False

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
t = 8
print(searchMatrix(arr, 8))