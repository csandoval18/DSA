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
  
  
    
    

arr = [1,2,3,4] 
k = 4
print(subsetSumToKRec(len(arr), k, arr))
print(subsetSumToKMemoize(len(arr), k, arr))
