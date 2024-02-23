from typing import List

# Find min coins needed that add up to 'amount' (target)

coins = [1,2,5] 
amount = 11

# Rules
# 1. Find all changing parameters f(idx, target) 
# 2. express all method => take the coin & dont take the coin 
# 3. min of all

# PS: There is an infinite supply of coins
def coinChange(coins: List[int], amount: int) -> int:
  def f(idx, target):
    if idx == 0:
      if target % coins[idx] == 0:
        return target//coins[idx]
      else:
        return float('inf')
        
    
    notTake = 0 + f(idx-1, target)
    take = float('inf')
    if coins[idx] <= target:
      take = 1 + f(idx, target-coins[idx])
    
    return min(notTake, take)
  
  n = len(coins)
  return f(n-1, amount)
      
def coinChangeMemo(coins: List[int], amount: int) -> int:
  n = len(coins)
  
  def f(idx: int, target: int, dp: List[List[int]]):
    if idx == 0:
      if target % coins[0] == 0:
        return target//coins[idx]
      else:
        return float('inf')
      
    if dp[idx][target] != -1:
      return dp[idx][target]
    
    # 0 represents that we add no count and move on to the index-1 of coins
    notTake = 0 + f(idx-1, target, dp)
    
    # We have to check if the current coins[idx] value exceeds or is equal the value of target. If it does, then we shouldn't take it
    # since the solution is not possible and continuing the recursion take extra computing
    take = float('inf')
    if coins[idx] <= target:
      take = 1 + f(idx, target-coins[idx], dp)
    
    return min(notTake, take)
  
  dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
  return f(n-1, amount, dp)
  
def coinChangeTab(coins: List[int], amount: int) -> int:
  n = len(coins)
  dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
  
  for target in range(amount+1):
    if target % coins[0] == 0:
      dp[0][target] = target // coins[0]
    else:
      dp[0][target] = float('inf')
  
  for i in range(1, len(coins)):
    for target in range(amount+1):
      notTake = 0 + dp[i-1][target]
      
      take = float('inf')
      if coins[i] <= target:
        take = 1 + dp[i][target - coins[i]]
      
      dp[i][target] = min(notTake, take)
      
  print(dp)
  res = dp[n-1][amount]
  if res >= float('inf'):
    return -1
  else:
    return res
  
def coinChangeSO(coins: List[int], amount: int) -> int:
  prevRow = [0] * (amount+1)
  
  for target in range(amount+1):
    if target % coins[0] == 0:
      prevRow[target] = target // coins[0]
    else:
      prevRow[target] = float('inf')
  
  for i in range(1, len(coins)):
    currRow = [0] * (amount+1)
    for target in range(amount+1):
      notTake = 0 + prevRow[target]  
      
      take = float('inf')
      if coins[i] <= target:
        take = 1 + currRow[target - coins[i]]
      
      currRow[target] = min(notTake, take)
    prevRow = currRow
    
  res = prevRow[amount]
  if res >= float('inf'):
    return -1
  else:
    return res
  
print(coinChange(coins, amount))
print(coinChangeMemo(coins, amount))
print(coinChangeTab(coins, amount))
print(coinChangeSO(coins, amount))