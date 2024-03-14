from typing import List

# In this version of the problem a limit capacity of purchasing stocks is given
def maxProfitRec(prices: List[int]) -> int:
  def f(i: int, buy: int, cap: int) -> int:
    # Recursive function to calculate the max profit
    if i == n or cap == 0:
      return 0 # Base case: If we have reached the end of the arr or used up
      # all transactions, return zero profit
      
    profit = 0
    if buy:
      # We can sell the stock
      profit = max(0 + f(i+1, True, cap), # No transaction
      prices[i] + f(i+1, False, cap-1)) # Sell the current stock 
    else:
      # We can buy the stock since buy == true, which means buying IS ALLOWED. It does not mean that we are holding a bought stock
      profit = max(0 + f(i+1, False, cap), # No transaction
      -prices[i] + f(i+1, True, cap))  # Buy the current stock 
    
    return profit
    
  n = len(prices)
  return f(0, False, 2) # Start at the first day (i)  
    

def maxProfitMemo(prices: List[int]) -> int:
  def f(i: int, buy: int, cap: int, dp: List[List[List[int]]]) -> int:
    if i == n or cap == 0:
      return 0 # Base case: If we have reached the end of the arr or used up
      # all transactions, return zero profit
      
    if dp[i][buy][cap] != -1:
      return dp[i][buy][cap] # If the result is already computed, return it
    
    profit = 0
    if buy: # We can sell the stock
      profit = max(0 + f(i+1, True, cap, dp), # No transaction
      prices[i] + f(i+1, False, cap-1, dp)) # We can sell the stock
    else: # We can buy the stock
      profit = max(0 + f(i+1, False, cap, dp), # No transaction 
      -prices[i] + f(i+1, True, cap, dp)) # We can buy the stock
    
    dp[i][buy][cap] = profit
    return profit
  
  n = len(prices)
  # Create a 3d dp table with dimensions (n) * n * 3 and initialize it with -1 values
  dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
  return f(0, False, 2, dp)
  
  
def maxProfitTab(prices: List[int]) -> int:
  n = len(prices)
  # Create a 3D DP table with dimension (n+1) * 2 * 3 and initialize it to 0 values
  dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
  # The base case is already covered as the DP array is initialized to 0 
  
  for i in range(n-1, -1, -1):
    for buy in range(2):
      for cap in range(1, 3):
        if buy:
          # We can sell the stock
          dp[i][buy][cap] = max(0 + dp[i+1][True][cap], 
          prices[i] + dp[i+1][False][cap-1])
        else:
          # We can buy the stock
          dp[i][buy][cap] = max(0 + dp[i+1][False][cap],
          -prices[i] + dp[i+1][True][cap]
          )
          
  return dp[0][False][2]

def maxProfitSO(prices: List[int]) -> int:
  n = len(prices)
  # Create two 2D arrays, ahead and curr, both of size 2*3, initialized to 0 values
  nxt = [[0 for _ in range(3)] for _ in range(2)]
  curr = [[0 for _ in range(3)] for _ in range(2)]
  
  for i in range(n-1, -1, -1):
    for buy in range(2):
      for cap in range(1, 3):
        if buy == 1:
          curr[buy][cap] = max(0 + nxt[True][cap], prices[i] + nxt[False][cap-1]) 
        else:
          curr[buy][cap] = max(0 + nxt[False][cap], -prices[i] + nxt[True][cap])
    nxt = curr
  return nxt[False][2]
  

prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxProfitRec(prices))
print(maxProfitMemo(prices))
print(maxProfitTab(prices))
print(maxProfitSO(prices))