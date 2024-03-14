from typing import List

# Matrix Multiplication
#  A        B
# [1,2] *  [2]
# [3,1]    [3]
#  2*2     2*1

# These two matrices are able to be multiplied because they share a 2 in their dimensions
# (2*2) * (2*1) = 2 * (2*2) * 1 = 2 * 1
#                  remove ^


# f(10,20,30,40,50)
#     A  B  C  D

# A = 10x20 | B = 20x30 | C = 30x40 | D = 40x50

# Recursion
def matrix_chain_multiplication(arr: List[int]):
  def f(i: int, j: int) -> int:
    if i == j:
      return 0
    
    min_partitions = float('inf')
    for k in range(i, j):
      steps = arr[i-1] * arr[k] * arr[j] 
      + f(i, k)
      + f(k+1, j)
      
      min_partitions = min(min_partitions, steps)
        
    return min_partitions
    
  n = len(arr)
  return f(1, n-1)
    
# TC: O(n*n)*n => O(n^3) | SC: O(n^2) + O(n)
# Memoization
def matrix_chain_multiplication(arr: List[int]):
  def f(i: int, j: int, dp: List[List[int]]) -> int:
    if i == j:
      return 0
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    min_partitions = float('inf')
    for k in range(i, j):
      steps = arr[i-1] * arr[k] * arr[j]
      + f(i, k, dp)
      + f(k+1, j, dp)
    
      min_partitions = min(min_partitions, steps)
      
    dp[i][j] = min_partitions
    return dp[i][j]
      
  n = len(arr)
  dp = [[-1 for _ in range(n)] for _ in range(n)]
  return f(1, n-1, dp)
  
# Tabulation
