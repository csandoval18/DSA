from typing import List

def change(amount: int, coins: List[int]) -> int:
  def f(idx: int, target: int) -> int:
    if idx == 0:
      if target % coins[0] == 0:
        return 1
      else:
        return 0
      
    notPick = f(idx-1, target)
    
    pick = 0
    if coins[idx] <= target:
      pick = f(idx, target-coins[idx])
    
    return notPick + pick
  
  n = len(coins)
  return f(n-1, amount)

def changeMemo(amount: int, coins: List[int]) -> int:
  def f(idx: int, target: int, dp: List[int]) -> int:
    if idx == 0:
      if target % coins[idx] == 0:
        return 1
      else:
        return 0
    
    if dp[idx][target] != -1:
      return dp[idx][target]
    
    notPick = f(idx-1, target, dp)
    
    pick = 0
    if coins[idx] <= target:
      pick = f(idx, target-coins[idx], dp)
    
    return pick + notPick

  n = len(coins)
  dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
  return f(n-1, amount, dp)
  
def changeTab(amount: int, coins: List[int]) -> int:
  n = len(coins)
  dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
  
  for target in range(amount+1):
    if target % coins[0] == 0:
      dp[0][target] = 1
    else:
      dp[0][target] = 0
  
  for i in range(1, n):
    for target in range(amount+1):
      notPick = dp[i-1][target]
    
      pick = 0
      if coins[i] <= target:
        pick = dp[i][target - coins[i]]
      
      dp[i][target] = notPick + pick
  
  return dp[n-1][amount]

def changeSO(amount: int, coins: List[int]) -> int:
  n = len(coins)
  prevRow = [0] * (amount+1)
  
  for target in range(amount+1):
    if target % coins[0] == 0:
      prevRow[target] = 1
    else: 
      prevRow[target] =  0
  
  for i in range(1, n):
    currRow = [0] * (amount+1)
    for target in range(amount+1):
      notPick = prevRow[target]
      
      pick = 0
      if coins[i] <= target:
        pick = currRow[target - coins[i]]
    
      currRow[target] = notPick + pick
    prevRow = currRow 
  return prevRow[amount]
  
coins = [1,2,5] 
amount = 5
print(change(amount, coins))
print(changeMemo(amount, coins))
print(changeTab(amount, coins))
print(changeSO(amount, coins))