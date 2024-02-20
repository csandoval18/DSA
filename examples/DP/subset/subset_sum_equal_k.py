from typing import List

# Subset Sum Equal to K 
# return true if is a subset is equal to k otherwise return false if no subset adds up to k

# Recursive
def subsetSumToKRec(n: int, k: int, arr: List[int]) -> bool:
  def f(idx: int, target: int) -> bool:
    if target == 0:
      return True
    
    if idx == 0:
      return arr[0] == target
    
    notTake = f(idx-1, target)
    take = False
    if arr[idx] <= target:
      take = f(idx-1, target - arr[idx])
    
    return take or notTake
  
  return f(n-1, k)

def subsetSumToKRec(n: int, k: int, arr: List[int]) -> bool:
  def f(idx: int, target: int) -> bool:
    if target
    
      
def subsetSumToKMemoize(n: int, k: int, arr: List[int]) -> bool:
  def f(idx: int, target: int, dp: List[List[bool]]) -> bool:
    if target == 0:
      return True
    
    if idx == 0:
      return arr[0] == target
    
    if dp[idx][target] != -1:
      return dp[idx][target]
    
    notTake = f(idx-1, target, dp)
    
    take = False
    if arr[idx] <= target:
      take = f(idx-1, target - arr[idx], dp)
    
    dp[idx][target] = take or notTake
    return dp[idx][target]
  
  dp = [[-1 for _ in range(k+1)] for _ in range(n)]
  return f(n-1, k, dp)
  
# Tabulation
def subsetSumToKMemoize(n: int, k: int, arr: List[int]) -> bool:
  dp = [[False for _ in range(k+1)] for _ in range(n)] 
  
  for i in range(n):
    # Set the first col to True since a sum of 0 is always possible with an empty subset
    dp[i][0] = True
    
    # Check if the first el of the arr can be used to make the target sum
    if arr[0] <= k:
      dp[0][arr[0]] = True
    
    # Fill in the DP table iteratively
    
    

arr = [1,2,3,4] 
k = 4
print(subsetSumToKRec(len(arr), k, arr))
print(subsetSumToKMemoize(len(arr), k, arr))
