from typing import List
# 1 [3,1,5,8] 1
# 0  1 2 3 4  5
#    i

def maxCoinsRec(nums: List[int]) -> int:
  def f(i: int, j: int) -> int:
    if i > j:
      return 0
    
    max_coins = float('-inf')
    for k in range(i, j+1):
      coins = nums[i-1] * nums[k] * nums[j+1] + f(i, k-1) + f(k+1, j)
      max_coins = max(max_coins, coins)
    
    return max_coins
      
  n = len(nums)
  nums.append(1)
  nums.insert(0, 1)
  return f(1, n)

# Alternative with taking into account the length of the string with the added 1s at the start and end
# The previous solution started comparing from range(i, j+1) j being inclusive but the recursion call starts
# from range(1, n) this basically ignores the added 1's indices. In this solution we start the recursion from range(0, n-1)
# taking into account the 1s added, but the loop for m/k changes from (i, j+1) to (i+1, j)
def maxCoinsRec2(nums: List[int]) -> int:
  def f(l: int, r: int) -> int:
    if l+1 == r:
      return 0
    
    max_coins = 0
    for m in range(l+1, r): # Iterate over the balloons to burst last
      coins = nums[l] * nums[m] * nums[r] + f(l, m) + f(m, r)
      max_coins = max(max_coins, coins)
    
    return max_coins
  
  nums = [1] + nums + [1]
  n = len(nums)
  return f(0, n-1)
  
  
def maxCoinMemo(nums: List[int]) -> int:
  def f(i: int, j: int, dp: List[List[int]]) -> int:
    if i > j:
      return 0
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    max_coins = float('-inf')
    for k in range(i, j+1):
      coins = nums[i-1] * nums[k] * nums[j+1] + f(i, k-1, dp) + f(k+1, j, dp)
      max_coins = max(max_coins, coins)
      
    dp[i][j] = max_coins
    return max_coins
  
  n = len(nums)
  nums.append(1)
  nums.insert(0, 1)
  dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
  return f(1, n, dp)


def maxCoinTab(nums: List[int]) -> int:
  n = len(nums)
  # Add 1s at start and end of list for cases when we pick the first and last coin
  nums = [1] + nums + [1]
  dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
  
  for i in range(n, -1, -1):
    for j in range(i, n+1):
      # if i > j: # Or make j start from i instead of 1
      #   continue
      max_coins = float('-inf')
      for k in range(i, j+1):
        coins = nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]
        max_coins = max(max_coins, coins)
        
      dp[i][j] = max_coins
  
  return dp[1][n]
      
      
nums = [3,1,5,8]
print(maxCoinsRec(nums))
nums = [3,1,5,8]
print(maxCoinsRec2(nums))
nums = [3,1,5,8]
print(maxCoinMemo(nums))
nums = [3,1,5,8]
print(maxCoinTab(nums))